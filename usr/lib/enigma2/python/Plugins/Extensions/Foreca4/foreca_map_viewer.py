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
grid_size = 6


def get_background_for_layer(layer_title, region="europe"):
    """Automatically select the optimal PNG background from available thumbnails"""

    region_lower = region.lower()

    # FIRST check the region – this has PRIORITY
    if region_lower in ['eu', 'europe']:
        return 'europa.png'
    elif any(word in region_lower for word in ['italy', 'italia', 'italien']):
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

    # THEN check the layer type
    layer_lower = layer_title.lower()

    if any(word in layer_lower for word in ['temp', 'temperature', 'warm', 'cold']):
        return 'temp_map.png'
    elif any(word in layer_lower for word in ['rain', 'precip', 'shower', 'snow']):
        return 'rain_map.png'
    elif any(word in layer_lower for word in ['cloud', 'fog', 'mist']):
        return 'cloud_map.png'
    elif any(word in layer_lower for word in ['pressure', 'baro', 'hpa']):
        return 'pressure_map.png'
    elif any(word in layer_lower for word in ['wind', 'gust', 'breeze']):
        return 'europa.png'  # No wind_map.png exists

    # Default background
    return 'europa.png'


def create_composite_map(weather_tiles_path, layer_title, region):
    """Create a composite map with opaque background"""
    print("[DEBUG] create_composite_map START")
    from time import time

    # 1. Screen dimensions
    screen_width, screen_height = getDesktop(0).size().width(), getDesktop(0).size().height()

    # 2. Create OPAQUE background (dark blue)
    # Color: (R, G, B, A) where 255 = fully opaque
    opaque_background = Image.new('RGBA', (screen_width, screen_height), (30, 40, 60, 255))

    # 3. Load base map (transparent)
    bg_file = get_background_for_layer(layer_title, region)
    bg_path = os.path.join(THUMB_PATH, bg_file)

    if os.path.exists(bg_path):
        try:
            background = Image.open(bg_path).convert('RGBA')
            orig_w, orig_h = background.size

            # Resize
            background = background.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

            # Paste transparent map over opaque background
            opaque_background.paste(background, (0, 0), background)

            composite = opaque_background  # Now has opaque background + map
        except Exception as e:
            print(f"[DEBUG] Map error: {e}")
            composite = opaque_background  # Only opaque background
    else:
        composite = opaque_background  # Only opaque background

    # 4. Load and resize weather tile (as before)
    weather_data = Image.open(weather_tiles_path).convert('RGBA')
    tile_w, tile_h = weather_data.size

    # 5. Calculate scaling
    scale = min(screen_width * 0.8 / tile_w, screen_height * 0.8 / tile_h)
    new_tile_w = int(tile_w * scale)
    new_tile_h = int(tile_h * scale)

    weather_data = weather_data.resize((new_tile_w, new_tile_h), Image.Resampling.LANCZOS)

    # 6. Position tile
    x_offset = (screen_width - new_tile_w) // 2
    y_offset = (screen_height - new_tile_h) // 2

    # 7. Combine with transparency (background is already opaque)
    weather_alpha = weather_data.split()[3]
    weather_alpha = weather_alpha.point(lambda x: int(x * 0.5))
    weather_data.putalpha(weather_alpha)

    composite.paste(weather_data, (x_offset, y_offset), weather_data)

    # 8. Add text (no extra background)
    draw = ImageDraw.Draw(composite)
    draw.text((20, 20), f"Foreca: {layer_title}", fill=(255, 255, 255, 230))
    draw.text((20, screen_height - 60), f"Region: {region}", fill=(200, 200, 200, 200))
    draw.text((20, screen_height - 30), f"Weather data overlay", fill=(180, 180, 180, 180))

    # 9. Save
    output_path = os.path.join(CACHE_BASE, f"foreca_opaque_{int(time())}.png")
    composite.save(output_path, 'PNG')

    print(f"[DEBUG] File saved with opaque background")
    return output_path


