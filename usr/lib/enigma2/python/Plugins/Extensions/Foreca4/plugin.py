#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#  $Id$
#
# -------------------------------------------------------
#
#              Foreca Weather Forecast E2
#
#   This Plugin retrieves the actual weather forecast
#   for the next 10 days from the Foreca website.
#
#        We wish all users wonderful weather!
#
#
#                 11/03/2025
#
#     Source of information: https://www.foreca.com
#
#             Design and idea by
#                  @Bauernbub
#            enigma2 mod by mogli123
#
# -------------------------------------------------------
#
#  Provided with no warranties of any sort.
#
# -------------------------------------------------------
#
# History:
# 2.6 Various minor changes
# 2.7 Wrap around mode enabled in screen-lists
# 2.8 Calculate next date based on displayed date when left/right key is pushed
#     after prior date jump using 0 - 9 keys was performed
# 2.9 Fix: Show correct date and time in weather videos
#     Main screen navigation modified to comply with standard usage:
#     scroll page up/down by left/right key
#     select previous/next day by left/right arrow key of numeric key group
# 2.9.1 Latvian cities and localization added. Thanks to muca
# 2.9.2 Iranian cities updated and localization added. Thanks to Persian Prince
#   Hungarian and Slovakian cities added. Thanks to torpe
# 2.9.3 Detail line in main screen condensed to show more text in SD screen
#   Grading of temperature colors reworked
#   Some code cosmetics
#   Translation code simplified: Setting the os LANGUAGE variable isn't needed anymore
#   Typos in German localization fixed
# 2.9.4 Many world-wide cities added. Thanks to AnodA
#   Hungarian and Slovakian localization added. Thanks to torpe
# 2.9.5 Fixed: Cities containing "_" didn't work as favorites. Thanks to kashmir
# 2.9.6 Size of temperature item slightly extended to match with skins using italic font
#   Grading of temperature colors reworked
# 2.9.7 Use specified "Frame size in full view" value when showing "5 day forecast" chart
#   Info screen reworked
#   False temperature colors fixed
#   Up/down keys now scroll by page in main screen (without highlighting selection)
# 3.0.0 Option added to select measurement units. Thanks to muca
#   Option added to select time format.
#   Setup menu reworked.
#   Main screen navigation modified: Select previous/next day by left/right key
#   Many Italian cities added and Italian localization updated. Thanks to mat8861
#   Czech, Greek, French, Latvian, Dutch, Polish, Russian localization updated. Thanks to muca
# 3.0.1 Fix broken transliteration
#   Disable selection in main screen.
# 3.0.2 Weather maps of Czech Republic, Greece, Hungary, Latvia, Poland, Russia, Slovakia added
#   Temperature Satellite video added
#   Control key assignment in slide show reworked to comply with Media Player standard
#   Some Italian cities added
#   Thumbnail folders compacted
#   Unused code removed, redundant code purged
#   Localization updated
# 3.0.3 List of German states and list of European countries sorted
#   Code cosmetics
#   Localization updated
# 3.0.4 Language determination improved
# 3.0.5 Setup of collating sequence reworked
# 3.0.6 Weather data in Russian version obtained from foreca.com instead of foreca.ru due
#     to structural discrepancy of Russian web site
#   Code cosmetics
# 3.0.7 Turkish cities updated. Thanks to atsiz77
#   Debug state noted in log file
# 3.0.8 Fixed for Foreca's pages changes
# 3.0.9 Path for weather map regions updated after change of Wetterkontor's pages. Thanks to Bag58.
#   Add missing spinner icon
# 3.1.0 Plugin splitted into a loader and UI part, as Foreca needs quite a while to load. Hence
#     actual load postponed until the user requests for it.
#   Finnish localization added. Thanks to kjuntara
#   Ukrainian localization added. Thanks to Irkoff
# 3.1.1 ForecaPreview skineable
# 3.1.2 Next screens skineable
# 3.1.3 Added font size for slideshow into setting
# 3.1.4 rem /www.metoffice.gov.uk due non existing infrared on this pages more
# 3.1.7 fix url foreca com
# 3.1.8 fix problem with national chars in favorite names
# 3.1.9 renamed parsed variables, added humidity into list - for display in default screen must be:
#   changed line:       self.itemHeight = 90   ... change to new height, if is needed
#   and rearanged lines:    self.valText1 = 365,5,600,28
#               self.valText2 = 365,33,600,28
#               self.valText3 = 365,59,600,28
#               self.valText4 = 365,87,600,28
#   similar in user skin - there text4Pos="x,y,w,h" must be added
# 3.2.0 fixed satellite maps, removed infrared - page not exist more, sanity check if nothing is downloaded
# 3.2.3-r3 change URL to .net and .ru
# 3.2.7 change URL to .hr, Py3-bugfix for videos and several code cleanups
# 3.2.8 'startservice.cfg', 'fav1.cfg' and 'fav2.cfg' are obsolete and now part of etc/enigma2/settings and therefore can be deleted
# 3.2.9 change URL to .biz (THX to jup @OpenA.TV) and some code improvements
#
# To do:
#   Add 10 day forecast on green key press
#   City search at Foreca website on yellow key press. This will eliminate complete city DB.
#   Option to add unlimited cities to a favorite list and to manage this favorite list (add & delete city, sort list).
#   Show home city (first entry of favorite list) on OK key press.
#   Skip to next/previous favorite city on left/right arrow key.
#   Show weather videos and maps on blue key
#   Show setup menu on Menu key
# 3.2.11 Umstellung auf Foreca Seite .biz und Nutzung WebClientContextFactory für https
# Unresolved: Crash when scrolling in help screen of city panel
# To do:
#   Show weather videos and maps on blue key
#   Show setup menu on Menu key
#
# 3.3.4 change URL to and many code improvements
#  RECODE FROM LULULLA TO 20241222
# To do:
#   Add choice list for pressur and other menu
#   check all url and fetch..
#   CACHE_PATH moved
#   FAlog moved
#   secure remove image from folde CACHE_PATH
#   Remove profile ICC from bad image
# 3.3.5 change URL to and many code improvements
#  RECODE FROM LULULLA
# To do:
#   Add server url online
# 3.3.6 fix translations and many code improvements
#  RECODE FROM LULULLA
# 3.3.7 removed .cfg files - add TV button for Menu Config
#  RECODE FROM LULULLA
# 3.3.8 Mahor fix on clean all code unnecessay / append new PY3
#  Translate 90% complete
#  # thank's Orlandoxx  restore Eumsat screen picxview
#  RECODE FROM LULULLA
#  Foreca 4 Weather and Forecast
#
#  RECODE FROM (C) Evg77734, 2025
#  v.1.3.4
#
# mod @lululla 2026.01.25 v.1.3.4_r2
# Core API:
# Authentication system, token/tile cache (foreca_map_api.py).
# Interface:
# Layer selection menu and basic viewer with timeline (foreca_map_menu.py, foreca_map_viewer.py).
# Integration:
# Menu item in the main plugin, configuration reading from file.
# Features:
# Download and merge 3x3 tile grids, overlay on existing background maps (temp_map.png, europa.png, etc.).
# Trial Limitations:
# The code is compatible with the trial plan limit: 1,000 tiles/day for maps.
# The cache I implemented helps avoid exceeding this limit by reusing already downloaded tiles.
# Language Translation:
# Implementation of GetText translation and Google AI API
# major fix
# graphic @Oktus

# mod @lululla 2026.01.25 v.1.3.5
# fix map viewer transcode to api from scraper
# mod @lululla 2026.01.25 v.1.3.6
# complete conversion migration from scraper to api foreca.


from __future__ import absolute_import

import os
from sys import version_info
from threading import Thread

from Components.ActionMap import ActionMap, HelpableActionMap
from Components.GUIComponent import GUIComponent
from Components.Label import Label
from Components.MenuList import MenuList
from Components.MultiContent import MultiContentEntryText
from Components.Pixmap import Pixmap
from Components.Sources.List import List
from Components.Sources.StaticText import StaticText
from enigma import (
    eListboxPythonMultiContent,
    gFont,
    getDesktop,
    RT_VALIGN_CENTER,
    eListbox,
    gRGB,
    eTimer
)
from Screens.HelpMenu import HelpableScreen
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from skin import parseColor
from Tools.BoundFunction import boundFunction
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Tools.LoadPixmap import LoadPixmap
import six

from . import _, PLUGIN_PATH, load_skin_for_class
from .foreca_map_api import ForecaMapAPI
from .foreca_map_menu import ForecaMapMenu
from .google_translate import translate_text, safe_translate, _get_system_language, translate_batch
from .slideshow import ForecaMapsMenu
from .unit_manager import UnitManager, UnitSettingsSimple
from .foreca_weather_api import ForecaWeatherAPI
from .daily_forecast import DailyForecast

VERSION = "1.3.6"

TARGET_LANG = _get_system_language()


# base constant
BASEURL = "https://www.foreca.com/"
data_file = os.path.join(PLUGIN_PATH, "color_database.txt")
unit_file = os.path.join(PLUGIN_PATH, "unit_config.conf")
config_file = os.path.join(PLUGIN_PATH, "api_config.txt")
default_unit = 'metric'  # Default a metrico
path_loc0 = '103169070/Rome-Italy'                        # Blue - Favorite 0
path_loc1 = '100524901/Moscow-Russia'                     # Green - Favorite 1
path_loc2 = '102961214/Thurles-County-Tipperary-Ireland'  # Yellow - Favorite 2


# Home @lululla
home_file = os.path.join(PLUGIN_PATH, "home.cfg")
if os.path.exists(home_file):
    try:
        with open(home_file, "r") as f:
            path_loc0 = f.read().strip()
    except BaseException:
        pass

# Favorite 1
fav1_file = os.path.join(PLUGIN_PATH, "fav1.cfg")
if os.path.exists(fav1_file):
    try:
        with open(fav1_file, "r") as f:
            path_loc1 = f.read().strip()
    except BaseException:
        pass

# Favorite 2
fav2_file = os.path.join(PLUGIN_PATH, "fav2.cfg")
if os.path.exists(fav2_file):
    try:
        with open(fav2_file, "r") as f:
            path_loc2 = f.read().strip()
    except BaseException:
        pass


global MAIN_PAGE_FF, myloc, MAIN_PAGE_F, town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, rgbmyr, rgbmyg, rgbmyb, lon, lat, sunrise, daylen, sunset, alpha, share_town0, f_day
myloc = 0
MAIN_PAGE_F = str(BASEURL) + path_loc0
town = ' n/a'
cur_temp = ' n/a'
fl_temp = ' n/a'
dewpoint = ' n/a'
pic = ' n/a'
wind = ' n/a'
wind_speed = ' n/a'
wind_gust = ' n/a'
rain_mm = ' n/a'
hum = ' n/a'
daylen = ' n/a'
pressure = ' n/a'
country = ' n/a'
MAIN_PAGE_FF = str(BASEURL) + path_loc0 + '/hourly?day=0'
f_town = ' n/a'
f_date = []
f_time = []
f_symb = []
f_cur_temp = []
f_flike_temp = []
f_wind = []
f_wind_speed = []
f_precipitation = []
f_rel_hum = []
rgbmyr = 0
rgbmyg = 80
rgbmyb = 239
alpha = '#40000000'
share_town0 = ''
f_day = ' n/a'
lon = ' n/a'
lat = ' n/a'
sunrise = ' n/a'
sunset = ' n/a'

# other constant @lululla
cur_wind_speed_recalc = 1
for_wind_speed_recalc = 1
size_w = getDesktop(0).size().width()
size_h = getDesktop(0).size().height()


