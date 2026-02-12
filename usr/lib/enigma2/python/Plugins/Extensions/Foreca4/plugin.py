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
#fix map viewer transcode to api from scraper

from __future__ import absolute_import

# Standard library imports
import os
from sys import version_info
from threading import Thread

# Enigma2 imports
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
    gRGB
)
from Screens.HelpMenu import HelpableScreen
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen
from skin import parseColor
from Tools.BoundFunction import boundFunction
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Tools.LoadPixmap import LoadPixmap

# Third-party imports
import six

# Local application imports
from . import _
from .cur_weather import getPageF
from .forecast_weather import getPageF_F
from .foreca_map_api import ForecaMapAPI
from .foreca_map_menu import ForecaMapMenu
from .google_translate import translate_text, safe_translate, _get_system_language, translate_batch
from .skin import (
    About_Foreca4_UHD,
    About_Foreca4_FHD,
    About_Foreca4_HD,
    ColorSelect_UHD,
    ColorSelect_FHD,
    ColorSelect_HD,
    ExtInfo_2_Foreca4_UHD,
    ExtInfo_2_Foreca4_FHD,
    ExtInfo_2_Foreca4_HD,
    ExtInfo_Foreca4_UHD,
    ExtInfo_Foreca4_FHD,
    ExtInfo_Foreca4_HD,
    ForecaPreview_4_UHD,
    ForecaPreview_4_FHD,
    ForecaPreview_4_HD,
    Meteogram_Foreca4_UHD,
    Meteogram_Foreca4_FHD,
    Meteogram_Foreca4_HD,
    Transparency_Foreca4_UHD,
    Transparency_Foreca4_FHD,
    Transparency_Foreca4_HD,
    CityPanel4_UHD,
    CityPanel4_FHD,
    CityPanel4_HD
)
from .slideshow import ForecaMapsMenu
from .tt_weather import getPageTT
from .unit_manager import UnitManager, UnitSettingsSimple
from .foreca_weather_api import ForecaWeatherAPI
from .daily_forecast import DailyForecast

VERSION = "1.3.5"

TARGET_LANG = _get_system_language()


# base constant
BASEURL = "https://www.foreca.com/"

config_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/"
unit_file = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/unit_config.conf"
config_file = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/api_config.txt"
default_unit = 'metric'  # Default a metrico
path_loc0 = '103169070/Rome-Italy'                        # Blue - Favorite 0
path_loc1 = '100524901/Moscow-Russia'                     # Green - Favorite 1
path_loc2 = '102961214/Thurles-County-Tipperary-Ireland'  # Yellow - Favorite 2


# Home @lululla
home_file = config_path + "home.cfg"
if os.path.exists(home_file):
    try:
        with open(home_file, "r") as f:
            path_loc0 = f.read().strip()
    except BaseException:
        pass

# Favorite 1
fav1_file = config_path + "fav1.cfg"
if os.path.exists(fav1_file):
    try:
        with open(fav1_file, "r") as f:
            path_loc1 = f.read().strip()
    except BaseException:
        pass

# Favorite 2
fav2_file = config_path + "fav2.cfg"
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

# other constant @lululla
cur_wind_speed_recalc = 1
for_wind_speed_recalc = 1
size_w = getDesktop(0).size().width()
size_h = getDesktop(0).size().height()


# utils
def conv_alpha(insel):
    rez = ' n/a'
    if insel == "#90000000":
        rez = '56%'
    elif insel == "#80000000":
        rez = '50%'
    elif insel == "#70000000":
        rez = '44%'
    elif insel == "#60000000":
        rez = '38%'
    elif insel == "#50000000":
        rez = '31%'
    elif insel == "#40000000":
        rez = '25%'
    elif insel == "#30000000":
        rez = '19%'
    elif insel == "#20000000":
        rez = '13%'
    elif insel == "#10000000":
        rez = '6%'
    return rez


def readsetalpha():
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


readsetalpha()


def savesetalpha(indata):
    f = open(
        '/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_alpha.conf',
        'w')
    f.write(indata)
    f.close()


def conv_day_len(indata):
    rez = indata
    try:
        inall = indata.split(' ')
        in2 = _(str(inall[1]))
        in3 = _(str(inall[3]))
        rez = inall[0] + ' ' + str(in2) + ' ' + inall[2] + ' ' + str(in3)
    except BaseException:
        rez = indata
    return rez


def is_valid(v):
    return bool(v) and str(v).strip().lower() != 'n/a'


def mywindSpeed(indata, metka):
    try:
        rez = 0
        rez = '%.01f' % float(int(indata) / 1)
        if metka == 1:
            return float(rez)
        else:
            rez = '%.01f' % float(int(indata))
            return float(rez)
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