"""
def create_composite_map(weather_tiles_path, layer_title, region):
    print("[DEBUG] create_composite_map START")

    from enigma import getDesktop
    from time import time
    import os

    # 1. Ottieni dimensioni REALI schermo
    screen_width, screen_height = getDesktop(0).size().width(), getDesktop(0).size().height()
    print(f"[DEBUG] Schermo: {screen_width}x{screen_height}")

    # 2. Crea uno sfondo opaco (nero con un po' di blu)
    background_color = (30, 40, 60, 255)  # R, G, B, A (255 = opaco)
    composite = Image.new('RGBA', (screen_width, screen_height), background_color)

    # 3. Carica mappa di sfondo (se esiste e non è trasparente?)
    bg_file = get_background_for_layer(layer_title, region)
    bg_path = os.path.join(THUMB_PATH, bg_file)

    print(f"[DEBUG] Usando mappa: {bg_file}")

    if os.path.exists(bg_path):
        try:
            background_map = Image.open(bg_path).convert('RGBA')
            orig_w, orig_h = background_map.size
            print(f"[DEBUG] Mappa originale: {orig_w}x{orig_h}")

            # RIDIMENSIONA mappa a schermo intero
            background_map = background_map.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
            print(f"[DEBUG] Mappa ridimensionata: {screen_width}x{screen_height}")

            # Se la mappa è trasparente, la disegniamo sopra lo sfondo opaco
            # Altrimenti, potremmo sostituire lo sfondo
            # In questo caso, usiamo la mappa come sovrapposizione (con opacità)
            # Ma prima assicuriamoci che la mappa abbia un canale alfa
            # Se la mappa è trasparente, possiamo fare un composite
            # Per sicurezza, creiamo un'immagine temporanea con sfondo opaco
            map_bg = Image.new('RGBA', (screen_width, screen_height), background_color)
            # Poi incolliamo la mappa sopra
            map_bg.paste(background_map, (0, 0), background_map)
            # Ora map_bg è opaco con la mappa sopra
            background_map = map_bg

        except Exception as e:
            print(f"[DEBUG] Errore caricamento mappa: {e}")
            background_map = None
    else:
        background_map = None

    # 4. Se abbiamo una mappa, la disegniamo sullo sfondo
    if background_map is not None:
        # Usiamo la mappa come sfondo (sostituisce lo sfondo uniforme)
        composite = background_map
    else:
        # Altrimenti, resta lo sfondo uniforme
        pass

    # 5. Carica tile meteo
    weather_data = Image.open(weather_tiles_path).convert('RGBA')
    tile_w, tile_h = weather_data.size
    print(f"[DEBUG] Tile meteo: {tile_w}x{tile_h}")

    # 6. Calcola fattore di scala (basato su mappa ORIGINALE o schermo)
    if bg_file and os.path.exists(bg_path) and 'orig_w' in locals():
        scale_x = screen_width / orig_w
        scale_y = screen_height / orig_h
        scale = (scale_x + scale_y) / 2
    else:
        # Se mappa non caricata, scala per adattare tile allo schermo
        scale = min(screen_width * 0.8 / tile_w, screen_height * 0.8 / tile_h)

    print(f"[DEBUG] Fattore scala: {scale:.2f}")

    # 7. Ridimensiona le tile
    new_tile_w = int(tile_w * scale)
    new_tile_h = int(tile_h * scale)
    print(f"[DEBUG] Tile ridimensionate: {new_tile_w}x{new_tile_h}")

    weather_data = weather_data.resize((new_tile_w, new_tile_h), Image.Resampling.LANCZOS)

    # 8. Posiziona tile al CENTRO schermo
    x_offset = (screen_width - new_tile_w) // 2
    y_offset = (screen_height - new_tile_h) // 2
    print(f"[DEBUG] Posizione tile: ({x_offset}, {y_offset})")

    # 9. Applica trasparenza alle tile meteo (50% opacità)
    weather_alpha = weather_data.split()[3]
    weather_alpha = weather_alpha.point(lambda x: int(x * 0.5))  # 50% trasparenza
    weather_data.putalpha(weather_alpha)

    # 10. Combina mappa + tile
    composite.paste(weather_data, (x_offset, y_offset), weather_data)

    # 11. Aggiungi testo informativo (con sfondo semitrasparente)
    draw = ImageDraw.Draw(composite)

    # Titolo in alto a sinistra con rettangolo di sfondo
    title_text = f"Foreca: {layer_title}"
    # Stima dimensione testo (approssimativa)
    title_font_size = 40
    title_bg = Image.new('RGBA', (screen_width, title_font_size + 20), (0, 0, 0, 0))
    title_draw = ImageDraw.Draw(title_bg)
    # Disegna rettangolo di sfondo
    title_draw.rectangle([0, 0, screen_width, title_font_size + 20], fill=(0, 0, 0, 180))
    # Posiziona sull'immagine principale
    composite.paste(title_bg, (0, 0), title_bg)
    draw.text((20, 10), title_text, fill=(255, 255, 255, 230))

    # Info in basso a sinistra con rettangolo di sfondo
    info_text1 = f"Regione: {region}"
    info_text2 = f"Tile: {tile_w}x{tile_h} → {new_tile_w}x{new_tile_h}"
    info_font_size = 24
    info_bg_height = info_font_size * 2 + 30
    info_bg = Image.new('RGBA', (screen_width, info_bg_height), (0, 0, 0, 0))
    info_draw = ImageDraw.Draw(info_bg)
    info_draw.rectangle([0, 0, screen_width, info_bg_height], fill=(0, 0, 0, 180))
    composite.paste(info_bg, (0, screen_height - info_bg_height), info_bg)
    draw.text((20, screen_height - info_bg_height + 10), info_text1, fill=(200, 200, 200, 200))
    draw.text((20, screen_height - info_bg_height + 10 + info_font_size + 5), info_text2,
              fill=(180, 180, 180, 180))

    # 12. Salva file (assicurati che sia in modalità RGB, non RGBA, per evitare trasparenza)
    output_path = os.path.join(CACHE_BASE, f"foreca_display_{int(time())}.png")
    # Converti in RGB per rimuovere il canale alfa
    composite_rgb = composite.convert('RGB')
    composite_rgb.save(output_path, 'PNG')

    print(f"[DEBUG] File salvato (RGB opaco): {output_path}")
    print(f"[DEBUG] create_composite_map END")

    return output_path
"""


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

        # Optimized configurations for each region
        region_configs = {
            'eu': {'zoom': 4, 'lat': 50.0, 'lon': 10.0, 'grid': 5},
            'europe': {'zoom': 4, 'lat': 50.0, 'lon': 10.0, 'grid': 5},
            'us': {'zoom': 3, 'lat': 40.0, 'lon': -100.0, 'grid': 5},
            'usa': {'zoom': 3, 'lat': 40.0, 'lon': -100.0, 'grid': 5},
            'asia': {'zoom': 2, 'lat': 30.0, 'lon': 100.0, 'grid': 4},
            'africa': {'zoom': 2, 'lat': 0.0, 'lon': 20.0, 'grid': 4},
            'samerica': {'zoom': 2, 'lat': -20.0, 'lon': -60.0, 'grid': 4},
            'oceania': {'zoom': 3, 'lat': -25.0, 'lon': 135.0, 'grid': 5},
        }

        # Use region-specific configuration or default
        config = region_configs.get(
            self.region.lower(),
            {'zoom': 3, 'lat': 50.0, 'lon': 10.0, 'grid': 4}
        )

        self.zoom = config['zoom']
        self.center_lat = config['lat']
        self.center_lon = config['lon']
        self.grid_size = config['grid']

        print(f"[ForecaMapViewer] Region: {self.region}")
        print(f"[ForecaMapViewer] Zoom: {self.zoom}, Center: ({self.center_lat}, {self.center_lon})")
        print(f"[ForecaMapViewer] Grid: {self.grid_size}x{self.grid_size}")

        self.timestamps = layer.get('times', {}).get('available', [])
        self.current_time_index = layer.get('times', {}).get('current', 0)

        self.size_w = getDesktop(0).size().width()
        self.size_h = getDesktop(0).size().height()

        print(
            f"[ForecaMapViewer] Initialized: region={region}, zoom={self.zoom}, "
            f"center=({self.center_lat}, {self.center_lon}), grid={self.grid_size}x{self.grid_size}"
        )

        Screen.__init__(self, session)
        self.setTitle(f"Foreca: {self.layer_title}")
        # ... rest of the code ...

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
        import math
        # Formule standard per Web Mercator (usato da Foreca)
        lat_rad = math.radians(lat)
        n = 2.0 ** zoom
        x_tile = int((lon + 180.0) / 360.0 * n)
        # Formula corretta per la coordinata Y
        y_tile = int((1.0 - math.log(math.tan(lat_rad) + 1.0 / math.cos(lat_rad)) / math.pi) / 2.0 * n)

        return x_tile, y_tile

    def get_grid_size_for_region(region):
        """Returns the optimal grid size for the region"""
        region_lower = region.lower()
        if region_lower in ['eu', 'europe', 'us', 'usa']:
            return 4  # 4x4 for continents
        else:
            return 3  # 3x3 for smaller regions

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

        # DEBUG: show current coordinates
        print(f"[ForecaMapViewer] Region: {self.region}")
        print(f"[ForecaMapViewer] Center: lat={self.center_lat}, lon={self.center_lon}, zoom={self.zoom}")

        # Determine grid size based on region
        if self.region.lower() in ['eu', 'europe', 'us', 'usa']:
            grid_size = 4
        else:
            grid_size = 3

        self["time"].setText(f"{display_time} | Zoom: {self.zoom} | Grid: {grid_size}x{grid_size}")
        self["info"].setText("Downloading tiles...")

        # Download tile grid
        self.download_tile_grid_async(timestamp, self.tile_grid_downloaded)

    def download_tile_grid_async(self, timestamp, callback):
        """Download a grid of tiles in a separate thread"""

        # Use the class grid_size
        grid_size = self.grid_size

        print(f"[DEBUG] Download grid: {grid_size}x{grid_size} for region: {self.region}")
        print(f"[DEBUG] Center: lat={self.center_lat}, lon={self.center_lon}, zoom={self.zoom}")

        api = self.api
        layer_id = self.layer_id
        zoom = self.zoom
        center_lat = self.center_lat
        center_lon = self.center_lon
        unit_system = self.unit_system

        def download_grid_thread():
            try:
                # Calculate center tile
                center_x, center_y = self.latlon_to_tile(center_lat, center_lon, zoom)
                print(f"[DEBUG] Center tile: ({center_x}, {center_y})")

                # For even grids (4x4, 6x6), a different offset is required
                if grid_size % 2 == 0:  # Even grid
                    offset = grid_size // 2
                    # For even grids, the center tile is not perfectly centered
                    # We need to shift slightly
                    start_x = center_x - offset + 1
                    start_y = center_y - offset + 1
                    end_x = center_x + offset
                    end_y = center_y + offset
                else:  # Odd grid (3x3, 5x5)
                    offset = grid_size // 2
                    start_x = center_x - offset
                    start_y = center_y - offset
                    end_x = center_x + offset
                    end_y = center_y + offset

                print(f"[DEBUG] Grid range: x[{start_x} to {end_x}], y[{start_y} to {end_y}]")

                tile_paths = []
                total_tiles = (end_x - start_x + 1) * (end_y - start_y + 1)

                # Download all tiles
                for tile_x in range(start_x, end_x + 1):
                    for tile_y in range(start_y, end_y + 1):

                        tile_path = api.get_tile(
                            layer_id,
                            timestamp,
                            zoom,
                            tile_x, tile_y,
                            unit_system
                        )

                        if tile_path:
                            # Calculate position in the grid (0-indexed)
                            grid_x = tile_x - start_x
                            grid_y = tile_y - start_y
                            tile_paths.append((grid_x, grid_y, tile_path))
                            print(f"[DEBUG] Downloaded tile ({tile_x}, {tile_y}) -> ({grid_x}, {grid_y})")
                        else:
                            print(f"[DEBUG] FAILED tile ({tile_x}, {tile_y})")

                print(f"[DEBUG] Downloaded {len(tile_paths)}/{total_tiles} tiles")

                if len(tile_paths) >= max(1, total_tiles * 0.5):  # At least 50%
                    merged_image = self.merge_tile_grid(tile_paths, grid_size)
                    if merged_image and callback:
                        callback(merged_image)
                else:
                    print(f"[ForecaMapViewer] Not enough tiles: {len(tile_paths)}/{total_tiles}")
                    if callback:
                        callback(None)

            except Exception as e:
                print(f"[ForecaMapViewer] Error in thread: {e}")
                import traceback
                traceback.print_exc()
                if callback:
                    callback(None)

        from threading import Thread
        thread = Thread(target=download_grid_thread, daemon=True)
        thread.start()

    def merge_tile_grid(self, tile_paths, grid_size):
        """Combines a grid of tiles into a single image"""
        try:
            print(
                f"[DEBUG] Starting merge. Grid size: {grid_size}, Tiles received: {len(tile_paths)}")

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
                    merged_image.paste(tile_img, (x, y), tile_img)
                    tiles_placed += 1
                except Exception as e:
                    print(f"[DEBUG] Error placing tile {tile_path}: {e}")

            print(f"[DEBUG] Tiles placed: {tiles_placed}/{len(tile_paths)}")

            # Save merged image
            merged_path = os.path.join(
                CACHE_BASE, f"merged_{self.layer_id}_{self.zoom}_{grid_size}x{grid_size}.png")
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
