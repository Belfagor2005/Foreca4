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
#     Source of information: https://www.foreca.ba
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

from __future__ import absolute_import

# Standard library imports
import os
from sys import version_info
from threading import Thread

# Enigma2 imports
from Components.ActionMap import ActionMap, HelpableActionMap
from Components.config import config
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
)
from enigma import gRGB
from Plugins.Plugin import PluginDescriptor
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
    About_Foreca4_FHD,
    About_Foreca4_HD,
    ColorSelect_FHD,
    ColorSelect_HD,
    ExtInfo_2_Foreca4_FHD,
    ExtInfo_2_Foreca4_HD,
    ExtInfo_Foreca4_FHD,
    ExtInfo_Foreca4_HD,
    ForecaPreview_4_FHD,
    ForecaPreview_4_HD,
    Meteogram_Foreca4_FHD,
    Meteogram_Foreca4_HD,
    Transparency_Foreca4_FHD,
    Transparency_Foreca4_HD,
)
from .slideshow import ForecaMapsMenu
from .tt_weather import getPageTT


VERSION = "1.3.4_r2"
try:
    TARGET_LANG = config.misc.language.value.split('_')[0]
except:
    TARGET_LANG = "en"


# base constant
BASEURL = "https://www.foreca.com/"
config_path = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/"

path_loc0 = '103169070/Rome-Italy'                        # Blue - Favorite 0
path_loc1 = '100524901/Moscow-Russia'                     # Green - Favorite 1
path_loc2 = '102961214/Thurles-County-Tipperary-Ireland'  # Yellow - Favorite 2


# Home @lululla
home_file = config_path + "home.cfg"
if os.path.exists(home_file):
    try:
        with open(home_file, "r") as f:
            path_loc0 = f.read().strip()
    except:
        pass

# Favorite 1
fav1_file = config_path + "fav1.cfg"
if os.path.exists(fav1_file):
    try:
        with open(fav1_file, "r") as f:
            path_loc1 = f.read().strip()
    except:
        pass

# Favorite 2
fav2_file = config_path + "fav2.cfg"
if os.path.exists(fav2_file):
    try:
        with open(fav2_file, "r") as f:
            path_loc2 = f.read().strip()
    except:
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
    if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_alpha.conf") is True:
        try:
            with open("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_alpha.conf", "r") as file:
                contents = file.readlines()
                a = str(contents[0])
                alpha = a.rstrip()
                file.close()
        except:
            alpha = '#40000000'
    # else:
        # alpha = '#40000000'


readsetalpha()


def savesetalpha(indata):
    f = open('/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_alpha.conf', 'w')
    f.write(indata)
    f.close()


def conv_day_len(indata):
    rez = indata
    try:
        inall = indata.split(' ')
        in2 = _(str(inall[1]))
        in3 = _(str(inall[3]))
        rez = inall[0] + ' ' + str(in2) + ' ' + inall[2] + ' ' + str(in3)
    except:
        rez = indata
    return rez


def mywindSpeed(indata, metka):
    try:
        rez = 0
        rez = '%.01f' % float(int(indata) / 1)
        if metka == 1:
            return float(rez)
        else:
            rez = '%.01f' % float(int(indata))
            return float(rez)
    except:
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
            print(f"[Foreca4] Loaded {len(_translation_cache)} translations from cache")
        except Exception as e:
            print(f"[Foreca4] Cache loading error: {e}")

    _translation_cache_loaded = True
    return _translation_cache


def save_translation_cache(original, translated):
    """Save a translation to the cache file"""
    # global _translation_cache
    try:
        with open(_translation_cache_file, "a", encoding='utf-8') as f:
            f.write(f"{original}={translated}\n")
    except Exception as e:
        print(f"[Foreca4] Cache save error: {e}")


def trans(text, use_batch=True):
    """
    Enhanced translation function using improved translation module.

    Args:
        text: Text to translate
        use_batch: Whether to use batch translation optimization

    Returns:
        Translated text or original if translation fails
    """
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
            for idx, (original, translated) in enumerate(zip(to_translate, translated_batch)):
                if translated and translated != original:
                    _translation_cache[original] = translated
                    # Update result at correct index
                    results[indices[idx]] = translated
                else:
                    results[indices[idx]] = original

        except Exception as e:
            print(f"[Foreca4] Batch translation error: {e}")
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


"""
def trans(t):
    rez = t
    try:
        s = t
        # 1. FIRST check the local cache
        cache = load_translation_cache()
        if s in cache:
            return cache[s]

        # 2. Try to translate with a shorter timeout
        import socket
        socket.setdefaulttimeout(2)  # 2 seconds instead of 10

        # Read system language
        try:
            from Components.config import config
            target_lang = config.misc.language.value.split('_')[0]
        except:
            target_lang = "en"  # Fallback

        print(f"[Foreca4] Translating '{s[:30]}...' to {target_lang}")
        translate_text_1 = translate_text(s, target_lang=target_lang)
        rez = translate_text_1
        # Save to cache for next time
        if rez != s:
            _translation_cache[s] = rez
            save_translation_cache(s, rez)
        socket.setdefaulttimeout(10)  # Restore

    except socket.timeout:
        print(f"[Foreca4] Translation TIMEOUT: '{t}'")
        rez = t
    except Exception as e:
        print(f"[Foreca4] Translation ERROR '{t}': {type(e).__name__}")
        rez = t

    return rez
"""