class ForecaPreview_4(Screen, HelpableScreen):
    def __init__(self, session):
        # GLOBAL VARIABLES – KEPT FOR COMPATIBILITY
        global town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country
        global f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum
        global lon, lat, sunrise, daylen, sunset, f_day

        self.session = session
        self.tag = 0

        self.unit_manager = UnitManager(config_path)
        self.weather_api = ForecaWeatherAPI(self.unit_manager)

        # DETERMINE LOCATION ID FROM PATH
        location_id = path_loc0.split(
            '/')[0] if '/' in path_loc0 else path_loc0

        # STRATEGY: TRY API FIRST, THEN FALL BACK TO SCRAPING
        api_current_ok = False
        api_forecast_ok = False

        # 1. TRY CURRENT WEATHER VIA API
        if self.weather_api.check_credentials():
            print(
                "[Foreca4] Trying API for current weather, ID: {0}".format(location_id))
            result_current = self.weather_api.get_current_weather(location_id)
            if result_current and result_current[0] != 'N/A':
                town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current
                api_current_ok = True
                print("[Foreca4] Current weather obtained via API")
            else:
                print(
                    "[Foreca4] Current weather API failed, falling back to scraping")
        else:
            print("[Foreca4] API credentials not configured, using scraping")

        # FALLBACK TO SCRAPING FOR CURRENT WEATHER
        if not api_current_ok:
            try:
                MAIN_PAGE_F = str(BASEURL) + path_loc0
                print("[Foreca4] Scraping from: {0}".format(MAIN_PAGE_F))
                result_current = getPageF(MAIN_PAGE_F)
                town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current
            except Exception as e:
                print(
                    "[Foreca4] Error scraping current weather: {0}".format(e))
                # DEFAULT VALUES
                town = cur_temp = fl_temp = dewpoint = pic = wind = 'N/A'
                wind_speed = wind_gust = rain_mm = hum = pressure = 'N/A'
                country = lon = lat = sunrise = daylen = sunset = 'N/A'

        # 2. TRY HOURLY FORECASTS VIA API
        if self.weather_api.check_credentials():
            print(
                "[Foreca4] Trying API for forecasts, ID: {0}".format(location_id))
            result_forecast = self.weather_api.get_hourly_forecast(
                location_id, days=1)
            if result_forecast and result_forecast[0] != 'N/A':
                f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = result_forecast
                api_forecast_ok = True
                print(
                    "[Foreca4] Forecasts obtained via API: {0} periods".format(
                        len(f_time)))
            else:
                print("[Foreca4] Forecast API failed, falling back to scraping")
        else:
            print("[Foreca4] API credentials not configured for forecasts")

        # 3. FALLBACK TO FORECAST SCRAPING
        if not api_forecast_ok:
            try:
                MAIN_PAGE_FF = str(BASEURL) + path_loc0 + '/hourly?day=0'
                result_forecast = getPageF_F(MAIN_PAGE_FF)
                f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = result_forecast
            except Exception as e:
                print("[Foreca4] Error scraping forecasts: {0}".format(e))
                # DEFAULT VALUES
                f_town = 'N/A'
                f_date = f_time = f_symb = f_cur_temp = f_flike_temp = []
                f_wind = f_wind_speed = f_precipitation = f_rel_hum = []
                f_day = 'N/A'

        if size_w == 1920:
            self.skin = ForecaPreview_4_FHD
        elif size_w == 2560:
            self.skin = ForecaPreview_4_UHD
        else:
            self.skin = ForecaPreview_4_HD

        Screen.__init__(self, session)
        HelpableScreen.__init__(self)
        self.setTitle(_("Foreca Weather Forecast") + " " + _("v.") + VERSION)
        self.list = []
        self["menu"] = List(self.list)
        self["Titel"] = StaticText()
        self["mytitel2"] = StaticText()
        self["Titel2"] = StaticText(_("Please wait ..."))
        self["Titel3"] = StaticText()
        self["Titel5"] = StaticText()
        self["mytitel1"] = StaticText()
        self["station"] = Label("N/A")
        self["town"] = Label("N/A")
        self["cur_temp"] = Label("N/A")
        self["fl_temp"] = Label("N/A")
        self["dewpoint"] = Label("N/A")
        self["pic"] = Pixmap()
        self["wind"] = Pixmap()
        self["wind_speed"] = Label("N/A")
        self["wind_gust"] = Label("N/A")
        self["rain_mm"] = Label("N/A")
        self["hum"] = Label("N/A")
        self["pressure"] = Label("N/A")
        self["description_w"] = Label('')
        self["pressure_pic"] = Pixmap()
        self["rain_mm_pic"] = Pixmap()
        self["hum_pic"] = Pixmap()
        self["plate1"] = Label("N/A")
        self["plate2"] = Label("N/A")
        self["plate3"] = Label("N/A")
        self["plate4"] = Label("N/A")
        self["plate5"] = Label("N/A")
        self["plate11"] = Label("N/A")
        self["plate22"] = Label("N/A")
        self["plate33"] = Label("N/A")
        self["plate44"] = Label("N/A")
        self["plate55"] = Label("N/A")
        self["day_len"] = Label('0 h 0 min')
        self["sunrise_text"] = Label(_('Sunrise'))
        self["sunrise_val"] = Label('00:00')
        self["sunset_text"] = Label(_('Sunset'))
        self["sunset_val"] = Label('00:00')
        self["sun"] = Pixmap()

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
            (_("Color select"), "color_select"),
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
        elif choice[1] == "color_select":
            self.session.open(Color_Select)
        elif choice[1] == "transparency":
            self.session.open(TransparencyBox)
        elif choice[1] == "info":
            self.session.open(InfoBox1)
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
                observations = self.weather_api.get_station_observations(
                    location_id, station_limit=1)

                if observations and len(observations) > 0:
                    station_name = observations[0].get('station', 'N/A')
                    station_dist = observations[0].get('distance', '')
                    text = "Station: {0} ({1})".format(
                        station_name, station_dist)
                    print("[DEBUG] Station text: {0}".format(text))

                    from enigma import eTimer

                    def update_ui():
                        try:
                            if "station" in self:
                                self["station"].setText(text)
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
            location_id = path_loc0.split('/')[0] if '/' in path_loc0 else path_loc0
        elif myloc == 1:
            location_id = path_loc1.split('/')[0] if '/' in path_loc1 else path_loc1
        elif myloc == 2:
            location_id = path_loc2.split('/')[0] if '/' in path_loc2 else path_loc2

        print(f"[DEBUG] Opening DailyForecast for location: {location_id}, name: {location_name}")
        
        if not self.weather_api.check_credentials():
            print("[DEBUG] API credentials not configured")
            self.session.open(
                MessageBox,
                _("API credentials not configured!\n\nPlease create api_config.txt file."),
                MessageBox.TYPE_ERROR
            )
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
            self.session.open(ExtInfo_Foreca4_FHD)
        else:
            self.session.open(ExtInfo_2_Foreca4_FHD)

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
                    rez = a.rstrip()
                    rgbmyr = rez.split(' ')[0]
                    rgbmyg = rez.split(' ')[1]
                    rgbmyb = rez.split(' ')[2]
                    file.close()
            except BaseException:
                rgbmyr = 0
                rgbmyg = 80
                rgbmyb = 239

    def update_button(self):
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate1"].instance.setBackgroundColor(self.color)
        self["plate2"].instance.setBackgroundColor(self.color)
        self["plate3"].instance.setBackgroundColor(self.color)
        self["plate4"].instance.setBackgroundColor(self.color)
        self["plate5"].instance.setBackgroundColor(self.color)
        self["plate11"].instance.setBackgroundColor(parseColor(alpha))
        self["plate22"].instance.setBackgroundColor(parseColor(alpha))
        self["plate33"].instance.setBackgroundColor(parseColor(alpha))
        self["plate44"].instance.setBackgroundColor(parseColor(alpha))
        self["plate55"].instance.setBackgroundColor(parseColor(alpha))

        self.my_cur_weather()
        self.my_forecast_weather()

    def StartPageFirst(self):
        self.readsetcolor()

        self["pic"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/d000.png")
        self["pic"].instance.show()

        self["wind"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/wS.png")
        self["wind"].instance.show()

        self["pressure_pic"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/barometer.png")
        self["pressure_pic"].instance.show()

        self["rain_mm_pic"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/precipitation.png")
        self["rain_mm_pic"].instance.show()

        self["hum_pic"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/humidity.png")
        self["hum_pic"].instance.show()

        self["sun"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/sun.png")
        self["sun"].instance.show()

        self["mytitel1"].text = _("Current weather and forecast")
        self["mytitel2"].text = "<< ver. " + str(VERSION) + " >>"

        # Date
        date_str = str(f_date[0]) if f_date and len(
            f_date) > 0 else _("No date available")

        # Day
        day_str = trans(f_day) if is_valid(f_day) else ""

        self["Titel"].text = f"{trans(str(town))}, {trans(str(country))} - {date_str}"
        if day_str:
            self["Titel"].text += " - " + day_str

        # Day length
        self["day_len"].setText(
            str(conv_day_len(daylen)) if is_valid(daylen) else "N/A"
        )

        # Sunrise / Sunset
        self["sunrise_val"].setText(
            str(sunrise) if is_valid(sunrise) else "N/A")
        self["sunset_val"].setText(str(sunset) if is_valid(sunset) else "N/A")

        self["sunrise_text"].setText(_("Sunrise"))
        self["sunset_text"].setText(_("Sunset"))

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
                    mywindSpeed(
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

            pos9 = trans('Precipitations:') + ' ' + \
                str(f_precipitation[n]) + '%'

            pos10 = trans('Humidity:') + ' ' + str(f_rel_hum[n]) + '%'

            self.list.append((
                str(f_time[n]),
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
        self["town"].setText(str(town) if is_valid(town) else "N/A")

        # Current temperature - convert if needed
        if is_valid(cur_temp):
            if unit_system == 'imperial':
                # Convert Celsius to Fahrenheit
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

        self["cur_temp"].setText(cur_temp_text)

        # Feels like temperature
        if is_valid(fl_temp):
            if unit_system == 'imperial':
                try:
                    temp_c = float(fl_temp)
                    temp_f = (temp_c * 9 / 5) + 32
                    self["fl_temp"].setText(
                        trans("Feels like") + f" {temp_f:.1f}°F")
                except BaseException:
                    self["fl_temp"].setText(
                        trans("Feels like") + f" {fl_temp}°C")
            else:
                self["fl_temp"].setText(trans("Feels like") + f" {fl_temp}°C")

        else:
            self["fl_temp"].setText(trans("Feels like") + " N/A")

        # Wind speed - needs conversion
        if is_valid(wind_speed):
            try:
                # wind_speed from scraping is in km/h
                wind_kmh = float(wind_speed)
                if unit_system == 'imperial':
                    # Convert km/h to mph
                    wind_mph = wind_kmh * 0.621371
                    self["wind_speed"].setText(
                        trans("Wind speed") + f" {wind_mph:.1f} mph")
                else:
                    self["wind_speed"].setText(
                        trans("Wind speed") + f" {wind_kmh:.1f} km/h")
            except BaseException:
                self["wind_speed"].setText(
                    trans("Wind speed") + f" {wind_speed}")

        # Wind gust - same conversion
        if is_valid(wind_gust):
            try:
                wind_kmh = float(wind_gust)
                if unit_system == 'imperial':
                    wind_mph = wind_kmh * 0.621371
                    self["wind_gust"].setText(
                        trans("Gust") + f" {wind_mph:.1f} mph")
                else:
                    self["wind_gust"].setText(
                        trans("Gust") + f" {wind_kmh:.1f} km/h")
            except BaseException:
                self["wind_gust"].setText(trans("Gust") + f" {wind_gust}")

        # Pressure - already handled in scraping (mmHg) but convert if needed
        if is_valid(pressure):
            try:
                pressure_mmhg = float(pressure)
                if unit_system == 'imperial':
                    # Convert mmHg to inHg
                    pressure_inhg = pressure_mmhg * 0.03937
                    self["pressure"].setText(f"{pressure_inhg:.2f} inHg")
                else:
                    # Convert mmHg to hPa (more standard for metric)
                    pressure_hpa = pressure_mmhg * 1.33322
                    self["pressure"].setText(f"{pressure_hpa:.0f} hPa")
            except BaseException:
                self["pressure"].setText(f"{pressure}")

        # Dewpoint
        if is_valid(dewpoint):
            self["dewpoint"].setText(
                trans("Dewpoint") +
                " {0}°C".format(dewpoint))
            print(
                "[WIDGET-FIX] dewpoint settato a: {0}{1}°C".format(trans("Dewpoint "), dewpoint))
        else:
            self["dewpoint"].setText(trans("Dewpoint") + " N/A")

        # Weather icon
        try:
            icon = "{0}.png".format(pic) if is_valid(pic) else "n600.png"
            icon_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/{0}".format(
                icon)
            if os.path.exists(icon_path):
                self["pic"].instance.setPixmapFromFile(icon_path)
        except Exception:
            pass

        # Weather description
        if is_valid(pic):
            description = self.symbolToCondition(str(pic))
            self["description_w"].setText(trans(description))
        else:
            self["description_w"].setText("N/A")

        # Wind direction icon
        try:
            if is_valid(wind) and 'w' in str(wind):
                myw = int(str(wind).split('w')[1])
                myw1 = self.degreesToWindDirection(myw)
                wind_icon = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/{0}.png".format(
                    myw1)
                if os.path.exists(wind_icon):
                    self["wind"].instance.setPixmapFromFile(wind_icon)
        except Exception:
            pass

        # Precipitation
        self["rain_mm"].setText(
            "{0} ".format(rain_mm) +
            trans("mm") if is_valid(rain_mm) else "N/A")

        # Humidity
        self["hum"].setText("{0}%".format(hum) if is_valid(hum) else "N/A")

        # Force immediate GUI update
        self.invalidate_current_weather_widgets()

    def StartPage(self):
        date_str = ""
        if f_date and len(f_date) > 0:
            date_str = str(f_date[0])
        else:
            date_str = _("No date available")

        day_str = trans(f_day) if is_valid(f_day) else ""

        self["Titel"].text = str(town) + ', ' + \
            trans(str(country)) + ' - ' + date_str
        if day_str:
            self["Titel"].text += ' - ' + day_str

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

        myloc = fav_index  # <-- THIS is the only real difference!
        location_id = path_loc.split('/')[0] if '/' in path_loc else path_loc

        # 1. CURRENT WEATHER VIA API (or scraping fallback)
        if self.weather_api.check_credentials():
            result_current = self.weather_api.get_current_weather(location_id)
            if result_current and result_current[0] != 'N/A':
                town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current
                print(
                    "[Foreca4] Fav{0}: Current weather via API".format(fav_index))
            else:
                # Fallback to scraping
                MAIN_PAGE_F = str(BASEURL) + path_loc
                result_current = getPageF(MAIN_PAGE_F)
                town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current
                print(
                    "[Foreca4] Fav{0}: Current weather via scraping".format(fav_index))
        else:
            # Scraping only
            MAIN_PAGE_F = str(BASEURL) + path_loc
            result_current = getPageF(MAIN_PAGE_F)
            town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current

        self.my_cur_weather()

        # 2. FORECAST VIA API (or scraping fallback)
        if self.weather_api.check_credentials():
            result_forecast = self.weather_api.get_hourly_forecast(
                location_id, days=1)
            if result_forecast and result_forecast[0] != 'N/A':
                f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = result_forecast
            else:
                # Fallback
                MAIN_PAGE_FF = str(BASEURL) + path_loc + '/hourly?day=0'
                f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(
                    MAIN_PAGE_FF)
        else:
            # Scraping only
            MAIN_PAGE_FF = str(BASEURL) + path_loc + '/hourly?day=0'
            f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(
                MAIN_PAGE_FF)

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

        # FALLBACK TO SCRAPING
        MAIN_PAGE_FF = str(BASEURL) + path_loc + '/hourly?day=' + str(ztag)
        f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(
            MAIN_PAGE_FF)

        self.my_forecast_weather()
        self.StartPage()

    def info(self):
        self.session.open(InfoBox1)

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
        self.session.open(Color_Select)

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
        widget_names = ["fl_temp", "wind_speed", "wind_gust", "dewpoint",
                        "town", "cur_temp", "description_w", "rain_mm",
                        "hum", "pressure"]

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
        rez = str(rgbmyr) + ' ' + str(rgbmyg) + ' ' + str(rgbmyb)
        self.savesetcolor(rez)
        savesetalpha(alpha)

        # Clean cache on exit (optional)
        self.clean_foreca_cache()
        self.close()


class Color_Select(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ColorSelect_FHD
    elif sz_w == 2560:
        skin = ColorSelect_UHD
    else:
        skin = ColorSelect_HD

    def __init__(self, session, args=0):
        self.session = session
        Screen.__init__(self, session)
        self.setTitle(_('Color selection'))

        self.Clist = []
        self.original_names = []
        self.display_names = []
        self.mydata = []

        self["Clist"] = MenuList([])
        self["colorname"] = Label()
        self["colorname"].setText(_('Color name'))
        self["colordatas"] = Label()
        self["colordatas"].setText(_('Color data'))
        self["pic1"] = Pixmap()
        self["plate0"] = Label("N/A")
        self["plate1"] = Label("N/A")
        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self.Exit,
                "left": self.left,
                "right": self.right,
                "up": self.up,
                "down": self.down,
                "ok": self.OK,
            }, -1
        )
        self.onShown.append(self.prepare)

    def prepare(self):
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

        self.Clist = []
        self.original_names = []
        self.display_names = []
        self.mydata = []
        self.last_translated_idx = 0

        file_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/new_rgb_full.txt"

        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for i, line in enumerate(lines):
                    line = line.strip()
                    if not line:
                        continue

                    if " #" in line:
                        name_part, data_part = line.split(" #", 1)
                        name_part = name_part.strip()
                        data_part = data_part.strip()
                    else:
                        name_part = line.strip()
                        data_part = ""

                    self.original_names.append(name_part)
                    self.display_names.append(name_part)
                    self.mydata.append(data_part)
                    self.Clist.append(f"{i}. {name_part}")

            except Exception as e:
                print(f"[Foreca4] Error reading color file: {e}")
                self.Clist.append("0. " + _("Error loading colors"))
                self.original_names.append("")
                self.display_names.append("")
                self.mydata.append("")
        else:
            self.Clist.append("0. " + _("Color file not found"))
            self.original_names.append("")
            self.display_names.append("")
            self.mydata.append("")

        self["Clist"].l.setList(self.Clist)
        self["Clist"].selectionEnabled(1)

        print(f"[Color_Select] Loaded items: {len(self.original_names)}")

        if self.Clist:
            print("[Color_Select] Translating first 30 items synchronously...")
            for i in range(0, min(30, len(self.original_names))):
                if self.display_names[i] == self.original_names[i]:
                    translated = self.translate_color(self.original_names[i])
                    if translated != self.original_names[i]:
                        self.display_names[i] = translated
                        self.Clist[i] = f"{i}. {translated}"

            self.update_gui()
            self.update_display(0)

            if len(self.original_names) > 30:
                print(
                    "[Color_Select] Starting background translation for remaining items...")
                self.translate_range(30, 150)
            self.last_translated_idx = 150

    def translate_range(self, start_idx, end_idx):
        import threading

        def translate():
            end_idx_actual = min(end_idx, len(self.original_names))
            print(
                f"[Color_Select] Translating range {start_idx} to {end_idx_actual}")

            # Translate in blocks of 20 items and update the GUI after each
            # block
            block_size = 20
            for block_start in range(start_idx, end_idx_actual, block_size):
                block_end = min(block_start + block_size, end_idx_actual)
                translated_in_block = False

                for i in range(block_start, block_end):
                    if self.display_names[i] == self.original_names[i]:
                        translated = self.translate_color(
                            self.original_names[i])
                        if translated != self.original_names[i]:
                            self.display_names[i] = translated
                            self.Clist[i] = f"{i}. {translated}"
                            translated_in_block = True

                # Update the GUI after each block
                if translated_in_block:
                    from enigma import eTimer

                    def update_gui_safe():
                        try:
                            self.update_gui()
                        except Exception as e:
                            print(f"[Color_Select] Error updating GUI: {e}")

                    timer = eTimer()
                    timer.callback.append(update_gui_safe)
                    timer.start(0, True)

                print(
                    f"[Color_Select] Translated block {block_start}-{block_end}")

            print(
                f"[Color_Select] Completed translation of range {start_idx}-{end_idx_actual}")

            # Update the index of the last translated item
            self.last_translated_idx = max(
                self.last_translated_idx, end_idx_actual)

        thread = threading.Thread(target=translate, daemon=True)
        thread.start()

    def translate_color(self, color_name):
        if not color_name:
            return color_name

        print("[Color_Select] Translate: '{0}'".format(color_name))
        try:
            if '-' in color_name:
                parts = color_name.split('-')
                translated_parts = []

                for part in parts:
                    part = part.strip()
                    if part:
                        translated_part = trans(part)
                        translated_parts.append(translated_part)
                    else:
                        translated_parts.append("")

                result = '-'.join(translated_parts)
                print(
                    "[Color_Select] Result with iphen: '{0}' -> '{1}'".format(color_name, result))
                return result

            result = trans(color_name)
            print(
                "[Color_Select] Result: '{0}' -> '{1}'".format(color_name, result))
            return result

        except Exception as e:
            print(
                "[Color_Select] ERROR translating '{0}': {1}".format(
                    color_name, e))
            return color_name

    def translate_all_async(self):
        """Translate all items in the background"""
        import threading

        def translate_all():
            total = len(self.original_names)
            block_size = 50

            for start in range(0, total, block_size):
                end = min(start + block_size, total)

                for i in range(start, end):
                    if self.display_names[i] == self.original_names[i]:
                        translated = self.translate_color(
                            self.original_names[i])
                        if translated != self.original_names[i]:
                            self.display_names[i] = translated
                            self.Clist[i] = f"{i}. {translated}"

                # Update the GUI after each block
                from enigma import eTimer
                timer = eTimer()
                timer.callback.append(self.update_gui)
                timer.start(0, True)

                print(f"[Color_Select] Translated block {start}-{end}")

            print(f"[Color_Select] All {total} items translated")

        thread = threading.Thread(target=translate_all, daemon=True)
        thread.start()

    def update_display(self, index):
        print(f"[Color_Select] update_display({index})")
        if 0 <= index < len(self.display_names):
            # self.translate_all_async()
            if self.display_names[index] == self.original_names[index]:
                translated = self.translate_color(self.original_names[index])
                if translated != self.display_names[index]:
                    self.display_names[index] = translated
                    self.Clist[index] = f"{index}. {translated}"
                    self.update_gui()
                    print(f"[Color_Select] Translated item {index} on the fly")

            display_name = self.display_names[index]
            self["colorname"].setText(display_name)
            print(f"[Color_Select] Set colorname: '{display_name}'")
            if index < len(self.mydata) and self.mydata[index]:
                color_info = self.mydata[index]
                parts = color_info.split(' ')
                if len(parts) >= 4:
                    myhtml = '#' + parts[0]
                    myr = parts[1]
                    myg = parts[2]
                    myb = parts[3]

                    color_text = (_('HTML') + ' (' + myhtml + ')   ' +
                                  _('Red') + ' (' + myr + ')   ' +
                                  _('Green') + ' (' + myg + ')   ' +
                                  _('Blue') + ' (' + myb + ')')

                    self["colordatas"].setText(color_text)
                    img_path = f"/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/samples/{myhtml}.png"
                    if os.path.exists(img_path):
                        self["pic1"].instance.setPixmapFromFile(img_path)
                        self["pic1"].instance.show()

    def update_gui(self):
        print("[Color_Select] update_gui()")
        self["Clist"].l.setList(self.Clist)
        current_idx = self["Clist"].getCurrentIndex()
        if current_idx < len(self.display_names):
            self["colorname"].setText(self.display_names[current_idx])

        self["Clist"].instance.invalidate()
        self["colorname"].instance.invalidate()

    def up(self):
        current_idx = self["Clist"].getCurrentIndex()
        new_idx = max(0, current_idx - 1)
        self["Clist"].goLineUp()
        self.update_display(new_idx)

    def down(self):
        current_idx = self["Clist"].getCurrentIndex()
        new_idx = min(len(self.Clist) - 1, current_idx + 1)
        self["Clist"].goLineDown()
        self.update_display(new_idx)

    def left(self):
        self["Clist"].pageUp()
        current_idx = self["Clist"].getCurrentIndex()
        self.update_display(current_idx)

        if current_idx + 100 > self.last_translated_idx:
            new_end = min(self.last_translated_idx +
                          100, len(self.original_names))
            print(
                f"[Color_Select] Translating ahead: {self.last_translated_idx} to {new_end}")
            self.translate_range(self.last_translated_idx, new_end)
            self.last_translated_idx = new_end

    def right(self):
        self["Clist"].pageDown()
        current_idx = self["Clist"].getCurrentIndex()
        self.update_display(current_idx)

        if current_idx + 100 > self.last_translated_idx:
            new_end = min(self.last_translated_idx +
                          100, len(self.original_names))
            print(
                f"[Color_Select] Translating ahead: {self.last_translated_idx} to {new_end}")
            self.translate_range(self.last_translated_idx, new_end)
            self.last_translated_idx = new_end

    def OK(self):
        global rgbmyr, rgbmyg, rgbmyb
        current_idx = self["Clist"].getCurrentIndex()

        if current_idx < len(self.mydata) and self.mydata[current_idx]:
            color_info = self.mydata[current_idx]
            parts = color_info.split(' ')
            if len(parts) >= 4:
                rgbmyr = parts[1]
                rgbmyg = parts[2]
                rgbmyb = parts[3]

        self.close()

    def Exit(self):
        self.close()


class InfoBox1(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = About_Foreca4_FHD
    elif sz_w == 2560:
        skin = About_Foreca4_UHD
    else:
        skin = About_Foreca4_HD

    def __init__(self, session):

        Screen.__init__(self, session)

        self['ver'] = StaticText(
            _('Foreca 4 Weather and Forecast') +
            ' ver. ' +
            str(VERSION))

        self["plate0"] = Label("N/A")
        self["plate1"] = Label("N/A")

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self.Exit,
                'ok': self.Exit,
            }, -1
        )

        self.onShow.append(self.Start2)

    def Start2(self):
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

    def Exit(self):
        self.close()


class ExtInfo_Foreca4_FHD(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ExtInfo_Foreca4_FHD
    elif sz_w == 2560:
        skin = ExtInfo_Foreca4_UHD
    else:
        skin = ExtInfo_Foreca4_HD

    def __init__(self, session):
        Screen.__init__(self, session)

        if myloc == 0:
            MAIN_PAGE_TT = 'https://www.forecaweather.com/' + str(path_loc0)
        elif myloc == 1:
            MAIN_PAGE_TT = 'https://www.forecaweather.com/' + str(path_loc1)
        elif myloc == 2:
            MAIN_PAGE_TT = 'https://www.forecaweather.com/' + str(path_loc2)

        self.mytown, self.mytext1, self.myh_temp, self.myl_temp, self.mytext2, self.mytext3, self.myh2_temp, self.myl2_temp, self.mytext4, self.mysymb_mo1, self.mysymb_mo2, self.myt_mo1, self.myt_mo2, self.mysymb_af1, self.mysymb_af2, self.myt_af1, self.myt_af2, self.mysymb_ev1, self.mysymb_ev2, self.myt_ev1, self.myt_ev2, self.mysymb_ov1, self.mysymb_ov2, self.myt_ov1, self.myt_ov2 = getPageTT(
            MAIN_PAGE_TT)

        self['title1'] = StaticText(_('Weather Radar'))
        self['title2'] = StaticText()
        self['title3'] = StaticText(_('Weather today'))
        self['title4'] = StaticText(_('Weather tomorrow'))
        self["pic"] = Pixmap()
        self['text1'] = StaticText()
        self['text2'] = StaticText()
        self['mo1'] = StaticText()
        self['mo2'] = StaticText()
        self['af1'] = StaticText()
        self['af2'] = StaticText()
        self['ev1'] = StaticText()
        self['ev2'] = StaticText()
        self['ov1'] = StaticText()
        self['ov2'] = StaticText()
        self["pic_af1"] = Pixmap()
        self["pic_ev1"] = Pixmap()
        self["pic_ov1"] = Pixmap()
        self["pic_mo1"] = Pixmap()
        self['mo1_text'] = StaticText()
        self['af1_text'] = StaticText()
        self['ev1_text'] = StaticText()
        self['ov1_text'] = StaticText()
        self["pic_af2"] = Pixmap()
        self["pic_ev2"] = Pixmap()
        self["pic_ov2"] = Pixmap()
        self["pic_mo2"] = Pixmap()
        self['mo2'] = StaticText()
        self['af2'] = StaticText()
        self['ev2'] = StaticText()
        self['ov2'] = StaticText()
        self['mo2_text'] = StaticText()
        self['af2_text'] = StaticText()
        self['ev2_text'] = StaticText()
        self['ov2_text'] = StaticText()
        self["plate0"] = Label("N/A")
        self["plate1"] = Label("N/A")
        self["pic_lot"] = Pixmap()
        self["pic_lat"] = Pixmap()
        self['lat_val'] = StaticText()
        self['lon_val'] = StaticText()

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self.Exit,
                'ok': self.OK,
            }, -1
        )

        self.onLayoutFinish.append(self.Start1)
        self.onShow.append(self.Start2)

    def OK(self):
        self.session.open(Meteogram_Foreca4_FHD)

    def Start2(self):
        self['title3'].text = str(_('Weather today'))
        self['title4'].text = str(_('Weather tomorrow'))

        self['title2'].text = str(self.mytown)

        t1 = str(self.mytext1) + ' ' + str(self.myh_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + \
            str(self.myl_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext2) + ' mm.'
        self["text1"].text = str(t1)

        t2 = str(self.mytext3) + ' ' + str(self.myh2_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + \
            str(self.myl2_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext4) + ' mm.'
        self["text2"].text = str(t2)

        self['mo1'].text = _('Morning')
        self['mo2'].text = _('Morning')
        self['af1'].text = _('Afternoon')
        self['af2'].text = _('Afternoon')
        self['ev1'].text = _('Evening')
        self['ev2'].text = _('Evening')
        self['ov1'].text = _('Overnight')
        self['ov2'].text = _('Overnight')

        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

        Thread4 = Thread(target=self.mytranslate)
        Thread4.start()

    def mytranslate(self):
        self['title3'].text = _('Weather today')
        self['title4'].text = _('Weather tomorrow')

        self['title2'].text = str(trans(self.mytown))

        t1 = str(self.mytext1) + ' ' + str(self.myh_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + \
            str(self.myl_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext2) + ' mm.'
        self["text1"].text = str(trans(t1))

        t2 = str(self.mytext3) + ' ' + str(self.myh2_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + \
            str(self.myl2_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext4) + ' mm.'
        self["text2"].text = str(trans(t2))

    def Start1(self):
        if os.path.exists("/tmp/385.png"):
            self["pic"].instance.setPixmapFromFile("/tmp/385.png")
            self["pic"].instance.show()

        self["pic_af1"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_af1) + ".png")
        self["pic_af1"].instance.show()
        self["pic_ev1"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ev1) + ".png")
        self["pic_ev1"].instance.show()
        self["pic_ov1"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ov1) + ".png")
        self["pic_ov1"].instance.show()
        self["pic_mo1"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_mo1) + ".png")
        self["pic_mo1"].instance.show()

        self["pic_af2"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_af2) + ".png")
        self["pic_af2"].instance.show()
        self["pic_ev2"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ev2) + ".png")
        self["pic_ev2"].instance.show()
        self["pic_ov2"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ov2) + ".png")
        self["pic_ov2"].instance.show()
        self["pic_mo2"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_mo2) + ".png")
        self["pic_mo2"].instance.show()

        self["pic_lot"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/longitude.png")
        self["pic_lot"].instance.show()
        self["pic_lat"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/latitude.png")
        self["pic_lat"].instance.show()

        self['mo1_text'].text = str(self.myt_mo1)
        self['af1_text'].text = str(self.myt_af1)
        self['ev1_text'].text = str(self.myt_ev1)
        self['ov1_text'].text = str(self.myt_ov1)

        self['mo2_text'].text = str(self.myt_mo2)
        self['af2_text'].text = str(self.myt_af2)
        self['ev2_text'].text = str(self.myt_ev2)
        self['ov2_text'].text = str(self.myt_ov2)

        self['lat_val'].text = str(lat)
        self['lon_val'].text = str(lon)

    def Exit(self):
        self.close()


class ExtInfo_2_Foreca4_FHD(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ExtInfo_2_Foreca4_FHD
    elif sz_w == 2560:
        skin = ExtInfo_2_Foreca4_UHD
    else:
        skin = ExtInfo_2_Foreca4_HD

    def __init__(self, session):

        Screen.__init__(self, session)

        self['title1'] = StaticText(_('Weather Radar'))
        self["pic"] = Pixmap()
        self["plate0"] = Label("N/A")
        self["plate1"] = Label("N/A")
        self["pic_lot"] = Pixmap()
        self["pic_lat"] = Pixmap()
        self['lat_val'] = StaticText()
        self['lon_val'] = StaticText()

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self.Exit,
                'ok': self.OK,
            }, -1
        )

        self.onLayoutFinish.append(self.Start1)
        self.onShow.append(self.Start2)

    def Start2(self):
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

    def Start1(self):
        if os.path.exists("/tmp/385.png"):
            self["pic"].instance.setPixmapFromFile("/tmp/385.png")
            self["pic"].instance.show()

        self["pic_lot"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/longitude.png")
        self["pic_lot"].instance.show()
        self["pic_lat"].instance.setPixmapFromFile(
            "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/latitude.png")
        self["pic_lat"].instance.show()

        self['lat_val'].text = str(lat)
        self['lon_val'].text = str(lon)

    def OK(self):
        self.session.open(Meteogram_Foreca4_FHD)

    def Exit(self):
        self.close()


class TransparencyBox(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = Transparency_Foreca4_FHD
    elif sz_w == 2560:
        skin = Transparency_Foreca4_UHD
    else:
        skin = Transparency_Foreca4_HD

    def __init__(self, session):

        Screen.__init__(self, session)

        self["list"] = MenuList([])
        self['text1'] = StaticText(_('Window transparency'))

        self["plate0"] = Label("N/A")
        self["plate1"] = Label("N/A")

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
                "cancel": self.Exit,
                "ok": self.Ok,
            }, -1
        )

        self.onShow.append(self.Start2)

    def Ok(self):
        global alpha

        sel = self["list"].getCurrent().split(' ')[2]
        if sel == "56%":
            alpha = '#90000000'
            self.close()
        elif sel == "50%":
            alpha = '#80000000'
            self.close()
        elif sel == "44%":
            alpha = '#70000000'
            self.close()
        elif sel == "38%":
            alpha = '#60000000'
            self.close()
        elif sel == "31%":
            alpha = '#50000000'
            self.close()
        elif sel == "25%":
            alpha = '#40000000'
            self.close()
        elif sel == "19%":
            alpha = '#30000000'
            self.close()
        elif sel == "13%":
            alpha = '#20000000'
            self.close()
        elif sel == "6%":
            alpha = '#10000000'
            self.close()

    def Start2(self):
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))
        self['text1'].text = (
            _('Window transparency') +
            ' - ' +
            conv_alpha(alpha))

        list = []

        list.append(_("Transparency level") + " 56% (#90000000)")  # 90
        list.append(_("Transparency level") + " 50% (#80000000)")  # 80
        list.append(_("Transparency level") + " 44% (#70000000)")  # 70
        list.append(_("Transparency level") + " 38% (#60000000)")  # 60
        list.append(_("Transparency level") + " 31% (#50000000)")  # 50
        list.append(_("Transparency level") + " 25% (#40000000)")  # 40
        list.append(_("Transparency level") + " 19% (#30000000)")  # 30
        list.append(_("Transparency level") + " 13% (#20000000)")  # 20
        list.append(_("Transparency level") + " 6%  (#10000000)")  # 10
        self["list"].setList(list)

    def Exit(self):
        self.close()


