#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_map_viewer.py - Final: 16:9 output (1280x720), dynamic grid, corrupted tiles handled
# Copyright (c) @Lululla 2026
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Pixmap import Pixmap
from Components.Label import Label
from enigma import getDesktop
from math import log, tan, pi, radians, cos
from PIL import Image  # , ImageDraw
from datetime import datetime
import os

from . import _, load_skin_for_class

# -------------------------------
TILE_SIZE = 256
THUMB_PATH = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/thumb/"
CACHE_BASE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"

# Final rendering size (FORCED 16:9)
FINAL_WIDTH = 1280
FINAL_HEIGHT = 720

# Region centers (lat, lon)
REGION_CENTERS = {
    'eu': (50.0, 10.0),
    'it': (42.5, 12.5),
    'de': (51.0, 10.0),
    'fr': (46.0, 2.0),
    'es': (40.0, -4.0),
    'uk': (54.0, -2.0),
    'pl': (52.0, 19.0),
    'nl': (52.0, 5.0),
    'be': (50.5, 4.5),
    'at': (47.5, 14.0),
    'ch': (46.8, 8.2),
}


# ------------------------------------------------------------
def get_background_for_layer(layer_title, region="europe"):
    """Select geographic background based on layer and region"""
    # layer_lower = layer_title.lower()
    # if any(
    # word in layer_lower for word in [
    # 'temp',
    # 'temperature',
    # 'warm',
    # 'cold']):
    # return 'temp_map.png'
    # elif any(word in layer_lower for word in ['rain', 'precip', 'shower', 'snow']):
    # return 'rain_map.png'
    # elif any(word in layer_lower for word in ['symb']):
    # return 'symb.png'
    # elif any(word in layer_lower for word in ['cloud', 'fog', 'mist']):
    # return 'cloud_map.png'
    # elif any(word in layer_lower for word in ['pressure', 'baro', 'hpa']):
    # return 'pressure_map.png'
    # elif any(word in layer_lower for word in ['wind', 'gust', 'breeze']):
    # return 'europa.png'

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
    return 'europa.png'


# ------------------------------------------------------------
def create_composite_map(
    weather_tiles_path,
    layer_title,
    region,
    canvas_size=(
        FINAL_WIDTH,
        FINAL_HEIGHT)):
    """
    Create composite map with tiles.
    canvas_size = tuple(width, height) for final output
    """
    # Colore neutro per sfondo al posto del nero
    BG_COLOR = (176, 196, 222)  # light steel blue
    canvas = Image.new("RGBA", canvas_size, BG_COLOR + (255,))

    # Background geografico
    bg_file = get_background_for_layer(layer_title, region)
    bg_path = os.path.join(THUMB_PATH, bg_file)
    if os.path.exists(bg_path):
        try:
            bg = Image.open(bg_path).convert("RGB")
            bg = bg.resize(canvas_size, Image.Resampling.LANCZOS)
            canvas.paste(bg, (0, 0))
        except Exception as e:
            print("[Composite] Background error:", e)

    # Scurisci per layer vento (se presente)
    if 'wind' in layer_title.lower():
        canvas = canvas.point(lambda p: int(p * 0.6))

    # Weather tiles
    if os.path.exists(weather_tiles_path):
        try:
            weather = Image.open(weather_tiles_path).convert("RGB")
            weather = weather.resize(canvas_size, Image.Resampling.LANCZOS)
            canvas.paste(weather, (0, 0))
        except Exception as e:
            print("[Composite] Weather tiles error:", e)
    else:
        print("[Composite] Weather tile not found:", weather_tiles_path)

    # Salva come PNG RGB opaco
    composite_path = os.path.join(
        CACHE_BASE,
        f"composite_{os.path.basename(weather_tiles_path)}"
    )
    canvas.convert("RGB").save(composite_path, 'PNG')
    return composite_path


