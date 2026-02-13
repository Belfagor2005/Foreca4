#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# daily_forecast.py - Weekly detailed forecast screen
# Copyright (c) @Lululla 2026

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from Components.MultiContent import MultiContentEntryText
from enigma import eListboxPythonMultiContent, gFont, RT_VALIGN_CENTER

from . import _, load_skin_for_class


class DailyForecastList(MenuList):
    """Custom MenuList for daily forecast with MultiContent"""

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        self.l.setFont(0, gFont("Regular", 28))
        self.l.setItemHeight(45)

    def postWidgetCreate(self, instance):
        MenuList.postWidgetCreate(self, instance)
        instance.setItemHeight(45)


class DailyForecast(Screen):
    """Screen showing 7-10 day detailed forecast"""

    def __init__(self, session, api, location_id, location_name):
        self.skin = load_skin_for_class(DailyForecast)
        Screen.__init__(self, session)

        self.api = api
        self.location_id = location_id
        self.location_name = location_name
        self.forecast_data = None

        self.setTitle(_("Weekly Forecast") + " - " + location_name)

        # Widgets
        self["title"] = Label("")
        self["info"] = Label(_("Loading weekly forecast..."))
        self["list"] = DailyForecastList([])

        self["actions"] = ActionMap(
            [
                "WizardActions",
                "DirectionActions",
                "OkCancelActions"
            ],
            {
                "cancel": self.exit,
                "ok": self.exit,
                "up": self.up,
                "down": self.down,
                "left": self.page_up,
                "right": self.page_down,
            }, -2
        )

        self.onLayoutFinish.append(self.load_forecast)

    def load_forecast(self):
        """Load and display the weekly forecast"""
        self["info"].setText(_("Loading weekly forecast..."))

        try:
            if hasattr(self.api, 'get_daily_forecast'):
                self.forecast_data = self.api.get_daily_forecast(
                    self.location_id, days=7)
        except Exception as e:
            print(f"[DailyForecast] API error: {e}")
            self.forecast_data = None

        if not self.forecast_data or not self.forecast_data.get('days'):
            self["info"].setText(_("Could not load forecast data"))
            return

        # Set title
        town = self.forecast_data.get('town', self.location_name)
        country = self.forecast_data.get('country', '')
        self["title"].setText(f"{town}, {country} - {_('7 Day Forecast')}")
        self["info"].setText(_("Use arrow keys to scroll"))

        # Create the list with MultiContent
        self["list"].setList(self._create_forecast_list())
        print("[DailyForecast] Display updated with MenuList")

    def _create_forecast_list(self):
        """Create MultiContent list for forecast"""
        list_data = []

        # Header
        list_data.append(self._create_header_entry())

        # Days
        for day in self.forecast_data.get('days', []):
            list_data.append(self._create_day_entry(day))

        # Footer
        list_data.append(self._create_footer_entry())

        return list_data

    def _create_header_entry(self):
        """Create header row"""
        return [
            None,  # No selection data
            MultiContentEntryText(
                pos=(20, 5),
                size=(200, 35),
                font=0,
                text=_("Day"),
                color=0x00a0ff,
                flags=RT_VALIGN_CENTER
            ),
            MultiContentEntryText(
                pos=(220, 5),
                size=(200, 35),
                font=0,
                text=_("Temp"),
                color=0x00a0ff,
                flags=RT_VALIGN_CENTER
            ),
            MultiContentEntryText(
                pos=(420, 5),
                size=(300, 35),
                font=0,
                text=_("Weather"),
                color=0x00a0ff,
                flags=RT_VALIGN_CENTER
            ),
            MultiContentEntryText(
                pos=(720, 5),
                size=(150, 35),
                font=0,
                text=_("Precip"),
                color=0x00a0ff,
                flags=RT_VALIGN_CENTER
            ),
            MultiContentEntryText(
                pos=(870, 5),
                size=(200, 35),
                font=0,
                text=_("Wind"),
                color=0x00a0ff,
                flags=RT_VALIGN_CENTER
            )
        ]

    def _create_day_entry(self, day):
        """Create a day row"""
        day_name = day.get('day_name', '')[:3]  # Abbreviazione
        date_str = day.get('date', '').split('-')[2]  # Solo giorno

        # Temperature
        min_temp = day.get('min_temp', 'N/A')
        max_temp = day.get('max_temp', 'N/A')
        temp_str = f"{min_temp}°/{max_temp}°"

        # Weather
        weather = _(day.get('description', 'N/A'))
        if len(weather) > 15:
            weather = weather[:15] + "..."

        # Precipitation
        precip = f"{day.get('precip_prob', '0')}%"

        # Wind
        wind_speed = day.get('wind_speed', 'N/A')
        wind_dir = day.get('wind_dir_str', '')
        if wind_speed != 'N/A' and wind_speed != 0:
            wind_str = f"{wind_speed} {wind_dir}"
        else:
            wind_str = "-"

        # Color based on temperature
        try:
            temp_val = float(max_temp)
            if temp_val >= 25:
                color = 0xff5555  # Rosso
            elif temp_val >= 15:
                color = 0xffaa55  # Arancio
            elif temp_val >= 5:
                color = 0x55ff55  # Verde
            else:
                color = 0x5555ff  # Blu
        except BaseException:
            color = 0xffffff  # Bianco

        return [
            None,
            # Day
            MultiContentEntryText(
                pos=(20, 5),
                size=(200, 35),
                font=0,
                text=f"{day_name} {date_str}",
                color=0xffffff,
                flags=RT_VALIGN_CENTER
            ),
            # Temperature
            MultiContentEntryText(
                pos=(220, 5),
                size=(200, 35),
                font=0,
                text=temp_str,
                color=color,
                flags=RT_VALIGN_CENTER
            ),
            # Weather
            MultiContentEntryText(
                pos=(420, 5),
                size=(300, 35),
                font=0,
                text=weather,
                color=0xffffff,
                flags=RT_VALIGN_CENTER
            ),
            # Precipitation
            MultiContentEntryText(
                pos=(720, 5),
                size=(150, 35),
                font=0,
                text=precip,
                color=0x55aaff,
                flags=RT_VALIGN_CENTER
            ),
            # Wind
            MultiContentEntryText(
                pos=(870, 5),
                size=(200, 35),
                font=0,
                text=wind_str,
                color=0xffffff,
                flags=RT_VALIGN_CENTER
            )
        ]

    def _create_footer_entry(self):
        """Create footer row"""
        return [
            None,
            MultiContentEntryText(
                pos=(20, 5),
                size=(1100, 35),
                font=0,
                text=_("Data provided by Foreca"),
                color=0xc0c0c0,
                flags=RT_VALIGN_CENTER
            )
        ]

    def up(self):
        self["list"].up()

    def down(self):
        self["list"].down()

    def page_up(self):
        self["list"].pageUp()

    def page_down(self):
        self["list"].pageDown()

    def exit(self):
        self.close()
