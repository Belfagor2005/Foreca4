#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_map_viewer.py - Base Foreca map viewer
# Copyright (c) @Lululla 20260122
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
from Components.Pixmap import Pixmap
from Components.Label import Label
from enigma import getDesktop
from math import log, tan, pi, radians, cos
from PIL import Image, ImageDraw
from datetime import datetime
import os

from . import _

THUMB_PATH = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/"
CACHE_BASE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"
grid_size = 3


def get_background_for_layer(layer_title, region="europe"):
    """Automatically selects the optimal PNG background"""

    layer_lower = layer_title.lower()
    bg_mapping = {
        # Maps by data type
        'temperature': 'temp_map.png',
        'temp': 'temp_map.png',
        'precipitation': 'rain_map.png',
        'rain': 'rain_map.png',
        'cloud': 'cloud_map.png',
        'pressure': 'pressure_map.png',
        'wind': 'wind_map.png',
        'snow': 'europa.png',  # snow overlay on base map
        'radar': 'rain_map.png',

        # Regional maps (if available)
        'europe': 'europa.png',
        'italy': 'italien.png',
        'germany': 'deutschland.png',
        'france': 'frankreich.png',
        'spain': 'spanien.png',
        'uk': 'grossbritannien.png',
        'austria': 'oesterreich.png',
        'switzerland': 'schweiz.png'
    }

    # 1. Try matching by data type
    for key in bg_mapping:
        if key in layer_lower:
            bg_file = bg_mapping[key]
            if os.path.exists(os.path.join(THUMB_PATH, bg_file)):
                return bg_file

    # 2. MAIN FALLBACK: for WIND or any other layer
    # First try the specific regional map, then fallback to generic Europe
    regional_map = f"{region.lower()}.png"  # e.g., "italien.png"
    if os.path.exists(os.path.join(THUMB_PATH, regional_map)):
        return regional_map
    else:
        # Final safe fallback
        return 'europa.png'


def create_composite_map(weather_tiles_path, layer_title, region):
    """Creates a composite map: background + Foreca weather data"""

    # 1. Select background
    bg_file = get_background_for_layer(layer_title, region)
    bg_path = f'/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/{bg_file}'

    # 2. Load background
    if os.path.exists(bg_path):
        background = Image.open(bg_path).convert('RGBA')
    else:
        # Fallback to Europe map
        background = Image.open('/thumb/europa.png').convert('RGBA')

    # 3. Load weather data (downloaded tiles)
    weather_data = Image.open(weather_tiles_path).convert('RGBA')

    # 4. Resize background to match weather data
    bg_resized = background.resize(weather_data.size, Image.Resampling.LANCZOS)

    # 5. Combine: background + weather data (semi-transparent)
    composite = Image.alpha_composite(bg_resized, weather_data)

    # 6. Add attribution
    draw = ImageDraw.Draw(composite)
    draw.text(
        (10, composite.height - 20),
        "Foreca Weather Data",
        fill=(255, 255, 255, 200)
    )

    return composite


