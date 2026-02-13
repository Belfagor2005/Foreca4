#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# unit_manager.py - Base Foreca map viewer
# unit_settings_simple.py - Schermata impostazioni unità semplificate
# Copyright (c) @Lululla 20260122

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.Pixmap import Pixmap
import os

from . import _, load_skin_for_class


class UnitManager:
    # Define constants for unit systems
    SYSTEM_METRIC = 'metric'
    SYSTEM_IMPERIAL = 'imperial'

    # Define constants for specific units
    WIND_KMH = 'KMH'
    WIND_MS = 'MS'
    WIND_KTS = 'KTS'
    WIND_MPH = 'MPH'

    PRESSURE_HPA = 'HPA'
    PRESSURE_MMHG = 'MMHG'
    PRESSURE_INHG = 'INHG'

    TEMP_C = 'C'
    TEMP_F = 'F'

    def __init__(self, config_path):
        self.config_path = config_path
        self.system = self.SYSTEM_METRIC
        self.wind_unit = self.WIND_KMH
        self.pressure_unit = self.PRESSURE_HPA
        self.temp_unit = self.TEMP_C
        self.load_config()

    def load_config(self):
        """Load unit configuration from file"""
        CONFIG_FILE = os.path.join(self.config_path, 'units.conf')
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    for line in f:
                        if '=' in line:
                            key, value = line.strip().split('=', 1)
                            if key == 'system':
                                self.system = value
                            elif key == 'wind_unit':
                                self.wind_unit = value
                            elif key == 'pressure_unit':
                                self.pressure_unit = value
                            elif key == 'temp_unit':
                                self.temp_unit = value
            except Exception as e:
                print(f"[Foreca4] Error loading unit config: {e}")

    def save_config(self):
        """Save unit configuration to file"""
        try:
            CONFIG_FILE = os.path.join(self.config_path, 'units.conf')
            with open(CONFIG_FILE, 'w') as f:
                f.write(f"system={self.system}\n")
                f.write(f"wind_unit={self.wind_unit}\n")
                f.write(f"pressure_unit={self.pressure_unit}\n")
                f.write(f"temp_unit={self.temp_unit}\n")
        except Exception as e:
            print(f"[Foreca4] Error saving unit config: {e}")

    def set_simple_unit_system(self, system):
        """
        Set a simplified unit system (metric or imperial)
        system: 'metric' or 'imperial'
        """
        if system == self.SYSTEM_METRIC:
            self.system = self.SYSTEM_METRIC
            self.wind_unit = self.WIND_KMH
            self.pressure_unit = self.PRESSURE_HPA
            self.temp_unit = self.TEMP_C
        elif system == self.SYSTEM_IMPERIAL:
            self.system = self.SYSTEM_IMPERIAL
            self.wind_unit = self.WIND_MPH
            self.pressure_unit = self.PRESSURE_INHG
            self.temp_unit = self.TEMP_F
        self.save_config()

    def get_simple_system(self):
        """Return the current simplified system"""
        return self.system

    def convert_wind(self, speed_in_ms):
        """
        Convert wind speed from m/s (Foreca API standard[citation:2]) to configured unit.
        Returns (converted_value, unit_label)
        """
        try:
            speed = float(speed_in_ms)
        except (ValueError, TypeError):
            return (0.0, self.get_wind_label())

        if self.wind_unit == self.WIND_KMH:
            return (speed * 3.6, self.get_wind_label())  # m/s to km/h
        elif self.wind_unit == self.WIND_KTS:
            return (speed * 1.94384, self.get_wind_label())  # m/s to knots
        elif self.wind_unit == self.WIND_MPH:
            return (speed * 2.23694, self.get_wind_label())  # m/s to mph
        else:  # MS - keep as m/s
            return (speed, self.get_wind_label())

    def convert_pressure(self, pressure_in_hpa):
        """
        Convert pressure from hPa to configured unit.
        pressure_in_hpa: pressione in hPa
        Returns: (value, label)
        """
        try:
            pressure = float(pressure_in_hpa)
        except (ValueError, TypeError):
            return (0.0, self.get_pressure_label())

        if self.pressure_unit == self.PRESSURE_MMHG:
            return (
                pressure * 0.750062,
                self.get_pressure_label())  # hPa to mmHg
        elif self.pressure_unit == self.PRESSURE_INHG:
            return (
                pressure * 0.02953,
                self.get_pressure_label())   # hPa to inHg
        else:  # HPA
            return (pressure, self.get_pressure_label())

    def get_wind_label(self):
        """Get display label for wind unit"""
        labels = {
            self.WIND_KMH: 'km/h',
            self.WIND_MS: 'm/s',
            self.WIND_KTS: 'kts',
            self.WIND_MPH: 'mph'
        }
        return labels.get(self.wind_unit, 'km/h')

    def get_pressure_label(self):
        """Get display label for pressure unit"""
        labels = {
            self.PRESSURE_HPA: 'hPa',
            self.PRESSURE_MMHG: 'mmHg',
            self.PRESSURE_INHG: 'inHg'
        }
        return labels.get(self.pressure_unit, 'hPa')

    def get_temp_label(self):
        """Get display label for temperature unit"""
        return '°C' if self.temp_unit == self.TEMP_C else '°F'

    def get_api_params(self):
        """
        Get parameters for Foreca API calls based on configuration[citation:2][citation:5].
        Returns dict with windunit and tempunit parameters.
        """
        # Map our internal units to Foreca API parameter values
        windunit_map = {
            self.WIND_MS: 'MS',
            self.WIND_KMH: 'KMH',
            self.WIND_KTS: 'KTS',
            self.WIND_MPH: 'MPH'
        }

        tempunit_map = {
            self.TEMP_C: 'C',
            self.TEMP_F: 'F'
        }

        return {
            'windunit': windunit_map.get(self.wind_unit, 'MS'),
            'tempunit': tempunit_map.get(self.temp_unit, 'C')
        }


