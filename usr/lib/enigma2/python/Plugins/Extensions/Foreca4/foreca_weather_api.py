#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_weather_api.py - API client per dati meteo Foreca
# Copyright (c) @Lululla 2026

import os
import json
import requests
from time import time
from . import _

CACHE_BASE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"
CONFIG_FILE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/api_config.txt"
TOKEN_FILE = CACHE_BASE + "token.json"


class ForecaWeatherAPI:
    """Foreca text weather data client API (current, forecast)"""

    def __init__(self, unit_manager=None):
        self.unit_manager = unit_manager
        self.base_url = "https://pfa.foreca.net"
        self.token = None
        self.token_expire = 0
        self.load_credentials()
        self.load_token()

    def load_credentials(self):
        """Load credentials from existing configuration file"""
        self.user = ""
        self.password = ""

        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('API_USER='):
                            self.user = line.split('=', 1)[1].strip()
                        elif line.startswith('API_PASSWORD='):
                            self.password = line.split('=', 1)[1].strip()

                print(
                    f"[ForecaWeatherAPI] Credentials loaded for: {self.user}")
            except Exception as e:
                print(f"[ForecaWeatherAPI] Error loading credentials: {e}")

    def load_token(self):
        """Load token from cache (shared with maps)"""
        if os.path.exists(TOKEN_FILE):
            try:
                with open(TOKEN_FILE, 'r') as f:
                    data = json.load(f)
                    if data['expire'] > time():
                        self.token = data['token']
                        self.token_expire = data['expire']
                        print("[ForecaWeatherAPI] Token loaded from cache")
            except Exception as e:
                print(f"[ForecaWeatherAPI] Error loading token: {e}")

    def _degrees_to_direction(self, degrees):
        """Convert wind degrees to direction string"""
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        index = round(degrees / 45) % 8
        return directions[index]

    def _symbol_to_description(self, symbol_code):
        """Convert symbol code to weather description"""
        # Reuse or adapt your existing symbolToCondition method
        descriptions = {
            'd000': _('Clear'),
            'n000': _('Clear'),
            'd100': _('Mostly clear'),
            'n100': _('Mostly clear'),
            'd200': _('Partly cloudy'),
            'n200': _('Partly cloudy'),
            'd210': _('Partly cloudy and light rain'),
            'n210': _('Partly cloudy and light rain'),
            'd211': _('Partly cloudy and light wet snow'),
            'n211': _('Partly cloudy and light wet snow'),
            'd212': _('Partly cloudy and light snow'),
            'n212': _('Partly cloudy and light snow'),
            'd220': _('Partly cloudy and showers'),
            'n220': _('Partly cloudy and showers'),
            'd221': _('Partly cloudy and wet snow showers'),
            'n221': _('Partly cloudy and wet snow showers'),
            'd222': _('Partly cloudy and snow showers'),
            'n222': _('Partly cloudy and snow showers'),
            'd240': _('Partly cloudy, possible thunderstorms with rain'),
            'n240': _('Partly cloudy, possible thunderstorms with rain'),
            'd300': _('Cloudy'),
            'n300': _('Cloudy'),
            'd310': _('Cloudy and light rain'),
            'n310': _('Cloudy and light rain'),
            'd311': _('Cloudy and light wet snow'),
            'n311': _('Cloudy and light wet snow'),
            'd312': _('Cloudy and light snow'),
            'n312': _('Cloudy and light snow'),
            'd320': _('Cloudy and showers'),
            'n320': _('Cloudy and showers'),
            'd321': _('Cloudy and wet snow showers'),
            'n321': _('Cloudy and wet snow showers'),
            'd322': _('Cloudy and snow showers'),
            'n322': _('Cloudy and snow showers'),
            'd340': _('Cloudy, thunderstorms with rain'),
            'n340': _('Cloudy, thunderstorms with rain'),
            'd400': _('Overcast'),
            'n400': _('Overcast'),
            'd410': _('Overcast and light rain'),
            'n410': _('Overcast and light rain'),
            'd411': _('Overcast and light wet snow'),
            'n411': _('Overcast and light wet snow'),
            'd412': _('Overcast and light snow'),
            'n412': _('Overcast and light snow'),
            'd430': _('Overcast and showers'),
            'n430': _('Overcast and showers'),
            'd421': _('Overcast and wet snow showers'),
            'n421': _('Overcast and wet snow showers'),
            'd432': _('Overcast and snow showers'),
            'n432': _('Overcast and snow showers'),
            'd420': _('Overcast and rain'),
            'n420': _('Overcast and rain'),
            'd431': _('Overcast and wet snow'),
            'n431': _('Overcast and wet snow'),
            'd422': _('Overcast and snow'),
            'n422': _('Overcast and snow'),
            'd440': _('Overcast, thunderstorms with rain'),
            'n440': _('Overcast, thunderstorms with rain'),
            'd500': _('Thin upper cloud'),
            'n500': _('Thin upper cloud'),
            'd600': _('Fog'),
            'n600': _('Fog')
        }
        return descriptions.get(symbol_code, 'Unknown')

    def get_token(self, force_new=False):
        """Get authentication token"""
        if not self.user or not self.password:
            print("[ForecaWeatherAPI] ERROR: Missing credentials!")
            return None

        # Use cache token if valid (within 5 minutes)
        if not force_new and self.token and self.token_expire > time() + 300:
            return self.token

        try:
            url = f"{self.base_url}/authorize/token?expire_hours=720"
            data = {"user": self.user, "password": self.password}

            response = requests.post(url, json=data, timeout=10)

            if response.status_code == 200:
                result = response.json()
                self.token = result['access_token']
                self.token_expire = time() + result['expires_in']

                # Save to cache (shared with maps)
                with open(TOKEN_FILE, 'w') as f:
                    json.dump({
                        'token': self.token,
                        'expire': self.token_expire
                    }, f)

                print("[ForecaWeatherAPI] New token received")
                return self.token
            else:
                print(f"[ForecaWeatherAPI] Auth error: {response.status_code}")
                return None

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error getting token: {e}")
            return None

    def get_station_observations(self, location_id, station_limit=3):
        """
        Get nearby weather station observations via Foreca API

        Args:
            location_id: Foreca location ID (e.g., "100659935")
            station_limit: maximum number of stations (default 3, max 6)

        Returns:
            List of station observations or None
        """
        token = self.get_token()
        if not token:
            print("[ForecaWeatherAPI] No token for station observations")
            return None

        try:
            headers = {"Authorization": f"Bearer {token}"}

            # Build parameters according to API spec
            params = {
                "stations": min(station_limit, 6),  # Max 6 stations
                "tempunit": "C",  # Default, overwritten by unit_manager if present
                "windunit": "MS"  # Default m/s, overwritten by unit_manager
            }

            # Override units if UnitManager exists
            if self.unit_manager:
                unit_params = self.unit_manager.get_api_params()
                params["tempunit"] = unit_params.get("tempunit", "C")
                params["windunit"] = unit_params.get("windunit", "MS")

            # Endpoint: latest station observations
            url = f"https://pfa.foreca.com/api/v1/observation/latest/{location_id}"
            print(f"[ForecaWeatherAPI] Requesting: {url}")
            print(f"[ForecaWeatherAPI] Params: {params}")

            response = requests.get(
                url, headers=headers, params=params, timeout=15)
            print(f"[ForecaWeatherAPI] HTTP Status: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                observations = data.get('observations', [])
                print(
                    f"[ForecaWeatherAPI] Got {len(observations)} station observations")

                # Debug: print first station sample
                if observations:
                    first = observations[0]
                    print(
                        f"[ForecaWeatherAPI] Sample: {first.get('station')} - {first.get('temperature')}°C")

                return observations
            else:
                print(
                    f"[ForecaWeatherAPI] Error {response.status_code}: {response.text[:200]}")
                return None

        except requests.exceptions.ConnectionError as e:
            print(f"[ForecaWeatherAPI] Connection error: {e}")
            print(
                "[ForecaWeatherAPI] Check if pfa.foreca.com is reachable from your network")
            return None
        except Exception as e:
            print(f"[ForecaWeatherAPI] Exception: {e}")
            return None

    def get_current_weather(self, location_id):
        """
        Get current weather via API
        Args:
            location_id: Foreca location ID (e.g., "100659935")
        Returns:
            Tuple compatible with getPageF() or None
        """
        token = self.get_token()
        if not token:
            print("[ForecaWeatherAPI] No token for current weather")
            return None

        try:
            headers = {"Authorization": f"Bearer {token}"}
            params = {
                "lang": "it",
                "tempunit": "C",  # Default Celsius
                "windunit": "KMH"  # Default km/h
            }

            # Add unit parameters if we have UnitManager
            if self.unit_manager:
                api_params = self.unit_manager.get_api_params()
                params.update(api_params)

            url = f"{self.base_url}/api/v1/current/{location_id}"
            print(f"[ForecaWeatherAPI] Requesting: {url}")

            response = requests.get(
                url, headers=headers, params=params, timeout=15)

            if response.status_code == 200:
                data = response.json()
                return self._parse_current_response(data)
            else:
                print(f"[ForecaWeatherAPI] HTTP error: {response.status_code}")
                return None

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error getting current weather: {e}")
            return None

    def get_hourly_forecast(self, location_id, days=1):
        """
        Get hourly forecasts via API
        Args:
            location_id: Foreca location ID
            days: forecast days (max 7)

        Returns:
            Tuple compatible with getPageF_F() or None
        """
        token = self.get_token()
        if not token:
            print("[ForecaWeatherAPI] No token for forecast")
            return None

        try:
            headers = {"Authorization": f"Bearer {token}"}
            params = {
                "periods": 24 * days,  # Schedules for requested days
                "lang": "it",
                "tempunit": "C",
                "windunit": "KMH"
            }

            if self.unit_manager:
                api_params = self.unit_manager.get_api_params()
                params.update(api_params)

            url = f"{self.base_url}/api/v1/forecast/hourly/{location_id}"
            print(f"[ForecaWeatherAPI] Requesting forecast: {url}")

            response = requests.get(
                url, headers=headers, params=params, timeout=15)

            if response.status_code == 200:
                data = response.json()
                return self._parse_hourly_response(data)
            else:
                print(
                    f"[ForecaWeatherAPI] Forecast HTTP error: {response.status_code}")
                return None

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error getting forecast: {e}")
            return None

    def _parse_current_response(self, data):
        """Parse API /current response in a compatible format"""
        try:
            current = data.get('current', {})
            location = data.get('location', {})

            # Extract data in the same format as getPageF()
            town = location.get('name', 'N/A')
            cur_temp = str(current.get('temperature', 'N/A'))
            fl_temp = str(current.get('feelsLikeTemp', 'N/A'))
            dewpoint = str(current.get('dewPoint', 'N/A'))

            # Convert API symbol to your local icons
            symbol = current.get('symbol', 'd000')
            pic = self._api_symbol_to_icon(symbol)

            wind_dir = current.get('windDir', 0)
            wind = f"w{wind_dir}"
            # Already in the correct units!
            wind_speed = str(current.get('windSpeed', 'N/A'))
            wind_gust = str(current.get('windGust', 'N/A'))

            # The API returns pressure in hPa
            pressure_hpa = current.get('pressure', 'N/A')
            # Convert to mmHg if needed (for compatibility)
            try:
                pressure_mmhg = float(pressure_hpa) * \
                    0.750062 if pressure_hpa != 'N/A' else 'N/A'
                pressure = str(pressure_mmhg)
            except BaseException:
                pressure = str(pressure_hpa)

            hum = str(current.get('relHumidity', 'N/A'))
            rain_mm = str(current.get('precipRate', '0'))  # mm/h

            # Other fields (may not be present in the API)
            country = location.get('country', 'N/A')
            lon = str(location.get('lon', 'N/A'))
            lat = str(location.get('lat', 'N/A'))

            # Sunrise/sunset may not be included in /current
            # You may need a separate API call
            sunrise = 'N/A'
            sunset = 'N/A'
            daylen = 'N/A'

            print(f"[ForecaWeatherAPI] Parsed current: {town}, {cur_temp}°C")

            return (town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed,
                    wind_gust, rain_mm, hum, pressure, country, lon, lat,
                    sunrise, daylen, sunset)

        except Exception as e:
            print(f"[ForecaWeatherAPI] Parsing error: {e}")
            # Fallback to compatible error values
            return (
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'd000',
                'w0',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A',
                'N/A')

    def _parse_hourly_response(self, data):
        """Parse API /forecast/hourly response"""
        try:
            forecast = data.get('forecast', [])
            location = data.get('location', {})
            town = location.get('name', 'N/A')
            date = []
            mytime = []
            symb3 = []
            cur_temp3 = []
            flike_temp3 = []
            wind3 = []
            wind_speed3 = []
            precipitation3 = []
            rel_hum3 = []

            for item in forecast[:24]:  # First 24 hours
                # Date and time
                time_str = item.get('time', '')
                if 'T' in time_str:
                    date_part = time_str.split('T')[0]
                    time_part = time_str.split('T')[1].split('+')[0][:5]
                    date.append(date_part)
                    mytime.append(time_part)
                else:
                    date.append('N/A')
                    mytime.append('N/A')

                # Symbol
                symbol = item.get('symbol', 'd000')
                symb3.append(self._api_symbol_to_icon(symbol))

                # Temperatures
                cur_temp3.append(str(item.get('temperature', 'N/A')))
                flike_temp3.append(str(item.get('feelsLikeTemp', 'N/A')))

                # Wind
                wind_dir = item.get('windDir', 0)
                wind3.append(str(wind_dir))
                wind_speed3.append(str(item.get('windSpeed', 'N/A')))

                # Precipitation and humidity
                precipitation3.append(
                    str(item.get('precipProb', '0')))  # Probability %
                rel_hum3.append(str(item.get('relHumidity', 'N/A')))

            # Day (may not be provided by the API)
            day = 'N/A'

            print(
                f"[ForecaWeatherAPI] Parsed forecast: {town}, {len(forecast)} periods")

            return (town, date, mytime, symb3, cur_temp3, flike_temp3,
                    wind3, wind_speed3, precipitation3, rel_hum3, day)

        except Exception as e:
            print(f"[ForecaWeatherAPI] Forecast parsing error: {e}")
            return ('N/A', [], [], [], [], [], [], [], [], [], 'N/A')

    def _parse_daily_forecast_response(self, data):
        """Parse API /forecast/daily response"""
        try:
            forecast = data.get('forecast', [])
            location = data.get('location', {})

            town = location.get('name', 'N/A')
            country = location.get('country', 'N/A')

            daily_data = {
                'town': town,
                'country': country,
                'days': []
            }

            for day in forecast:
                date_str = day.get('date', '')
                symbol = day.get('symbol', 'd000')

                # Temperatures
                max_temp = day.get('maxTemp', 'N/A')
                min_temp = day.get('minTemp', 'N/A')

                # Precipitation
                precip_prob = day.get('precipProb', '0')
                precip_mm = day.get('precipAccum', '0')

                # Wind
                wind_speed = day.get('windSpeed', 'N/A')
                wind_dir = day.get('windDir', 0)
                wind_dir_str = self._degrees_to_direction(wind_dir)

                # Sunrise/sunset (if available)
                sunrise = day.get('sunrise', 'N/A')
                sunset = day.get('sunset', 'N/A')

                # UV index (if available)
                uv_index = day.get('uvIndex', 'N/A')

                # Day name (you can derive from date)
                day_name = self._get_day_name(date_str)

                daily_data['days'].append({
                    'date': date_str,
                    'day_name': day_name,
                    'symbol': self._api_symbol_to_icon(symbol),
                    'max_temp': max_temp,
                    'min_temp': min_temp,
                    'precip_prob': precip_prob,
                    'precip_mm': precip_mm,
                    'wind_speed': wind_speed,
                    'wind_dir': wind_dir,
                    'wind_dir_str': wind_dir_str,
                    'sunrise': sunrise,
                    'sunset': sunset,
                    'uv_index': uv_index,
                    'description': self._symbol_to_description(symbol)
                })

            print(
                f"[ForecaWeatherAPI] Parsed {len(daily_data['days'])} daily forecasts")
            return daily_data

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error parsing daily forecast: {e}")
            return None

    def _get_day_name(self, date_str):
        """Convert date string to day name"""
        try:
            from datetime import datetime
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.strftime("%A")  # Monday, Tuesday, etc.
        except BaseException:
            return date_str

    def _api_symbol_to_icon(self, api_symbol):
        """Map API symbols to your local icons"""
        # Complete mapping based on the available weather codes
        symbol_map = {
            'd000': 'd000', 'n000': 'n000',
            'd100': 'd100', 'n100': 'n100',
            'd200': 'd200', 'n200': 'n200',
            'd210': 'd210', 'n210': 'n210',
            'd211': 'd211', 'n211': 'n211',
            'd212': 'd212', 'n212': 'n212',
            'd220': 'd220', 'n220': 'n220',
            'd221': 'd221', 'n221': 'n221',
            'd222': 'd222', 'n222': 'n222',
            'd240': 'd240', 'n240': 'n240',
            'd300': 'd300', 'n300': 'n300',
            'd310': 'd310', 'n310': 'n310',
            'd311': 'd311', 'n311': 'n311',
            'd312': 'd312', 'n312': 'n312',
            'd320': 'd320', 'n320': 'n320',
            'd321': 'd321', 'n321': 'n321',
            'd322': 'd322', 'n322': 'n322',
            'd340': 'd340', 'n340': 'n340',
            'd400': 'd400', 'n400': 'n400',
            'd410': 'd410', 'n410': 'n410',
            'd411': 'd411', 'n411': 'n411',
            'd412': 'd412', 'n412': 'n412',
            'd420': 'd420', 'n420': 'n420',
            'd421': 'd421', 'n421': 'n421',
            'd422': 'd422', 'n422': 'n422',
            'd430': 'd430', 'n430': 'n430',
            'd431': 'd431', 'n431': 'n431',
            'd432': 'd432', 'n432': 'n432',
            'd440': 'd440', 'n440': 'n440',
            'd500': 'd500', 'n500': 'n500',
            'd600': 'd600', 'n600': 'n600'
        }
        return symbol_map.get(api_symbol, 'd000')

    def check_credentials(self):
        """Verifica se le credenziali sono configurate"""
        return bool(self.user and self.password)