# ------------------------------------------------------------
class ForecaMapViewer(Screen):
    """Foreca Map Viewer – 16:9, dynamic grid, corrupt tile handling"""

    def __init__(self, session, api, layer, unit_system='metric', region='eu'):
        self.skin = load_skin_for_class(ForecaMapViewer)
        Screen.__init__(self, session)
        self.api = api
        self.layer = layer
        self.layer_id = layer['id']
        self.layer_title = layer.get('title', 'Map')
        self.unit_system = unit_system
        self.region = region.lower()

        # Center by region
        if self.region in REGION_CENTERS:
            self.center_lat, self.center_lon = REGION_CENTERS[self.region]
        else:
            self.center_lat, self.center_lon = 50.0, 10.0

        desktop = getDesktop(0)
        self.screen_w = desktop.size().width()
        self.screen_h = desktop.size().height()
        # Dynamic Grid: HD -> 5x3 (1280x768), FHD/UHD -> 5x5 (1280x1280)
        if self.screen_h <= 720:
            self.grid_cols = 5
            self.grid_rows = 3
        else:
            self.grid_cols = 5
            self.grid_rows = 5

        self.tile_size = TILE_SIZE
        self.map_w = self.grid_cols * self.tile_size
        self.map_h = self.grid_rows * self.tile_size

        self.zoom = 4
        self.timestamps = layer.get('times', {}).get('available', [])
        self.current_time_index = layer.get('times', {}).get('current', 0)

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

        # Pulisci cache all'avvio
        self.clear_cache()

        self.onLayoutFinish.append(self.load_current_tile)

    # ------------------------------------------------------------
    def clear_cache(self):
        """Removes all PNG files from the cache (forces clean download)"""
        try:
            if os.path.exists(CACHE_BASE):
                for f in os.listdir(CACHE_BASE):
                    if f.endswith('.png'):
                        os.remove(os.path.join(CACHE_BASE, f))
                print("[Foreca] Cache pulita")
        except Exception as e:
            print(f"[Foreca] Errore pulizia cache: {e}")

    # ------------------------------------------------------------
    def latlon_to_tile(self, lat, lon, zoom):
        lat_rad = radians(lat)
        n = 2.0 ** zoom
        x = int((lon + 180.0) / 360.0 * n)
        y = int((1.0 - log(tan(lat_rad) + 1.0 / cos(lat_rad)) / pi) / 2.0 * n)
        return x, y

    # ------------------------------------------------------------
    def load_current_tile(self):
        if not self.timestamps:
            self["time"].setText(_("No data available"))
            return

        if self.current_time_index >= len(self.timestamps):
            self.current_time_index = 0

        timestamp = self.timestamps[self.current_time_index]

        try:
            dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
            display_time = dt.strftime("%d/%m %H:%M UTC")
        except BaseException:
            display_time = timestamp

        self["time"].setText(f"{display_time} | Zoom: {self.zoom}")
        self["info"].setText("Downloading tiles...")
        self.download_tile_grid_async(timestamp, self.tile_grid_downloaded)

    # ------------------------------------------------------------
    def download_tile_grid_async(self, timestamp, callback):
        def download_thread():
            cx, cy = self.latlon_to_tile(
                self.center_lat, self.center_lon, self.zoom)
            offset_cols = self.grid_cols // 2
            offset_rows = self.grid_rows // 2

            tile_paths = []
            for dx in range(-offset_cols, offset_cols + 1):
                for dy in range(-offset_rows, offset_rows + 1):
                    tx = cx + dx
                    ty = cy + dy
                    path = self.api.get_tile(
                        self.layer_id,
                        timestamp,
                        self.zoom,
                        tx, ty,
                        self.unit_system
                    )
                    if path:
                        tile_paths.append(
                            (dx + offset_cols, dy + offset_rows, path))

            if len(tile_paths) > 0:
                merged = self.merge_tile_grid(tile_paths)
                if merged and callback:
                    callback(merged)
            else:
                print("[Foreca] Nessuna tile scaricata")
                callback(None)

        from threading import Thread
        Thread(target=download_thread).start()

    # ------------------------------------------------------------
    def merge_tile_grid(self, tile_paths):
        """
        Merges valid tiles on a matte black background.
        Missing/corrupt tiles are skipped -> they remain black.
        """
        try:
            # merged = Image.new('RGB', (self.map_w, self.map_h), (0, 0, 0))
            merged = Image.new('RGBA', (self.map_w, self.map_h), (0, 0, 0, 0))

            for col, row, path in tile_paths:
                try:
                    tile = Image.open(path).convert('RGBA')
                except Exception as e:
                    print(f"[Foreca] Tile corrotta, saltata: {path} - {e}")
                    continue

                x = col * self.tile_size
                y = row * self.tile_size
                merged.paste(tile, (x, y), tile)

            merged_path = os.path.join(
                CACHE_BASE, f"merged_{self.layer_id}_{self.zoom}.png")
            merged.save(merged_path, 'PNG')
            return merged_path

        except Exception as e:
            print(f"[Foreca] Merge error: {e}")
            import traceback
            traceback.print_exc()
            return None

    # ------------------------------------------------------------
    def tile_grid_downloaded(self, merged_image_path):
        if merged_image_path and os.path.exists(merged_image_path):
            try:
                composite_path = create_composite_map(
                    merged_image_path,
                    self.layer_title,
                    self.region,
                    canvas_size=(self.map_w, self.map_h)
                )

                self["map"].instance.setPixmapFromFile(composite_path)
                self["map"].instance.show()
                self.update_layer_info()

                current_time = self.timestamps[self.current_time_index]
                try:
                    dt = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%SZ")
                    display_time = dt.strftime("%d/%m %H:%M UTC")
                except BaseException:
                    display_time = current_time

                self["time"].setText(
                    f"{display_time} | Zoom: {self.zoom} | Grid: {self.grid_cols}x{self.grid_rows}")
                self["info"].setText("Use ← → to change time | OK to exit")

            except Exception as e:
                print(f"[Foreca] Display error: {e}")
                import traceback
                traceback.print_exc()
                self["time"].setText("Error displaying map")
        else:
            self["time"].setText("Error downloading map grid")
            self["info"].setText("Check connection and API credentials")

    # ------------------------------------------------------------
    def update_layer_info(self):
        """Update label with layer and region"""
        try:
            layer_name = self.layer_title
            data_type = self.get_data_type_from_layer(layer_name)
            region_name = self.region.upper()
            unit = "Metric" if self.unit_system == 'metric' else "Imperial"
            self["layerinfo"].setText(f"{data_type} - {region_name} ({unit})")
        except BaseException:
            self["layerinfo"].setText(self.layer_title)

    def get_data_type_from_layer(self, layer_name):
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
        if len(self.timestamps) > 1:
            self.current_time_index = (
                self.current_time_index - 1
            ) % len(self.timestamps)
            self.load_current_tile()

    def next_time(self):
        if len(self.timestamps) > 1:
            self.current_time_index = (
                self.current_time_index + 1
            ) % len(self.timestamps)
            self.load_current_tile()

    def exit(self):
        self.close()