class UnitSettingsSimple(Screen):
    """Screen for changing units (metric/imperial)"""

    def __init__(self, session, unit_manager):
        self.skin = load_skin_for_class(UnitSettingsSimple)
        Screen.__init__(self, session)
        self.unit_manager = unit_manager
        self.current_system = unit_manager.get_simple_system()

        self.setTitle(_("Unit Settings"))

        self["key_red"] = Label(_("Cancel"))
        self["key_green"] = Label(_("Save"))
        self["title"] = Label(_("Select unit system"))
        self["info"] = Label(_("Changes apply immediately"))

        self["option_metric"] = Label(_("Metric System"))
        self["metric_details"] = Label(_("Celsius, km/h, hPa"))
        self["option_imperial"] = Label(_("Imperial System"))
        self["imperial_details"] = Label(_("Fahrenheit, mph, inHg"))
        self["background_plate"] = Label("N/A")
        self["selection_overlay"] = Label("N/A")
        self["check_metric"] = Pixmap()
        self["check_imperial"] = Pixmap()

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "ColorActions",
                "DirectionActions"
            ],
            {
                "cancel": self.exit,
                "red": self.exit,
                "green": self.save,
                "ok": self.toggle_selection,
                "up": self.up,
                "down": self.down,
            }, -1
        )
        self.onLayoutFinish.append(self.update_display)
        self.onClose.append(self.cleanup)

    def initialize_display(self):
        # Set background color using current RGB values
        current_color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["background_plate"].instance.setBackgroundColor(current_color)
        # Set selection plate with current transparency
        self["selection_overlay"].instance.setBackgroundColor(parseColor(alpha))

    def update_display(self):
        """Update checkboxes based on the current selection"""
        check_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/check.png"
        empty_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/empty.png"
        # Hide both initially
        self["check_metric"].hide()
        self["check_imperial"].hide()
        if self.current_system == 'metric':
            if os.path.exists(check_path):
                self["check_metric"].instance.setPixmapFromFile(check_path)
            if os.path.exists(empty_path):
                self["check_imperial"].instance.setPixmapFromFile(empty_path)
        else:
            if os.path.exists(check_path):
                self["check_imperial"].instance.setPixmapFromFile(check_path)
            if os.path.exists(empty_path):
                self["check_metric"].instance.setPixmapFromFile(empty_path)
        
        self.initialize_display()
        self["check_metric"].show()
        self["check_imperial"].show()

    def up(self):
        """Select metric"""
        self.current_system = 'metric'
        self.update_display()

    def down(self):
        """Select imperial"""
        self.current_system = 'imperial'
        self.update_display()

    def toggle_selection(self):
        """Switch between the two options"""
        self.current_system = 'imperial' if self.current_system == 'metric' else 'metric'
        self.update_display()

    def save(self):
        """Save preferences"""
        try:
            self.unit_manager.set_simple_unit_system(self.current_system)
            self.close(True)  # Return True to indicate units changed
        except Exception as e:
            print(f"[UnitSettings] Error saving: {e}")
            self.close(False)  # Return False on error

    def cleanup(self):
        if hasattr(self, 'close_timer') and self.close_timer:
            try:
                self.close_timer.stop()
            except BaseException:
                pass

    def exit(self):
        self.close(False)
