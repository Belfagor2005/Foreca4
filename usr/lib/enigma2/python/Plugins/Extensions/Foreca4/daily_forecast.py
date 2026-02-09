#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# daily_forecast.py - Weekly detailed forecast screen
# Copyright (c) @Lululla 2026

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from enigma import getDesktop
import requests

from .skin import (
    DailyForecast_UHD,
    DailyForecast_FHD,
    DailyForecast_HD
)
from . import _


class DailyForecast(Screen):
    """Screen showing 7-10 day detailed forecast"""
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = DailyForecast_FHD
    elif sz_w == 2560:
        skin = DailyForecast_UHD
    else:
        skin = DailyForecast_HD

    def __init__(self, session, api, location_id, location_name):
        Screen.__init__(self, session)
        self.api = api
        self.location_id = location_id
        self.location_name = location_name
        self.forecast_data = None

        self.setTitle(_("Weekly Forecast") + " - " + location_name)
        self["title"] = Label("")
        self["info"] = Label(_("Loading weekly forecast..."))
        self["forecast_text"] = ScrollLabel()
        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions"
            ],
            {
                "cancel": self.exit,
                "ok": self.exit,
                "up": self.page_up,
                "down": self.page_down,
                "left": self.page_up,
                "right": self.page_down,
            }, -1
        )
        self.onLayoutFinish.append(self.load_forecast)

    def load_forecast(self):
        """Load and display the weekly forecast"""
        self["info"].setText(_("Loading weekly forecast..."))
        try:
            if hasattr(self.api, 'get_daily_forecast'):
                print(f"[DailyForecast] Calling API for location: {self.location_id}")
                self.forecast_data = self.api.get_daily_forecast(self.location_id, days=7)

                if self.forecast_data:
                    print(f"[DailyForecast] API returned {len(self.forecast_data.get('days', []))} days")
                else:
                    print("[DailyForecast] API returned None")
            else:
                print("[DailyForecast] API method get_daily_forecast not available")
                self.forecast_data = None
        except Exception as e:
            print(f"[DailyForecast] API error: {e}")
            import traceback
            traceback.print_exc()
            self.forecast_data = None

        # If API fails, show error message
        if not self.forecast_data:
            self["info"].setText(_("Could not load forecast data"))
            self["forecast_text"].setText(
                _("Weekly forecast data is not available.\n\n") +
                _("Possible reasons:\n") +
                _("1. No API credentials configured\n") +
                _("2. API service temporarily unavailable\n") +
                _("3. Location not supported\n\n") +
                _("Please check your api_config.txt file.")
            )
            return

        self.display_forecast()

    def create_sample_data(self):
        """Create sample data for testing"""
        from datetime import datetime, timedelta
        sample_data = {
            'town': self.location_name,
            'country': 'N/A',
            'days': []
        }
        today = datetime.now()
        for i in range(7):
            day_date = today + timedelta(days=i)
            day_name = day_date.strftime("%A")
            date_str = day_date.strftime("%Y-%m-%d")

            sample_data['days'].append({
                'date': date_str,
                'day_name': day_name,
                'max_temp': f"{10 + i}",
                'min_temp': f"{5 + i}",
                'precip_prob': f"{i * 10}",
                'precip_mm': f"{i * 2}",
                'wind_speed': f"{5 + i}",
                'wind_dir_str': ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W'][i % 7],
                'sunrise': '07:00',
                'sunset': '19:00',
                'uv_index': f"{i % 5}",
                'description': ['Sunny', 'Cloudy', 'Rainy', 'Windy', 'Clear', 'Foggy', 'Stormy'][i % 7]
            })

        return sample_data

    def display_forecast(self):
        """Format and display the forecast data without BBCode tags"""
        try:
            text_lines = []
            text_lines.append(f"{self.forecast_data['town']}, {self.forecast_data['country']}")
            text_lines.append(_("7-Day Detailed Forecast"))
            text_lines.append("=" * 40)

            for day in self.forecast_data['days']:
                text_lines.append(f"\n{day['day_name']} ({day['date']})")
                temp_line = f"  {_('Temperature')}: {day['min_temp']}° / {day['max_temp']}°C"
                text_lines.append(temp_line)
                text_lines.append(f"  {_('Weather')}: {day['description']}")

                # Precipitation
                precip_line = f"  {_('Precipitation')}: {day['precip_prob']}% ({day['precip_mm']} mm)"
                text_lines.append(precip_line)

                # Wind
                wind_line = f"  {_('Wind')}: {day['wind_speed']} km/h {day['wind_dir_str']}"
                text_lines.append(wind_line)

                # Sunrise/Sunset
                if day['sunrise'] != 'N/A' and day['sunset'] != 'N/A':
                    sun_line = f"  {_('Sun')}: ↑{day['sunrise']} ↓{day['sunset']}"
                    text_lines.append(sun_line)

                # UV Index
                if day['uv_index'] != 'N/A':
                    uv_line = f"  {_('UV Index')}: {day['uv_index']}"
                    text_lines.append(uv_line)

            # Footer
            text_lines.append("\n" + "=" * 40)
            text_lines.append(_("Data provided by Foreca"))

            # Display
            self["forecast_text"].setText("\n".join(text_lines))
            self["info"].setText(_("Use arrow keys to scroll"))
            self["title"].setText(
                f"{self.location_name} - {_('Weekly Forecast')}")

        except Exception as e:
            print(f"[DailyForecast] Error displaying forecast: {e}")
            self["info"].setText(_("Error displaying forecast"))
            self["forecast_text"].setText(str(e))

    def get_daily_forecast(self, location_id, days=7):
        token = self.get_token()
        if not token:
            print("[ForecaWeatherAPI] No token for daily forecast")
            return None

        try:
            headers = {"Authorization": f"Bearer {token}"}
            params = {
                "days": min(days, 10),
                "lang": "it",  # Cambiato da 'en' a 'it'
                "tempunit": "C",
                "windunit": "KMH"
            }

            if self.unit_manager:
                api_params = self.unit_manager.get_api_params()
                params.update(api_params)

            url = f"{self.base_url}/api/v1/forecast/daily/{location_id}"
            print(f"[ForecaWeatherAPI] Requesting daily forecast: {url}")
            response = requests.get(url, headers=headers, params=params, timeout=15)
            print(f"[ForecaWeatherAPI] Response status: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                print(f"[ForecaWeatherAPI] Daily forecast response received: {len(data.get('forecast', []))} days")
                return self._parse_daily_forecast_response(data)
            elif response.status_code == 401:
                print("[ForecaWeatherAPI] Token expired, forcing new token...")
                token = self.get_token(force_new=True)
                if token:
                    headers = {"Authorization": f"Bearer {token}"}
                    response = requests.get(url, headers=headers, params=params, timeout=15)
                    if response.status_code == 200:
                        data = response.json()
                        return self._parse_daily_forecast_response(data)
                return None
            else:
                print(f"[ForecaWeatherAPI] HTTP error: {response.status_code}")
                print(f"Response: {response.text[:200]}")
                return None

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error getting daily forecast: {e}")
            import traceback
            traceback.print_exc()
            return None

    def _parse_daily_forecast_response(self, data):
        """Analyze API response for daily forecasts"""
        try:
            forecast = data.get('forecast', [])
            location = data.get('location', {})

            daily_data = {
                'town': location.get('name', 'N/A'),
                'country': location.get('country', 'N/A'),
                'days': []
            }

            for day in forecast:
                daily_data['days'].append({
                    'date': day.get('date', ''),
                    'day_name': self._get_day_name(day.get('date', '')),
                    'symbol': self._api_symbol_to_icon(day.get('symbol', 'd000')),
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
                    'description': self._symbol_to_description(day.get('symbol', 'd000'))
                })

            print(
                f"[ForecaWeatherAPI] Analizzate {len(daily_data['days'])} previsioni giornaliere")
            return daily_data

        except Exception as e:
            print(f"[ForecaWeatherAPI] Errore nell'analisi: {e}")
            return None

    def page_up(self):
        self["forecast_text"].pageUp()

    def page_down(self):
        self["forecast_text"].pageDown()

    def exit(self):
        self.close()
