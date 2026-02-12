# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import gettext
import codecs

from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Components.Language import language
from Tools.Directories import fileExists
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

    resolution = get_resolution_type()
    skin_file = join(SKINS_PATH, resolution, "%s.xml" % class_name)

    if not fileExists(skin_file):
        skin_file = join(SKINS_PATH, "hd", "%s.xml" % class_name)

    if fileExists(skin_file):
        try:
            with codecs.open(skin_file, 'r', 'utf-8') as f:
                return f.read()
        except BaseException:
            pass

    return None


def load_skin_for_class(cls):
    return load_skin_by_class(cls.__name__)