class ForecaMapViewer(Screen):
    """Viewer for Foreca maps with background overlay"""

    def __init__(self, session, api, layer):
        self.api = api
        self.layer = layer
        self.layer_id = layer['id']
        self.layer_title = layer.get('title', 'Map')

        self.zoom = 4
        self.center_lat = 50.0  # Central Germany
        self.center_lon = 10.0

        self.timestamps = layer.get('times', {}).get('available', [])
        self.current_time_index = layer.get('times', {}).get('current', 0)

        self.size_w = getDesktop(0).size().width()
        self.size_h = getDesktop(0).size().height()

        # Skin
        if self.size_w == 1920:
            self.skin = """
            <screen position="center,center" size="1920,1080" flags="wfNoBorder">
                <widget name="map" position="0,0" size="1920,1080" zPosition="1" />
                <widget name="title" position="50,30" size="1820,50" font="Regular;40"
                        foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1"
                        halign="center" valign="center" />
                <widget name="time" position="50,1000" size="1820,50" font="Regular;30"
                        foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1"
                        halign="center" />
                <widget name="info" position="50,1050" size="1820,30" font="Regular;24"
                        foregroundColor="#c0c0c0" backgroundColor="#40000000" transparent="1"
                        halign="center" />
            </screen>"""
        else:
            self.skin = """
            <screen position="center,center" size="1280,720" flags="wfNoBorder">
                <widget name="map" position="0,0" size="1280,720" zPosition="1" />
                <widget name="title" position="30,20" size="1220,35" font="Regular;28"
                        foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1"
                        halign="center" valign="center" />
                <widget name="time" position="30,670" size="1220,30" font="Regular;20"
                        foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1"
                        halign="center" />
                <widget name="info" position="30,700" size="1220,20" font="Regular;18"
                        foregroundColor="#c0c0c0" backgroundColor="#40000000" transparent="1"
                        halign="center" />
            </screen>"""

        Screen.__init__(self, session)
        self.setTitle(f"Foreca: {self.layer_title}")

        self["map"] = Pixmap()
        self["title"] = Label(self.layer_title)
        self["time"] = Label("Loading...")
        self["info"] = Label("Use ← → to change time | OK to exit")

        self["actions"] = ActionMap(
            ["OkCancelActions", "DirectionActions"],
            {
                "cancel": self.exit,
                "ok": self.exit,
                "left": self.prev_time,
                "right": self.next_time,
            },
            -1
        )
        self.onLayoutFinish.append(self.load_current_tile)

    def latlon_to_tile(self, lat, lon, zoom):
        """Convert latitude/longitude to tile coordinates"""
        lat_rad = radians(lat)
        n = 2.0 ** zoom
        x = int((lon + 180.0) / 360.0 * n)
        y = int((1.0 - log(tan(lat_rad) + 1.0 / cos(lat_rad)) / pi) / 2.0 * n)
        return x, y

    def load_current_tile(self):
        """Load a grid of tiles and merge them"""
        if not self.timestamps:
            self["time"].setText(_("No data available"))
            return

        if self.current_time_index >= len(self.timestamps):
            self.current_time_index = 0

        timestamp = self.timestamps[self.current_time_index]

        # Format timestamp for display
        try:
            dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
            display_time = dt.strftime("%d/%m %H:%M UTC")
        except:
            display_time = timestamp

        self["time"].setText(f"{display_time} | Zoom: {self.zoom}")
        self["info"].setText("Downloading tiles...")

        # Download tile grid
        self.download_tile_grid_async(timestamp, self.tile_grid_downloaded)

    def download_tile_grid_async(self, timestamp, callback):
        """Download a grid of tiles in a separate thread"""

        def download_grid_thread():
            # Calculate center tile
            center_x, center_y = self.latlon_to_tile(self.center_lat, self.center_lon, self.zoom)

            # Grid size (e.g., 3x3 tiles = 768x768 pixels)
            # grid_size = 3
            offset = grid_size // 2  # 1

            tile_paths = []

            # Download all tiles in the grid
            for dx in range(-offset, offset + 1):
                for dy in range(-offset, offset + 1):
                    tile_x = center_x + dx
                    tile_y = center_y + dy

                    tile_path = self.api.get_tile(
                        self.layer_id,
                        timestamp,
                        self.zoom,
                        tile_x, tile_y
                    )

                    if tile_path:
                        tile_paths.append((dx + offset, dy + offset, tile_path))

            if len(tile_paths) == grid_size * grid_size:
                # All tiles downloaded, merge them
                merged_image = self.merge_tile_grid(tile_paths, grid_size)
                if merged_image and callback:
                    callback(merged_image)
            else:
                print(f"[ForecaMapViewer] Missing tiles: {len(tile_paths)}/{grid_size * grid_size}")
                if callback:
                    callback(None)

        from threading import Thread
        Thread(target=download_grid_thread).start()

    def merge_tile_grid(self, tile_paths, grid_size):
        """Unisce una griglia di tiles in un'unica immagine"""
        try:
            print(f"[DEBUG] Starting merge. Grid size: {grid_size}, Tiles received: {len(tile_paths)}")
            """
            for i, (col, row, tile_path) in enumerate(tile_paths):
                print(f"[DEBUG] Tile {i}: pos({col},{row}), path: {tile_path}")
                if not os.path.exists(tile_path):
                    print(f"[DEBUG] ERRORE: Tile {i} non esiste!")
                else:
                    size = os.path.getsize(tile_path)
                    print(f"[DEBUG] Tile {i} size: {size} bytes")
            """
            # Create new empty image
            tile_size = 256
            total_size = tile_size * grid_size
            print(f"[DEBUG] Creating image {total_size}x{total_size}")

            # Create transparent image (RGBA)
            merged_image = Image.new('RGBA', (total_size, total_size), (0, 0, 0, 0))

            # Place each tile in correct position
            tiles_placed = 0
            for col, row, tile_path in tile_paths:
                try:
                    tile_img = Image.open(tile_path).convert('RGBA')
                    x = col * tile_size
                    y = row * tile_size
                    print(f"[DEBUG] Placing tile at ({x},{y})")
                    merged_image.paste(tile_img, (x, y), tile_img)
                    tiles_placed += 1
                except Exception as e:
                    print(f"[DEBUG] Error placing tile {tile_path}: {e}")

            print(f"[DEBUG] Tiles placed: {tiles_placed}/{len(tile_paths)}")

            # Save merged image
            merged_path = os.path.join(CACHE_BASE, f"merged_{self.layer_id}_{self.zoom}.png")
            merged_image.save(merged_path, 'PNG')
            print(f"[DEBUG] Merged image saved: {merged_path}")

            return merged_path

        except Exception as e:
            print(f"[DEBUG] Error in merge_tile_grid: {e}")
            import traceback
            traceback.print_exc()
            return None

    def tile_grid_downloaded(self, merged_image_path):
        """Callback when the tile grid is downloaded and merged"""
        if merged_image_path:
            try:
                # 1. Open the merged image
                img = Image.open(merged_image_path).convert('RGBA')

                # 2. Create background image (if we have one)
                # TODO: Download background map tiles for context
                # For now, use a simple gradient background
                background = self.create_background(img.size)

                # 3. Composite: background + weather data
                if background:
                    # Blend images (weather over background)
                    composite = Image.alpha_composite(background, img)
                else:
                    composite = img

                # 4. Resize for screen
                screen_width = self.size_w
                screen_height = self.size_h

                # Calculate ratio to maintain aspect
                img_ratio = composite.width / composite.height
                screen_ratio = screen_width / screen_height

                if img_ratio > screen_ratio:
                    # Image wider than screen
                    new_width = screen_width
                    new_height = int(screen_width / img_ratio)
                else:
                    # Image taller than screen
                    new_height = screen_height
                    new_width = int(screen_height * img_ratio)

                # Resize with high quality
                resized_img = composite.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # 5. Create background at screen size
                display_img = Image.new('RGB', (screen_width, screen_height), (0, 0, 0))

                # 6. Center the resized image on the background
                x_offset = (screen_width - new_width) // 2
                y_offset = (screen_height - new_height) // 2
                display_img.paste(resized_img, (x_offset, y_offset))

                # 7. Save for display
                display_path = os.path.join(CACHE_BASE, f"display_{self.layer_id}_{self.zoom}.png")
                display_img.save(display_path, 'PNG')

                print(f"[ForecaMapViewer] Display image: {display_path} ({screen_width}x{screen_height})")

                # 8. Show on screen
                self["map"].instance.setPixmapFromFile(display_path)
                self["map"].instance.show()

                # Update info
                current_time = self.timestamps[self.current_time_index]
                dt = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%SZ")
                display_time = dt.strftime("%d/%m %H:%M UTC")
                self["time"].setText(f"{display_time} | Zoom: {self.zoom} | Grid: 3x3")
                self["info"].setText("Use ← → to change time | OK to exit")

            except Exception as e:
                print(f"[ForecaMapViewer] Error processing image: {e}")
                self["time"].setText("Error processing image")
                # Fallback: show the original merged image
                self["map"].instance.setPixmapFromFile(merged_image_path)
                self["map"].instance.show()
        else:
            self["time"].setText("Error downloading map grid")
            self["info"].setText("Check connection and API credentials")

    def create_background(self, size):
        """Create simple background - TO BE IMPROVED with actual map tiles"""
        # This is a placeholder. In the future, download OpenStreetMap tiles
        # or use static background maps
        try:
            # Simple gradient background
            from PIL import ImageDraw

            bg = Image.new('RGBA', size, (30, 30, 60, 255))  # Dark blue

            # Add grid lines for reference
            draw = ImageDraw.Draw(bg)
            width, height = size

            # Draw grid
            for i in range(0, width, 100):
                draw.line([(i, 0), (i, height)], fill=(50, 50, 80, 100), width=1)
            for i in range(0, height, 100):
                draw.line([(0, i), (width, i)], fill=(50, 50, 80, 100), width=1)

            return bg

        except Exception as e:
            print(f"[ForecaMapViewer] Error creating background: {e}")
            return None

    def prev_time(self):
        """Previous time step"""
        if self.timestamps and len(self.timestamps) > 1:
            self.current_time_index = (self.current_time_index - 1) % len(self.timestamps)
            self.load_current_tile()

    def next_time(self):
        """Next time step"""
        if self.timestamps and len(self.timestamps) > 1:
            self.current_time_index = (self.current_time_index + 1) % len(self.timestamps)
            self.load_current_tile()

    def exit(self):
        self.close()
