#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_stations.py - Display nearby station observations
# Copyright (c) @Lululla 2026

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Label import Label
from Components.ScrollLabel import ScrollLabel
from enigma import getDesktop

from .skin import (
    ForecaStations_UHD,
    ForecaStations_FHD,
    ForecaStations_HD
)
from . import _


class ForecaStations(Screen):
    """Screen for nearby weather station observations"""
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ForecaStations_FHD
    elif sz_w == 2560:
        skin = ForecaStations_UHD
    else:
        skin = ForecaStations_HD

    def __init__(self, session, api, location_id, location_name):
        self.session = session
        self.api = api
        self.location_id = location_id
        self.location_name = location_name
        self.observations = []

        Screen.__init__(self, session)
        self.setTitle(_("Station Observations") + " - " + location_name)

        self["list"] = MenuList([])
        self["info"] = Label(_("Loading nearby stations..."))
        self["details"] = ScrollLabel()
        self["distance"] = Label("")

        self["actions"] = ActionMap(
            ["OkCancelActions", "DirectionActions"],
            {
                "cancel": self.exit,
                "ok": self.show_station_details,
                "up": self.up,
                "down": self.down,
                "left": self.page_up,
                "right": self.page_down,
            },
            -1
        )

        self.onLayoutFinish.append(self.load_stations)

    def load_stations(self):
        """Load nearby weather stations list"""
        self["info"].setText(_("Loading..."))

        self.observations = self.api.get_station_observations(
            self.location_id, station_limit=15)

        if not self.observations:
            self["info"].setText(_("No station data available"))
            self["list"].setList([(_("No stations found"), None)])
            return

        items = []
        for obs in self.observations:
            station_name = obs.get('station', 'Unknown')
            distance = obs.get('distance', 'N/A')
            temp = obs.get('temperature', 'N/A')

            # Format list entry
            if isinstance(temp, (int, float)):
                temp_str = f"+{temp}°" if temp >= 0 else f"{temp}°"
            else:
                temp_str = str(temp)

            item_text = f"{station_name} ({distance}) - {temp_str}C"
            items.append((item_text, obs))

        self["list"].setList(items)
        self["info"].setText(f"{len(items)} {_('stations nearby')}")

        # Select first station
        if items:
            self.show_station_details()

    def show_station_details(self):
        """Show details of the selected station"""
        selection = self["list"].getCurrent()
        if not selection or not selection[1]:
            return

        station = selection[1]
        details = self._format_station_details(station)

        self["details"].setText(details)

        # Update distance
        distance = station.get('distance', 'N/A')
        self["distance"].setText(f"{_('Distance')}: {distance}")

    def _format_station_details(self, station):
        """Format station details with correct units"""
        lines = []

        # Name and distance
        lines.append(f"[b]{station.get('station', 'Unknown')}[/b]")
        lines.append(f"{_('Distance')}: {station.get('distance', 'N/A')}")
        lines.append("")

        # Temperatures (already in correct units)
        temp = station.get('temperature', 'N/A')
        feels = station.get('feelsLikeTemp', 'N/A')

        # Add + sign for positive temperatures
        if isinstance(temp, (int, float)):
            temp_str = f"+{temp}" if temp >= 0 else f"{temp}"
            lines.append(f"{_('Temperature')}: {temp_str}°")
        else:
            lines.append(f"{_('Temperature')}: {temp}")

        if isinstance(feels, (int, float)) and feels != 'N/A':
            feels_str = f"+{feels}" if feels >= 0 else f"{feels}"
            lines.append(f"{_('Feels like')}: {feels_str}°")

        # Other data
        lines.append(f"{_('Humidity')}: {station.get('relHumidity', 'N/A')}%")

        # Pressure (if available)
        pressure = station.get('pressure')
        if pressure:
            lines.append(f"{_('Pressure')}: {pressure} hPa")

        # Wind (already in correct units)
        wind_speed = station.get('windSpeed', 'N/A')
        wind_dir = station.get('windDirString', 'N/A')

        if wind_speed and wind_speed != 'N/A':
            wind_unit = "km/h"  # Or "mph" if imperial
            lines.append(f"{_('Wind')}: {wind_speed} {wind_unit} {wind_dir}")

        # Timestamp
        time_str = station.get('time', '')
        if 'T' in time_str:
            dt_part = time_str.split('T')[0]
            tm_part = time_str.split('T')[1].split('+')[0][:5]
            lines.append("")
            lines.append(f"{_('Last update')}: {dt_part} {tm_part}")

        return "\n".join(lines)

    def up(self):
        self["list"].up()
        self.show_station_details()

    def down(self):
        self["list"].down()
        self.show_station_details()

    def page_up(self):
        self["details"].pageUp()

    def page_down(self):
        self["details"].pageDown()

    def exit(self):
        self.close()
