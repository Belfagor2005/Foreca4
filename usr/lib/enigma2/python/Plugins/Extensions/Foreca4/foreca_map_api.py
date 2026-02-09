#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# foreca_map_api.py - Gestione API mappe Foreca
# Copyright (c) @Lululla 20260122
import os
import json
import hashlib
import requests
from time import time
from threading import Thread

CACHE_BASE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca4_map_cache/"
CACHE_EXPIRE = 3600  # 1 ora per tile
TOKEN_FILE = CACHE_BASE + "token.json"
CONFIG_FILE = "/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/api_config.txt"


class ForecaMapAPI:
    """Manages the Foreca Map API with cache and file-based configuration"""

    def __init__(self, region='eu'):
        self.user = ""
        self.password = ""
        self.token_expire_hours = 720
        server_map = {
            'eu': 'map-eu.foreca.com',
            'us': 'map-us.foreca.com',
            # Add others if discovered: 'asia', 'au', etc.
        }
        self.map_server = server_map.get(region, 'map-eu.foreca.com')
        self.auth_server = 'pfa.foreca.com'

        self.token = None
        self.token_expire = 0

        if not os.path.exists(CACHE_BASE):
            os.makedirs(CACHE_BASE, exist_ok=True)
            print(f"[ForecaMapAPI] Created cache folder: {CACHE_BASE}")
        self.load_config()
        self.load_token()
        print(
            f"[ForecaMapAPI] Initialized for user: {self.user}, region: {region}")

    def load_config(self):
        """Load configuration from file"""
        default_config = {
            "API_USER": "ekekaz",
            "API_PASSWORD": "im5issEYcMUG",
            "TOKEN_EXPIRE_HOURS": "720",
            "MAP_SERVER": "map-eu.foreca.com",
            "AUTH_SERVER": "pfa.foreca.com"
        }

        config_data = default_config.copy()

        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    lines = f.readlines()

                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, value = line.split('=', 1)
                            key = key.strip()
                            value = value.strip()
                            config_data[key] = value

                print(
                    f"[ForecaMapAPI] Configuration loaded from {CONFIG_FILE}")
            except Exception as e:
                print(f"[ForecaMapAPI] Error loading config: {e}")
                # Create example config file
                self.create_example_config()
        else:
            print("[ForecaMapAPI] Config file not found, creating example")
            self.create_example_config()
            # Use hardcoded values as fallback
            config_data = default_config

        # Assign values
        self.user = config_data.get("API_USER", "ekekaz")
        self.password = config_data.get("API_PASSWORD", "im5issEYcMUG")
        self.token_expire_hours = int(
            config_data.get(
                "TOKEN_EXPIRE_HOURS", 720))
        self.map_server = config_data.get("MAP_SERVER", "map-eu.foreca.com")
        self.auth_server = config_data.get("AUTH_SERVER", "pfa.foreca.com")

        # Check if credentials are present
        if not self.user or not self.password:
            print("[ForecaMapAPI] WARNING: API credentials missing in config file!")

    def _get_colorscheme_for_layer(self, layer_id, unit_system='metric'):
        """
        Returns the appropriate color scheme for a layer and a unit system.
        unit_system: 'metric' or 'imperial'
        """
        # Mapping based on the foreca_capabilities.json file
        # ID 2: Temperature
        # ID 8: Wind
        colorschemes = {
            # Temperature
            2: {'metric': 'default', 'imperial': 'temp-fahrenheit-noalpha'},
            8: {'metric': 'winds-noalpha', 'imperial': 'winds-mph-noalpha'},  # Wind
            # Add other layer IDs here if needed (e.g. 3, 4, etc.)
        }

        # Get the mapping for the layer, if it exists
        layer_map = colorschemes.get(layer_id, {})
        # Return the scheme for the unit system, defaulting to 'default' if not
        # found
        return layer_map.get(unit_system, 'default')

    def create_example_config(self):
        """Create example configuration file"""
        try:
            example_content = """# Foreca API Configuration
                # Rename this file to api_config.txt and fill with your credentials

                # Your Foreca API username
                API_USER=ekekaz

                # Your Foreca API password
                API_PASSWORD=im5issEYcMUG

                # Token expiration in hours (max 720 = 30 days)
                TOKEN_EXPIRE_HOURS=720

                # Map server (EU, US, etc.)
                MAP_SERVER=map-eu.foreca.com

                # Authentication server
                AUTH_SERVER=pfa.foreca.com

                # Save this file as api_config.txt (remove .example)
                """
            example_file = CONFIG_FILE + ".example"
            with open(example_file, 'w') as f:
                f.write(example_content)
            print(f"[ForecaMapAPI] Created example file: {example_file}")
        except Exception as e:
            print(f"[ForecaMapAPI] Error creating example: {e}")

    def load_token(self):
        """Load token from cache"""
        if os.path.exists(TOKEN_FILE):
            try:
                with open(TOKEN_FILE, 'r') as f:
                    data = json.load(f)
                    if data['expire'] > time():
                        self.token = data['token']
                        self.token_expire = data['expire']
                        print("[ForecaMapAPI] Token loaded from cache")
            except Exception as e:
                print(f"[ForecaMapAPI] Error loading token: {e}")

    def get_token(self, force_new=False):
        """Get a valid authentication token"""

        print(
            f"[DEBUG] get_token called. "
            f"force_new={force_new}, "
            f"token_exists={self.token is not None}, "
            f"expire={self.token_expire}, "
            f"current_time={time()}"
        )

        # Check if credentials exist
        if not self.user or not self.password:
            print("[ForecaMapAPI] ERROR: Missing credentials!")
            return None

        # Use cached token if still valid (with 5 minutes safety margin)
        if not force_new and self.token and self.token_expire > time() + 300:
            print("[DEBUG] Cached token is still valid")
            return self.token

        print("[DEBUG] Requesting a NEW token...")
        try:
            url = f"https://{self.auth_server}/authorize/token?expire_hours={self.token_expire_hours}"
            data = {"user": self.user, "password": self.password}
            print(f"[DEBUG] Auth URL: {url}")

            response = requests.post(url, json=data, timeout=10)
            print(f"[DEBUG] Auth HTTP status: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                self.token = result['access_token']
                self.token_expire = time() + result['expires_in']

                print(
                    f"[DEBUG] New token received: {self.token[:30]}..., "
                    f"expires in {result['expires_in']} seconds"
                )

                # Save token to cache
                with open(TOKEN_FILE, 'w') as f:
                    json.dump({
                        'token': self.token,
                        'expire': self.token_expire
                    }, f)

                return self.token
            else:
                print(
                    f"[DEBUG] Auth HTTP error {response.status_code}: "
                    f"{response.text[:100]}"
                )
                return None

        except Exception as e:
            print(f"[DEBUG] get_token exception: {e}")
            import traceback
            traceback.print_exc()
            return None

    def get_capabilities(self):
        """Get available layers list"""
        token = self.get_token()
        if not token:
            print("[ForecaMapAPI] No token for capabilities")
            return []

        cache_file = CACHE_BASE + "capabilities.json"

        # Use cache if valid (30 minutes)
        if os.path.exists(cache_file):
            mtime = os.path.getmtime(cache_file)
            if time() - mtime < 1800:  # 30 minutes
                try:
                    with open(cache_file, 'r') as f:
                        data = json.load(f)
                        print(
                            f"[ForecaMapAPI] Capabilities from cache: {len(data.get('images', []))} layers")
                        return data.get('images', [])
                except Exception as e:
                    print(f"[ForecaMapAPI] Error cache capabilities: {e}")

        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                f"https://{self.map_server}/api/v1/capabilities",
                headers=headers,
                timeout=15
            )

            if response.status_code == 200:
                data = response.json()
                # Save to cache
                with open(cache_file, 'w') as f:
                    json.dump(data, f)
                print(
                    f"[ForecaMapAPI] Capabilities downloaded: {len(data.get('images', []))} layers")
                return data.get('images', [])
            else:
                print(
                    f"[ForecaMapAPI] Error capabilities HTTP {response.status_code}")
                return []

        except Exception as e:
            print(f"[ForecaMapAPI] Error capabilities: {e}")
            return []

    def get_tile(self, layer_id, timestamp, zoom, x, y, unit_system='metric'):
        """Download a single tile with cache support"""
        print("[DEBUG] === get_tile START ===")

        # Get token
        token = self.get_token()
        if not token:
            print("[DEBUG] ERROR: No token obtained!")
            return None

        # Determine color scheme based on unit system
        colorscheme = self._get_colorscheme_for_layer(layer_id, unit_system)

        # Create a cache key that also includes the color scheme
        cache_key = f"{layer_id}_{timestamp}_{zoom}_{x}_{y}_{colorscheme}"
        cache_hash = hashlib.md5(cache_key.encode()).hexdigest()
        cache_file = os.path.join(CACHE_BASE, f"{cache_hash}.png")

        # Check cache
        if os.path.exists(cache_file):
            mtime = os.path.getmtime(cache_file)
            if time() - mtime < CACHE_EXPIRE:
                print(f"[DEBUG] Tile loaded from cache: {cache_key}")
                return cache_file

        try:
            # BUILD THE URL WITH THE COLORSCHEME PARAMETER
            url = f"https://{self.map_server}/api/v1/image/tile/{zoom}/{x}/{y}/{timestamp}/{layer_id}?colorscheme={colorscheme}"
            headers = {"Authorization": f"Bearer {token}"}
            print(f"[DEBUG] Tile URL: {url}")

            response = requests.get(url, headers=headers, timeout=30)

            print(f"[DEBUG] HTTP response: {response.status_code}")
            if response.status_code != 200:
                print(f"[DEBUG] Error response content: {response.text[:200]}")

            if response.status_code == 200:
                with open(cache_file, 'wb') as f:
                    f.write(response.content)
                print(f"[DEBUG] Tile downloaded successfully: {cache_key}")
                return cache_file
            else:
                print(f"[DEBUG] Tile download error: {response.status_code}")
                return None

        except Exception as e:
            print(f"[DEBUG] Tile download exception: {e}")
            return None

    def download_tile_async(
            self,
            layer_id,
            timestamp,
            zoom,
            x,
            y,
            callback,
            unit_system='metric'):
        """Download tile in separate thread"""
        def download_thread():
            result = self.get_tile(
                layer_id, timestamp, zoom, x, y, unit_system)
            if callback:
                callback(result)

        Thread(target=download_thread).start()

    def check_credentials(self):
        """Check if credentials are configured"""
        return bool(self.user and self.password)

    def clear_cache(self, days_old=1):
        """Clear old cache files"""
        try:
            current_time = time()
            deleted_files = 0

            for filename in os.listdir(CACHE_BASE):
                filepath = os.path.join(CACHE_BASE, filename)

                # Skip token file and capabilities
                if filename in ["token.json", "capabilities.json"]:
                    continue

                if os.path.isfile(filepath):
                    # Check if file is older than X days
                    file_age = current_time - os.path.getmtime(filepath)
                    if file_age > (days_old * 86400):  # days to seconds
                        os.remove(filepath)
                        deleted_files += 1

            if deleted_files > 0:
                print(
                    f"[ForecaMapAPI] Cleared {deleted_files} old cache files")

        except Exception as e:
            print(f"[ForecaMapAPI] Error clearing cache: {e}")