def read_alpha():
    global alpha
    alpha = '#40000000'
    if os.path.exists(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_alpha.conf") is True:
        try:
            with open("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_alpha.conf", "r") as file:
                contents = file.readlines()
                a = str(contents[0])
                alpha = a.rstrip()
                file.close()
        except BaseException:
            alpha = '#40000000'


read_alpha()


def save_alpha(indata):
    f = open(
        '/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_alpha.conf',
        'w')
    f.write(indata)
    f.close()


def conv_day_len(indata):
    trspz = indata
    try:
        inall = indata.split(' ')
        in2 = _(str(inall[1]))
        in3 = _(str(inall[3]))
        trspz = inall[0] + ' ' + str(in2) + ' ' + inall[2] + ' ' + str(in3)
    except BaseException:
        trspz = indata
    return trspz


def is_valid(v):
    return bool(v) and str(v).strip().lower() != 'n/a'


def my_speed_wind(indata, metka):
    try:
        trspz = 0
        trspz = '%.01f' % float(int(indata) / 1)
        if metka == 1:
            return float(trspz)
        else:
            trspz = '%.01f' % float(int(indata))
            return float(trspz)
    except BaseException:
        return 0.00


# translations @lululla
_translation_cache = {}     # In-memory cache
_translation_queue = []     # Queue for batch translations
_is_translating = False
_translation_cache_file = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/translation_cache.txt"
_translation_cache_loaded = False


def load_translation_cache():
    """Load previously saved translations from a file"""
    global _translation_cache_loaded, _translation_cache

    if _translation_cache_loaded:
        return _translation_cache

    _translation_cache = {}
    if os.path.exists(_translation_cache_file):
        try:
            with open(_translation_cache_file, "r", encoding='utf-8') as f:
                for line in f:
                    if '=' in line:
                        original, translated = line.strip().split('=', 1)
                        _translation_cache[original] = translated
            print("[Foreca4] Loaded {0} translations from cache"
                  .format(len(_translation_cache)))
        except Exception as e:
            print("[Foreca4] Cache loading error: {0}"
                  .format(e))

    _translation_cache_loaded = True
    return _translation_cache


def save_translation_cache(original, translated):
    """Save a translation to the cache file"""
    try:
        with open(_translation_cache_file, "a", encoding='utf-8') as f:
            f.write("{0}={1}\n".format(original, translated))
    except Exception as e:
        print("[Foreca4] Cache save error: {0}".format(e))


def trans(text, use_batch=True):
    """Enhanced translation function using improved translation module."""
    if not text or not isinstance(text, str):
        return text or ""

    # Clean the text
    text = text.strip()
    if not text:
        return ""

    # Check cache first
    if text in _translation_cache:
        return _translation_cache[text]

    # For single translations or when batch is disabled
    if not use_batch:
        translated = translate_text(text)
        if translated and translated != text:
            _translation_cache[text] = translated
            return translated
        return text

    # For batch mode, we'll queue translations
    # (This would need integration with a batch system)
    return safe_translate(text, fallback=text)


def translate_batch_strings(texts):
    """Translate multiple strings efficiently using batch mode."""
    if not texts:
        return []

    # Filter out None or empty strings
    valid_texts = [str(t).strip() for t in texts if t and str(t).strip()]
    if not valid_texts:
        return []

    # Check cache first
    results = []
    to_translate = []
    indices = []

    for i, text in enumerate(valid_texts):
        if text in _translation_cache:
            results.append(_translation_cache[text])
        else:
            to_translate.append(text)
            indices.append(i)
            results.append(None)  # Placeholder

    # Translate remaining texts in batch
    if to_translate:
        try:
            translated_batch = translate_batch(to_translate)

            # Update cache and results
            for idx, (original, translated) in enumerate(
                    zip(to_translate, translated_batch)):
                if translated and translated != original:
                    _translation_cache[original] = translated
                    # Update result at correct index
                    results[indices[idx]] = translated
                else:
                    results[indices[idx]] = original

        except Exception as e:
            print("[Foreca4] Batch translation error: {0}".format(e))
            # Fallback: translate individually
            for idx, text in enumerate(to_translate):
                translated = safe_translate(text, fallback=text)
                _translation_cache[text] = translated
                results[indices[idx]] = translated

    # Replace any None values with original text
    for i in range(len(results)):
        if results[i] is None:
            results[i] = valid_texts[i] if i < len(valid_texts) else ""

    return results


class Foreca_Preview(Screen, HelpableScreen):
    def __init__(self, session):
        global town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country
        global f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum
        global lon, lat, sunrise, daylen, sunset, f_day

        self.session = session
        self.unit_manager = UnitManager(PLUGIN_PATH)
        self.weather_api = ForecaWeatherAPI(self.unit_manager)
        self.tag = 0

        # DETERMINE LOCATION ID FROM PATH
        location_id = path_loc0.split(
            '/')[0] if '/' in path_loc0 else path_loc0
        # 1. TRY CURRENT WEATHER VIA API
        town = cur_temp = fl_temp = dewpoint = pic = wind = wind_speed = wind_gust = rain_mm = hum = pressure = country = lon = lat = sunrise = daylen = sunset = 'N/A'

        if self.weather_api.check_credentials():
            print(
                "[Foreca4] Trying API for current weather, ID: {0}".format(location_id))
            result_current = self.weather_api.get_current_weather(location_id)

            if (
                result_current
                and isinstance(result_current, (list, tuple))
                and len(result_current) == 17
                and result_current[0] != 'N/A'
            ):
                town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current
                print("[Foreca4] Current weather obtained via API")
            else:
                print(
                    "[Foreca4] Current weather API failed, falling back to scraping")
        else:
            print("[Foreca4] API credentials not configured, using scraping")

        # 2. TRY HOURLY FORECASTS VIA API
        if self.weather_api.check_credentials():
            print(
                "[Foreca4] Trying API for forecasts, ID: {0}".format(location_id))
            result_forecast = self.weather_api.get_hourly_forecast(
                location_id, days=1)
            if result_forecast and result_forecast[0] != 'N/A':
                f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = result_forecast
                # api_forecast_ok = True
                print(
                    "[Foreca4] Forecasts obtained via API: {0} periods".format(
                        len(f_time)))
            else:
                print("[Foreca4] Forecast API failed, falling back to scraping")
        else:
            print("[Foreca4] API credentials not configured for forecasts")

        self.skin = load_skin_for_class(Foreca_Preview)
        Screen.__init__(self, session)
        HelpableScreen.__init__(self)
        self.setTitle(_("Foreca Weather Forecast") + " " + _("v.") + VERSION)
        self.list = []
        self["menu"] = List(self.list)

        # Title widgets
        self["title_main"] = StaticText()
        self["title_version"] = StaticText()
        self["title_loading"] = StaticText(_("Please wait ..."))
        self["title_sub"] = StaticText()
        self["title_section"] = StaticText()
        self["title_section_weather"] = StaticText()

        # Station info
        self["station_name"] = Label("N/A")

        # Current weather displays
        self["city_name"] = Label("N/A")
        self["temperature_current"] = Label("N/A")
        self["temperature_feelslike"] = Label("N/A")
        self["dewpoint_value"] = Label("N/A")
        self["weather_icon"] = Pixmap()
        self["wind_icon"] = Pixmap()
        self["wind_speed_value"] = Label("N/A")
        self["wind_gust_value"] = Label("N/A")
        self["rain_value"] = Label("N/A")
        self["humidity_value"] = Label("N/A")
        self["pressure_value"] = Label("N/A")
        self["weather_description"] = Label('')

        # Icon pixmaps
        self["icon_pressure"] = Pixmap()
        self["icon_rain"] = Pixmap()
        self["icon_humidity"] = Pixmap()

        # Background plates (RINOMINATI!)
        self["selection_overlay"] = Label("N/A")
        self["color_bg_today"] = Label("N/A")
        self["color_bg_forecast"] = Label("N/A")
        self["color_bg_sun"] = Label("N/A")
        self["color_bg_coords"] = Label("N/A")
        self["transp_bg_today"] = Label("N/A")
        self["transp_bg_forecast"] = Label("N/A")
        self["transp_bg_sun"] = Label("N/A")
        self["transp_bg_coords"] = Label("N/A")
        self["transp_bg_header"] = Label("N/A")

        # Sun info
        self["day_length"] = Label('0 h 0 min')
        self["sunrise_label"] = Label(_('Sunrise'))
        self["sunrise_value"] = Label('00:00')
        self["sunset_label"] = Label(_('Sunset'))
        self["sunset_value"] = Label('00:00')
        self["icon_sun"] = Pixmap()

        self.color = gRGB(255, 255, 255)
        self["actions"] = HelpableActionMap(
            self, "ForecaActions",
            {
                "cancel": (self.exit, _("Exit - End")),
                "showEventInfo": (self.info, _("Info - About")),
                "menu": (self.Menu, _("Menu - Settings")),
                "left": (self.left, _("Left - Previous day")),
                "right": (self.right, _("Right - Next day")),
                "up": (self.up, _("Up - Previous page")),
                "ok": (self.OK, _("OK - Ext Info")),
                "down": (self.down, _("Down - Next page")),
                "previous": (self.previousDay, _("Left arrow - Previous day")),
                "next": (self.nextDay, _("Right arrow - Next day")),
                "red": (self.red, _("Red - Color select")),
                "green": (self.Fav1, _("Green - Favorite 1")),
                "yellow": (self.Fav2, _("Yellow - Favorite 2")),
                "blue": (self.Fav0, _("Blue - Home")),
                "0": (boundFunction(self.keyNumberGlobal, 0), _("0 - Today")),
                "1": (boundFunction(self.keyNumberGlobal, 1), _("1 - Today + 1 day")),
                "2": (boundFunction(self.keyNumberGlobal, 2), _("2 - Today + 2 days")),
                "3": (boundFunction(self.keyNumberGlobal, 3), _("3 - Today + 3 days")),
                "4": (boundFunction(self.keyNumberGlobal, 4), _("4 - Today + 4 days")),
                "5": (boundFunction(self.keyNumberGlobal, 5), _("5 - Today + 5 days")),
                "6": (boundFunction(self.keyNumberGlobal, 6), _("6 - Today + 6 days")),
                "7": (boundFunction(self.keyNumberGlobal, 7), _("7 - Today + 7 days")),
                "8": (boundFunction(self.keyNumberGlobal, 8), _("8 - Today + 8 days")),
                "9": (boundFunction(self.keyNumberGlobal, 9), _("9 - Today + 9 days")),
            },
            -2
        )
        self.onLayoutFinish.append(self.StartPageFirst)
        self.onShow.append(self.update_button)

    @property
    def unit_system(self):
        """Property for compatibility with existing code"""
        return self.unit_manager.get_simple_system()

    def Menu(self):
        """Simple menu with ChoiceBox"""
        from Screens.ChoiceBox import ChoiceBox

        menu_items = [
            (_("City Selection"), "city"),
            (_("Weather Maps"), "maps"),
            (_("Weekly Forecast"), "daily_forecast"),
            (_("Station Observations"), "stations"),
            (_("Unit Settings"), "units"),
            (_("Color select"), "colorselector"),
            (_("Transparency Settings"), "transparency"),
            (_("Info"), "info"),
            (_("Exit"), "exit")
        ]

        self.session.openWithCallback(
            self.menu_callback,
            ChoiceBox,
            title=_("Foreca Menu"),
            list=menu_items
        )

    def menu_callback(self, choice):
        """Manages the selection"""
        if choice is None:
            return
        if choice[1] == "city":
            self.session.open(CityPanel4)
        elif choice[1] == "maps":
            self.open_maps_menu()
        elif choice[1] == "daily_forecast":
            self.open_daily_forecast()
        elif choice[1] == "stations":
            self.open_station_observations()
        elif choice[1] == "units":
            self.session.openWithCallback(
                self.units_settings_closed,
                UnitSettingsSimple,
                self.unit_manager
            )
        elif choice[1] == "colorselector":
            self.session.open(ColorSelector)
        elif choice[1] == "transparency":
            self.session.open(TransparencySelector)
        elif choice[1] == "info":
            self.session.open(InfoDialog)
        elif choice[1] == "exit":
            self.exit()

    def open_maps_menu(self):
        """Open the weather maps menu"""
        from Screens.ChoiceBox import ChoiceBox

        maps_menu = [
            (_("Weather Maps (Wetterkontor)"), "wetterkontor"),
            (_("Foreca Live Maps (API)"), "foreca_api"),
            (_("Satellite Photos"), "satellite"),
            (_("Back"), "back")
        ]

        self.session.openWithCallback(
            self.maps_menu_callback,
            ChoiceBox,
            title=_("Weather Maps & Satellite"),
            list=maps_menu
        )

    def maps_menu_callback(self, choice):
        """Callback for the maps menu"""
        if choice is None:
            return

        if choice[1] == "wetterkontor":
            # Existing: Wetterkontor regions menu - pass callback
            self.session.openWithCallback(
                self.region_selected_callback,
                ForecaMapsMenu,
                'europe'
            )

        elif choice[1] == "foreca_api":
            self.open_foreca_api_maps()

        elif choice[1] == "satellite":
            self.session.open(
                MessageBox,
                _("Satellite photos coming soon!"),
                MessageBox.TYPE_INFO
            )

        elif choice[1] == "back":
            self.Menu()

    def open_station_observations(self):
        """Open station observations for the current location"""
        print(
            "[DEBUG] open_station_observations called, myloc={0}".format(myloc))

        location_id = ""
        location_name = str(town) if is_valid(town) else "Unknown"

        if myloc == 0:
            location_id = path_loc0.split(
                '/')[0] if '/' in path_loc0 else path_loc0
        elif myloc == 1:
            location_id = path_loc1.split(
                '/')[0] if '/' in path_loc1 else path_loc1
        elif myloc == 2:
            location_id = path_loc2.split(
                '/')[0] if '/' in path_loc2 else path_loc2

        print(
            "[DEBUG] Location ID: {0}, Name: {1}".format(
                location_id,
                location_name))
        if not location_id:
            self.session.open(
                MessageBox,
                _("No location selected"),
                MessageBox.TYPE_INFO)
            return

        from .foreca_stations import ForecaStations
        print("[DEBUG] Opening ForecaStations...")
        self.session.open(
            ForecaStations,
            self.weather_api,
            location_id,
            location_name)

    def _update_station_label(self):
        """Thread to update the nearest station name safely"""
        try:
            # Determine the current location ID
            location_id = ""
            if myloc == 0:
                location_id = path_loc0.split(
                    '/')[0] if '/' in path_loc0 else path_loc0
            elif myloc == 1:
                location_id = path_loc1.split(
                    '/')[0] if '/' in path_loc1 else path_loc1
            elif myloc == 2:
                location_id = path_loc2.split(
                    '/')[0] if '/' in path_loc2 else path_loc2

            if location_id and hasattr(self, 'weather_api'):
                # Request only the nearest station
                self.weather_api.get_token(force_new=True)

                observations = self.weather_api.get_station_observations(
                    location_id, station_limit=1)

                if observations and len(observations) > 0:
                    station_name = observations[0].get('station', 'N/A')
                    station_dist = observations[0].get('distance', '')
                    text = "Station: {0} ({1})".format(
                        station_name, station_dist)
                    print("[DEBUG] Station text: {0}".format(text))

                    def update_ui():
                        try:
                            if "station_name" in self:
                                self["station_name"].setText(text)
                                print("[DEBUG] UI updated: {0}".format(text))
                        except Exception as e:
                            print("[DEBUG] UI update error: {0}".format(e))

                    # Stop previous timer if it exists
                    if hasattr(
                            self,
                            "station_update_timer") and self.station_update_timer:
                        self.station_update_timer.stop()

                    # Create and start a single-shot timer
                    self.station_update_timer = eTimer()
                    self.station_update_timer.callback.append(update_ui)
                    self.station_update_timer.start(0, True)

        except Exception as e:
            print("[Foreca4] Error updating station: {0}".format(e))
            import traceback
            traceback.print_exc()

    def region_selected_callback(self, result=None):
        """Callback when selecting a region (no need to do anything)"""
        pass

    def units_settings_closed(self, result=None):
        """Callback when unit settings are closed"""
        if result:  # If units were changed
            print("[Foreca4] Units changed, reloading display...")
            self.my_cur_weather()
            self.my_forecast_weather()

    def create_default_unit_config(self):
        """Create the default configuration file if it does not exist"""
        if not os.path.exists(unit_file):
            try:
                with open(unit_file, 'w') as f:
                    f.write("# configuration file for units: metric or imperial\n")
                    f.write("metric\n")
                print(
                    "[Foreca4] Created default unit config: {0}".format(unit_file))
            except Exception as e:
                print("[Foreca4] Error creating unit config: {0}".format(e))

    def read_unit_preference(self):
        """Read the unit preference from file"""
        if not os.path.exists(unit_file):
            self.create_default_unit_config()
        try:
            with open(unit_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if line.lower() in ['metric', 'imperial']:
                            return line.lower()
                        else:
                            print(
                                "[Foreca4] Invalid unit in config: '{0}'".format(line))
                            break
        except Exception as e:
            print("[Foreca4] Error reading unit config: {0}".format(e))
        return default_unit

    def get_unit_system_preference(self):
        """Read drive preferences from a configuration file"""
        default_system = 'metric'  # Default to metric

        if os.path.exists(unit_file):
            try:
                with open(unit_file, 'r') as f:
                    content = f.read().strip()
                    if content in ['metric', 'imperial']:
                        return content
            except Exception as e:
                print("[Foreca4] Error reading unit config: {0}".format(e))

        return default_system

    def open_foreca_api_maps(self):
        """Open Foreca API maps with region detection"""
        print("[DEBUG] open_foreca_api_maps called")
        # Check if api_config.txt exists
        config_file = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/api_config.txt"
        if not os.path.exists(config_file):
            self.session.open(
                MessageBox,
                _("API configuration file not found!\n\nPlease create file:\n{0}\n\nwith your Foreca API credentials.").format(config_file),
                MessageBox.TYPE_ERROR,
                timeout=10)
            return

        try:
            # Determine region from current location
            region = self.determine_region_from_location(
                location_id=path_loc0.split('/')[0] if '/' in path_loc0 else path_loc0,
                country_name=country,
                lon=lon,
                lat=lat)

            print(f"[Foreca4] Using region: {region} for maps")

            # Pass region to API
            api = ForecaMapAPI(region=region)

            if not api.check_credentials():
                self.session.open(
                    MessageBox,
                    _("API credentials not configured.\nPlease create api_config.txt file.\n\nExample file created: api_config.txt"),
                    MessageBox.TYPE_ERROR,
                    timeout=10)
                return

            # Use the unit_system property
            print(f"[DEBUG] self.unit_system: {self.unit_system}")
            self.session.open(ForecaMapMenu, api, self.unit_system, region)

        except Exception as e:
            print(f"[Foreca4] Error opening API maps: {e}")
            import traceback
            traceback.print_exc()
            self.session.open(
                MessageBox,
                _("Could not initialize map API.\nCheck configuration."),
                MessageBox.TYPE_ERROR
            )

    def open_daily_forecast(self):
        """Open weekly detailed forecast"""
        location_id = ""
        location_name = str(town) if is_valid(town) else "Unknown"

        if myloc == 0:
            location_id = path_loc0.split(
                '/')[0] if '/' in path_loc0 else path_loc0
        elif myloc == 1:
            location_id = path_loc1.split(
                '/')[0] if '/' in path_loc1 else path_loc1
        elif myloc == 2:
            location_id = path_loc2.split(
                '/')[0] if '/' in path_loc2 else path_loc2

        print(
            "[DEBUG] Opening DailyForecast for location: {0}, name: {1}".format(
                location_id,
                location_name))

        if not self.weather_api.check_credentials():
            print("[DEBUG] API credentials not configured")
            self.session.open(
                MessageBox,
                _("API credentials not configured!\n\nPlease create api_config.txt file."),
                MessageBox.TYPE_ERROR)
            return

        if not location_id:
            self.session.open(
                MessageBox,
                _("No location selected"),
                MessageBox.TYPE_INFO)
            return

        self.session.open(
            DailyForecast,
            self.weather_api,
            location_id,
            location_name)

    def OK(self):
        PY3 = version_info[0] == 3
        if PY3:
            self.session.open(WeatherDetailView, self.weather_api)
        else:
            self.session.open(RadarMapView)

    def savesetcolor(self, indata):
        f = open(
            '/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_color.conf',
            'w')
        f.write(indata)
        f.close()

    def readsetcolor(self):
        global rgbmyr, rgbmyg, rgbmyb
        rgbmyr = 0
        rgbmyg = 80
        rgbmyb = 239
        if os.path.exists(
                "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_color.conf") is True:
            try:
                with open("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_color.conf", "r") as file:
                    contents = file.readlines()
                    a = str(contents[0])
                    trspz = a.rstrip()
                    rgbmyr = trspz.split(' ')[0]
                    rgbmyg = trspz.split(' ')[1]
                    rgbmyb = trspz.split(' ')[2]
                    file.close()
            except BaseException:
                rgbmyr = 0
                rgbmyg = 80
                rgbmyb = 239

    def update_button(self):
        """Update background colors for all plates"""
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))

        # Update colored backgrounds
        self["selection_overlay"].instance.setBackgroundColor(self.color)
        self["color_bg_today"].instance.setBackgroundColor(self.color)
        self["color_bg_forecast"].instance.setBackgroundColor(self.color)
        self["color_bg_sun"].instance.setBackgroundColor(self.color)
        self["color_bg_coords"].instance.setBackgroundColor(self.color)

        # Update transparent overlays
        transparent_color = parseColor(alpha)
        self["transp_bg_today"].instance.setBackgroundColor(transparent_color)
        self["transp_bg_forecast"].instance.setBackgroundColor(
            transparent_color)
        self["transp_bg_sun"].instance.setBackgroundColor(transparent_color)
        self["transp_bg_coords"].instance.setBackgroundColor(transparent_color)
        self["transp_bg_header"].instance.setBackgroundColor(transparent_color)

        # self.my_cur_weather()
        # self.my_forecast_weather()

    def StartPageFirst(self):
        self.readsetcolor()

        self["weather_icon"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/d000.png")
        self["weather_icon"].instance.show()

        self["wind_icon"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/wS.png")
        self["wind_icon"].instance.show()

        self["icon_pressure"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/barometer.png")
        self["icon_pressure"].instance.show()

        self["icon_rain"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/precipitation.png")
        self["icon_rain"].instance.show()

        self["icon_humidity"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/humidity.png")
        self["icon_humidity"].instance.show()

        self["icon_sun"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/sun.png")
        self["icon_sun"].instance.show()

        self["title_section_weather"].text = _("Current weather and forecast")
        self["title_version"].text = "<< ver. " + str(VERSION) + " >>"

        if "title_loading" in self:
            self["title_loading"].text = ""

        # Date
        date_str = str(f_date[0]) if f_date and len(
            f_date) > 0 else _("No date available")

        # Day
        day_str = trans(f_day) if is_valid(f_day) else ""

        self["title_main"].text = f"{trans(str(town))}, {trans(str(country))} - {date_str}"
        if day_str:
            self["title_main"].text += " - " + day_str

        # Day length
        self["day_length"].setText(
            str(conv_day_len(daylen)) if is_valid(daylen) else "N/A"
        )

        # Sunrise / Sunset
        self["sunrise_value"].setText(
            str(sunrise) if is_valid(sunrise) else "N/A")
        self["sunset_value"].setText(
            str(sunset) if is_valid(sunset) else "N/A")

        self["sunrise_label"].setText(_("Sunrise"))
        self["sunset_label"].setText(_("Sunset"))

        self.my_forecast_weather()
        self.my_cur_weather()

        Thread(target=self.mypicload).start()

    def mypicload(self):
        download_pic = '/tmp/385.png ' + 'https://map-cf.foreca.net/teaser/map/light/rain/6/' + \
            str(lon) + '/' + str(lat) + '/317/385.png?names'
        try:
            os.system('wget -O ' + str(download_pic))
        except BaseException:
            pass

    def my_forecast_weather(self):
        self.list = []
        i = len(f_time)
        n = 0

        # Prepare descriptions for batch translation
        descriptions_to_translate = []
        for symb in f_symb:
            if is_valid(symb):
                descriptions_to_translate.append(
                    self.symbolToCondition(str(symb)))
            else:
                descriptions_to_translate.append("Unknown")

        # Translate all descriptions at once
        translated_descriptions = translate_batch_strings(
            descriptions_to_translate)

        while n <= i - 1:
            if int(f_cur_temp[n]) >= 0:
                myf_cur_temp = '+' + str(f_cur_temp[n])
            else:
                myf_cur_temp = str(f_cur_temp[n])

            try:
                minipng = LoadPixmap(cached=True, path=resolveFilename(
                    SCOPE_PLUGINS, "Extensions/Foreca4/thumb/" + str(f_symb[n]) + ".png"))
            except BaseException:
                minipng = LoadPixmap(cached=True, path=resolveFilename(
                    SCOPE_PLUGINS, "Extensions/Foreca4/thumb/n600.png"))

            try:
                f_myw = int(f_wind[n])
                f_myw1 = self.degreesToWindDirection(f_myw)
                minipng1 = LoadPixmap(
                    cached=True,
                    path=resolveFilename(
                        SCOPE_PLUGINS,
                        "Extensions/Foreca4/thumb/" +
                        str(f_myw1) +
                        ".png"))
            except BaseException:
                minipng1 = LoadPixmap(cached=True, path=resolveFilename(
                    SCOPE_PLUGINS, "Extensions/Foreca4/thumb/w360.png"))

            try:
                f_w_s = str(
                    my_speed_wind(
                        f_wind_speed[n],
                        for_wind_speed_recalc)) + ' ' + trans('km/h')
            except BaseException:
                f_w_s = '0.00' + ' ' + trans('km/h')

            # Use translated description
            f_description = translated_descriptions[n] if n < len(
                translated_descriptions) else descriptions_to_translate[n]

            if int(f_flike_temp[n]) >= 0:
                myf_flike_temp = '+' + str(f_flike_temp[n])
            else:
                myf_flike_temp = str(f_flike_temp[n])

            pos8 = trans('Feels like: ') + str(myf_flike_temp) + \
                six.ensure_str(six.unichr(176)) + 'C'

            precip = f_precipitation[n] if n < len(f_precipitation) else '0'
            pos9 = trans('Precipitations:') + ' ' + str(precip) + '%'

            hum_val = f_rel_hum[n] if n < len(f_rel_hum) else '0'
            pos10 = trans('Humidity:') + ' ' + str(hum_val) + '%'

            self.list.append((
                str(f_time[n]) if n < len(f_time) else '',
                trans('Temp'),
                minipng,
                str(myf_cur_temp) + six.ensure_str(six.unichr(176)) + 'C',
                minipng1,
                trans('Wind'),
                str(f_w_s),
                str(f_description),
                str(pos8),
                str(pos9),
                str(pos10)
            ))
            n = n + 1

        from threading import Thread
        Thread(target=self._update_station_label).start()
        self["menu"].setList(self.list)

    def my_cur_weather(self):
        """Update current weather display with proper conversions"""
        # Use unit_manager for conversions
        unit_system = self.unit_manager.get_simple_system()

        # City name
        self["city_name"].setText(str(town) if is_valid(town) else "N/A")

        # Current temperature
        if is_valid(cur_temp):
            if unit_system == 'imperial':

                try:
                    temp_c = float(cur_temp)
                    temp_f = (temp_c * 9 / 5) + 32
                    cur_temp_text = f"{temp_f:.1f}°F"
                except BaseException:
                    cur_temp_text = f"{cur_temp}°C"
            else:
                cur_temp_text = f"{cur_temp}°C"
        else:
            cur_temp_text = "N/A"

        self["temperature_current"].setText(cur_temp_text)

        # Feels like temperature
        if is_valid(fl_temp):
            if unit_system == 'imperial':
                try:
                    temp_c = float(fl_temp)
                    temp_f = (temp_c * 9 / 5) + 32
                    self["temperature_feelslike"].setText(
                        trans("Feels like") + f" {temp_f:.1f}°F")
                except BaseException:
                    self["temperature_feelslike"].setText(
                        trans("Feels like") + f" {fl_temp}°C")
            else:
                self["temperature_feelslike"].setText(
                    trans("Feels like") + f" {fl_temp}°C")
        else:
            self["temperature_feelslike"].setText(trans("Feels like") + " N/A")

        # Wind speed
        if is_valid(wind_speed):
            try:
                wind_kmh = float(wind_speed)
                if unit_system == 'imperial':
                    wind_mph = wind_kmh * 0.621371
                    self["wind_speed_value"].setText(
                        trans("Wind speed") + f" {wind_mph:.1f} mph")
                else:
                    self["wind_speed_value"].setText(
                        trans("Wind speed") + f" {wind_kmh:.1f} km/h")
            except BaseException:
                self["wind_speed_value"].setText(
                    trans("Wind speed") + f" {wind_speed}")

        # Wind gust
        if is_valid(wind_gust):
            try:
                wind_kmh = float(wind_gust)
                if unit_system == 'imperial':
                    wind_mph = wind_kmh * 0.621371
                    self["wind_gust_value"].setText(
                        trans("Gust") + f" {wind_mph:.1f} mph")
                else:
                    self["wind_gust_value"].setText(
                        trans("Gust") + f" {wind_kmh:.1f} km/h")
            except BaseException:
                self["wind_gust_value"].setText(
                    trans("Gust") + f" {wind_gust}")

        # Pressure
        if is_valid(pressure):
            try:
                pressure_mmhg = float(pressure)
                if unit_system == 'imperial':
                    # Convert mmHg to inHg
                    pressure_inhg = pressure_mmhg * 0.03937
                    self["pressure_value"].setText(f"{pressure_inhg:.2f} inHg")
                else:
                    pressure_hpa = pressure_mmhg * 1.33322
                    self["pressure_value"].setText(f"{pressure_hpa:.0f} hPa")
            except BaseException:
                self["pressure_value"].setText(f"{pressure}")

        # Dewpoint
        if is_valid(dewpoint):
            self["dewpoint_value"].setText(
                trans("Dewpoint") +
                " {0}°C".format(dewpoint))
        else:
            self["dewpoint_value"].setText(trans("Dewpoint") + " N/A")

        # Weather icon
        try:
            icon = "{0}.png".format(pic) if is_valid(pic) else "n600.png"
            icon_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/{0}".format(
                icon)
            if os.path.exists(icon_path):
                self["weather_icon"].instance.setPixmapFromFile(icon_path)
        except Exception:
            pass

        # Weather description
        if is_valid(pic):
            description = self.symbolToCondition(str(pic))
            self["weather_description"].setText(trans(description))
        else:
            self["weather_description"].setText("N/A")

        # Wind direction icon
        try:
            if is_valid(wind) and 'w' in str(wind):
                myw = int(str(wind).split('w')[1])
                myw1 = self.degreesToWindDirection(myw)
                wind_icon = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/{0}.png".format(
                    myw1)
                if os.path.exists(wind_icon):
                    self["wind_icon"].instance.setPixmapFromFile(wind_icon)
        except Exception:
            pass

        # Precipitation
        self["rain_value"].setText(
            "{0} ".format(rain_mm) +
            trans("mm") if is_valid(rain_mm) else "N/A")

        # Humidity
        self["humidity_value"].setText(
            "{0}%".format(hum) if is_valid(hum) else "N/A")

        # Force immediate GUI update
        self.invalidate_current_weather_widgets()

    def StartPage(self):
        date_str = ""
        if f_date and len(f_date) > 0:
            date_str = str(f_date[0])
        else:
            date_str = _("No date available")

        day_str = trans(f_day) if is_valid(f_day) else ""

        self["title_main"].text = str(town) + ', ' + \
            trans(str(country)) + ' - ' + date_str
        if day_str:
            self["title_main"].text += ' - ' + day_str

        self["mytitel1"].text = _("Current weather and forecast")
        self["mytitel2"].text = "<< ver. " + str(VERSION) + ' >>'
        self["Titel3"].text = ""
        self["Titel5"].text = ""
        self["Titel2"].text = _("Please wait ...")

    def keyNumberGlobal(self, number):
        self.tag = number
        self.Zukunft(self.tag)

    def titel(self):
        self.setTitle(_("Foreca Weather Forecast") + " " + _("v.") + VERSION)

    def _load_favorite(self, fav_index, path_loc):
        """
        Load a favorite (single function for all favorites)

        Args:
            fav_index: 0=Home, 1=Fav1, 2=Fav2
            path_loc: location path (e.g. "103169070/Rome-Italy")
        """
        global myloc, town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country
        global f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum
        global lon, lat, sunrise, daylen, sunset, f_day

        myloc = fav_index
        location_id = path_loc.split('/')[0] if '/' in path_loc else path_loc

        # 1. CURRENT WEATHER VIA API (or scraping fallback)
        if self.weather_api.check_credentials():
            result_current = self.weather_api.get_current_weather(location_id)
            if (
                result_current
                and isinstance(result_current, (list, tuple))
                and len(result_current) == 17
                and result_current[0] != 'N/A'
            ):
                town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current
                print(
                    "[Foreca4] Fav{0}: Current weather via API".format(fav_index))
            else:
                town = cur_temp = fl_temp = dewpoint = pic = wind = wind_speed = wind_gust = rain_mm = hum = pressure = country = lon = lat = sunrise = daylen = sunset = 'N/A'

        # self.my_cur_weather()

        # 2. FORECAST VIA API (or scraping fallback)
        if self.weather_api.check_credentials():
            result_forecast = self.weather_api.get_hourly_forecast(
                location_id, days=1)
            if result_forecast and result_forecast[0] != 'N/A':
                f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = result_forecast

        self.my_forecast_weather()

        # 3. UPDATE INTERFACE
        self["day_len"].setText(str(conv_day_len(daylen))
                                if is_valid(daylen) else "N/A")
        self["sunrise_val"].setText(
            str(sunrise) if is_valid(sunrise) else "N/A")
        self["sunset_val"].setText(str(sunset) if is_valid(sunset) else "N/A")

        # 4. LOAD MAP IN BACKGROUND
        Thread(target=self.mypicload).start()

        # 5. UPDATE TITLE AND DAILY FORECASTS
        self.titel()
        self.Zukunft(0)

    def Fav0(self):
        """Home (Blue button)"""
        self._load_favorite(0, path_loc0)

    def Fav1(self):
        """Favorite 1 (Green button)"""
        self._load_favorite(1, path_loc1)

    def Fav2(self):
        """Favorite 2 (Yellow button)"""
        self._load_favorite(2, path_loc2)

    def Zukunft(self, ztag=0):
        """Load forecast for a specific day"""
        global f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day

        self.tag = ztag

        # Determine which favorite is active
        path_loc = ""
        if myloc == 0:
            path_loc = path_loc0
        elif myloc == 1:
            path_loc = path_loc1
        elif myloc == 2:
            path_loc = path_loc2
        else:
            path_loc = path_loc0  # Default

        location_id = path_loc.split('/')[0] if '/' in path_loc else path_loc

        # FIRST TRY API
        if self.weather_api.check_credentials() and location_id:
            result_forecast = self.weather_api.get_hourly_forecast(
                location_id, days=ztag + 1)
            if result_forecast and result_forecast[0] != 'N/A':
                f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = result_forecast
                self.my_forecast_weather()
                self.StartPage()
                return

        self.my_forecast_weather()
        self.StartPage()

    def info(self):
        self.session.open(InfoDialog)

    def left(self):
        if self.tag > 0:
            self.tag = self.tag - 1
            self.Zukunft(self.tag)

    def right(self):
        if self.tag < 9:
            self.tag = self.tag + 1
            self.Zukunft(self.tag)

    def up(self):
        self["menu"].pageUp()

    def down(self):
        self["menu"].pageDown()

    def previousDay(self):
        self.left()

    def nextDay(self):
        self.right()

    def determine_region_from_location(
            self,
            location_id,
            country_name="",
            lon="",
            lat=""):
        """
        Determine the optimal API region based on location.
        Returns: 'eu' or 'us'
        """
        # Default to Europe
        region = 'eu'

        # 1. Try to get coordinates from current data
        try:
            if lon and lat and lon != 'N/A' and lat != 'N/A':
                lon_float = float(lon)
                lat_float = float(lat)

                # Check if location is in North America
                if (-125.0 <= lon_float <= -66.0) and (24.0 <= lat_float <= 49.0):
                    return 'us'
                # Could add more regions here in future
        except (ValueError, TypeError):
            pass

        # 2. Check by country name (case insensitive)
        country_lower = str(country_name).lower()

        us_countries = [
            'united states', 'usa', 'u.s.a', 'u.s.', 'america',
            'canada', 'mexico'
        ]

        for us_country in us_countries:
            if us_country in country_lower:
                return 'us'

        # 3. Check by location ID patterns (if it contains US cities/IDs)
        location_str = str(location_id).lower()
        us_patterns = ['new york', 'los angeles', 'chicago', 'miami',
                       'texas', 'california', 'florida', '/us/', '/usa/']

        for pattern in us_patterns:
            if pattern in location_str:
                return 'us'

        return region

    def symbolToCondition(self, symbol):
        symbol_map = {
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
            'n600': _('Fog')}
        return symbol_map.get(symbol, _('Unknown'))

    def degreesToWindDirection(self, degrees):
        try:
            directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
            index = round(degrees / 45) % 8
            return "w" + directions[int(index)]
        except BaseException:
            return "w360"

    def red(self):
        self.session.open(ColorSelector)

    def clean_foreca_cache(self):
        """Clean Foreca cache files"""
        cache_dir = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"
        if not os.path.exists(cache_dir):
            return
        import time
        current_time = time.time()

        try:
            deleted = 0
            kept = 0

            for filename in os.listdir(cache_dir):
                filepath = os.path.join(cache_dir, filename)

                # Keep important files
                if filename in ["token.json", "capabilities.json"]:
                    kept += 1
                    continue

                if os.path.isfile(filepath):
                    # Delete temporary display files (they start with
                    # 'display_' or 'merged_')
                    if filename.startswith(
                            ('display_', 'merged_', 'foreca4_merged_', 'foreca4_display_')):
                        try:
                            os.remove(filepath)
                            deleted += 1
                        except BaseException:
                            pass
                    else:
                        # For tile cache files, keep if recent (less than 1
                        # day)
                        file_age = current_time - os.path.getmtime(filepath)
                        if file_age > 86400:  # 1 day
                            try:
                                os.remove(filepath)
                                deleted += 1
                            except BaseException:
                                pass
                        else:
                            kept += 1

            print(
                f"[Foreca4] Cache cleanup: {deleted} files deleted, {kept} files kept")

        except Exception as e:
            print("[Foreca4] Error cleaning cache: {0}".format(e))

    def cleanup_background_threads(self):
        """Clean up any background threads"""
        # Set a flag to stop threads
        self.stop_threads = True
        # You might need more sophisticated thread management
        print("[Foreca4] Cleaning up background threads")

    def invalidate_current_weather_widgets(self):
        """Force GUI update for current weather widgets"""
        widget_names = [
            "temperature_feelslike",
            "wind_speed_value",
            "wind_gust_value",
            "dewpoint_value",
            "city_name",
            "temperature_current",
            "weather_description",
            "rain_value",
            "humidity_value",
            "pressure_value",
            "day_length",
            "sunrise_value",
            "sunset_value",
            "sunrise_label",
            "sunset_label",
            "title_main",
            "title_section_weather",
            "title_version"
        ]

        for name in widget_names:
            try:
                if name in self:
                    self[name].instance.invalidate()
            except BaseException:
                pass

    def exit(self):
        """Exit plugin and optionally clean cache"""
        # Stop timers and clean
        if hasattr(self, 'station_timer'):
            self.station_timer.stop()
        if hasattr(self, 'station_update_timer'):
            self.station_update_timer.stop()

        # Stop any background threads
        self.cleanup_background_threads()

        # Config Save
        trspz = str(rgbmyr) + ' ' + str(rgbmyg) + ' ' + str(rgbmyb)
        self.savesetcolor(trspz)
        save_alpha(alpha)

        # Clean cache on exit (optional)
        self.clean_foreca_cache()
        self.close()


class ColorSelector(Screen):

    def __init__(self, session, args=0):
        self.skin = load_skin_for_class(ColorSelector)
        self.session = session
        Screen.__init__(self, session)
        self.setTitle(_('Color Selector'))

        self.color_list = []
        self.source_names = []
        self.translated_names = []
        self.color_data = []

        self["menu"] = MenuList([])
        self["color_name_label"] = Label()
        self["color_name_label"].setText(_('Color name'))
        self["color_info_label"] = Label()
        self["color_info_label"].setText(_('Color data'))

        self["color_preview"] = Pixmap()
        self["background_plate"] = Label("N/A")
        self["selection_overlay"] = Label("N/A")

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self.exit_screen,
                "left": self.page_up,
                "right": self.page_down,
                "up": self.move_up,
                "down": self.move_down,
                "ok": self.confirm_selection,
            }, -1
        )

        self.onShown.append(self.initialize_data)

    def initialize_data(self):
        current_color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["background_plate"].instance.setBackgroundColor(current_color)
        self["selection_overlay"].instance.setBackgroundColor(
            parseColor(alpha))

        self.color_list = []
        self.source_names = []
        self.translated_names = []
        self.color_data = []
        self.last_processed_index = 0
        if os.path.exists(data_file):
            try:
                with open(data_file, "r", encoding="utf-8") as file_handle:
                    file_lines = file_handle.readlines()

                for idx, line_content in enumerate(file_lines):
                    line_content = line_content.strip()
                    if not line_content:
                        continue

                    if " #" in line_content:
                        color_name, color_values = line_content.split(" #", 1)
                        color_name = color_name.strip()
                        color_values = color_values.strip()
                    else:
                        color_name = line_content.strip()
                        color_values = ""

                    self.source_names.append(color_name)
                    self.translated_names.append(color_name)
                    self.color_data.append(color_values)
                    self.color_list.append(f"{idx}. {color_name}")

            except Exception as error:
                print(f"[ColorSelector] Error reading file: {error}")
                self.color_list.append("0. " + _("Error loading colors"))
                self.source_names.append("")
                self.translated_names.append("")
                self.color_data.append("")
        else:
            self.color_list.append("0. " + _("Color file not found"))
            self.source_names.append("")
            self.translated_names.append("")
            self.color_data.append("")

        self["menu"].l.setList(self.color_list)
        self["menu"].selectionEnabled(1)

        print(f"[ColorSelector] Loaded items: {len(self.source_names)}")

        if self.color_list:
            for idx in range(0, min(30, len(self.source_names))):
                if self.translated_names[idx] == self.source_names[idx]:
                    translated_text = self.translate_color_name(
                        self.source_names[idx])
                    if translated_text != self.source_names[idx]:
                        self.translated_names[idx] = translated_text
                        self.color_list[idx] = f"{idx}. {translated_text}"

            self.refresh_display()
            self.update_current_selection(0)

            if len(self.source_names) > 30:
                self.process_batch_async(30, 150)
            self.last_processed_index = 150

    def process_batch_async(self, start_position, end_position):
        import threading

        def translation_worker():
            nonlocal end_position  # Dichiara che stai usando la variabile esterna
            end_position = min(end_position, len(self.source_names))
            print(
                f"[ColorSelector] Processing range {start_position} - {end_position}")

            batch_size = 20
            for batch_start in range(start_position, end_position, batch_size):
                batch_end = min(batch_start + batch_size, end_position)
                has_updates = False

                for position in range(batch_start, batch_end):
                    if self.translated_names[position] == self.source_names[position]:
                        translated_text = self.translate_color_name(
                            self.source_names[position])
                        if translated_text != self.source_names[position]:
                            self.translated_names[position] = translated_text
                            self.color_list[position] = f"{position}. {translated_text}"
                            has_updates = True

                if has_updates:
                    def safe_refresh():
                        try:
                            self.refresh_display()
                        except Exception as error:
                            print(f"[ColorSelector] Update error: {error}")

                    update_timer = eTimer()
                    update_timer.callback.append(safe_refresh)
                    update_timer.start(0, True)

                print(
                    f"[ColorSelector] Processed batch {batch_start}-{batch_end}")

            print(
                f"[ColorSelector] Completed range {start_position}-{end_position}")
            self.last_processed_index = max(
                self.last_processed_index, end_position)

        worker_thread = threading.Thread(
            target=translation_worker, daemon=True)
        worker_thread.start()

    def translate_color_name(self, original_text):
        if not original_text:
            return original_text

        print(f"[ColorSelector] Translating: '{original_text}'")
        try:
            if '-' in original_text:
                text_parts = original_text.split('-')
                translated_parts = []

                for segment in text_parts:
                    segment = segment.strip()
                    if segment:
                        translated_segment = trans(segment)
                        translated_parts.append(translated_segment)
                    else:
                        translated_parts.append("")

                final_text = '-'.join(translated_parts)
                print(
                    f"[ColorSelector] Result: '{original_text}' -> '{final_text}'")
                return final_text

            final_text = trans(original_text)
            print(
                f"[ColorSelector] Result: '{original_text}' -> '{final_text}'")
            return final_text

        except Exception as error:
            print(
                f"[ColorSelector] ERROR translating '{original_text}': {error}")
            return original_text

    def update_current_selection(self, selected_index):
        print(f"[ColorSelector] Updating selection {selected_index}")
        if 0 <= selected_index < len(self.translated_names):
            if self.translated_names[selected_index] == self.source_names[selected_index]:
                translated_text = self.translate_color_name(
                    self.source_names[selected_index])
                if translated_text != self.translated_names[selected_index]:
                    self.translated_names[selected_index] = translated_text
                    self.color_list[selected_index] = f"{selected_index}. {translated_text}"
                    self.refresh_display()

            display_name = self.translated_names[selected_index]
            self["color_name_label"].setText(display_name)

            if selected_index < len(
                    self.color_data) and self.color_data[selected_index]:
                color_values = self.color_data[selected_index]
                value_parts = color_values.split(' ')

                if len(value_parts) >= 4:
                    html_code = '#' + value_parts[0]
                    red_value = int(value_parts[1])
                    green_value = int(value_parts[2])
                    blue_value = int(value_parts[3])

                    # Create color object
                    color_object = gRGB(red_value, green_value, blue_value)

                    # Calculate brightness for text contrast (0-255)
                    brightness = (
                        red_value * 299 + green_value * 587 + blue_value * 114) / 1000

                    # Choose text color based on background brightness
                    if brightness > 128:
                        # Dark text for light backgrounds
                        text_color = parseColor("#000000")  # Black
                    else:
                        # Light text for dark backgrounds
                        text_color = parseColor("#FFFFFF")  # White

                    # --- COLOR_NAME_LABEL (colored text) ---
                    # The color_name_label text takes the selected color
                    self["color_name_label"].instance.setForegroundColor(
                        color_object)

                    # --- COLOR_INFO_LABEL (colored background with contrasting text) ---
                    # Colored background
                    self["color_info_label"].instance.setBackgroundColor(
                        color_object)
                    self["color_info_label"].instance.setTransparent(False)
                    # Contrasting text (white or black for readability)
                    self["color_info_label"].instance.setForegroundColor(
                        text_color)

                    # --- COLOR_PREVIEW ---
                    self["color_preview"].instance.setBackgroundColor(
                        color_object)

                    info_text = (_('HTML') + ' (' + html_code + ')   ' +
                                 _('Red') + ' (' + str(red_value) + ')   ' +
                                 _('Green') + ' (' + str(green_value) + ')   ' +
                                 _('Blue') + ' (' + str(blue_value) + ')')

                    self["color_info_label"].setText(info_text)

    def refresh_display(self, apply_sort=False):
        print("[ColorSelector] Refreshing display")

        if apply_sort:
            combined_data = list(zip(self.translated_names, self.color_list,
                                     self.source_names, self.color_data))
            combined_data.sort(key=lambda item: item[0].lower())
            self.translated_names, self.color_list, self.source_names, self.color_data = zip(
                *combined_data)
            self.translated_names = list(self.translated_names)
            self.color_list = list(self.color_list)
            self.source_names = list(self.source_names)
            self.color_data = list(self.color_data)

        self["menu"].l.setList(self.color_list)
        current_position = self["menu"].getCurrentIndex()

        if current_position < len(self.translated_names):
            self["color_name_label"].setText(
                self.translated_names[current_position])

        self["menu"].instance.invalidate()
        self["color_name_label"].instance.invalidate()

    def move_up(self):
        current_position = self["menu"].getCurrentIndex()
        new_position = max(0, current_position - 1)
        self["menu"].goLineUp()
        self.update_current_selection(new_position)

    def move_down(self):
        current_position = self["menu"].getCurrentIndex()
        new_position = min(len(self.color_list) - 1, current_position + 1)
        self["menu"].goLineDown()
        self.update_current_selection(new_position)

    def page_up(self):
        self["menu"].pageUp()
        current_position = self["menu"].getCurrentIndex()
        self.update_current_selection(current_position)

        if current_position + 100 > self.last_processed_index:
            new_limit = min(self.last_processed_index +
                            100, len(self.source_names))
            print(
                f"[ColorSelector] Preloading: {self.last_processed_index} -> {new_limit}")
            self.process_batch_async(self.last_processed_index, new_limit)
            self.last_processed_index = new_limit

    def page_down(self):
        self["menu"].pageDown()
        current_position = self["menu"].getCurrentIndex()
        self.update_current_selection(current_position)

        if current_position + 100 > self.last_processed_index:
            new_limit = min(self.last_processed_index +
                            100, len(self.source_names))
            print(
                f"[ColorSelector] Preloading: {self.last_processed_index} -> {new_limit}")
            self.process_batch_async(self.last_processed_index, new_limit)
            self.last_processed_index = new_limit

    def confirm_selection(self):
        global rgbmyr, rgbmyg, rgbmyb
        current_position = self["menu"].getCurrentIndex()

        if current_position < len(
                self.color_data) and self.color_data[current_position]:
            color_values = self.color_data[current_position]
            value_parts = color_values.split(' ')

            if len(value_parts) >= 4:
                rgbmyr = value_parts[1]
                rgbmyg = value_parts[2]
                rgbmyb = value_parts[3]

        self.close()

    def exit_screen(self):
        self.close()


class InfoDialog(Screen):

    def __init__(self, session):
        self.skin = load_skin_for_class(InfoDialog)
        Screen.__init__(self, session)
        self['version_label'] = Label(
            _('Foreca 4 Weather and Forecast') +
            ' ver. ' +
            str(VERSION))

        self['author_label'] = Label(
            _('Created by @Bauernbub'))

        self['mod_label'] = Label(
            _('mod Lululla, 2026'))

        self['website_label'] = Label(
            _('https://linuxsat-support.com'))

        self["background_plate"] = Label("N/A")
        self["selection_overlay"] = Label("N/A")

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self.exit_dialog,
                'ok': self.exit_dialog,
            }, -1
        )

        self.onShow.append(self.initialize_colors)

    def initialize_colors(self):
        """Initialize the background colors using current RGB and alpha values"""
        current_color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["background_plate"].instance.setBackgroundColor(current_color)
        self["selection_overlay"].instance.setBackgroundColor(
            parseColor(alpha))

        print(
            f"[InfoDialog] Colors initialized - RGB: {rgbmyr},{rgbmyg},{rgbmyb} Alpha: {alpha}")

    def exit_dialog(self):
        """Close the dialog"""
        self.close()


