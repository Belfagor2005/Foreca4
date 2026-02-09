#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_map_viewer.py - Base Foreca map viewer
# Copyright (c) @Lululla 20260122
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Pixmap import Pixmap
from Components.Label import Label
from enigma import getDesktop
from math import log, tan, pi, radians, cos
from PIL import Image, ImageDraw
from datetime import datetime
import os

from .skin import (
    ForecaMapViewer_UHD,
    ForecaMapViewer_FHD,
    ForecaMapViewer_HD
)
from . import _

THUMB_PATH = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/"
CACHE_BASE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"
grid_size = 3


def get_background_for_layer(layer_title, region="europe"):
    """Automatically selects the optimal PNG background from available thumbnails"""

    layer_lower = layer_title.lower()

    # Smart mapping based on layer keywords
    if any(
        word in layer_lower for word in [
            'temp',
            'temperature',
            'warm',
            'cold']):
        return 'temp_map.png'
    elif any(word in layer_lower for word in ['rain', 'precip', 'shower', 'snow']):
        return 'rain_map.png'
    elif any(word in layer_lower for word in ['cloud', 'fog', 'mist']):
        return 'cloud_map.png'
    elif any(word in layer_lower for word in ['pressure', 'baro', 'hpa']):
        return 'pressure_map.png'
    elif any(word in layer_lower for word in ['wind', 'gust', 'breeze']):
        # No wind_map.png available, use europa
        return 'europa.png'

    # Regional backgrounds
    region_lower = region.lower()
    if any(word in region_lower for word in ['italy', 'italia', 'italien']):
        return 'italien.png'
    elif any(word in region_lower for word in ['germany', 'deutsch', 'germania']):
        return 'deutschland.png'
    elif any(word in region_lower for word in ['france', 'francia', 'frankreich']):
        return 'frankreich.png'
    elif any(word in region_lower for word in ['spain', 'espana', 'spanien']):
        return 'spanien.png'
    elif any(word in region_lower for word in ['uk', 'britain', 'grossbritannien']):
        return 'grossbritannien.png'
    elif any(word in region_lower for word in ['austria', 'oesterreich']):
        return 'oesterreich.png'
    elif any(word in region_lower for word in ['switzerland', 'schweiz', 'svizzera']):
        return 'schweiz.png'

    # Default background
    return 'europa.png'


def create_composite_map(weather_tiles_path, layer_title, region):
    """Creates a composite map: background + Foreca weather data"""
    print("[DEBUG] create_composite_map called")
    print(f"[DEBUG] Weather tiles path: {weather_tiles_path}")
    print(f"[DEBUG] Layer title: {layer_title}")
    print(f"[DEBUG] Region: {region}")

    # 1. Select background
    bg_file = get_background_for_layer(layer_title, region)
    print(f"[DEBUG] Selected background file: {bg_file}")

    bg_path = os.path.join(THUMB_PATH, bg_file)
    print(f"[DEBUG] Background path: {bg_path}")

    # 2. Load background
    background = None
    if os.path.exists(bg_path):
        print(f"[DEBUG] Loading background from: {bg_path}")
        try:
            background = Image.open(bg_path).convert('RGBA')
            print(f"[DEBUG] Background loaded successfully: {background.size}")
        except Exception as e:
            print(f"[DEBUG] Error loading background: {e}")
            background = None

    if background is None:
        # Try fallback to europa.png
        fallback_path = os.path.join(THUMB_PATH, 'europa.png')
        if os.path.exists(fallback_path):
            print(f"[DEBUG] Loading fallback: {fallback_path}")
            background = Image.open(fallback_path).convert('RGBA')
        else:
            # Create simple colored background
            print("[DEBUG] Creating colored background")
            background = Image.new('RGBA', (768, 768), (40, 60, 80, 255))

    # 3. Load weather data
    print(f"[DEBUG] Loading weather tiles from: {weather_tiles_path}")
    weather_data = Image.open(weather_tiles_path).convert('RGBA')
    print(f"[DEBUG] Weather data size: {weather_data.size}")

    # 4. Resize background to match weather data
    print(
        f"[DEBUG] Resizing background: {background.size} -> {weather_data.size}")
    bg_resized = background.resize(weather_data.size, Image.Resampling.LANCZOS)

    # 5. Combine: background + weather data
    # First, make weather data slightly transparent to see background
    # Adjust alpha channel of weather data (0=transparent, 255=opaque)
    weather_alpha = weather_data.split()[3]
    # Reduce alpha by 30% to make more transparent
    weather_alpha = weather_alpha.point(lambda x: int(x * 0.7))
    weather_data.putalpha(weather_alpha)

    composite = Image.alpha_composite(bg_resized, weather_data)

    # 6. Add attribution
    draw = ImageDraw.Draw(composite)
    draw.text(
        (10, composite.height - 20),
        f"Foreca: {layer_title}",
        fill=(255, 255, 255, 200)
    )

    print(f"[DEBUG] Composite created: {composite.size}")
    from time import time
    composite_filename = f"composite_{int(time())}.png"
    composite_path = os.path.join(CACHE_BASE, composite_filename)
    try:
        composite.save(composite_path, 'PNG')
        return composite_path
    except BaseException:
        return weather_tiles_path