class Meteogram_Foreca4_FHD(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = Meteogram_Foreca4_FHD
    elif sz_w == 2560:
        skin = Meteogram_Foreca4_UHD
    else:
        skin = Meteogram_Foreca4_HD

    def __init__(self, session):
        Screen.__init__(self, session)

        if myloc == 0:
            self['title1'] = StaticText(_('Meteogram') + str(share_town0))
        else:
            self['title1'] = StaticText(_('Meteogram'))

        self["pic"] = Pixmap()
        self["plate0"] = Label("N/A")
        self["plate1"] = Label("N/A")

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions",
                "HelpActions",
                "EPGSelectActions"
            ],
            {
                "cancel": self.Exit,
                'ok': self.Exit,
            }, -1
        )
        self.onLayoutFinish.append(self.Start1)
        self.onShow.append(self.Start2)

    def Start2(self):
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

    def Start1(self):
        if myloc == 0:
            if os.path.exists("/tmp/foreca_com_2_w.png"):
                self["pic"].instance.setPixmapFromFile(
                    "/tmp/foreca_com_2_w.png")
                self["pic"].instance.show()
            else:
                self["pic"].instance.setPixmapFromFile(
                    "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/no_data.png")
                self["pic"].instance.show()
        else:
            self["pic"].instance.setPixmapFromFile(
                "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/no_data.png")
            self["pic"].instance.show()

    def Exit(self):
        self.close()