class WeatherDetailView(Screen):
    """
    Enhanced weather detail screen with today and tomorrow forecasts
    """

    def __init__(self, session, weather_api):
        self.skin = load_skin_for_class(WeatherDetailView)
        Screen.__init__(self, session)

        # Core data
        self.weather_api = weather_api
        self.location_data = self._load_location_data()
        self.weather_data = self._fetch_weather_data()

        # DEBUG: stampa i dati ricevuti
        print(f"[WeatherDetailView] weather_data: {self.weather_data}")
        print(f"[WeatherDetailView] town: {self.weather_data.get('town')}")
        print(
            f"[WeatherDetailView] today keys: {self.weather_data.get('today', {}).keys()}")

        # Initialize UI components
        self._init_ui_elements()
        self._setup_actions()

        # Event hooks
        self.onLayoutFinish.append(self._on_layout_finished)
        self.onShow.append(self._on_screen_shown)

    def _load_location_data(self):
        """Load location based on myloc setting"""
        # global myloc, path_loc0, path_loc1, path_loc2, lat, lon

        location_paths = [path_loc0, path_loc1, path_loc2]
        selected_path = location_paths[myloc] if 0 <= myloc < 3 else path_loc0
        location_id = selected_path.split(
            '/')[0] if '/' in selected_path else selected_path

        return {
            'path': selected_path,
            'id': location_id,
            'lat': lat,
            'lon': lon
        }

    def _fetch_weather_data(self):
        """Fetch weather data from API or use fallback"""
        default_data = {
            'town': 'N/A',
            'country': 'N/A',
            'lat': self.location_data.get('lat', 'N/A'),
            'lon': self.location_data.get('lon', 'N/A'),
            'today': {},
            'tomorrow': {}
        }

        if not (self.weather_api and self.weather_api.check_credentials()):
            return default_data

        try:
            data = self.weather_api.get_today_tomorrow_details(
                self.location_data['id'])
            return data if data else default_data
        except Exception as e:
            print(f"[WeatherDetailView] Error fetching data: {e}")
            return default_data

    def _init_ui_elements(self):
        """Initialize all UI widgets"""
        # Title section
        self['title_main'] = Label(_('Weather Radar'))
        self['title_location'] = Label()
        self['title_today'] = Label(_('Weather today'))
        self['title_tomorrow'] = Label(_('Weather tomorrow'))

        # Summary text
        self['summary_today'] = Label()
        self['summary_tomorrow'] = Label()

        # Period labels
        self['label_morning_1'] = Label(_('Morning'))
        self['label_morning_2'] = Label(_('Morning'))
        self['label_afternoon_1'] = Label(_('Afternoon'))
        self['label_afternoon_2'] = Label(_('Afternoon'))
        self['label_evening_1'] = Label(_('Evening'))
        self['label_evening_2'] = Label(_('Evening'))
        self['label_overnight_1'] = Label(_('Overnight'))
        self['label_overnight_2'] = Label(_('Overnight'))

        # Temperature displays
        self['temp_morning_1'] = Label()
        self['temp_morning_2'] = Label()
        self['temp_afternoon_1'] = Label()
        self['temp_afternoon_2'] = Label()
        self['temp_evening_1'] = Label()
        self['temp_evening_2'] = Label()
        self['temp_overnight_1'] = Label()
        self['temp_overnight_2'] = Label()

        # Temperature labels
        self['temp_label_morning_1'] = Label()
        self['temp_label_morning_2'] = Label()
        self['temp_label_afternoon_1'] = Label()
        self['temp_label_afternoon_2'] = Label()
        self['temp_label_evening_1'] = Label()
        self['temp_label_evening_2'] = Label()
        self['temp_label_overnight_1'] = Label()
        self['temp_label_overnight_2'] = Label()

        # Symbol pixmaps
        self['symbol_morning_1'] = Pixmap()
        self['symbol_morning_2'] = Pixmap()
        self['symbol_afternoon_1'] = Pixmap()
        self['symbol_afternoon_2'] = Pixmap()
        self['symbol_evening_1'] = Pixmap()
        self['symbol_evening_2'] = Pixmap()
        self['symbol_overnight_1'] = Pixmap()
        self['symbol_overnight_2'] = Pixmap()

        # Radar map
        self['radar_map'] = Pixmap()

        # Coordinate displays
        self['icon_longitude'] = Pixmap()
        self['icon_latitude'] = Pixmap()
        self['value_longitude'] = Label()
        self['value_latitude'] = Label()

        # Background plates
        self["background_plate"] = Label("N/A")
        self["selection_overlay"] = Label("N/A")

    def _setup_actions(self):
        """Setup action map for navigation - METODO MANCANTE"""
        self["actions"] = ActionMap(
            ["OkCancelActions", "DirectionActions"],
            {
                "cancel": self._close_screen,
                "ok": self._load_simple_radar,
            }, -1
        )

    def _on_layout_finished(self):
        """Called when layout is finished - load static content"""
        self._load_radar_map()
        self._load_coordinate_icons()
        self._load_weather_symbols()
        self._update_coordinate_values()
        self._setup_temperature_labels()

    def _on_screen_shown(self):
        """Called when screen is shown - update dynamic content"""
        print("[WeatherDetailView] _on_screen_shown START")

        print(f"[WeatherDetailView] Widgets disponibili: {list(self.keys())}")

        self._update_titles()
        self._update_summaries()
        self._update_temperature_values()
        self._update_background_colors()
        self._start_translation_thread()

        if 'title_location' in self:
            print(
                f"[WeatherDetailView] title_location text: {self['title_location'].text}")
        if 'summary_today' in self:
            print(
                f"[WeatherDetailView] summary_today text: {self['summary_today'].text}")
        if 'temp_morning_1' in self:
            print(
                f"[WeatherDetailView] temp_morning_1 text: {self['temp_morning_1'].text}")

        print("[WeatherDetailView] _on_screen_shown END")

    def _load_simple_radar(self):
        self.session.open(RadarMapView)

    def _load_radar_map(self):
        """Load radar map if available"""
        radar_path = "/tmp/385.png"
        if os.path.exists(radar_path):
            self['radar_map'].instance.setPixmapFromFile(radar_path)
            self['radar_map'].instance.show()

    def _load_coordinate_icons(self):
        """Load longitude/latitude icons"""
        base_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/"

        lon_path = os.path.join(base_path, "longitude.png")
        if os.path.exists(lon_path):
            self['icon_longitude'].instance.setPixmapFromFile(lon_path)
            self['icon_longitude'].instance.show()

        lat_path = os.path.join(base_path, "latitude.png")
        if os.path.exists(lat_path):
            self['icon_latitude'].instance.setPixmapFromFile(lat_path)
            self['icon_latitude'].instance.show()

    def _load_weather_symbols(self):
        """Load weather symbols for both days"""
        today = self.weather_data.get('today', {})
        tomorrow = self.weather_data.get('tomorrow', {})

        self._set_symbols_for_day('1', today)
        self._set_symbols_for_day('2', tomorrow)

    def _setup_temperature_labels(self):
        """Set up temperature unit labels"""
        self['temp_label_morning_1'].setText("°C")
        self['temp_label_morning_2'].setText("°C")
        self['temp_label_afternoon_1'].setText("°C")
        self['temp_label_afternoon_2'].setText("°C")
        self['temp_label_evening_1'].setText("°C")
        self['temp_label_evening_2'].setText("°C")
        self['temp_label_overnight_1'].setText("°C")
        self['temp_label_overnight_2'].setText("°C")

    def _set_symbols_for_day(self, day_suffix, day_data):
        """Set weather symbols for a specific day"""
        periods = ['morning', 'afternoon', 'evening', 'overnight']
        symbol_map = {
            'morning': 'symbol_morning_',
            'afternoon': 'symbol_afternoon_',
            'evening': 'symbol_evening_',
            'overnight': 'symbol_overnight_'
        }

        base_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/"

        for period in periods:
            period_data = day_data.get(period, {})
            symbol_code = period_data.get('symbol', 'd000')
            symbol_path = os.path.join(base_path, f"{symbol_code}.png")

            widget_name = f"{symbol_map[period]}{day_suffix}"
            if os.path.exists(symbol_path):
                self[widget_name].instance.setPixmapFromFile(symbol_path)
                self[widget_name].instance.show()

    def _update_coordinate_values(self):
        """Update latitude and longitude values"""
        self['value_latitude'].text = str(self.weather_data.get('lat', 'N/A'))
        self['value_longitude'].text = str(self.weather_data.get('lon', 'N/A'))

    def _update_titles(self):
        """Update all titles with translated text"""
        self['title_today'].text = str(_('Weather today'))
        self['title_tomorrow'].text = str(_('Weather tomorrow'))

        town_name = self.weather_data.get('town', 'N/A')
        self['title_location'].text = str(trans(town_name))

    def _update_summaries(self):
        """Update weather summaries for both days"""
        today = self.weather_data.get('today', {})
        tomorrow = self.weather_data.get('tomorrow', {})

        self['summary_today'].text = self._format_summary(today)
        self['summary_tomorrow'].text = self._format_summary(tomorrow)

    def _format_summary(self, day_data):
        """Format weather summary for a day"""
        weather_text = day_data.get('text', 'N/A')
        max_temp = day_data.get('max_temp', 'N/A')
        min_temp = day_data.get('min_temp', 'N/A')
        rain = day_data.get('rain_mm', '0')
        return f"{weather_text} {max_temp}°C, {min_temp}°C. {rain} mm."

    def _update_temperature_values(self):
        """Update temperature values for all periods"""
        today = self.weather_data.get('today', {})
        tomorrow = self.weather_data.get('tomorrow', {})

        # Today
        self['temp_morning_1'].text = str(
            today.get(
                'morning', {}).get(
                'temp', 'N/A'))
        self['temp_afternoon_1'].text = str(
            today.get(
                'afternoon', {}).get(
                'temp', 'N/A'))
        self['temp_evening_1'].text = str(
            today.get(
                'evening', {}).get(
                'temp', 'N/A'))
        self['temp_overnight_1'].text = str(
            today.get(
                'overnight', {}).get(
                'temp', 'N/A'))

        # Tomorrow
        self['temp_morning_2'].text = str(
            tomorrow.get(
                'morning', {}).get(
                'temp', 'N/A'))
        self['temp_afternoon_2'].text = str(
            tomorrow.get(
                'afternoon', {}).get(
                'temp', 'N/A'))
        self['temp_evening_2'].text = str(
            tomorrow.get(
                'evening', {}).get(
                'temp', 'N/A'))
        self['temp_overnight_2'].text = str(
            tomorrow.get(
                'overnight', {}).get(
                'temp', 'N/A'))

    def _update_background_colors(self):
        """Update background colors with current settings"""
        # global rgbmyr, rgbmyg, rgbmyb, alpha
        bg_color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["background_plate"].instance.setBackgroundColor(bg_color)
        self["selection_overlay"].instance.setBackgroundColor(
            parseColor(alpha))

    def _start_translation_thread(self):
        """Start background thread for translations"""
        from threading import Thread
        Thread(target=self._translate_content).start()

    def _translate_content(self):
        """Translate dynamic content in background"""
        try:
            self['title_today'].text = _('Weather today')
            self['title_tomorrow'].text = _('Weather tomorrow')
            self['title_location'].text = str(
                trans(self.weather_data.get('town', 'N/A')))

            today = self.weather_data.get('today', {})
            tomorrow = self.weather_data.get('tomorrow', {})

            self['summary_today'].text = str(
                trans(self._format_summary(today)))
            self['summary_tomorrow'].text = str(
                trans(self._format_summary(tomorrow)))
        except Exception as e:
            print(f"[WeatherDetailView] Translation error: {e}")

    def _close_screen(self):
        """Close the screen"""
        self.close()


