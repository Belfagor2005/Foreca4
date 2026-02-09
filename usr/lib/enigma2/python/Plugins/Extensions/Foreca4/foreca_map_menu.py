#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_map_menu.py - Foreca map selection menu
# Copyright (c) @Lululla 20260122
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Label import Label
from enigma import getDesktop

from .skin import (
    ForecaMapMenu_UHD,
    ForecaMapMenu_FHD,
    ForecaMapMenu_HD
)
from . import _


class ForecaMapMenu(Screen):
    """Menu to select Foreca map layers"""
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ForecaMapMenu_FHD
    elif sz_w == 2560:
        skin = ForecaMapMenu_UHD
    else:
        skin = ForecaMapMenu_HD

    def __init__(self, session, api, unit_system='metric'):
        self.session = session
        self.api = api
        self.unit_system = unit_system
        self.layers = []
        Screen.__init__(self, session)
        self["list"] = MenuList([])
        self["info"] = Label(_("Loading available maps..."))
        self["actions"] = ActionMap(
            ["OkCancelActions", "DirectionActions"],
            {
                "cancel": self.exit,
                "ok": self.select_layer,
                "up": self.up,
                "down": self.down,
            },
            -1
        )
        self.onLayoutFinish.append(self.load_layers)

    def load_layers(self):
        """Load available layers"""
        self.layers = self.api.get_capabilities()

        if not self.layers:
            self["info"].setText(_("Error loading maps. Check connection."))
            return

        items = []
        for layer in self.layers:
            title = layer.get('title', f"Layer {layer['id']}")
            items.append((title, layer))

        self["list"].setList(items)
        self["info"].setText(_("Select a map with OK"))

    def up(self):
        self["list"].up()

    def down(self):
        self["list"].down()

    def select_layer(self):
        """Select layer and open viewer"""
        selection = self["list"].getCurrent()
        if selection:
            from .foreca_map_viewer import ForecaMapViewer
            self.session.open(ForecaMapViewer, self.api, selection[1], self.unit_system)

    def exit(self):
        self.close()
