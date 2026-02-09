#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# slideshow.py - Manage overlay map Foreca
# Copyright (c) @Lululla 2026
from __future__ import absolute_import

from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.Pixmap import Pixmap
from Components.AVSwitch import AVSwitch
from Components.Sources.StaticText import StaticText
from Screens.Screen import Screen
from enigma import eTimer, ePicLoad, getDesktop
import os
import requests
from threading import Thread

from .skin import (
    ForecaMapsMenu_UHD,
    ForecaMapsMenu_FHD,
    ForecaMapsMenu_HD,
    ForecaSlideshow_UHD,
    ForecaSlideshow_FHD,
    ForecaSlideshow_HD
)
from . import _


CACHE_BASE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"
WETTERKONTOR_CACHE = os.path.join(CACHE_BASE, "wetterkontor/")

if not os.path.exists(WETTERKONTOR_CACHE):
    os.makedirs(WETTERKONTOR_CACHE, exist_ok=True)


REGION_MAPS_EUROPE = [
    (_("Austria"), "oesterreich"),
    (_("Belgium"), "belgien"),
    (_("Czech Republic"), "tschechien"),
    (_("Denmark"), "daenemark"),
    (_("Finland"), "finnland"),
    (_("France"), "frankreich"),
    (_("Germany"), "deutschland"),
    (_("Greece"), "griechenland"),
    (_("Great Britain"), "grossbritannien"),
    (_("Hungary"), "ungarn"),
    (_("Ireland"), "irland"),
    (_("Italy"), "italien"),
    (_("Latvia"), "lettland"),
    (_("Luxembourg"), "luxemburg"),
    (_("Netherlands"), "niederlande"),
    (_("Norway"), "norwegen"),
    (_("Poland"), "polen"),
    (_("Portugal"), "portugal"),
    (_("Russia"), "russland"),
    (_("Slovakia"), "slowakei"),
    (_("Spain"), "spanien"),
    (_("Sweden"), "schweden"),
    (_("Switzerland"), "schweiz"),
]

REGION_MAPS_GERMANY = [
    (_("Baden-Wuerttemberg"), "badenwuerttemberg"),
    (_("Bavaria"), "bayern"),
    (_("Berlin"), "berlin"),
    (_("Brandenburg"), "brandenburg"),
    (_("Bremen"), "bremen"),
    (_("Hamburg"), "hamburg"),
    (_("Hesse"), "hessen"),
    (_("Mecklenburg-Vorpommern"), "mecklenburgvorpommern"),
    (_("Lower Saxony"), "niedersachsen"),
    (_("North Rhine-Westphalia"), "nordrheinwestfalen"),
    (_("Rhineland-Palatine"), "rheinlandpfalz"),
    (_("Saarland"), "saarland"),
    (_("Saxony"), "sachsen"),
    (_("Saxony-Anhalt"), "sachsenanhalt"),
    (_("Schleswig-Holstein"), "schleswigholstein"),
    (_("Thuringia"), "thueringen"),
]

REGION_MAPS_CONTINENTS = [
    (_("Europe"), "europa"),
    (_("North Africa"), "afrika_nord"),
    (_("South Africa"), "afrika_sued"),
    (_("North America"), "nordamerika"),
    (_("Middle America"), "mittelamerika"),
    (_("South America"), "suedamerika"),
    (_("Middle East"), "naherosten"),
    (_("East Asia"), "ostasien"),
    (_("Southeast Asia"), "suedostasien"),
    (_("Middle Asia"), "zentralasien"),
    (_("Australia"), "australienundozeanien"),
]