class RadarMapView(Screen):
    """
    Simple radar map view with location coordinates
    """

    def __init__(self, session, weather_api):
        self.skin = load_skin_for_class(RadarMapView)
        Screen.__init__(self, session)

        # Core data
        self.weather_api = weather_api
        self.location_data = self._load_location_data()
        self.coordinates = self._fetch_coordinates()

        # Initialize UI
        self._init_ui_elements()
        self._setup_actions()

        # Event hooks
        self.onLayoutFinish.append(self._load_static_content)
        self.onShow.append(self._update_dynamic_content)

    def _load_location_data(self):
        """Load location based on myloc setting"""
        location_paths = [path_loc0, path_loc1, path_loc2]
        selected_path = location_paths[myloc] if 0 <= myloc < 3 else path_loc0

        location_id = selected_path.split(
            '/')[0] if '/' in selected_path else selected_path

        return {
            'path': selected_path,
            'id': location_id
        }

    def _fetch_coordinates(self):
        """Fetch coordinates from API or use defaults"""
        coordinates = {
            'lat': lat,
            'lon': lon
        }

        if self.weather_api and self.weather_api.check_credentials():
            try:
                location_data = self.weather_api._get_location_details(
                    self.location_data['id'])
                if location_data:
                    coordinates['lat'] = location_data.get('lat', lat)
                    coordinates['lon'] = location_data.get('lon', lon)
            except Exception as e:
                print(f"[RadarMapView] Error fetching coordinates: {e}")

        return coordinates

    def _init_ui_elements(self):
        """Initialize all UI widgets"""
        # Title
        self['title'] = Label(_('Weather Radar'))

        # Radar map
        self['radar_map'] = Pixmap()

        # Coordinate icons and values
        self['icon_longitude'] = Pixmap()
        self['icon_latitude'] = Pixmap()
        self['value_latitude'] = Label()
        self['value_longitude'] = Label()

        # Background plates
        self["background_plate"] = Label("N/A")
        self["selection_overlay"] = Label("N/A")

    def _setup_actions(self):
        """Setup action map for navigation"""
        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self._close_screen,
                "ok": self._show_info_dialog,
            }, -1
        )

    def _load_static_content(self):
        """Load static content (images)"""
        self._load_radar_map()
        self._load_coordinate_icons()
        self._update_coordinate_values()

    def _update_dynamic_content(self):
        """Update dynamic content (colors)"""
        self._update_background_colors()

    def _load_radar_map(self):
        """Load radar map if available"""
        radar_path = "/tmp/385.png"
        if os.path.exists(radar_path):
            self['radar_map'].instance.setPixmapFromFile(radar_path)
            self['radar_map'].instance.show()
        else:
            print(f"[RadarMapView] Radar map not found: {radar_path}")

    def _load_coordinate_icons(self):
        """Load longitude/latitude icons"""
        base_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/"

        # Longitude icon
        lon_path = os.path.join(base_path, "longitude.png")
        if os.path.exists(lon_path):
            self['icon_longitude'].instance.setPixmapFromFile(lon_path)
            self['icon_longitude'].instance.show()
        else:
            print(f"[RadarMapView] Longitude icon not found: {lon_path}")

        # Latitude icon
        lat_path = os.path.join(base_path, "latitude.png")
        if os.path.exists(lat_path):
            self['icon_latitude'].instance.setPixmapFromFile(lat_path)
            self['icon_latitude'].instance.show()
        else:
            print(f"[RadarMapView] Latitude icon not found: {lat_path}")

    def _update_coordinate_values(self):
        """Update latitude and longitude values"""
        self['value_latitude'].text = str(self.coordinates['lat'])
        self['value_longitude'].text = str(self.coordinates['lon'])

        print(
            f"[RadarMapView] Coordinates: Lat={self.coordinates['lat']}, Lon={self.coordinates['lon']}")

    def _update_background_colors(self):
        """Update background colors with current settings"""
        bg_color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["background_plate"].instance.setBackgroundColor(bg_color)

        selection_color = parseColor(alpha)
        self["selection_overlay"].instance.setBackgroundColor(selection_color)

    def _show_info_dialog(self):
        """Show information dialog"""
        self.session.open(InfoDialog)

    def _close_screen(self):
        """Close the screen"""
        self.close()


