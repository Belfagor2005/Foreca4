Foreca API Map System (FULLY IMPLEMENTED)

Authentication: Read from api_config.txt → JWT token (30 days)
Dynamic Layers: Show layers menu from /api/v1/capabilities (Temperature, Precipitation, Wind, Clouds, Pressure, etc.)
Viewer: 3x3 grid tiles, timeline, overlay on background maps
Cache: Unified foreca4_map_cache/ folder for tokens, capabilities, and tiles
Integration: "Foreca Live Maps (API)" menu item in the main plugin
Background Mapping System
Smart mapping layer → background PNG:
temperature → temp_map.png
precipitation → rain_map.png
cloud → cloud_map.png
pressure → pressure_map.png
wind → europa.png (fallback - no wind_map.png) (existing)
radar → rain_map.png
Hierarchical fallback: regional map → europe.png

End User Documentation
Registration Guide: https://developer.foreca.com (FREE 30-day trial)

Configuration: Create api_config.txt with:
API_USER=your_user
API_PASSWORD=your_password
TOKEN_EXPIRE_HOURS=720
MAP_SERVER=map-eu.foreca.com
AUTH_SERVER=pfa.foreca.com

CRITICAL LINKS AND RESOURCES
Official API Documentation: https://developer.foreca.com
Trial Registration: Module on developer.foreca.com (1000 requests/day)
Available PNG Backgrounds: /thumb/[temp|rain|cloud|pressure]_map.png + regional maps
Old Plugin (reference): https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py
Configuration File: Foreca4/api_config.txt (template in api_config.txt.example)

CURRENT LIMITS/CONSIDERATIONS
Trial Account: 1000 tile requests/day, expires after 30 days
Mandatory Attribution: Show "Foreca" + specific attributions for radar/satellite data
Wind Map Background: No existing wind_map.png → use europa.png as background
Satellite Data: API supports satellite layers (EUMETSAT/NOAA) but not yet implemented

@Lululla



Sistema Mappe API Foreca (FULLY IMPLEMENTED)

Autenticazione: Lettura da api_config.txt → token JWT (30 giorni)
Layer Dinamici: Menu mostra layer da /api/v1/capabilities (Temperature, Precipitazione, Vento, Nuvole, Pressione, etc.)
Visualizzatore: Griglia 3x3 tile, timeline, overlay su mappe di background
Cache: Cartella unificata foreca4_map_cache/ per token, capabilities e tile
Integrazione: Voce menu "Foreca Live Maps (API)" in plugin principale
Background Mapping System
Mappatura intelligente layer→background PNG:
temperature → temp_map.png
precipitation → rain_map.png
cloud → cloud_map.png
pressure → pressure_map.png
wind → europa.png (fallback - nessun wind_map.png esistente)
radar → rain_map.png
Fallback gerarchico: mappa regionale → europa.png

Documentazione Utente Finale
Guida registrazione: https://developer.foreca.com (FREE 30-day trial)

Configurazione: Creare api_config.txt con:
API_USER=tuo_user
API_PASSWORD=tua_password
TOKEN_EXPIRE_HOURS=720
MAP_SERVER=map-eu.foreca.com
AUTH_SERVER=pfa.foreca.com

LINK E RISORSE CRITICHE
Documentazione Ufficiale API: https://developer.foreca.com
Registrazione Trial: Modulo su developer.foreca.com (1000 richieste/giorno)
Background PNG Disponibili: /thumb/[temp|rain|cloud|pressure]_map.png + mappe regionali
Vecchio Plugin (riferimento): https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py
File di Configurazione: Foreca4/api_config.txt (template in api_config.txt.example)

LIMITI/CONSIDERAZIONI ATTUALI
Account Trial: 1000 richieste tile/giorno, scade dopo 30 giorni
Attribuzione Obbligatoria: Mostrare "Foreca" + attribuzioni specifiche per dati radar/satellite
Wind Map Background: Nessun wind_map.png esistente → usa europa.png come sfondo
Satellite Data: API supporta layer satellite (EUMETSAT/NOAA) ma non ancora implementato

@Lululla


Система карт Foreca API (ПОЛНОСТЬЮ РЕАЛИЗОВАНА)

Аутентификация: Чтение из api_config.txt → JWT-токен (30 дней)
Динамические слои: Отображение меню слоев из /api/v1/capabilities (Температура, Осадки, Ветер, Облачность, Давление и т. д.)
Просмотрщик: Сетка 3x3, временная шкала, наложение на фоновые карты
Кэш: Единая папка foreca4_map_cache/ для токенов, возможностей и тайлов
Интеграция: Пункт меню "Foreca Live Maps (API)" в основном плагине
Система фонового картографирования
Слой интеллектуального картографирования → фоновый PNG:
температура → temp_map.png
осадки → rain_map.png
облака → cloud_map.png
давление → pressure_map.png
ветер → europa.png (резервный вариант) - нет wind_map.png) (существует)
радар → rain_map.png
Иерархический резерв: региональная карта → europe.png

Документация для конечного пользователя
Руководство по регистрации: https://developer.foreca.com (БЕСПЛАТНАЯ 30-дневная пробная версия)

Конфигурация: Создайте файл api_config.txt со следующим содержимым:
API_USER=ваш_пользователь
API_PASSWORD=ваш_пароль
TOKEN_EXPIRE_HOURS=720
MAP_SERVER=map-eu.foreca.com
AUTH_SERVER=pfa.foreca.com

ВАЖНЫЕ ССЫЛКИ И РЕСУРСЫ
Официальная документация API: https://developer.foreca.com
Регистрация пробной версии: Модуль на developer.foreca.com (1000 запросов в день)
Доступные фоновые изображения PNG: /thumb/[temp|rain|cloud|pressure]_map.png + региональные карты
Старый плагин (ссылка): https://github.com/Belfagor2005/e2openplugin-Foreca/blob/master/plugin/ui.py
Файл конфигурации: Foreca4/api_config.txt (шаблон в api_config.txt.example)

ТЕКУЩИЕ ОГРАНИЧЕНИЯ/СООБРАЖЕНИЯ
Пробный аккаунт: 1000 запросов тайлов в день, истекает через 30 дней
Обязательная атрибуция: Отображать "Foreca" + конкретные атрибуции для радиолокационных/спутниковых данных
Фон карты ветра: Нет существующего файла wind_map.png → использовать europa.png в качестве фона
Спутниковые данные: API поддерживает спутниковые слои (EUMETSAT/NOAA), но пока не реализовано

@Lululla