class CityPanel4List(GUIComponent):
    def __init__(self, entries):
        GUIComponent.__init__(self)
        self.lst = eListboxPythonMultiContent()
        self.lst.setFont(0, gFont("Regular", 30))
        self.foregroundColor = 0xffffff  # bianco
        self.foregroundColorSelected = 0x00a0ff  # blu
        self.backgroundColor = 0x000000  # nero
        self.backgroundColorSelected = 0x2c2c2c  # grigio scuro
        self.itemHeight = 40
        self.column = 50
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
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = CityPanel4_FHD
    elif sz_w == 2560:
        skin = CityPanel4_UHD
    else:
        skin = CityPanel4_HD

    def __init__(self, session):
        self.session = session
        self.config_path = config_path
        Screen.__init__(self, session)
        self.setup_title = _("Select a city")
        self.city_list = []
        self.Mlist = []
        self["Mlist"] = CityPanel4List([])

        self["key_green"] = StaticText(_("Favorite 1"))
        self["key_yellow"] = StaticText(_("Favorite 2"))
        self["key_blue"] = StaticText(_("Home"))
        self["key_ok"] = StaticText(_("Forecast"))
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
        from enigma import eTimer

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

        city_cfg_path = os.path.join(self.config_path, "new_city.cfg")
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

            from enigma import eTimer

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

        fav_file = os.path.join(self.config_path, f"{fav_type}.cfg")
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


class UnitSettings(Screen):
    """Unit settings screen"""

    def __init__(self, session):
        Screen.__init__(self, session)
        self.setTitle(_("Unit Settings"))

        self["list"] = MenuList([
            _("Metric System (Celsius, km/h, hPa)"),
            _("Imperial System (Fahrenheit, mph, inHg)")
        ])

        self["actions"] = ActionMap(["OkCancelActions"], {
            "ok": self.select_unit,
            "cancel": self.exit
        }, -1)

    def select_unit(self):
        selection = self["list"].getCurrentIndex()
        unit_system = "metric" if selection == 0 else "imperial"

        # Save to configuration file
        with open(unit_file, "w") as f:
            f.write("# configuration file for the units : metric or imperial\n{0}".format(
                unit_system))

        self.session.open(
            MessageBox,
            _("Unit settings saved. Restart plugin to apply changes."),
            MessageBox.TYPE_INFO
        )
        self.close()

    def exit(self):
        self.close()


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

    session.open(ForecaPreview_4)


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