class TransparencySelector(Screen):

    def __init__(self, session):
        self.skin = load_skin_for_class(TransparencySelector)
        Screen.__init__(self, session)

        self.transparency_levels = [
            {"name": "56%", "value": "#90000000"},
            {"name": "50%", "value": "#80000000"},
            {"name": "44%", "value": "#70000000"},
            {"name": "38%", "value": "#60000000"},
            {"name": "31%", "value": "#50000000"},
            {"name": "25%", "value": "#40000000"},
            {"name": "19%", "value": "#30000000"},
            {"name": "13%", "value": "#20000000"},
            {"name": "6%", "value": "#10000000"}
        ]

        self["menu"] = MenuList([])
        self['title_label'] = Label(_('Window transparency'))

        self["background_plate"] = Label("N/A")
        self["selection_overlay"] = Label("N/A")

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions",
                "ShortcutActions",
                "WizardActions"
            ],
            {
                "cancel": self.exit_screen,
                "ok": self.confirm_selection,
            }, -1
        )

        self.onShow.append(self.initialize_display)

    def confirm_selection(self):
        global alpha

        selected_item = self["menu"].getCurrent()
        if selected_item:
            # Extract percentage from the selected item
            parts = selected_item.split(' ')
            if len(parts) >= 3:
                percentage = parts[2]  # Gets "56%" etc.

                # Find matching transparency value
                for level in self.transparency_levels:
                    if level["name"] == percentage:
                        alpha = level["value"]
                        print(
                            f"[TransparencySelector] Selected: {percentage} -> {alpha}")
                        break

        self.close()

    def initialize_display(self):
        # Set background color using current RGB values
        current_color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["background_plate"].instance.setBackgroundColor(current_color)
        # Set selection plate with current transparency
        self["selection_overlay"].instance.setBackgroundColor(
            parseColor(alpha))

        def conv_alpha(insel):
            trspz = ' n/a'
            if insel == "#90000000":
                trspz = '56%'
            elif insel == "#80000000":
                trspz = '50%'
            elif insel == "#70000000":
                trspz = '44%'
            elif insel == "#60000000":
                trspz = '38%'
            elif insel == "#50000000":
                trspz = '31%'
            elif insel == "#40000000":
                trspz = '25%'
            elif insel == "#30000000":
                trspz = '19%'
            elif insel == "#20000000":
                trspz = '13%'
            elif insel == "#10000000":
                trspz = '6%'
            return trspz

        # Update title with current transparency
        self['title_label'].setText(
            _('Window transparency') +
            ' - ' +
            conv_alpha(alpha))

        # Build the menu list
        menu_items = []
        for level in self.transparency_levels:
            menu_items.append(
                _("Transparency level") +
                f" {level['name']} ({level['value']})"
            )

        self["menu"].setList(menu_items)

        # Optional: Set initial selection to current alpha value
        self.select_current_transparency()

    def select_current_transparency(self):
        """Find and select the menu item matching current alpha value"""
        for index, level in enumerate(self.transparency_levels):
            if level["value"] == alpha:
                self["menu"].setCurrentIndex(index)
                print(
                    f"[TransparencySelector] Current selection: {level['name']}")
                break

    def exit_screen(self):
        self.close()