class ForecaPreview_4(Screen, HelpableScreen):
    def __init__(self, session):
        global town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset
        global f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day

        self.session = session
        self.tag = 0

        MAIN_PAGE_F = str(BASEURL) + path_loc0
        MAIN_PAGE_FF = str(BASEURL) + path_loc0 + '/hourly?day=0'

        print(f"[Foreca4] Fetching from: {MAIN_PAGE_F}")

        try:
            # DEVI usare le variabili GLOBALI già dichiarate sopra
            result_current = getPageF(MAIN_PAGE_F)
            print(f"[Foreca4] Current weather result: {result_current[:5]}...")  # Prima 5 elementi

            # Assegna alle variabili GLOBALI
            town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = result_current
        except Exception as e:
            print(f"[Foreca4] Error getting current weather: {e}")
            # Inizializza le variabili GLOBALI
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
            lon = ' n/a'
            lat = ' n/a'
            sunrise = ' n/a'
            daylen = ' n/a'
            sunset = ' n/a'

        print(f"[Foreca4] Fetching forecast from: {MAIN_PAGE_FF}")
        try:
            result_forecast = getPageF_F(MAIN_PAGE_FF)
            print(f"[Foreca4] Forecast result length: {len(result_forecast[1]) if result_forecast and len(result_forecast) > 1 else 'N/A'}")

            # Assegna alle variabili GLOBALI
            f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = result_forecast
        except Exception as e:
            print(f"[Foreca4] Error getting forecast: {e}")
            # Inizializza le variabili GLOBALI
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
            f_day = ' n/a'

        if size_w == 1920:
            self.skin = ForecaPreview_4_FHD
        else:
            self.skin = ForecaPreview_4_HD

        Screen.__init__(self, session)
        self.setTitle(_("Foreca Weather Forecast") + " " + _("v.") + VERSION)
        self.list = []
        self["menu"] = List(self.list)
        self["Titel"] = StaticText()
        self["mytitel2"] = StaticText()
        self["Titel2"] = StaticText(_("Please wait ..."))
        self["Titel3"] = StaticText()
        self["Titel5"] = StaticText()
        self["mytitel1"] = StaticText()
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
        HelpableScreen.__init__(self)
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

    def menu_callback(self, choice):
        """Gestisce la selezione"""
        if choice is None:
            return

        if choice[1] == "city":
            self.session.open(CityPanel4)
        elif choice[1] == "maps":
            self.open_maps_menu()
        elif choice[1] == "transparency":
            self.session.open(TransparencyBox)

    def Menu(self):
        """Menu semplice con ChoiceBox"""
        from Screens.ChoiceBox import ChoiceBox

        menu_items = [
            (_("City Selection"), "city"),
            (_("Weather Maps"), "maps"),
            (_("Transparency Settings"), "transparency"),
            (_("Exit"), "exit")
        ]

        self.session.openWithCallback(
            self.menu_callback,
            ChoiceBox,
            title=_("Foreca Menu"),
            list=menu_items
        )

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

    def region_selected_callback(self, result=None):
        """Callback quando si seleziona una regione (non serve fare nulla)"""
        pass

    def open_foreca_api_maps(self):
        """Open Foreca API maps"""
        try:
            api = ForecaMapAPI()
            if not api.check_credentials():
                self.session.open(
                    MessageBox,
                    _("API credentials not configured.\nPlease create api_config.txt file.\n\nExample file created: api_config.txt.example"),
                    MessageBox.TYPE_ERROR,
                    timeout=10
                )
                return
            self.session.open(ForecaMapMenu, api)
        except Exception as e:
            print(f"[Foreca4] Error opening API maps: {e}")
            self.session.open(
                MessageBox,
                _("Could not initialize map API.\nCheck configuration."),
                MessageBox.TYPE_ERROR
            )

    def OK(self):
        PY3 = version_info[0] == 3
        if PY3:
            self.session.open(ExtInfo_Foreca4_FHD)
        else:
            self.session.open(ExtInfo_2_Foreca4_FHD)

    def savesetcolor(self, indata):
        f = open('/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_color.conf', 'w')
        f.write(indata)
        f.close()

    def readsetcolor(self):
        global rgbmyr, rgbmyg, rgbmyb
        rgbmyr = 0
        rgbmyg = 80
        rgbmyb = 239
        if os.path.exists("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_color.conf") is True:
            try:
                with open("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/set_color.conf", "r") as file:
                    contents = file.readlines()
                    a = str(contents[0])
                    rez = a.rstrip()
                    rgbmyr = rez.split(' ')[0]
                    rgbmyg = rez.split(' ')[1]
                    rgbmyb = rez.split(' ')[2]
                    file.close()
            except:
                rgbmyr = 0
                rgbmyg = 80
                rgbmyb = 239
        # else:
            # rgbmyr = 0
            # rgbmyg = 80
            # rgbmyb = 239

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
        self.update_widget_translations()

    def debug_data(self):
        """Debug function to check data"""
        print(f"[Foreca4 DEBUG] town: {town}")
        print(f"[Foreca4 DEBUG] country: {country}")
        print(f"[Foreca4 DEBUG] f_date type: {type(f_date)}, length: {len(f_date)}")
        print(f"[Foreca4 DEBUG] f_date content: {f_date}")
        print(f"[Foreca4 DEBUG] f_day: {f_day}")

        if f_date and len(f_date) > 0:
            print(f"[Foreca4 DEBUG] f_date[0]: {f_date[0]}")
        else:
            print("[Foreca4 DEBUG] f_date is empty or None")

    def StartPageFirst(self):
        # global town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, f_date, lon, lat, sunrise, daylen, sunset, f_day

        self.debug_data()

        self.readsetcolor()
        self["pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/d000.png")
        self["pic"].instance.show()
        self["wind"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/wS.png")
        self["wind"].instance.show()
        self["pressure_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/barometer.png")
        self["pressure_pic"].instance.show()
        self["rain_mm_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/precipitation.png")
        self["rain_mm_pic"].instance.show()
        self["hum_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/humidity.png")
        self["hum_pic"].instance.show()
        self["sun"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/sun.png")
        self["sun"].instance.show()

        # TRANSLATE widget titles
        self["mytitel1"].text = _("Current weather and forecast")
        self["mytitel2"].text = "<< ver. " + str(VERSION) + ' >>'

        date_str = ""
        if f_date and len(f_date) > 0:
            date_str = str(f_date[0])
        else:
            date_str = trans("No date available")

        day_str = trans(f_day) if f_day and f_day != ' n/a' else ""

        # TRANSLATE the title widget
        self["Titel"].text = trans(str(town)) + ', ' + trans(str(country)) + ' - ' + date_str
        if day_str:
            self["Titel"].text += ' - ' + day_str

        if daylen and daylen != ' n/a':
            self["day_len"].setText(str(conv_day_len(daylen)))
        else:
            self["day_len"].setText("N/A")

        if sunrise and sunrise != ' n/a':
            self["sunrise_val"].setText(str(sunrise))
        else:
            self["sunrise_val"].setText("N/A")

        if sunset and sunset != ' n/a':
            self["sunset_val"].setText(str(sunset))
        else:
            self["sunset_val"].setText("N/A")

        # TRANSLATE sunrise/sunset labels
        self["sunrise_text"].setText(trans("Sunrise"))
        self["sunset_text"].setText(trans("Sunset"))

        self.update_button()

        Thread0 = Thread(target=self.mypicload)
        Thread0.start()

    # def StartPageFirst(self):
        # # global town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, f_date, lon, lat, sunrise, daylen, sunset, f_day
        # self.readsetcolor()
        # self["pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/d000.png")
        # self["pic"].instance.show()
        # self["wind"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/wS.png")
        # self["wind"].instance.show()
        # self["pressure_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/barometer.png")
        # self["pressure_pic"].instance.show()
        # self["rain_mm_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/precipitation.png")
        # self["rain_mm_pic"].instance.show()
        # self["hum_pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/humidity.png")
        # self["hum_pic"].instance.show()
        # self["sun"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/sun.png")
        # self["sun"].instance.show()
        # self["mytitel1"].text = _("Current weather and forecast")
        # self["mytitel2"].text = _("<< ver. ") + str(VERSION) + ' >>'
        # self["Titel"].text = _(str(town)) + ', ' + _(str(country)) + ' - ' + str(f_date[0]) + ' - ' + _(f_day)
        # self["day_len"].setText(str(conv_day_len(daylen)))
        # self["sunrise_val"].setText(str(sunrise))
        # self["sunset_val"].setText(str(sunset))

        # Thread0 = Thread(target=self.mypicload)
        # Thread0.start()

    def mypicload(self):
        # global lon, lat
        download_pic = '/tmp/385.png ' + 'https://map-cf.foreca.net/teaser/map/light/rain/6/' + str(lon) + '/' + str(lat) + '/317/385.png?names'
        try:
            os.system('wget -O ' + str(download_pic))
        except:
            pass

    def my_forecast_weather(self):
        # global f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum

        self.list = []
        i = len(f_time)
        n = 0

        # Prepare descriptions for batch translation
        descriptions_to_translate = []
        for symb in f_symb:
            if symb != ' n/a':
                descriptions_to_translate.append(self.symbolToCondition(str(symb)))
            else:
                descriptions_to_translate.append("Unknown")

        # Translate all descriptions at once
        translated_descriptions = translate_batch_strings(descriptions_to_translate)

        while n <= i - 1:
            if int(f_cur_temp[n]) >= 0:
                myf_cur_temp = '+' + str(f_cur_temp[n])
            else:
                myf_cur_temp = str(f_cur_temp[n])

            try:
                minipng = LoadPixmap(cached=True, path=resolveFilename(SCOPE_PLUGINS, "Extensions/Foreca4/thumb/" + str(f_symb[n]) + ".png"))
            except:
                minipng = LoadPixmap(cached=True, path=resolveFilename(SCOPE_PLUGINS, "Extensions/Foreca4/thumb/n600.png"))

            try:
                f_myw = int(f_wind[n])
                f_myw1 = self.degreesToWindDirection(f_myw)
                minipng1 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_PLUGINS, "Extensions/Foreca4/thumb/" + str(f_myw1) + ".png"))
            except:
                minipng1 = LoadPixmap(cached=True, path=resolveFilename(SCOPE_PLUGINS, "Extensions/Foreca4/thumb/w360.png"))

            try:
                f_w_s = str(mywindSpeed(f_wind_speed[n], for_wind_speed_recalc)) + ' ' + trans('km/h')
            except:
                f_w_s = '0.00' + ' ' + trans('km/h')

            # Use translated description
            f_description = translated_descriptions[n] if n < len(translated_descriptions) else descriptions_to_translate[n]

            if int(f_flike_temp[n]) >= 0:
                myf_flike_temp = '+' + str(f_flike_temp[n])
            else:
                myf_flike_temp = str(f_flike_temp[n])

            pos8 = trans('Feels like: ') + str(myf_flike_temp) + six.ensure_str(six.unichr(176)) + 'C'

            pos9 = trans('Precipitations:') + ' ' + str(f_precipitation[n]) + '%'

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

        self["menu"].setList(self.list)

    def my_cur_weather(self):
        """Update current weather display with proper translations"""
        # global town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country
        # Translate city and country
        translated_town = _(str(town)) if town != ' n/a' else _("N/A")
        # translated_country = _(str(country)) if country != ' n/a' else ""  # RIMUOVI O COMMENTA

        self["town"].setText(translated_town)

        # Temperature values
        if cur_temp != ' n/a':
            self["cur_temp"].setText(f"{cur_temp}°C")
        else:
            self["cur_temp"].setText("N/A")

        # Feels like temperature
        if fl_temp != ' n/a':
            self["fl_temp"].setText(_('Feels like ') + f"{fl_temp}°C")
        else:
            self["fl_temp"].setText(_('Feels like ') + _("N/A"))

        # Dewpoint
        if dewpoint != ' n/a':
            self["dewpoint"].setText(_('Dewpoint ') + f"{dewpoint}°C")
        else:
            self["dewpoint"].setText(_('Dewpoint ') + _("N/A"))

        # Weather icon
        try:
            icon_path = f"/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/{pic}.png"
            if os.path.exists(icon_path):
                self["pic"].instance.setPixmapFromFile(icon_path)
            else:
                self["pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/n600.png")
        except:
            pass

        # Weather description
        if pic != ' n/a':
            description = self.symbolToCondition(str(pic))
            self["description_w"].setText(_(description))
        else:
            self["description_w"].setText("N/A")

        # Wind direction icon
        try:
            if wind != ' n/a' and 'w' in str(wind):
                myw = int(wind.split('w')[1])
                myw1 = self.degreesToWindDirection(myw)
                wind_icon = f"/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/{myw1}.png"
                if os.path.exists(wind_icon):
                    self["wind"].instance.setPixmapFromFile(wind_icon)
        except:
            pass

        # Wind speed
        if wind_speed != ' n/a':
            speed = mywindSpeed(wind_speed, cur_wind_speed_recalc)
            self["wind_speed"].setText(_('Wind speed ') + f"{speed} " + _('km/h'))
        else:
            self["wind_speed"].setText(_('Wind speed ') + _('N/A'))

        # Wind gust
        if wind_gust != ' n/a':
            gust = mywindSpeed(wind_gust, cur_wind_speed_recalc)
            self["wind_gust"].setText(_('Gust ') + f"{gust} " + _('km/h'))
        else:
            self["wind_gust"].setText(_('Gust ') + _('N/A'))

        # Precipitation
        self["rain_mm"].setText(f"{rain_mm} " + _('mm') if rain_mm != ' n/a' else _("N/A"))

        # Humidity
        self["hum"].setText(f"{hum}%" if hum != ' n/a' else _("N/A"))

        # Pressure
        self["pressure"].setText(f"{pressure} " + _('hPa') if pressure != ' n/a' else _("N/A"))

    """
    # def my_cur_weather(self):
        # # global town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset
        # self["town"].setText(_(str(town)))
        # self["cur_temp"].setText(str(cur_temp) + six.ensure_str(six.unichr(176)) + 'C')
        # self["fl_temp"].setText(_('Feels like ') + str(fl_temp) + six.ensure_str(six.unichr(176)) + 'C')
        # self["dewpoint"].setText(_('Dewpoint ') + '       ' + str(dewpoint) + six.ensure_str(six.unichr(176)) + 'C')

        # try:
            # self["pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(pic) + ".png")
            # self["pic"].instance.show()
        # except:
            # self["pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/n600.png")
            # self["pic"].instance.show()

        # try:
            # myw = int(wind.split('w')[1])
            # myw1 = self.degreesToWindDirection(myw)
            # self["wind"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(myw1) + ".png")
            # self["wind"].instance.show()
        # except:
            # self["wind"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/w360.png")
            # self["wind"].instance.show()

        # try:
            # self["wind_speed"].setText(_('Wind speed ') + str(mywindSpeed(wind_speed, cur_wind_speed_recalc)) + ' ' + _('km/h'))
        # except:
            # self["wind_speed"].setText(_('Wind speed ') + ' n/a' + ' ' + _('km/h'))

        # try:
            # self["wind_gust"].setText(_('Gust ') + '  ' + str(mywindSpeed(wind_gust, cur_wind_speed_recalc)) + ' ' + _('km/h'))
        # except:
            # self["wind_gust"].setText(_('Gust ') + '  ' + ' n/a' + ' ' + _('km/h'))

        # self["rain_mm"].setText(str(rain_mm) + ' ' + _('mm'))
        # self["hum"].setText(str(hum) + '%')
        # self["pressure"].setText(str(pressure) + ' ' + _('hPa') + '.')
        # self["description_w"].setText(_(str(self.symbolToCondition(str(pic)))))
    """

    def StartPage(self):
        date_str = ""
        if f_date and len(f_date) > 0:
            date_str = str(f_date[0])
        else:
            date_str = trans("No date available")

        day_str = trans(f_day) if f_day and f_day != ' n/a' else ""

        # TRANSLATE the title widget
        self["Titel"].text = trans(str(town)) + ', ' + trans(str(country)) + ' - ' + date_str
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

    def Fav0(self):
        global myloc, town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, lon, lat, sunrise, daylen, sunset, f_day
        myloc = 0
        MAIN_PAGE_F = str(BASEURL) + path_loc0
        town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = getPageF(MAIN_PAGE_F)

        self.my_cur_weather()

        MAIN_PAGE_FF = str(BASEURL) + path_loc0 + '/hourly?day=0'
        f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(MAIN_PAGE_FF)
        self.my_forecast_weather()

        self.update_widget_translations()

        self["day_len"].setText(str(conv_day_len(daylen)))
        self["sunrise_val"].setText(str(sunrise))
        self["sunset_val"].setText(str(sunset))

        Thread1 = Thread(target=self.mypicload)
        Thread1.start()

        self.titel()
        self.Zukunft(0)

    def Fav1(self):
        global myloc, town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, lon, lat, sunrise, daylen, sunset, f_day
        myloc = 1
        MAIN_PAGE_F = str(BASEURL) + path_loc1
        town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = getPageF(MAIN_PAGE_F)

        self.my_cur_weather()

        MAIN_PAGE_FF = str(BASEURL) + path_loc1 + '/hourly?day=0'
        f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(MAIN_PAGE_FF)
        self.my_forecast_weather()

        self.update_widget_translations()

        self["day_len"].setText(str(conv_day_len(daylen)))
        self["sunrise_val"].setText(str(sunrise))
        self["sunset_val"].setText(str(sunset))

        Thread2 = Thread(target=self.mypicload)
        Thread2.start()

        self.titel()
        self.Zukunft(0)

    def Fav2(self):
        global myloc, town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, lon, lat, sunrise, daylen, sunset, f_day
        myloc = 2
        MAIN_PAGE_F = str(BASEURL) + path_loc2
        town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset = getPageF(MAIN_PAGE_F)

        self.my_cur_weather()

        MAIN_PAGE_FF = str(BASEURL) + path_loc2 + '/hourly?day=0'
        f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(MAIN_PAGE_FF)

        self.my_forecast_weather()

        self.update_widget_translations()

        self["day_len"].setText(str(conv_day_len(daylen)))
        self["sunrise_val"].setText(str(sunrise))
        self["sunset_val"].setText(str(sunset))

        Thread3 = Thread(target=self.mypicload)
        Thread3.start()

        self.titel()
        self.Zukunft(0)

    def Zukunft(self, ztag=0):
        global f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day
        self.tag = ztag

        if myloc == 0:
            MAIN_PAGE_FF = str(BASEURL) + path_loc0 + '/hourly?day=' + str(ztag)
            f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(MAIN_PAGE_FF)
            self.my_forecast_weather()
        elif myloc == 1:
            MAIN_PAGE_FF = str(BASEURL) + path_loc1 + '/hourly?day=' + str(ztag)
            f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(MAIN_PAGE_FF)
            self.my_forecast_weather()
        elif myloc == 2:
            MAIN_PAGE_FF = str(BASEURL) + path_loc2 + '/hourly?day=' + str(ztag)
            f_town, f_date, f_time, f_symb, f_cur_temp, f_flike_temp, f_wind, f_wind_speed, f_precipitation, f_rel_hum, f_day = getPageF_F(MAIN_PAGE_FF)
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

    def symbolToCondition(self, symbol):
        symbol_map = {
            'd000': _('Clear'), 'n000': _('Clear'),
            'd100': _('Mostly clear'), 'n100': _('Mostly clear'),
            'd200': _('Partly cloudy'), 'n200': _('Partly cloudy'),
            'd210': _('Partly cloudy and light rain'), 'n210': _('Partly cloudy and light rain'),
            'd211': _('Partly cloudy and light wet snow'), 'n211': _('Partly cloudy and light wet snow'),
            'd212': _('Partly cloudy and light snow'), 'n212': _('Partly cloudy and light snow'),
            'd220': _('Partly cloudy and showers'), 'n220': _('Partly cloudy and showers'),
            'd221': _('Partly cloudy and wet snow showers'), 'n221': _('Partly cloudy and wet snow showers'),
            'd222': _('Partly cloudy and snow showers'), 'n222': _('Partly cloudy and snow showers'),
            'd240': _('Partly cloudy, possible thunderstorms with rain'), 'n240': _('Partly cloudy, possible thunderstorms with rain'),
            'd300': _('Cloudy'), 'n300': _('Cloudy'),
            'd310': _('Cloudy and light rain'), 'n310': _('Cloudy and light rain'),
            'd311': _('Cloudy and light wet snow'), 'n311': _('Cloudy and light wet snow'),
            'd312': _('Cloudy and light snow'), 'n312': _('Cloudy and light snow'),
            'd320': _('Cloudy and showers'), 'n320': _('Cloudy and showers'),
            'd321': _('Cloudy and wet snow showers'), 'n321': _('Cloudy and wet snow showers'),
            'd322': _('Cloudy and snow showers'), 'n322': _('Cloudy and snow showers'),
            'd340': _('Cloudy, thunderstorms with rain'), 'n340': _('Cloudy, thunderstorms with rain'),
            'd400': _('Overcast'), 'n400': _('Overcast'),
            'd410': _('Overcast and light rain'), 'n410': _('Overcast and light rain'),
            'd411': _('Overcast and light wet snow'), 'n411': _('Overcast and light wet snow'),
            'd412': _('Overcast and light snow'), 'n412': _('Overcast and light snow'),
            'd430': _('Overcast and showers'), 'n430': _('Overcast and showers'),
            'd421': _('Overcast and wet snow showers'), 'n421': _('Overcast and wet snow showers'),
            'd432': _('Overcast and snow showers'), 'n432': _('Overcast and snow showers'),
            'd420': _('Overcast and rain'), 'n420': _('Overcast and rain'),
            'd431': _('Overcast and wet snow'), 'n431': _('Overcast and wet snow'),
            'd422': _('Overcast and snow'), 'n422': _('Overcast and snow'),
            'd440': _('Overcast, thunderstorms with rain'), 'n440': _('Overcast, thunderstorms with rain'),
            'd500': _('Thin upper cloud'), 'n500': _('Thin upper cloud'),
            'd600': _('Fog'), 'n600': _('Fog')
        }
        return symbol_map.get(symbol, _('Unknown'))

    def degreesToWindDirection(self, degrees):
        try:
            directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
            index = round(degrees / 45) % 8
            return "w" + directions[int(index)]
        except:
            return "w360"

    def red(self):
        self.session.open(Color_Select)

    def exit(self):
        """Exit plugin and optionally clean cache"""
        rez = str(rgbmyr) + ' ' + str(rgbmyg) + ' ' + str(rgbmyb)
        self.savesetcolor(rez)
        savesetalpha(alpha)

        # Clean cache on exit (optional)
        self.clean_foreca_cache()

        self.close()

    def update_widget_translations(self):
        """Update all translatable widgets in the GUI with proper translation handling"""
        # global town, cur_temp, fl_temp, dewpoint, wind_speed, wind_gust, rain_mm, hum, pressure, country
        # global f_date, f_day, daylen, sunrise, sunset, pic

        try:
            # Update title widgets with proper translation
            self["mytitel1"].text = _("Current weather and forecast")
            self["mytitel2"].text = "<< ver. " + str(VERSION) + ' >>'

            # Update main title with proper formatting
            date_str = ""
            if f_date and len(f_date) > 0:
                date_str = str(f_date[0])
            else:
                date_str = trans("No date available")

            day_str = trans(f_day) if f_day and f_day != ' n/a' else ""

            # Format title properly
            town_str = trans(str(town)) if town != ' n/a' else "N/A"
            country_str = trans(str(country)) if country != ' n/a' else ""

            title_parts = []
            if town_str:
                title_parts.append(town_str)
            if country_str:
                title_parts.append(country_str)
            if date_str:
                title_parts.append(date_str)
            if day_str:
                title_parts.append(day_str)

            self["Titel"].text = ' - '.join(title_parts)

            # Update sunrise/sunset labels
            if hasattr(self, 'sunrise_text'):
                self["sunrise_text"].setText(trans('Sunrise'))
            if hasattr(self, 'sunset_text'):
                self["sunset_text"].setText(trans('Sunset'))

            # Update day length
            if hasattr(self, 'day_len'):
                if daylen and daylen != ' n/a':
                    self["day_len"].setText(str(conv_day_len(daylen)))
                else:
                    self["day_len"].setText("N/A")

            # Update sunrise/sunset times
            if hasattr(self, 'sunrise_val'):
                self["sunrise_val"].setText(str(sunrise) if sunrise != ' n/a' else "N/A")
            if hasattr(self, 'sunset_val'):
                self["sunset_val"].setText(str(sunset) if sunset != ' n/a' else "N/A")

            # Update current weather widgets
            if hasattr(self, 'town'):
                self["town"].setText(trans(str(town)) if town != ' n/a' else "N/A")

            if hasattr(self, 'description_w'):
                if pic != ' n/a':
                    description = self.symbolToCondition(str(pic))
                    self["description_w"].setText(trans(description))
                else:
                    self["description_w"].setText("N/A")

            # Update temperature widgets with proper formatting
            if hasattr(self, 'cur_temp'):
                if cur_temp != ' n/a':
                    self["cur_temp"].setText(f"{cur_temp}°C")
                else:
                    self["cur_temp"].setText("N/A")

            # CORREZIONE CRITICA: Usa le variabili globali corrette
            if hasattr(self, 'fl_temp'):
                if fl_temp != ' n/a':
                    self["fl_temp"].setText(trans('Feels like ') + f"{fl_temp}°C")
                else:
                    self["fl_temp"].setText(trans('Feels like ') + "N/A")

            if hasattr(self, 'dewpoint'):
                if dewpoint != ' n/a':
                    self["dewpoint"].setText(trans('Dewpoint ') + f"{dewpoint}°C")
                else:
                    self["dewpoint"].setText(trans('Dewpoint ') + "N/A")

            # Update wind widgets
            if hasattr(self, 'wind_speed'):
                if wind_speed != ' n/a':
                    speed = mywindSpeed(wind_speed, cur_wind_speed_recalc)
                    self["wind_speed"].setText(trans('Wind speed ') + f"{speed} " + trans('km/h'))
                else:
                    self["wind_speed"].setText(trans('Wind speed ') + trans('N/A'))

            if hasattr(self, 'wind_gust'):
                if wind_gust != ' n/a':
                    gust = mywindSpeed(wind_gust, cur_wind_speed_recalc)
                    self["wind_gust"].setText(trans('Gust ') + f"{gust} " + trans('km/h'))
                else:
                    self["wind_gust"].setText(trans('Gust ') + trans('N/A'))

            # Update other weather widgets
            if hasattr(self, 'rain_mm'):
                if rain_mm != ' n/a':
                    self["rain_mm"].setText(f"{rain_mm} " + trans('mm'))
                else:
                    self["rain_mm"].setText("N/A")

            if hasattr(self, 'hum'):
                if hum != ' n/a':
                    self["hum"].setText(f"{hum}%")
                else:
                    self["hum"].setText("N/A")

            if hasattr(self, 'pressure'):
                if pressure != ' n/a':
                    self["pressure"].setText(f"{pressure} " + trans('hPa'))
                else:
                    self["pressure"].setText("N/A")

            # Force GUI update for all widgets
            self.invalidate_widgets()

        except Exception as e:
            print(f"[Foreca4] Error in update_widget_translations: {e}")
            import traceback
            traceback.print_exc()

    def invalidate_widgets(self):
        """Invalidate all widgets to force GUI refresh"""
        widgets_to_invalidate = [
            "Titel", "mytitel1", "mytitel2", "town", "description_w",
            "cur_temp", "fl_temp", "dewpoint", "wind_speed", "wind_gust",
            "rain_mm", "hum", "pressure", "day_len", "sunrise_text",
            "sunset_text", "sunrise_val", "sunset_val"
        ]

        for widget_name in widgets_to_invalidate:
            try:
                if hasattr(self, widget_name):
                    widget = self[widget_name]
                    if hasattr(widget, 'instance'):
                        widget.instance.invalidate()
                    elif hasattr(widget, 'invalidate'):
                        widget.invalidate()
            except:
                pass

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
                    # Delete temporary display files (they start with 'display_' or 'merged_')
                    if filename.startswith(('display_', 'merged_', 'foreca4_merged_', 'foreca4_display_')):
                        try:
                            os.remove(filepath)
                            deleted += 1
                        except:
                            pass
                    else:
                        # For tile cache files, keep if recent (less than 1 day)
                        file_age = current_time - os.path.getmtime(filepath)
                        if file_age > 86400:  # 1 day
                            try:
                                os.remove(filepath)
                                deleted += 1
                            except:
                                pass
                        else:
                            kept += 1

            print(f"[Foreca4] Cache cleanup: {deleted} files deleted, {kept} files kept")

        except Exception as e:
            print(f"[Foreca4] Error cleaning cache: {e}")


