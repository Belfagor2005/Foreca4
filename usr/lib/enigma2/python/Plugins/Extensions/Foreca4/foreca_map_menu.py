#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_map_menu.py - Foreca map selection menu
# @Lululla 20260122
# @Lululla 20260122
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
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList
from Components.Label import Label

from . import _


class ForecaMapMenu(Screen):
    """Menu to select Foreca map layers"""
    
    def __init__(self, session, api):
        self.session = session
        self.api = api
        self.layers = []
        self.skin = """
        <screen position="center,center" size="800,700" title="Foreca Live Maps">
            <widget name="list" position="46,7" size="700,650" itemHeight="35" font="Regular;32" scrollbarMode="showNever" />
            <widget name="info" position="50,665" size="700,30" font="Regular;24" halign="center" />
        </screen>"""
        
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
            self.session.open(ForecaMapViewer, self.api, selection[1])
    
    def exit(self):
        self.close()
