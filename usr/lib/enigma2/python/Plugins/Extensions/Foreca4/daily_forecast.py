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
        self["info"].setText(_("Loading..."))

        # Try API first
        self.forecast_data = self.api.get_daily_forecast(self.location_id, days=7)

        if self.forecast_data:
            self.display_forecast()
        else:
            # Fallback to scraping or show error
            self["info"].setText(_("No forecast data available"))
            self["forecast_text"].setText(_("Could not load weekly forecast."))

    def display_forecast(self):
        """Format and display the forecast data"""
        try:
            text_lines = []

            # Header
            text_lines.append(f"[b]{self.forecast_data['town']}, {self.forecast_data['country']}[/b]")
            text_lines.append(_("7-Day Detailed Forecast"))
            text_lines.append("=" * 40)

            # Daily forecasts
            for day in self.forecast_data['days']:
                # Day header
                day_header = f"\n[b]{day['day_name']} ({day['date']})[/b]"
                text_lines.append(day_header)

                # Temperatures
                temp_line = f"  {_('Temperature')}: {day['min_temp']}° / {day['max_temp']}°C"
                text_lines.append(temp_line)

                # Weather description
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
            self["title"].setText(f"{self.location_name} - {_('Weekly Forecast')}")

        except Exception as e:
            print(f"[DailyForecast] Error displaying forecast: {e}")
            self["info"].setText(_("Error displaying forecast"))
            self["forecast_text"].setText(str(e))

    def get_daily_forecast(self, location_id, days=7):
        """
        Get daily forecasts for the next 7-10 days via Foreca API.
        Returns formatted data for meteogram display.
        """
        token = self.get_token()
        if not token:
            print("[ForecaWeatherAPI] No token for daily forecast")
            return None

        try:
            headers = {"Authorization": f"Bearer {token}"}
            params = {
                "days": min(days, 10),  # Max 10 days
                "lang": "en",  # Or use system language
                "tempunit": "C",
                "windunit": "KMH"
            }

            # Add unit parameters if we have UnitManager
            if self.unit_manager:
                api_params = self.unit_manager.get_api_params()
                params.update(api_params)

            # Endpoint for daily forecast
            url = f"{self.base_url}/api/v1/forecast/daily/{location_id}"
            print(f"[ForecaWeatherAPI] Requesting daily forecast: {url}")

            response = requests.get(url, headers=headers, params=params, timeout=15)

            if response.status_code == 200:
                data = response.json()
                return self._parse_daily_forecast_response(data)
            else:
                print(f"[ForecaWeatherAPI] Daily forecast HTTP error: {response.status_code}")
                print(f"Response: {response.text[:200]}")
                return None

        except Exception as e:
            print(f"[ForecaWeatherAPI] Error getting daily forecast: {e}")
            return None

    def _parse_daily_forecast_response(self, data):
        """Analizza la risposta dell'API per le previsioni giornaliere"""
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

            print(f"[ForecaWeatherAPI] Analizzate {len(daily_data['days'])} previsioni giornaliere")
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
