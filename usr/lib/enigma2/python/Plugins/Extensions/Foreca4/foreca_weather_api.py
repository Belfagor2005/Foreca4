#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_weather_api.py - API client per dati meteo Foreca
# Copyright (c) @Lululla 2026

import os
import json
import requests
from time import time
from . import _
from .google_translate import _get_system_language

CACHE_BASE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"
CONFIG_FILE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/api_config.txt"
TOKEN_FILE = CACHE_BASE + "token.json"


class ForecaWeatherAPI:
    """Foreca text weather data client API (current, forecast)"""

    def __init__(self, unit_manager=None):
        self.unit_manager = unit_manager
        self.base_url = "https://pfa.foreca.com"
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

    def check_credentials(self):
        """Check whether credentials are configured"""
        return bool(self.user and self.password)

    def _degrees_to_direction(self, degrees):
        """Convert wind degrees to direction string"""
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        index = round(degrees / 45) % 8
        return directions[index]

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

    def _get_api_lang(self):
        """Convert system language to Foreca API language code"""
        lang = _get_system_language()
        lang_map = {
            'it': 'it',
            'de': 'de',
            'fr': 'fr',
            'es': 'es',
            'pl': 'pl',
            'ru': 'ru',
            'fi': 'fi',
            'sv': 'sv',
            'nl': 'nl',
            'cs': 'cs',
            'sk': 'sk',
            'hu': 'hu',
            'tr': 'tr',
            'en': 'en'
        }
        return lang_map.get(lang, 'en')

    def _get_location_details(self, location_id):
        """Get location name, country, coordinates from API"""
        token = self.get_token()
        if not token:
            return {
                'name': 'N/A',
                'country': 'N/A',
                'lon': 'N/A',
                'lat': 'N/A'}
        try:
            headers = {"Authorization": f"Bearer {token}"}
            url = f"{self.base_url}/api/v1/location/{location_id}"
            resp = requests.get(url, headers=headers, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                return {
                    'name': data.get('name', 'N/A'),
                    'country': data.get('country', 'N/A'),
                    'lon': data.get('lon', 'N/A'),
                    'lat': data.get('lat', 'N/A')
                }
        except Exception as e:
            print(f"[ForecaWeatherAPI] Error getting location: {e}")
        return {'name': 'N/A', 'country': 'N/A', 'lon': 'N/A', 'lat': 'N/A'}

    def _get_day_name(self, date_str):
        """Convert date string to day name"""
        try:
            from datetime import datetime
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.strftime("%A")  # Monday, Tuesday, etc.
        except BaseException:
            return date_str

    def get_token(self, force_new=False):
        """Get authentication token"""
        if not self.user or not self.password:
            print("[ForecaWeatherAPI] ERROR: Missing credentials!")
            return None

        if not force_new and self.token and self.token_expire > time() + 300:
            print("[ForecaWeatherAPI] Using cached token")
            return self.token

        print("[ForecaWeatherAPI] Requesting NEW token...")
        try:
            url = f"{self.base_url}/authorize/token?expire_hours=720"
            data = {"user": self.user, "password": self.password}

            response = requests.post(url, json=data, timeout=10)

            if response.status_code == 200:
                result = response.json()
                self.token = result['access_token']
                self.token_expire = time() + result['expires_in']

                # Salva in cache
                with open(TOKEN_FILE, 'w') as f:
                    json.dump({
                        'token': self.token,
                        'expire': self.token_expire
                    }, f)

                print("[ForecaWeatherAPI] New token received")
                return self.token
            else:
                print(f"[ForecaWeatherAPI] Auth error: {response.status_code}")
                print(f"Response: {response.text[:200]}")
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
        token = self.get_token()
        if not token:
            return None
        try:
            headers = {"Authorization": f"Bearer {token}"}
            params = {
                "lang": self._get_api_lang(),
                "tempunit": "C",
                "windunit": "KMH"
            }
            if self.unit_manager:
                params.update(self.unit_manager.get_api_params())

            url = f"{self.base_url}/api/v1/current/{location_id}"
            response = requests.get(
                url, headers=headers, params=params, timeout=15)

            if response.status_code == 200:
                data = response.json()
                location_data = self._get_location_details(location_id)
                data['location'] = location_data
                return self._parse_current_response(data)
            else:
                return None
        except Exception as e:
            print(f"[ForecaWeatherAPI] Error: {e}")
            return None

    def get_daily_forecast(self, location_id, days=7):
        token = self.get_token()
        if not token:
            print("[ForecaWeatherAPI] No token for daily forecast")
            return None

        try:
            headers = {"Authorization": f"Bearer {token}"}
            params = {
                "days": min(days, 10),
                "lang": self._get_api_lang(),
                "tempunit": "C",
                "windunit": "KMH"
            }

            if self.unit_manager:
                api_params = self.unit_manager.get_api_params()
                params.update(api_params)

            url = f"https://pfa.foreca.com/api/v1/forecast/daily/{location_id}"
            print(f"[ForecaWeatherAPI] Requesting daily forecast: {url}")

            response = requests.get(
                url, headers=headers, params=params, timeout=15)

            if response.status_code == 200:
                data = response.json()
                location_data = self._get_location_details(location_id)
                data['location'] = location_data

                print("[ForecaWeatherAPI] Daily forecast response received")
                return self._parse_daily_forecast_response(data)
            else:
                print(f"[ForecaWeatherAPI] HTTP error: {response.status_code}")
                return None

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error getting daily forecast: {e}")
            return None

    def get_today_tomorrow_details(self, location_id):
        token = self.get_token()
        if not token:
            return None

        try:
            headers = {"Authorization": f"Bearer {token}"}
            lang = self._get_api_lang()

            # 1. Location details
            location = self._get_location_details(location_id)

            # 2. Current weather
            current_url = f"{self.base_url}/api/v1/current/{location_id}"
            current_resp = requests.get(
                current_url,
                headers=headers,
                params={"lang": lang, "tempunit": "C"},
                timeout=10
            )
            current_data = current_resp.json() if current_resp.status_code == 200 else {}

            # 3. Hourly forecast (48h)
            hourly_url = f"{self.base_url}/api/v1/forecast/hourly/{location_id}"
            hourly_resp = requests.get(
                hourly_url,
                headers=headers,
                params={"periods": 48, "lang": lang, "tempunit": "C"},
                timeout=15
            )
            if hourly_resp.status_code != 200:
                return None

            hourly_data = hourly_resp.json()
            forecast = hourly_data.get('forecast', [])

            # Organize by day
            from datetime import datetime, timedelta
            today = datetime.now().strftime("%Y-%m-%d")
            tomorrow = (
                datetime.now() +
                timedelta(
                    days=1)).strftime("%Y-%m-%d")

            today_periods = [
                p for p in forecast if p.get(
                    'time', '').startswith(today)]
            tomorrow_periods = [
                p for p in forecast if p.get(
                    'time', '').startswith(tomorrow)]

            # Time slots (approximation)
            def extract_period(periods, hour_range):
                for p in periods:
                    hour = int(
                        p.get(
                            'time',
                            '12:00').split('T')[1].split(':')[0])
                    if hour_range[0] <= hour <= hour_range[1]:
                        return p
                return periods[0] if periods else None

            # Today
            morning = extract_period(today_periods, (6, 10))
            afternoon = extract_period(today_periods, (11, 16))
            evening = extract_period(today_periods, (17, 21))
            overnight = extract_period(today_periods, (22, 5))

            # Tomorrow
            morning2 = extract_period(tomorrow_periods, (6, 10))
            afternoon2 = extract_period(tomorrow_periods, (11, 16))
            evening2 = extract_period(tomorrow_periods, (17, 21))
            overnight2 = extract_period(tomorrow_periods, (22, 5))

            # Summary texts (from current or first period)
            today_summary = current_data.get(
                'current', {}).get(
                'symbolPhrase', 'N/A')
            today_max = max([p.get('temperature', 0)
                            for p in today_periods]) if today_periods else 'N/A'
            today_min = min([p.get('temperature', 0)
                            for p in today_periods]) if today_periods else 'N/A'
            today_rain = sum([p.get('precipAccum', 0)
                             for p in today_periods]) if today_periods else 0

            tomorrow_max = max([p.get('temperature', 0)
                               for p in tomorrow_periods]) if tomorrow_periods else 'N/A'
            tomorrow_min = min([p.get('temperature', 0)
                               for p in tomorrow_periods]) if tomorrow_periods else 'N/A'
            tomorrow_rain = sum([p.get('precipAccum', 0)
                                for p in tomorrow_periods]) if tomorrow_periods else 0

            return {
                'town': location.get('name', 'N/A'),
                'country': location.get('country', 'N/A'),
                'lat': location.get('lat', 'N/A'),
                'lon': location.get('lon', 'N/A'),
                'today': {
                    'text': today_summary,
                    'max_temp': today_max,
                    'min_temp': today_min,
                    'rain_mm': f"{today_rain:.1f}",
                    'morning': {'symbol': morning.get('symbol', 'd000') if morning else 'd000', 'temp': morning.get('temperature', 'N/A') if morning else 'N/A'},
                    'afternoon': {'symbol': afternoon.get('symbol', 'd000') if afternoon else 'd000', 'temp': afternoon.get('temperature', 'N/A') if afternoon else 'N/A'},
                    'evening': {'symbol': evening.get('symbol', 'd000') if evening else 'd000', 'temp': evening.get('temperature', 'N/A') if evening else 'N/A'},
                    'overnight': {'symbol': overnight.get('symbol', 'd000') if overnight else 'd000', 'temp': overnight.get('temperature', 'N/A') if overnight else 'N/A'},
                },
                'tomorrow': {
                    'text': 'N/A',  # Could add tomorrow summary if available
                    'max_temp': tomorrow_max,
                    'min_temp': tomorrow_min,
                    'rain_mm': f"{tomorrow_rain:.1f}",
                    'morning': {'symbol': morning2.get('symbol', 'd000') if morning2 else 'd000', 'temp': morning2.get('temperature', 'N/A') if morning2 else 'N/A'},
                    'afternoon': {'symbol': afternoon2.get('symbol', 'd000') if afternoon2 else 'd000', 'temp': afternoon2.get('temperature', 'N/A') if afternoon2 else 'N/A'},
                    'evening': {'symbol': evening2.get('symbol', 'd000') if evening2 else 'd000', 'temp': evening2.get('temperature', 'N/A') if evening2 else 'N/A'},
                    'overnight': {'symbol': overnight2.get('symbol', 'd000') if overnight2 else 'd000', 'temp': overnight2.get('temperature', 'N/A') if overnight2 else 'N/A'},
                }
            }
        except Exception as e:
            print(
                f"[ForecaWeatherAPI] Error in get_today_tomorrow_details: {e}")
            import traceback
            traceback.print_exc()
            return None

    def get_hourly_forecast(self, location_id, days=1):
        token = self.get_token()
        if not token:
            return None
        try:
            headers = {"Authorization": f"Bearer {token}"}
            params = {
                "periods": 24 * days,
                "lang": self._get_api_lang(),
                "tempunit": "C",
                "windunit": "KMH"
            }
            if self.unit_manager:
                params.update(self.unit_manager.get_api_params())

            url = f"{self.base_url}/api/v1/forecast/hourly/{location_id}"
            response = requests.get(
                url, headers=headers, params=params, timeout=15)

            if response.status_code == 200:
                data = response.json()
                location_data = self._get_location_details(location_id)
                data['location'] = location_data
                return self._parse_hourly_response(data)
            else:
                return None
        except Exception as e:
            print(f"[ForecaWeatherAPI] Error: {e}")
            return None

    def _parse_current_response(self, data):
        """Parse API /current response in a compatible format"""
        try:
            current = data.get('current', {})
            location = data.get('location', {})

            # Extract data in the same format as
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
            location = data.get('location', {})  # <-- QUESTA RIGA È CRITICA!
            town = location.get('name', 'N/A')
            country = location.get('country', 'N/A')
            # DEBUG
            print(
                f"[ForecaWeatherAPI] Location from daily forecast: {town}, {country}")
            daily_data = {
                'town': town,
                'country': country,
                'days': []
            }
            for day in forecast:
                date_str = day.get('date', '')
                symbol = day.get('symbol', 'd000')

                daily_data['days'].append({
                    'date': date_str,
                    'day_name': self._get_day_name(date_str),
                    'symbol': self._api_symbol_to_icon(symbol),
                    'max_temp': day.get('maxTemp', 'N/A'),
                    'min_temp': day.get('minTemp', 'N/A'),
                    'precip_prob': day.get('precipProb', '0'),
                    'precip_mm': day.get('precipAccum', '0'),
                    'wind_speed': day.get('windSpeed', 'N/A'),
                    'wind_dir': day.get('windDir', 0),
                    'wind_dir_str': self._degrees_to_direction(day.get('windDir', 0)),
                    'sunrise': day.get('sunrise', 'N/A'),
                    'sunset': day.get('sunset', 'N/A'),
                    'uv_index': day.get('uvIndex', 'N/A'),
                    'description': self._symbol_to_description(symbol)
                })

            print(
                f"[ForecaWeatherAPI] Parsed {len(daily_data['days'])} daily forecasts")
            return daily_data

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error parsing daily forecast: {e}")
            import traceback
            traceback.print_exc()
            return None