class ForecaSlideshow(Screen):
    """Slideshow for Wetterkontor weather maps"""
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ForecaSlideshow_FHD
    elif sz_w == 2560:
        skin = ForecaSlideshow_UHD
    else:
        skin = ForecaSlideshow_HD

    def __init__(self, session, region_code, region_name):
        print("[Foreca4] ForecaSlideshow class loaded")
        print(f"[Foreca4] Region code: {region_code}, Name: {region_name}")
        Screen.__init__(self, session)
        self.setTitle(_("Weather Maps Slideshow"))

        self["image"] = Pixmap()
        self["title"] = Label(region_name)
        self["info"] = Label(_("Loading..."))
        self["key_red"] = StaticText(_("Play/Pause"))
        self["key_green"] = StaticText(_("Next"))
        self["key_yellow"] = StaticText(_("Previous"))
        self["key_blue"] = StaticText(_("Exit"))
        self["playButton"] = Pixmap()
        self["pauseButton"] = Pixmap()
        self["playButton"].hide()
        self["pauseButton"].hide()
        self.region_code = region_code
        self.current_image = 0
        self.total_images = 6
        self.is_playing = True

        self.slide_timer = eTimer()
        self.slide_timer.timeout.get().append(self.next_image)
        self.slide_interval = 4000  # 5 seconds

        self["actions"] = ActionMap(
            [
                "OkCancelActions",
                "DirectionActions"
            ],
            {
                "cancel": self.exit,
                "ok": self.play_pause,
                "left": self.previous_image,
                "right": self.next_image,
                "up": self.increase_speed,
                "down": self.decrease_speed,
                "red": self.play_pause,         # Pulsante ROSSO per play/pause
                "green": self.next_image,       # Pulsante VERDE per prossima
                "yellow": self.previous_image,  # Pulsante GIALLO per precedente
                "blue": self.exit,              # Pulsante BLU per uscire
            }, -1
        )

        self.picload = ePicLoad()
        self.picload.PictureData.get().append(self.pic_data)
        self.onLayoutFinish.append(self.start_download)

    def start_download(self):
        """Start image download after screen is ready"""
        # Configure picload NOW that widgets exist
        sc = AVSwitch().getFramebufferScale()
        self.picload.setPara([
            self["image"].instance.size().width(),
            self["image"].instance.size().height(),
            sc[0],
            sc[1],
            0,              # cache
            0,              # resize (0=simple)
            "#00000000"     # background color
        ])

        # Start download in background
        self["info"].setText(_("Downloading images..."))
        Thread(target=self.download_all_images).start()

    def download_all_images(self):
        """Download all 6 images for the region"""

        for i in range(self.total_images):
            url = f"http://img.wetterkontor.de/karten/{self.region_code}{i}.jpg"
            cache_file = os.path.join(
                WETTERKONTOR_CACHE,
                f"{self.region_code}_{i}.jpg")
            if not os.path.exists(cache_file):
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        with open(cache_file, 'wb') as f:
                            f.write(response.content)
                        print(f"[Foreca4] Downloaded: {url}")
                    else:
                        print(f"[Foreca4] Failed to download: {url}")
                except Exception as e:
                    print(f"[Foreca4] Error downloading {url}: {e}")

        self.show_image(0)

    def show_image(self, index):
        """Show specific image"""
        if 0 <= index < self.total_images:
            self.current_image = index
            cache_file = os.path.join(
                WETTERKONTOR_CACHE,
                f"{self.region_code}_{index}.jpg")

            if os.path.exists(cache_file):
                self["info"].setText(f"{index + 1}/{self.total_images}")
                self.picload.startDecode(cache_file)
            else:
                self["info"].setText(_("Image not available"))

    def pic_data(self, picInfo=None):
        """Callback when image is loaded"""
        ptr = self.picload.getData()
        if ptr:
            self["image"].instance.setPixmap(ptr)
            self["image"].instance.show()

            # Start slideshow timer if not already running
            if self.is_playing and not self.slide_timer.isActive():
                self.slide_timer.start(self.slide_interval)

    def next_image(self):
        """Show next image"""
        next_idx = (self.current_image + 1) % self.total_images
        self.show_image(next_idx)

    def previous_image(self):
        """Show previous image"""
        prev_idx = (self.current_image - 1) % self.total_images
        self.show_image(prev_idx)

    def play_pause(self):
        """Pause or resume the slideshow"""
        if self.is_playing:
            self.slide_timer.stop()
            self["info"].setText(f"{self.current_image + 1}/{self.total_images} (Pausa)")
            self["playButton"].show()
            self["pauseButton"].hide()
            self.is_playing = False
        else:
            self.slide_timer.start(self.slide_interval)
            self["info"].setText(f"{self.current_image + 1}/{self.total_images}")
            self["playButton"].hide()
            self["pauseButton"].show()
            self.is_playing = True

    def increase_speed(self):
        """Increase slideshow speed"""
        if self.slide_interval > 1000:
            self.slide_interval -= 1000
            if self.is_playing:
                self.slide_timer.start(self.slide_interval)
            self["info"].setText(
                _("Faster: {}s").format(
                    self.slide_interval // 1000))

    def decrease_speed(self):
        """Decrease slideshow speed"""
        if self.slide_interval < 10000:
            self.slide_interval += 1000
            if self.is_playing:
                self.slide_timer.start(self.slide_interval)
            self["info"].setText(
                _("Slower: {}s").format(
                    self.slide_interval // 1000))

    def exit(self):
        """Exit slideshow"""
        self.slide_timer.stop()
        del self.picload
        self.close()


class ForecaMapsMenu(Screen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ForecaMapsMenu_FHD
    elif sz_w == 2560:
        skin = ForecaMapsMenu_UHD
    else:
        skin = ForecaMapsMenu_HD

    def __init__(self, session, map_type):
        self.session = session
        self.map_type = map_type  # 'europe', 'germany', 'continents'
        Screen.__init__(self, session)

        if map_type == 'europe':
            self.setTitle(_("European Weather Maps"))
            self.regions = REGION_MAPS_EUROPE
        elif map_type == 'germany':
            self.setTitle(_("German States Weather Maps"))
            self.regions = REGION_MAPS_GERMANY
        else:  # continents
            self.setTitle(_("Continents Weather Maps"))
            self.regions = REGION_MAPS_CONTINENTS

        from Components.MenuList import MenuList
        self["list"] = MenuList([])

        self.populate_list()
        self["actions"] = ActionMap(["OkCancelActions", "DirectionActions"],
                                    {
            "cancel": self.exit,
            "ok": self.select_region,
            "up": self.up,
            "down": self.down,
        }, -1)

    def populate_list(self):
        items = []
        for name, code in self.regions:
            items.append(name)
        self["list"].setList(items)

    def up(self):
        self["list"].up()

    def down(self):
        self["list"].down()

    def select_region(self):
        index = self["list"].getSelectedIndex()
        if 0 <= index < len(self.regions):
            region_name, region_code = self.regions[index]
            self.session.open(ForecaSlideshow, region_code, region_name)

    def exit(self):
        self.close()
