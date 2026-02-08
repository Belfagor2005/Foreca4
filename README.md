<p align="center">
  <img src="https://github.com/Belfagor2005/Foreca4/blob/main/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/foreca_4.png" alt="Foreca4">
</p>

<p align="center">
  <a href="https://github.com/Belfagor2005/Foreca4/actions/workflows/pylint.yml">
    <img src="https://github.com/Belfagor2005/Foreca4/actions/workflows/pylint.yml/badge.svg" alt="Python package">
  </a>
  <a href="https://github.com/Belfagor2005/Foreca4">
    <img src="https://img.shields.io/badge/Version-1.3.4_r4-blue.svg" alt="Version">
  </a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License">
  </a>
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.x-yellow.svg" alt="Python">
  </a>
</p>



# Foreca Weather Forecast E2

Foreca Weather Forecast E2 is an **Enigma2 plugin** that retrieves and displays **actual weather forecasts for up to 10 days** using data provided by **Foreca**.

> We wish all users wonderful weather! ☀️🌦️

---

## 📅 Project Information

* **First release date:** 11/03/2025
* **Weather data source:** [https://www.foreca.com](https://www.foreca.com)

---

## 🔢 Version History

### 3.3.4

* Changed URLs
* Many code improvements
* Cache path moved
* FAlog moved
* Secure image removal from cache folder
* Removed ICC profiles from problematic images

### 3.3.5

* Changed URLs
* Many code improvements
* Planned: add online server URL

### 3.3.6

* Fixed translations
* Many code improvements

### 3.3.7

* Removed `.cfg` files
* Added **TV button** for Menu Configuration

### 3.3.8

* Major cleanup: removed unnecessary code
* Added full Python 3 support
* Translation ~90% complete

---

## 🌍 Foreca 4 Weather and Forecast

* **Original code:** (C) Evg77734, 2025
* **Base version:** v1.3.4
* **Current mod:** @lululla — 2026-01-25 — v1.3.4_r2

---

## 🧠 Core Components

### Core API

* Authentication system
* Token and tile cache management
* Module: `foreca_map_api.py`

### Interface

* Layer selection menu
* Basic map viewer with timeline
* Modules:

  * `foreca_map_menu.py`
  * `foreca_map_viewer.py`

### Integration

* Menu item integrated into the main plugin
* Configuration loaded from file

---

## 🗺️ Map Features

* Download and merge **3×3 tile grids**
* Overlay tiles on existing background maps

  * Examples: `temp_map.png`, `europa.png`, etc.

---

## ⚠️ Trial Plan Limitations

The code is compatible with the **Foreca trial plan** limitations:

* **Maximum:** 1,000 tiles per day
* A **local cache system** is implemented to reuse already downloaded tiles
* This helps avoid exceeding the daily limit

---

## 🌐 Language & Translation

* Full implementation of **GetText** for translations
* Integrated **Google AI / Google Translate API**
* Major translation fixes applied

---

## 📝 To Do

* Add choice list for pressure and other menu options
* Verify all URLs and fetch methods
* Add online server URL selection

---

## ✅ Status

* Actively maintained
* Python 3 ready
* Stable and optimized for Enigma2 environments


## Overview

**Foreca4** is a Weather Map System based on the **Foreca Weather API**, providing live and dynamic weather layers integrated into Enigma2.

---

## Features

- **Authentication**
  - Credentials read from `api_config.txt`
  - JWT token valid for 30 days

- **Dynamic Layers**
  - Layers loaded dynamically from `/api/v1/capabilities`
  - Temperature, Precipitation, Wind, Clouds, Pressure, Radar, etc.

- **Viewer**
  - 3x3 grid tiles
  - Timeline support
  - Overlay on background maps

- **Cache System**
  - Unified `foreca4_map_cache/` directory
  - Stores tokens, capabilities, and tiles

- **Integration**
  - Menu entry: **“Foreca Live Maps (API)”**
  - Fully integrated in the main plugin menu

---

## Background Mapping System

Smart mapping of Foreca layers to background PNGs:

| Layer           | Background PNG       |
|-----------------|----------------------|
| Temperature     | `temp_map.png`       |
| Precipitation   | `rain_map.png`       |
| Clouds          | `cloud_map.png`      |
| Pressure        | `pressure_map.png`   |
| Wind            | `europa.png` *(fallback)* |
| Radar           | `rain_map.png`       |

**Fallback logic:**  
Regional map → `europe.png`

---

## End User Documentation

### Registration
- Foreca Developer Portal:  
  👉 https://developer.foreca.com  
- Free **30-day trial**

### Configuration

Create `api_config.txt`:

```ini
API_USER=your_user
API_PASSWORD=your_password
TOKEN_EXPIRE_HOURS=720
MAP_SERVER=map-eu.foreca.com
AUTH_SERVER=pfa.foreca.com
````

Template available in:

```
api_config.txt.example
```

---

## Critical Links & Resources

* **Official API Documentation**
  [https://developer.foreca.com](https://developer.foreca.com)

* **Trial Registration**

  * 1000 requests/day

* **Available PNG Backgrounds**

  ```
  /thumb/[temp|rain|cloud|pressure]_map.png
  + regional maps
  ```

* **Old Plugin (Reference)**
  [https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py](https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py)

* **Configuration File**

  ```
  Foreca4/api_config.txt
  ```

---

## Current Limits & Considerations

* **Trial Account**

  * 1000 tile requests/day
  * Expires after 30 days

* **Mandatory Attribution**

  * “Foreca” attribution required
  * Additional attribution for radar/satellite data

* **Wind Map**

  * No `wind_map.png` available
  * Uses `europa.png` as fallback

* **Satellite Data**

  * Supported by API (EUMETSAT / NOAA)
  * Not yet implemented

---

## 👥 Credits

* **Design and original idea:** @Bauernbub
* **Enigma2 modifications:** mogli123
* **Major recode and maintenance:** Lululla
* **EUMETSAT screen picxview restore:** thanks to Orlandoxx

---
## License

This project is licensed under the **GNU General Public License v3.0**.

---

© Lululla



## Sistema Mappe API Foreca (FULLY IMPLEMENTED)

- **Autenticazione**
  - Lettura da `api_config.txt`
  - Token JWT valido 30 giorni

- **Layer Dinamici**
  - Menu dinamico da `/api/v1/capabilities`
  - Temperature, Precipitazione, Vento, Nuvole, Pressione, ecc.

- **Visualizzatore**
  - Griglia tile 3x3
  - Timeline
  - Overlay su mappe di background

- **Cache**
  - Cartella unificata `foreca4_map_cache/`
  - Token, capabilities e tile

- **Integrazione**
  - Voce menu **“Foreca Live Maps (API)”** nel plugin principale

---

## Background Mapping System

Mappatura intelligente **layer → background PNG**:

| Layer         | Background PNG |
|--------------|----------------|
| Temperature  | `temp_map.png` |
| Precipitazione | `rain_map.png` |
| Nuvole       | `cloud_map.png` |
| Pressione    | `pressure_map.png` |
| Vento        | `europa.png` *(fallback)* |
| Radar        | `rain_map.png` |

**Fallback gerarchico:**  
mappa regionale → `europa.png`

---

## Documentazione Utente Finale

- **Guida Registrazione**
  - https://developer.foreca.com  
  - Free **30-day trial**

### Configurazione

Creare il file `api_config.txt`:

```ini
API_USER=tuo_user
API_PASSWORD=tua_password
TOKEN_EXPIRE_HOURS=720
MAP_SERVER=map-eu.foreca.com
AUTH_SERVER=pfa.foreca.com
````

Template disponibile in:

```
api_config.txt.example
```

---

## Link e Risorse Critiche

* **Documentazione Ufficiale API**
  [https://developer.foreca.com](https://developer.foreca.com)

* **Registrazione Trial**

  * 1000 richieste/giorno

* **Background PNG Disponibili**

  ```
  /thumb/[temp|rain|cloud|pressure]_map.png
  + mappe regionali
  ```

* **Vecchio Plugin (riferimento)**
  [https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py](https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py)

* **File di Configurazione**

  ```
  Foreca4/api_config.txt
  ```

---

## Limiti e Considerazioni Attuali

* **Account Trial**

  * 1000 richieste tile/giorno
  * Scadenza dopo 30 giorni

* **Attribuzione Obbligatoria**

  * Visualizzare “Foreca”
  * Attribuzioni specifiche per dati radar/satellite

* **Wind Map Background**

  * Nessun `wind_map.png` disponibile
  * Usa `europa.png` come sfondo

* **Satellite Data**

  * Supportati da API (EUMETSAT / NOAA)
  * Non ancora implementati

---

## 👥 Crediti

* **Progettazione e idea originale:** @Bauernbub
* **Modifiche a Enigma2:** mogli123
* **Ricodifica e manutenzione importanti:** Lululla
* **Ripristino della schermata PicxView di EUMETSAT:** grazie a Orlandoxx

---

© Lululla




## Система карт Foreca API (ПОЛНОСТЬЮ РЕАЛИЗОВАНА)

- **Аутентификация**
  - Чтение из `api_config.txt`
  - JWT-токен действителен 30 дней

- **Динамические слои**
  - Меню слоев из `/api/v1/capabilities`
  - Температура, Осадки, Ветер, Облачность, Давление и т. д.

- **Просмотрщик**
  - Сетка 3×3 тайлов
  - Временная шкала
  - Наложение на фоновые карты

- **Кэш**
  - Единая папка `foreca4_map_cache/`
  - Хранение токенов, возможностей и тайлов

- **Интеграция**
  - Пункт меню **«Foreca Live Maps (API)»** в основном плагине

---

## Система фонового картографирования

Интеллектуальное сопоставление **слой → фоновый PNG**:

| Слой          | Фоновый PNG |
|---------------|-------------|
| Температура   | `temp_map.png` |
| Осадки        | `rain_map.png` |
| Облака        | `cloud_map.png` |
| Давление      | `pressure_map.png` |
| Ветер         | `europa.png` *(резервный вариант)* |
| Радар         | `rain_map.png` |

**Иерархический резерв:**  
региональная карта → `europe.png`

---

## Документация для конечного пользователя

- **Руководство по регистрации**
  - https://developer.foreca.com  
  - Бесплатная **30-дневная пробная версия**

### Конфигурация

Создайте файл `api_config.txt` со следующим содержимым:

```ini
API_USER=ваш_пользователь
API_PASSWORD=ваш_пароль
TOKEN_EXPIRE_HOURS=720
MAP_SERVER=map-eu.foreca.com
AUTH_SERVER=pfa.foreca.com
````

Шаблон доступен в:

```
api_config.txt.example
```

---

## Важные ссылки и ресурсы

* **Официальная документация API**
  [https://developer.foreca.com](https://developer.foreca.com)

* **Регистрация пробной версии**

  * 1000 запросов в день

* **Доступные фоновые PNG**

  ```
  /thumb/[temp|rain|cloud|pressure]_map.png
  + региональные карты
  ```

* **Старый плагин (ссылка)**
  [https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py](https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py)

* **Файл конфигурации**

  ```
  Foreca4/api_config.txt
  ```

---

## Текущие ограничения и соображения

* **Пробный аккаунт**

  * 1000 запросов тайлов в день
  * Истекает через 30 дней

* **Обязательная атрибуция**

  * Отображать «Foreca»
  * Дополнительные атрибуции для радиолокационных/спутниковых данных

* **Фон карты ветра**

  * Файл `wind_map.png` отсутствует
  * Используется `europa.png` в качестве фона

* **Спутниковые данные**

  * Поддерживаются API (EUMETSAT / NOAA)
  * Пока не реализованы

---
* **Дизайн и оригинальная идея:** @Bauernbub
* **Модификации Enigma2:** mogli123
* **Основная переработка кода и поддержка:** Lululla
* **Восстановление picxview на экране EUMETSAT:** спасибо Orlandoxx

© Lululla