def debug_background_search():
    """Debug function to test background selection"""
    THUMB_PATH = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/"

    test_cases = [
        ("Temperature", "europe"),
        ("Cloud Cover", "italy"),
        ("Precipitation", "germany"),
        ("Wind Speed", "france"),
        ("Pressure", "spain"),
    ]

    for layer, region in test_cases:
        print(f"\n=== Testing: {layer} / {region} ===")
        bg_file = get_background_for_layer(layer, region)
        print(f"Result: {bg_file}")

        if bg_file:
            path = os.path.join(THUMB_PATH, bg_file)
            exists = os.path.exists(path)
            print(f"Exists: {exists} ({path})")


def debug_map_creation():
    """Test map creation to see what's happening"""
    test_tile = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/test_tile.png"

    # Create a test tile if it doesn't exist
    if not os.path.exists(test_tile):
        from PIL import Image, ImageDraw
        # Red semi-transparent
        img = Image.new('RGBA', (768, 768), (255, 0, 0, 100))
        draw = ImageDraw.Draw(img)
        draw.text((100, 100), "TEST WEATHER DATA", fill=(255, 255, 255, 255))
        img.save(test_tile)

    # Test different layer types
    test_cases = [
        ("Temperature", "europe"),
        ("Cloud Cover", "italy"),
        ("Wind Speed", "germany"),
        ("Precipitation", "france"),
    ]

    for layer, region in test_cases:
        print(f"\n=== Testing: {layer} / {region} ===")
        result = create_composite_map(test_tile, layer, region)
        print(f"Result type: {type(result)}")
        print(f"Result: {result}")
        if isinstance(result, str):
            print(f"File exists: {os.path.exists(result)}")