class Color_Select(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ColorSelect_FHD
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

        self["plate0"] = Label(_("N/A"))
        self["plate1"] = Label(_("N/A"))

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
        # global rgbmyr, rgbmyg, rgbmyb, alpha
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
                with open(file_path, "r", encoding='utf-8') as f:
                    lines = f.readlines()

                for i, line in enumerate(lines):
                    line = line.strip()
                    if not line:
                        continue

                    if ' #' in line:
                        name_part, data_part = line.split(' #', 1)
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

        print("[Color_Select] === START ===")
        print(f"[Color_Select] Loaded items: {len(self.original_names)}")
        if self.Clist:
            self.update_display(0)

        self.translate_range(0, 100)
        self.last_translated_idx = 100

    def translate_range(self, start_idx, end_idx):
        import threading

        def translate():
            end_idx_actual = min(end_idx, len(self.original_names))
            print(f"[Color_Select] Translating range {start_idx} to {end_idx_actual}")
            translated_any = False
            for i in range(start_idx, end_idx_actual):
                if self.display_names[i] == self.original_names[i]:
                    translated = self.translate_color(self.original_names[i])

                    if translated != self.original_names[i]:
                        self.display_names[i] = translated
                        self.Clist[i] = f"{i}. {translated}"
                        translated_any = True

            if translated_any:
                self.update_gui()
                print(f"[Color_Select] Range {start_idx}-{end_idx_actual} translated")

        thread = threading.Thread(target=translate, daemon=True)
        thread.start()

    def translate_color(self, color_name):
        if not color_name:
            return color_name

        print(f"[Color_Select] Translate: '{color_name}'")
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
                print(f"[Color_Select] Result with iphen: '{color_name}' -> '{result}'")
                return result

            result = trans(color_name)
            print(f"[Color_Select] Result: '{color_name}' -> '{result}'")
            return result

        except Exception as e:
            print(f"[Color_Select] ERROR translating '{color_name}': {e}")
            return color_name

    def update_display(self, index):
        print(f"[Color_Select] update_display({index})")
        if 0 <= index < len(self.display_names):
            if self.display_names[index] == self.original_names[index]:
                translated = self.translate_color(self.original_names[index])
                if translated != self.display_names[index]:
                    self.display_names[index] = translated
                    self.Clist[index] = f"{index}. {translated}"
                    self.update_gui()

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
                    print("[Color_Select] Set colordatas")

                    img_path = f"/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/samples/{myhtml}.png"
                    if os.path.exists(img_path):
                        self["pic1"].instance.setPixmapFromFile(img_path)
                        self["pic1"].instance.show()
                        print("[Color_Select] Loaded image")

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
        if current_idx + 50 > self.last_translated_idx:
            new_end = self.last_translated_idx + 50
            self.translate_range(self.last_translated_idx, new_end)
            self.last_translated_idx = new_end

    def right(self):
        self["Clist"].pageDown()
        current_idx = self["Clist"].getCurrentIndex()
        self.update_display(current_idx)
        if current_idx + 50 > self.last_translated_idx:
            new_end = self.last_translated_idx + 50
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
    else:
        skin = About_Foreca4_HD

    def __init__(self, session):

        Screen.__init__(self, session)

        self['ver'] = StaticText(_('Foreca 4 Weather and Forecast') + ' ver. ' + str(VERSION))

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
        # global rgbmyr, rgbmyg, rgbmyb, alpha
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

    def Exit(self):
        self.close()


class ExtInfo_Foreca4_FHD(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ExtInfo_Foreca4_FHD
    else:
        skin = ExtInfo_Foreca4_HD

    def __init__(self, session):

        Screen.__init__(self, session)

        # global myloc

        if myloc == 0:
            MAIN_PAGE_TT = 'https://www.forecaweather.com/' + str(path_loc0)
        elif myloc == 1:
            MAIN_PAGE_TT = 'https://www.forecaweather.com/' + str(path_loc1)
        elif myloc == 2:
            MAIN_PAGE_TT = 'https://www.forecaweather.com/' + str(path_loc2)

        self.mytown, self.mytext1, self.myh_temp, self.myl_temp, self.mytext2, self.mytext3, self.myh2_temp, self.myl2_temp, self.mytext4, self.mysymb_mo1, self.mysymb_mo2, self.myt_mo1, self.myt_mo2, self.mysymb_af1, self.mysymb_af2, self.myt_af1, self.myt_af2, self.mysymb_ev1, self.mysymb_ev2, self.myt_ev1, self.myt_ev2, self.mysymb_ov1, self.mysymb_ov2, self.myt_ov1, self.myt_ov2 = getPageTT(MAIN_PAGE_TT)

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

        t1 = str(self.mytext1) + ' ' + str(self.myh_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + str(self.myl_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext2) + ' mm.'
        self["text1"].text = str(t1)

        t2 = str(self.mytext3) + ' ' + str(self.myh2_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + str(self.myl2_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext4) + ' mm.'
        self["text2"].text = str(t2)

        self['mo1'].text = _('Morning')
        self['mo2'].text = _('Morning')
        self['af1'].text = _('Afternoon')
        self['af2'].text = _('Afternoon')
        self['ev1'].text = _('Evening')
        self['ev2'].text = _('Evening')
        self['ov1'].text = _('Overnight')
        self['ov2'].text = _('Overnight')

        # global rgbmyr, rgbmyg, rgbmyb, alpha
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

        Thread4 = Thread(target=self.mytranslate)
        Thread4.start()

    def mytranslate(self):
        self['title3'].text = str(trans(_('Weather today')))
        self['title4'].text = str(trans(_('Weather tomorrow')))

        self['title2'].text = str(trans(self.mytown))

        t1 = str(self.mytext1) + ' ' + str(self.myh_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + str(self.myl_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext2) + ' mm.'
        self["text1"].text = str(trans(t1))

        t2 = str(self.mytext3) + ' ' + str(self.myh2_temp) + six.ensure_str(six.unichr(176)) + 'C, ' + str(self.myl2_temp) + six.ensure_str(six.unichr(176)) + 'C. ' + str(self.mytext4) + ' mm.'
        self["text2"].text = str(trans(t2))

    def Start1(self):
        # global lon, lat
        if os.path.exists("/tmp/385.png"):
            self["pic"].instance.setPixmapFromFile("/tmp/385.png")
            self["pic"].instance.show()

        self["pic_af1"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_af1) + ".png")
        self["pic_af1"].instance.show()
        self["pic_ev1"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ev1) + ".png")
        self["pic_ev1"].instance.show()
        self["pic_ov1"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ov1) + ".png")
        self["pic_ov1"].instance.show()
        self["pic_mo1"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_mo1) + ".png")
        self["pic_mo1"].instance.show()

        self["pic_af2"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_af2) + ".png")
        self["pic_af2"].instance.show()
        self["pic_ev2"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ev2) + ".png")
        self["pic_ev2"].instance.show()
        self["pic_ov2"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_ov2) + ".png")
        self["pic_ov2"].instance.show()
        self["pic_mo2"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/" + str(self.mysymb_mo2) + ".png")
        self["pic_mo2"].instance.show()

        self["pic_lot"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/longitude.png")
        self["pic_lot"].instance.show()
        self["pic_lat"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/latitude.png")
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
        # global rgbmyr, rgbmyg, rgbmyb, alpha
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

    def Start1(self):
        # global lon, lat
        if os.path.exists("/tmp/385.png"):
            self["pic"].instance.setPixmapFromFile("/tmp/385.png")
            self["pic"].instance.show()

        self["pic_lot"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/longitude.png")
        self["pic_lot"].instance.show()
        self["pic_lat"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/latitude.png")
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
        # global rgbmyr, rgbmyg, rgbmyb, alpha
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))
        self['text1'].text = (_('Window transparency') + ' - ' + conv_alpha(alpha))

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
    else:
        skin = Meteogram_Foreca4_HD

    def __init__(self, session):

        # global share_town0, myloc

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
        # global rgbmyr, rgbmyg, rgbmyb, alpha
        self.color = gRGB(int(rgbmyr), int(rgbmyg), int(rgbmyb))
        self["plate0"].instance.setBackgroundColor(self.color)
        self["plate1"].instance.setBackgroundColor(parseColor(alpha))

    def Start1(self):
        # global myloc
        if myloc == 0:
            if os.path.exists("/tmp/foreca_com_2_w.png"):
                self["pic"].instance.setPixmapFromFile("/tmp/foreca_com_2_w.png")
                self["pic"].instance.show()
            else:
                self["pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/no_data.png")
                self["pic"].instance.show()
        else:
            self["pic"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/no_data.png")
            self["pic"].instance.show()

    def Exit(self):
        self.close()


class CityPanel4List(MenuList):
    """Custom list for city selection with unified styling"""

    def __init__(self, list, font0=22, font1=16, itemHeight=30, enableWrapAround=True):
        MenuList.__init__(self, [], False, eListboxPythonMultiContent)
        GUIComponent.__init__(self)

        self.font0 = gFont("Regular", font0)
        self.font1 = gFont("Regular", font1)
        self.itemHeight = itemHeight

        self.foregroundColorSelected = 8900346
        self.foregroundColor = 0xffffff
        self.backgroundColorSelected = 0x565656
        self.column = 30

    def applySkin(self, desktop, parent):
        """Apply skin attributes with unified color system"""
        from skin import parseColor, parseFont

        def font(value):
            self.font0 = parseFont(value, ((1, 1), (1, 1)))

        def font1(value):
            self.font1 = parseFont(value, ((1, 1), (1, 1)))

        def itemHeight(value):
            self.itemHeight = int(value)

        def foregroundColor(value):
            self.foregroundColor = parseColor(value).argb()

        def foregroundColorSelected(value):
            self.foregroundColorSelected = parseColor(value).argb()

        def backgroundColorSelected(value):
            self.backgroundColorSelected = parseColor(value).argb()

        def column(value):
            self.column = int(value)

        # Process skin attributes
        if self.skinAttributes:
            for (attrib, value) in list(self.skinAttributes):
                try:
                    locals().get(attrib)(value)
                    self.skinAttributes.remove((attrib, value))
                except Exception as e:
                    print(f"[CityPanel4List] Error processing {attrib}: {e}")

        # Apply to list
        self.l.setFont(0, self.font0)
        self.l.setFont(1, self.font1)
        self.l.setItemHeight(self.itemHeight)

        return GUIComponent.applySkin(self, desktop, parent)


class CityPanel4(Screen):
    """City selection panel for Foreca4 plugin"""

    def __init__(self, session):
        self.session = session
        self.config_path = config_path

        size_w = getDesktop(0).size().width()
        self.skin = self.get_unified_skin(size_w)

        Screen.__init__(self, session)
        self.setup_title = _("Select a city")

        self.Mlist = []
        self["Mlist"] = CityPanel4List([])

        self["key_green"] = StaticText(_("Favorite 1"))
        self["key_yellow"] = StaticText(_("Favorite 2"))
        self["key_blue"] = StaticText(_("Home"))
        self["key_ok"] = StaticText(_("Forecast"))
        self["key_red"] = StaticText(_("Keyboard"))

        self.setTitle(_("Select a city"))

        self.filtered_list = []
        self.search_text = ""
        self.search_ok = False
        self["actions"] = HelpableActionMap(
            self, "ForecaActions",
            {
                "text": (self.open_keyboard, _("Keyboard")),
                "cancel": (self.exit, _("Exit")),
                "red": (self.open_keyboard, _("Open Keyboard")),
                "left": (self.left, _("Previous page")),
                "right": (self.right, _("Next page")),
                "up": (self.up, _("Previous")),
                "down": (self.down, _("Next")),
                "ok": (self.ok, _("Select")),
                "green": (self.save_favorite1, _("Assign to Favorite 1")),
                "yellow": (self.save_favorite2, _("Assign to Favorite 2")),
                "blue": (self.save_home, _("Assign to Home")),
                "nextBouquet": (self.jump_down, _("Jump 500 down")),
                "prevBouquet": (self.jump_up, _("Jump 500 up")),
                "volumeDown": (self.jump_100_down, _("Jump 100 down")),
                "volumeUp": (self.jump_100_up, _("Jump 100 up")),
                "showEventInfo": (self.show_info, _("Show info")),
            },
            -2
        )

        self.onShown.append(self.prepare_city_list)

    def get_unified_skin(self, size_w):
        """Get unified skin based on resolution"""
        if size_w == 1920:
            return self.get_fhd_skin()
        elif size_w == 2560:
            return self.get_uhd_skin()
        else:
            return self.get_hd_skin()

    def get_fhd_skin(self):
        """FHD skin with unified colors"""
        return """
        <screen name="CityPanel4" position="center,center" size="1200,900" title="Select a city">
            <!-- Button widgets with unified colors -->
            <widget source="key_red" render="Label" position="10,5" size="295,70" backgroundColor="key_red" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_green" render="Label" position="305,5" size="295,70" backgroundColor="key_green" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_yellow" render="Label" position="600,5" size="295,70" backgroundColor="key_yellow" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_blue" render="Label" position="895,5" size="295,70" backgroundColor="key_blue" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <!-- Separator -->
            <eLabel backgroundColor="#fe00" position="10,80" size="1180,2" />

            <!-- City list -->
            <widget name="Mlist" itemHeight="35" position="10,90" size="1180,665" enableWrapAround="1" scrollbarMode="showOnDemand" foregroundColor="$text_color" foregroundColorSelected="$selected_text_color" backgroundColorSelected="$selected_bg_color" />

            <!-- Bottom separator -->
            <eLabel backgroundColor="#fe00" position="10,770" size="1180,2" />

            <!-- Button icons -->
            <ePixmap position="1025,864" size="60,30" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_text.png" />
            <ePixmap position="379,864" size="60,30" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png" />
            <ePixmap position="42,864" size="60,30" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png" />
            <ePixmap position="705,864" size="60,30" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png" />
            <ePixmap position="1135,864" size="60,30" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png" />
            <ePixmap position="1085,864" size="60,30" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" />
        </screen>"""

    def get_uhd_skin(self):
        """UHD skin"""
        return """
        <screen name="CityPanel4" position="center,center" size="1600,1200" title="Select a city">
            <!-- Button widgets with unified colors -->
            <widget source="key_red" render="Label" position="14,7" size="394,94" backgroundColor="key_red" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_green" render="Label" position="407,7" size="394,94" backgroundColor="key_green" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_yellow" render="Label" position="800,7" size="394,94" backgroundColor="key_yellow" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_blue" render="Label" position="1194,7" size="394,94" backgroundColor="key_blue" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <eLabel backgroundColor="#fe00" position="14,107" size="1574,3"/>

            <widget name="Mlist" itemHeight="47" position="14,120" size="1574,887" enableWrapAround="1"
                    scrollbarMode="showOnDemand" foregroundColor="$text_color"
                    foregroundColorSelected="$selected_text_color"
                    backgroundColorSelected="$selected_bg_color"/>

            <eLabel backgroundColor="#fe00" position="14,1027" size="1574,3"/>

            <ePixmap position="1367,1152" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_text.png"/>
            <ePixmap position="506,1152" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png"/>
            <ePixmap position="56,1152" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png"/>
            <ePixmap position="940,1152" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png"/>
            <ePixmap position="1514,1152" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png"/>
            <ePixmap position="1447,1152" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png"/>
        </screen>"""

    def get_hd_skin(self):
        """HD skin"""
        return """
        <screen name="CityPanel4" position="center,center" size="800,600" title="Select a city">
            <!-- Button widgets with unified colors -->
            <widget source="key_red" render="Label" position="6,3" size="196,46" backgroundColor="key_red" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_green" render="Label" position="203,3" size="196,46" backgroundColor="key_green" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_yellow" render="Label" position="400,3" size="196,46" backgroundColor="key_yellow" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <widget source="key_blue" render="Label" position="596,3" size="196,46" backgroundColor="key_blue" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
                <convert type="ConditionalShowHide" />
            </widget>
            <eLabel backgroundColor="#fe00" position="6,53" size="786,1"/>

            <widget name="Mlist" itemHeight="23" position="6,60" size="786,443" enableWrapAround="1"
                    scrollbarMode="showOnDemand" foregroundColor="$text_color"
                    foregroundColorSelected="$selected_text_color"
                    backgroundColorSelected="$selected_bg_color"/>
            <eLabel backgroundColor="#fe00" position="6,513" size="786,1"/>
            <ePixmap position="683,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_text.png"/>
            <ePixmap position="252,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png"/>
            <ePixmap position="28,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png"/>
            <ePixmap position="470,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png"/>
            <ePixmap position="756,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png"/>
            <ePixmap position="723,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png"/>
        </screen>"""

    def prepare_city_list(self):
        """Load cities from new_city.cfg file"""
        self.maxidx = 0
        self.Mlist = []

        city_cfg_path = os.path.join(self.config_path, "new_city.cfg")
        if os.path.exists(city_cfg_path):
            try:
                with open(city_cfg_path, "r", encoding='utf-8') as f:
                    for line in f:
                        text = line.strip()
                        if text:  # Skip empty lines
                            self.maxidx += 1
                            entry = (text.replace("_", " "), text)
                            self.Mlist.append(self.create_city_entry(entry))
                print(f"[CityPanel4] Loaded {self.maxidx} cities")
            except Exception as e:
                print(f"[CityPanel4] Error loading new_city.cfg: {e}")
                # Show error message
                self.session.open(MessageBox,
                                  _("Error loading city list!"),
                                  MessageBox.TYPE_ERROR,
                                  timeout=5)
        else:
            print(f"[CityPanel4] new_city.cfg not found at {city_cfg_path}")
            self.session.open(MessageBox,
                              _("City list file not found!"),
                              MessageBox.TYPE_WARNING,
                              timeout=5)

        self.filtered_list = self.Mlist
        self["Mlist"].l.setList(self.filtered_list)
        self["Mlist"].selectionEnabled(1)

    def create_city_entry(self, entry):
        """Create MultiContent entry for city"""
        mblau = self["Mlist"].foregroundColorSelected
        weiss = self["Mlist"].foregroundColor
        grau = self["Mlist"].backgroundColorSelected
        itemHeight = self["Mlist"].itemHeight
        col = self["Mlist"].column

        res = [entry]
        res.append(MultiContentEntryText(
            pos=(0, 0),
            size=(col, itemHeight),
            font=0,
            text="",
            color=weiss,
            color_sel=mblau,
            backcolor_sel=grau,
            flags=RT_VALIGN_CENTER
        ))
        res.append(MultiContentEntryText(
            pos=(col, 0),
            size=(1000, itemHeight),
            font=0,
            text=entry[0],
            color=weiss,
            color_sel=mblau,
            backcolor_sel=grau,
            flags=RT_VALIGN_CENTER
        ))
        return res

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
                search_term = result.lower()

                for item in self.Mlist:
                    city_name = item[0][0].lower()
                    if search_term in city_name:
                        self.search_ok = True
                        self.filtered_list.append(item)

                if len(self.filtered_list) < 1:
                    self.session.open(MessageBox,
                                      _('No City found in search!!!'),
                                      MessageBox.TYPE_INFO,
                                      timeout=5)
                    return
                else:
                    self['Mlist'].l.setList(self.filtered_list)
                    self['Mlist'].moveToIndex(0)
                    self["Mlist"].selectionEnabled(1)
            except Exception as e:
                print(f"[CityPanel4] Search error: {e}")
                self.session.open(MessageBox,
                                  _('An error occurred during search!'),
                                  MessageBox.TYPE_ERROR,
                                  timeout=5)

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
        """Get currently selected city"""
        try:
            selection = self['Mlist'].l.getCurrentSelection()
            if selection:
                return selection[0][1].replace(" ", "_")
        except Exception as e:
            print(f"[CityPanel4] Error getting selection: {e}")
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
            print(f"[CityPanel4] Error saving {fav_type}: {e}")
            self.session.open(MessageBox,
                              _("Error saving favorite!"),
                              MessageBox.TYPE_ERROR,
                              timeout=5)
            return False

    def ok(self):
        """Select city for forecast"""
        selected = self.get_selected_city()
        if selected:
            print(f"[CityPanel4] Selected city: {selected}")
            self.close(selected)

    def show_info(self):
        """Show information/help"""
        info_text = _(
            "City Selection Help:\n\n"
            "• Use arrow keys to navigate\n"
            "• OK to select city\n"
            "• GREEN to save as Favorite 1\n"
            "• YELLOW to save as Favorite 2\n"
            "• BLUE to save as Home\n"
            "• RED to open search keyboard\n"
            "• CH+/CH- to jump 500 cities\n"
            "• VOL+/VOL- to jump 100 cities"
        )
        self.session.open(MessageBox, info_text, MessageBox.TYPE_INFO)

    # Navigation methods
    def up(self):
        self["Mlist"].up()
        self["Mlist"].selectionEnabled(1)

    def down(self):
        self["Mlist"].down()
        self["Mlist"].selectionEnabled(1)

    def left(self):
        self["Mlist"].pageUp()

    def right(self):
        self["Mlist"].pageDown()

    def jump_up(self):
        cur = self["Mlist"].l.getCurrentSelectionIndex()
        if (cur + 500) <= self.maxidx:
            self["Mlist"].instance.moveSelectionTo(cur + 500)
        else:
            self["Mlist"].instance.moveSelectionTo(self.maxidx - 1)

    def jump_down(self):
        cur = self["Mlist"].l.getCurrentSelectionIndex()
        if (cur - 500) >= 0:
            self["Mlist"].instance.moveSelectionTo(cur - 500)
        else:
            self["Mlist"].instance.moveSelectionTo(0)

    def jump_100_up(self):
        cur = self["Mlist"].l.getCurrentSelectionIndex()
        if (cur + 100) <= self.maxidx:
            self["Mlist"].instance.moveSelectionTo(cur + 100)
        else:
            self["Mlist"].instance.moveSelectionTo(self.maxidx - 1)

    def jump_100_down(self):
        cur = self["Mlist"].l.getCurrentSelectionIndex()
        if (cur - 100) >= 0:
            self["Mlist"].instance.moveSelectionTo(cur - 100)
        else:
            self["Mlist"].instance.moveSelectionTo(0)

    def exit(self):
        if self.search_ok:
            self.search_ok = False
        self.close(None)


def main(session, **kwargs):
    session.open(ForecaPreview_4)


def Plugins(path, **kwargs):
    list = [PluginDescriptor(
        name=_("Foreca 4") + " ver. " + str(VERSION),
        description=_("Current weather and forecast for the next 10 days"),
        icon="foreca_4.png",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        fnc=main)
    ]
    return list