class CityPanel4List(GUIComponent):
    def __init__(self, entries):
        GUIComponent.__init__(self)
        self.lst = eListboxPythonMultiContent()
        self.lst.setFont(0, gFont("Regular", 30))
        self.foregroundColor = 0xffffff  # white
        self.foregroundColorSelected = 0x00a0ff  # blue
        self.backgroundColor = 0x000000  # black
        self.backgroundColorSelected = 0x2c2c2c  # dark gray
        self.itemHeight = 45
        self.column = 70
        self.setList(entries)

    GUI_WIDGET = eListbox

    def postWidgetCreate(self, instance):
        instance.setContent(self.lst)
        instance.setItemHeight(self.itemHeight)

    def preWidgetRemove(self, instance):
        instance.setContent(None)

    def setList(self, entries):
        self.lst.setList(entries)

    def getCurrentIndex(self):
        if self.instance:
            return self.instance.getCurrentIndex()
        return 0

    def moveToIndex(self, index):
        if self.instance:
            self.instance.moveSelectionTo(index)

    def getCurrentSelection(self):
        if self.instance:
            return self.lst.getCurrentSelection()
        return None

    def getItemsPerPage(self):
        if self.instance:
            return self.instance.size().height() // self.itemHeight
        return 10

    def selectionEnabled(self, enabled):
        if self.instance:
            self.instance.setSelectionEnable(enabled)

    def moveSelectionTo(self, index):
        if self.instance:
            self.instance.moveSelectionTo(index)