class ForecaMapViewer(Screen):
    """Viewer for Foreca maps with background overlay"""
    sz_w = getDesktop(0).size().width()
    if sz_w == 1920:
        skin = ForecaMapViewer_FHD
    elif sz_w == 2560:
        skin = ForecaMapViewer_UHD
    else:
        skin = ForecaMapViewer_HD

    def __init__(self, session, api, layer, unit_system='metric', region='eu'):
        self.api = api
        self.layer = layer
        self.layer_id = layer['id']
        self.layer_title = layer.get('title', 'Map')
        self.unit_system = unit_system
        self.region = region

        self.zoom = 4
        self.center_lat = 50.0  # Central Germany
        self.center_lon = 10.0

        self.timestamps = layer.get('times', {}).get('available', [])
        self.current_time_index = layer.get('times', {}).get('current', 0)

        self.size_w = getDesktop(0).size().width()
        self.size_h = getDesktop(0).size().height()
        Screen.__init__(self, session)
        self.setTitle(f"Foreca: {self.layer_title}")
        self["map"] = Pixmap()
        self["title"] = Label(self.layer_title)
        self["layerinfo"] = Label("")
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

        debug_background_search()

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
        except BaseException:
            display_time = timestamp

        self["time"].setText(f"{display_time} | Zoom: {self.zoom}")
        self["info"].setText("Downloading tiles...")

        # Download tile grid
        self.download_tile_grid_async(timestamp, self.tile_grid_downloaded)

    def download_tile_grid_async(self, timestamp, callback):
        """Download a grid of tiles in a separate thread"""

        def download_grid_thread():
            # Calculate center tile
            center_x, center_y = self.latlon_to_tile(
                self.center_lat, self.center_lon, self.zoom)

            # Grid size (e.g., 3x3 tiles = 768x768 pixels)
            # grid_size = 3
            offset = grid_size // 2  # 1

            tile_paths = []

            # Download all tiles in the grid
            for dx in range(-offset, offset + 1):
                for dy in range(-offset, offset + 1):
                    tile_x = center_x + dx
                    tile_y = center_y + dy

                    # passa unit_system
                    tile_path = self.api.get_tile(
                        self.layer_id,
                        timestamp,
                        self.zoom,
                        tile_x, tile_y,
                        self.unit_system
                    )

                    if tile_path:
                        tile_paths.append(
                            (dx + offset, dy + offset, tile_path))

            if len(tile_paths) == grid_size * grid_size:
                # All tiles downloaded, merge them
                merged_image = self.merge_tile_grid(tile_paths, grid_size)
                if merged_image and callback:
                    callback(merged_image)
            else:
                print(
                    f"[ForecaMapViewer] Missing tiles: {len(tile_paths)}/{grid_size * grid_size}")
                if callback:
                    callback(None)

        from threading import Thread
        Thread(target=download_grid_thread).start()

    def merge_tile_grid(self, tile_paths, grid_size):
        """Combines a grid of tiles into a single image"""
        try:
            print(
                f"[DEBUG] Starting merge. Grid size: {grid_size}, Tiles received: {len(tile_paths)}")
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
            merged_image = Image.new(
                'RGBA', (total_size, total_size), (0, 0, 0, 0))

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
            merged_path = os.path.join(
                CACHE_BASE, f"merged_{self.layer_id}_{self.zoom}.png")
            merged_image.save(merged_path, 'PNG')
            print(f"[DEBUG] Merged image saved: {merged_path}")

            return merged_path

        except Exception as e:
            print(f"[DEBUG] Error in merge_tile_grid: {e}")
            import traceback
            traceback.print_exc()
            return None

    def tile_grid_downloaded(self, merged_image_path):
        if merged_image_path:
            try:
                composite_path = create_composite_map(
                    merged_image_path,
                    self.layer_title,
                    self.region
                )

                if isinstance(composite_path,
                              str) and os.path.exists(composite_path):
                    self["map"].instance.setPixmapFromFile(composite_path)
                    self["map"].instance.show()
                else:
                    # Fallback
                    self["map"].instance.setPixmapFromFile(merged_image_path)
                    self["map"].instance.show()

                self.update_layer_info()

            except Exception as e:
                print(f"[ForecaMapViewer] Error: {e}")
                import traceback
                traceback.print_exc()
                self["time"].setText("Error displaying map")
                self["layerinfo"].setText("")

            try:
                # Update info
                current_time = self.timestamps[self.current_time_index]
                try:
                    dt = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%SZ")
                    display_time = dt.strftime("%d/%m %H:%M UTC")
                except BaseException:
                    display_time = current_time

                self["time"].setText(
                    "{0} | Zoom: {1} | Grid: 3x3".format(
                        display_time, self.zoom))
                self["info"].setText("Use ← → to change time | OK to exit")

            except Exception as e:
                print("[ForecaMapViewer] Error: {0}".format(e))
                import traceback
                traceback.print_exc()
                self["time"].setText("Error displaying map")
        else:
            self["time"].setText("Error downloading map grid")
            self["info"].setText("Check connection and API credentials")
            self["layerinfo"].setText("")

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
                draw.line([(i, 0), (i, height)], fill=(
                    50, 50, 80, 100), width=1)
            for i in range(0, height, 100):
                draw.line([(0, i), (width, i)], fill=(
                    50, 50, 80, 100), width=1)

            return bg

        except Exception as e:
            print(f"[ForecaMapViewer] Error creating background: {e}")
            return None

    def update_layer_info(self):
        """Update the informational label with layer and region details"""
        try:
            # Get information from the layer
            layer_name = self.layer_title

            # Determine the data type (Temperature, Wind, etc.)
            data_type = self.get_data_type_from_layer(layer_name)

            # Determine the region (default, could be configurable in the
            # future)
            region = "Europe"

            # Build the informational text
            info_text = "{0} - {1}".format(data_type, region)

            # Add unit information if available
            if hasattr(self, 'unit_system') and self.unit_system:
                if self.unit_system == 'imperial':
                    unit_info = " (Imperial Units)"
                else:
                    unit_info = " (Metric Units)"
                info_text += unit_info

            # Update the widget
            self["layerinfo"].setText(info_text)

            print("[ForecaMapViewer] Layer info: {0}".format(info_text))

        except Exception as e:
            print("[ForecaMapViewer] Error updating layer info: {0}".format(e))
            self["layerinfo"].setText("{0}".format(self.layer_title))

    def get_data_type_from_layer(self, layer_name):
        """Extract data type from layer name"""
        layer_lower = layer_name.lower()

        if 'temp' in layer_lower:
            return "Temperature"
        elif 'wind' in layer_lower:
            return "Wind"
        elif 'cloud' in layer_lower:
            return "Cloud Cover"
        elif 'precip' in layer_lower or 'rain' in layer_lower:
            return "Precipitation"
        elif 'pressure' in layer_lower:
            return "Pressure"
        elif 'snow' in layer_lower:
            return "Snow"
        elif 'radar' in layer_lower:
            return "Radar"
        else:
            return layer_name

    def prev_time(self):
        """Previous time step"""
        if self.timestamps and len(self.timestamps) > 1:
            self.current_time_index = (
                self.current_time_index - 1) % len(self.timestamps)
            self.load_current_tile()
            self.update_layer_info()

    def next_time(self):
        """Next time step"""
        if self.timestamps and len(self.timestamps) > 1:
            self.current_time_index = (
                self.current_time_index + 1) % len(self.timestamps)
            self.load_current_tile()
            self.update_layer_info()

    def exit(self):
        self.close()
