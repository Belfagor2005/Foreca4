# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import gettext
import codecs

from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Components.Language import language
from os.path import join, dirname
from enigma import getDesktop


PLUGIN_PATH = dirname(__file__)
SKINS_PATH = join(PLUGIN_PATH, "skins")
PluginLanguageDomain = "Foreca4"
PluginLanguagePath = "Extensions/Foreca4/locale"
isDreambox = os.path.exists("/usr/bin/apt-get")


def localeInit():
    if isDreambox:
        lang = language.getLanguage()[:2]
        os.environ["LANGUAGE"] = lang
    if PluginLanguageDomain and PluginLanguagePath:
        gettext.bindtextdomain(
            PluginLanguageDomain,
            resolveFilename(
                SCOPE_PLUGINS,
                PluginLanguagePath))


if isDreambox:
    def _(txt):
        return gettext.dgettext(PluginLanguageDomain, txt) if txt else ""
else:
    def _(txt):
        translated = gettext.dgettext(PluginLanguageDomain, txt)
        if translated:
            return translated
        else:
            print(
                "[%s] fallback to default translation for %s" %
                (PluginLanguageDomain, txt))
            return gettext.gettext(txt)


localeInit()
language.addCallback(localeInit)


# ============ DETECT SCREEN RESOLUTION ============
def get_screen_resolution():
    """Get current screen resolution"""
    desktop = getDesktop(0)
    return desktop.size()


def get_resolution_type():
    """Get resolution type: hd, fhd, wqhd"""
    width = get_screen_resolution().width()

    if width >= 2560:
        return 'wqhd'
    elif width >= 1920:
        return 'fhd'
    else:  # 1280x720 or smaller
        return 'hd'


def load_skin_by_class(class_name):
    """Load skin using class name and current resolution"""

    print("\n" + "=" * 60)
    print(f"[SKIN DEBUG] Looking for skin: '{class_name}'")
    print(f"[SKIN DEBUG] SKINS_PATH = {SKINS_PATH}")

    # Lista tutte le cartelle skins
    import os
    if os.path.exists(SKINS_PATH):
        print(f"[SKIN DEBUG] Contents of {SKINS_PATH}:")
        for item in os.listdir(SKINS_PATH):
            print(f"  - {item}")
    else:
        print("[SKIN DEBUG] SKINS_PATH does NOT exist!")

    resolution = get_resolution_type()
    print(f"[SKIN DEBUG] resolution = {resolution}")

    skin_file = join(SKINS_PATH, resolution, f"{class_name}.xml")
    print(f"[SKIN DEBUG] Trying: {skin_file}")
    print(f"[SKIN DEBUG] Exists? {os.path.exists(skin_file)}")

    if not os.path.exists(skin_file):
        print("[SKIN DEBUG] NOT FOUND, trying HD fallback")
        skin_file = join(SKINS_PATH, "hd", f"{class_name}.xml")
        print(f"[SKIN DEBUG] Trying: {skin_file}")
        print(f"[SKIN DEBUG] Exists? {os.path.exists(skin_file)}")

    if os.path.exists(skin_file):
        print("[SKIN DEBUG] ✓ FOUND! Loading file...")
        try:
            with codecs.open(skin_file, 'r', 'utf-8') as f:
                content = f.read()
                print(f"[SKIN DEBUG] ✓ Loaded {len(content)} bytes")
                print(f"[SKIN DEBUG] First 100 chars: {content[:100].replace(chr(10), ' ')}")
                print("=" * 60 + "\n")
                return content
        except Exception as e:
            print(f"[SKIN DEBUG] ✗ Error reading file: {e}")
    else:
        print(f"[SKIN DEBUG] ✗ SKIN FILE MISSING: {skin_file}")

    print("=" * 60 + "\n")
    return None


def load_skin_for_class(cls):
    return load_skin_by_class(cls.__name__)