class CityPanel4(Screen):
    """City selection panel for Foreca4 plugin"""

    def __init__(self, session):
        self.skin = load_skin_for_class(CityPanel4)
        self.session = session
        Screen.__init__(self, session)
        self.setup_title = _("Select a city")
        self.city_list = []
        self.Mlist = []
        self["Mlist"] = CityPanel4List([])

        self["key_green"] = StaticText(_("Favorite 1"))
        self["key_yellow"] = StaticText(_("Favorite 2"))
        self["key_blue"] = StaticText(_("Home"))
        self["key_ok"] = Label(_("Forecast"))
        self["key_red"] = StaticText(_("Keyboard"))
        self["description"] = Label()

        self.setTitle(_("Select a city"))
        self.filtered_list = []
        self.search_text = ""
        self.search_ok = False
        self["actions"] = HelpableActionMap(
            self, "ForecaActions",
            {
                "cancel": (self.exit, _("Exit")),
                "red": (self.open_keyboard, _("Open Keyboard")),
                "green": (self.save_favorite1, _("Assign to Favorite 1")),
                "yellow": (self.save_favorite2, _("Assign to Favorite 2")),
                "blue": (self.save_home, _("Assign to Home")),
                "left": (self.left, _("Previous page")),
                "right": (self.right, _("Next page")),
                "up": (self.up, _("Previous")),
                "down": (self.down, _("Next")),
                "ok": (self.ok, _("Select")),
                "text": (self.open_keyboard, _("Keyboard")),
                "nextBouquet": (self.jump_down, _("Jump 500 down")),
                "prevBouquet": (self.jump_up, _("Jump 500 up")),
                "volumeDown": (self.jump_100_down, _("Jump 100 down")),
                "volumeUp": (self.jump_100_up, _("Jump 100 up")),
                "showEventInfo": (self.show_info, _("Show info")),
            },
            -2
        )
        self.onFirstExecBegin.append(self.onFirstExec)
        self.onShown.append(self.prepare_city_list)

    def onFirstExec(self):
        """Called when screen is first shown"""

        def init_selection():
            if self.filtered_list:
                self.select_first_item()
                self.update_description()

        self.init_timer = eTimer()
        self.init_timer.callback.append(init_selection)
        self.init_timer.start(200, True)  # 200ms

    def prepare_city_list(self):
        self.maxidx = 0
        self.Mlist = []
        self.city_list = []

        city_cfg_path = os.path.join(PLUGIN_PATH, "new_city.cfg")
        if not os.path.exists(city_cfg_path):
            self.session.open(
                MessageBox,
                _("City list file not found!"),
                MessageBox.TYPE_WARNING,
                timeout=5
            )
            return

        try:
            with open(city_cfg_path, "r", encoding="utf-8") as f:
                line_number = 0
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    if line.startswith("#"):
                        # For headers/headers
                        text = line
                        mlist_entry = self.create_city_entry(
                            text, is_header=True)
                        self.Mlist.append(mlist_entry)
                        continue

                    if "/" not in line:
                        print(
                            f"[CityPanel4] Line {line_number} noT valid: {line}")
                        continue

                    city_id, city_name = line.split("/", 1)
                    city_name = city_name.replace("_", " ")
                    mlist_entry = self.create_city_entry(
                        city_name, city_id=city_id)
                    self.Mlist.append(mlist_entry)
                    self.city_list.append((city_name, city_id))

                    line_number += 1

            print("[CityPanel4] Upload {0} CITY".format(len(self.Mlist)))

            self.filtered_list = self.Mlist
            self["Mlist"].setList(self.filtered_list)

            self["Mlist"].selectionEnabled(True)

            def select_first():
                self.select_first_item()

            self.timer = eTimer()
            self.timer.callback.append(select_first)
            self.timer.start(100, True)  # 100ms

        except Exception as e:
            print("[CityPanel4] Error loading cities: {0}".format(e))
            import traceback
            traceback.print_exc()

    def create_city_entry(self, text, city_id=None, is_header=False):
        """Create MultiContent entry for city or header"""
        list_widget = self["Mlist"]

        # Use colors from the widget list
        if is_header:
            text_color = 0x808080  # Grey for header
            text_color_selected = 0x808080
            back_color_selected = list_widget.backgroundColor
        else:
            text_color = list_widget.foregroundColor
            text_color_selected = list_widget.foregroundColorSelected
            back_color_selected = list_widget.backgroundColorSelected

        itemHeight = list_widget.itemHeight
        col = list_widget.column

        # The structure must be a LIST!
        # The first element is a tuple with the data (text, city_id, is_header)
        # Then follow the MultiContentEntry elements
        entry = [
            (text, city_id, is_header),  # Data
            MultiContentEntryText(
                pos=(0, 0),
                size=(col, itemHeight),
                font=0,
                text="",
                color=text_color,
                color_sel=text_color_selected,
                backcolor_sel=back_color_selected,
                flags=RT_VALIGN_CENTER
            ),
            MultiContentEntryText(
                pos=(col, 0),
                size=(1000, itemHeight),
                font=0,
                text=text,
                color=text_color,
                color_sel=text_color_selected,
                backcolor_sel=back_color_selected,
                flags=RT_VALIGN_CENTER
            )
        ]

        return entry

    def open_keyboard(self):
        """Open virtual keyboard for city search"""
        from Screens.VirtualKeyBoard import VirtualKeyBoard
        self.session.openWithCallback(
            self.filter_cities,
            VirtualKeyBoard,
            title=_("Search your City"),
            text=''
        )

    def filter_cities(self, result):
        """Filter city list based on search"""
        if result:
            try:
                self.filtered_list = []
                self.city_list = []
                search_term = result.lower()

                for item in self.Mlist:
                    data = item[0]  # (text, city_id, is_header)
                    text = data[0].lower()
                    is_header = data[2] if len(data) > 2 else False

                    if is_header:
                        if search_term == "" or search_term in text:
                            self.filtered_list.append(item)
                    else:
                        if search_term in text:
                            self.search_ok = True
                            self.filtered_list.append(item)
                            self.city_list.append((data[0], data[1]))

                if len(self.filtered_list) < 1:
                    self.session.open(MessageBox,
                                      _('No City found in search!!!'),
                                      MessageBox.TYPE_INFO,
                                      timeout=5)
                    return
                else:
                    self["Mlist"].setList(self.filtered_list)
                    self.select_first_item()
                    self["Mlist"].selectionEnabled(1)
            except Exception as e:
                print("[CityPanel4] Search error: {0}".format(e))
                self.session.open(
                    MessageBox,
                    _('An error occurred during search!'),
                    MessageBox.TYPE_ERROR,
                    timeout=5
                )

    def update_description(self):
        try:
            current_index = self["Mlist"].getCurrentIndex()
            if current_index is not None and self.filtered_list:
                if 0 <= current_index < len(self.filtered_list):
                    item = self.filtered_list[current_index]
                    if item and len(item) > 0:
                        data = item[0]  # (text, city_id, is_header)

                        if len(data) > 2 and data[2]:  # is_header
                            self["description"].setText(
                                _("Header - not selectable"))
                        elif len(data) >= 2:
                            city_name, city_id = data[0], data[1]
                            city_name_disp = city_name.replace("_", " ")
                            self["description"].setText(
                                f"{city_name_disp}  id: {city_id}")
                            print(
                                f"[CityPanel4] Selected: {city_name_disp} (id: {city_id})")
                        else:
                            self["description"].setText(_("No city selected"))
                else:
                    self["description"].setText(_("No city selected"))
            else:
                self["description"].setText(_("No city selected"))
        except Exception as e:
            print("[CityPanel4] update_description error: {0}".format(e))
            self["description"].setText(_("No city selected"))

    def save_favorite1(self):
        """Save selected city as Favorite 1"""
        selected = self.get_selected_city()
        if selected:
            self.save_favorite("fav1", selected)

    def save_favorite2(self):
        """Save selected city as Favorite 2"""
        selected = self.get_selected_city()
        if selected:
            self.save_favorite("fav2", selected)

    def save_home(self):
        """Save selected city as Home"""
        selected = self.get_selected_city()
        if selected:
            self.save_favorite("home", selected)

    def get_selected_city(self):
        try:
            current_index = self["Mlist"].getCurrentIndex()
            if current_index is not None and 0 <= current_index < len(
                    self.filtered_list):
                item = self.filtered_list[current_index]
                data = item[0]  # (text, city_id, is_header)
                if len(data) > 2 and not data[2]:  # not is_header
                    city_name, city_id = data[0], data[1]
                    return f"{city_id}/{city_name.replace(' ', '_')}"
        except Exception as e:
            print("[CityPanel4] Error getting selection: {0}".format(e))
        return None

    def save_favorite(self, fav_type, city):
        """Save city to favorite file AND update global variable"""
        global path_loc0, path_loc1, path_loc2

        fav_file = os.path.join(PLUGIN_PATH, f"{fav_type}.cfg")
        try:
            with open(fav_file, "w", encoding='utf-8') as f:
                f.write(city)

            # UPDATE GLOBAL VARIABLE
            if fav_type == "home":
                path_loc0 = city
            elif fav_type == "fav1":
                path_loc1 = city
            elif fav_type == "fav2":
                path_loc2 = city

            # Show confirmation
            fav_names = {
                "fav1": _("Favorite 1"),
                "fav2": _("Favorite 2"),
                "home": _("Home")
            }

            message = f"{fav_names.get(fav_type, fav_type)}:\n{city}"
            self.session.open(MessageBox,
                              message,
                              MessageBox.TYPE_INFO,
                              timeout=8)
            return True
        except Exception as e:
            print("[CityPanel4] Error saving {0}: {1}".format(fav_type, e))
            self.session.open(
                MessageBox,
                _("Error saving favorite!"),
                MessageBox.TYPE_ERROR,
                timeout=5
            )
            return False

    def ok(self):
        """Select city for forecast"""
        selected = self.get_selected_city()
        if selected:
            print("[CityPanel4] Selected city: {0}".format(selected))
            self.close(selected)

    def show_info(self):
        """Show information/help"""
        info_text = (
            _("City Selection Help:\n\n")
            + _("• Use arrow keys to navigate\n")
            + _("• OK to select city\n")
            + _("• GREEN to save as Favorite 1\n")
            + _("• YELLOW to save as Favorite 2\n")
            + _("• BLUE to save as Home\n")
            + _("• RED to open search keyboard\n")
            + _("• CH+/CH- to jump 500 cities\n")
            + _("• VOL+/VOL- to jump 100 cities")
        )
        self.session.open(MessageBox, info_text, MessageBox.TYPE_INFO)

    def select_first_item(self):
        """Select first selectable item (non-header) in the list"""
        for idx, item in enumerate(self.filtered_list):
            data = item[0]  # (text, city_id, is_header)
            if len(data) <= 2 or not data[2]:  # not is_header
                self["Mlist"].moveToIndex(idx)
                self.update_description()
                break

    def get_current_selectable_index(self):
        """Get current index in selectable items list"""
        current_index = self["Mlist"].getCurrentIndex()
        if current_index is not None and 0 <= current_index < len(
                self.filtered_list):
            return current_index
        return 0

    def move_next_selectable(self, direction):
        """Move to next selectable item with wrap-around"""
        if not self.filtered_list:
            return

        current_index = self.get_current_selectable_index()
        total_items = len(self.filtered_list)
        for i in range(1, total_items + 1):
            next_index = (current_index + direction * i) % total_items
            item = self.filtered_list[next_index]
            data = item[0]  # (text, city_id, is_header)

            # Se non è un header, selezionalo
            if len(data) <= 2 or not data[2]:  # not is_header
                self["Mlist"].moveToIndex(next_index)
                self.update_description()
                break

    def left(self):
        """Move one page up"""
        items_per_page = self["Mlist"].getItemsPerPage()
        self.jump_selectable(-items_per_page)

    def right(self):
        """Move one page down"""
        items_per_page = self["Mlist"].getItemsPerPage()
        self.jump_selectable(items_per_page)

    def up(self):
        """Move to previous selectable item"""
        self.move_next_selectable(-1)

    def down(self):
        """Move to next selectable item"""
        self.move_next_selectable(1)

    def jump_up(self):
        """Jump 500 items up"""
        self.jump_selectable(-500)

    def jump_down(self):
        """Jump 500 items down"""
        self.jump_selectable(500)

    def jump_100_up(self):
        """Jump 100 items up"""
        self.jump_selectable(-100)

    def jump_100_down(self):
        """Jump 100 items down"""
        self.jump_selectable(100)

    def jump_selectable(self, step):
        """Jump by specified number of items, skipping headers"""
        if not self.filtered_list:
            return

        current_index = self.get_current_selectable_index()
        total_items = len(self.filtered_list)
        direction = 1 if step > 0 else -1
        abs_step = abs(step)

        for i in range(1, abs_step + 1):
            next_index = (current_index + direction) % total_items
            item = self.filtered_list[next_index]
            data = item[0]  # (text, city_id, is_header)
            while len(data) > 2 and data[2]:  # is_header
                next_index = (next_index + direction) % total_items
                item = self.filtered_list[next_index]
                data = item[0]
            current_index = next_index

        self["Mlist"].moveToIndex(current_index)
        self.update_description()

    def exit(self):
        """Exit the city selection panel"""
        if self.search_ok:
            self.search_ok = False
        if hasattr(self, 'init_timer'):
            self.init_timer.stop()
        if hasattr(self, 'timer'):
            self.timer.stop()
        self.close(None)


def checkInternet():
    try:
        import socket
        socket.setdefaulttimeout(0.5)
        socket.socket(
            socket.AF_INET, socket.SOCK_STREAM).connect(
            ('8.8.8.8', 53))
        return True
    except BaseException:
        return False


def main(session, **kwargs):
    if not checkInternet():
        session.open(
            MessageBox,
            _("No Internet connection detected. Please check your network."),
            MessageBox.TYPE_INFO
        )
        return

    session.open(Foreca_Preview)


def Plugins(path, **kwargs):
    from Plugins.Plugin import PluginDescriptor
    list = [PluginDescriptor(
        name=_("Foreca 4") + " ver. " + str(VERSION),
        description=_("Current weather and forecast for the next 10 days"),
        icon="foreca_4.png",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        fnc=main)
    ]
    return list
