#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) Evg77734 2025
#

from re import DOTALL, compile
from sys import version_info

PY3 = version_info[0] == 3
if PY3:
    from urllib.request import urlopen, Request  # , pathname2url
else:
    # from urllib import pathname2url
    from urllib2 import urlopen, Request

er = ' n/a'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
}


def mylogwrite(indata):
    with open('/tmp/foreca_current_log.txt', 'a') as f:
        f.write(str(indata) + '\n')


def getPageF(MAIN_PAGE, page=None):
    working = True
    if not page:
        page = ""
    url = "%s%s" % (MAIN_PAGE, page)
    try:
        req = Request(url, headers=HEADERS)
        resp = urlopen(req, timeout=10)
        return getForecaPageF(resp.read().decode('utf-8') if PY3 else resp.read())
    except:
        return ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a'


def getForecaPageF(html):
    try:
        fulltext = compile(r'Weather today - (.+?)</title>', DOTALL)
        town = str(fulltext.findall(html)[0]).split(', ')[0]
    except:
        town = er

    try:
        fulltext = compile(r'<p class="large"><span class="value temp temp_c warm">(.+?)&deg;.+?', DOTALL)
        cur_temp = str(fulltext.findall(html)[0])
    except:
        try:
            fulltext = compile(r'<p class="large"><span class="value temp temp_c cold">(.+?)&deg;.+?', DOTALL)
            cur_temp = str(fulltext.findall(html)[0])
        except:
            cur_temp = er

    try:
        fulltext = compile(r'<p>Feels like <span class="value temp temp_c warm"><em>(.+?)&deg;.+?', DOTALL)
        fl_temp = str(fulltext.findall(html)[0])
    except:
        try:
            fulltext = compile(r'<p>Feels like <span class="value temp temp_c cold"><em>(.+?)&deg;.+?', DOTALL)
            fl_temp = str(fulltext.findall(html)[0])
        except:
            fl_temp = er

    try:
        fulltext = compile(r'>Dewpoint <span class="value temp temp_c warm"><em>(.+?)&deg;.+?', DOTALL)
        dewpoint = str(fulltext.findall(html)[0])
    except:
        try:
            fulltext = compile(r'Dewpoint <span class="value temp temp_c cold"><em>(.+?)&deg;.+?', DOTALL)
            dewpoint = str(fulltext.findall(html)[0])
        except:
            dewpoint = er

    try:
        fulltext = compile(r'<img src="/public/images/symbols/(.+?).svg" alt=".+?', DOTALL)
        pic = str(fulltext.findall(html)[0])
    except:
        pic = er

    try:
        fulltext = compile(r'<img src="/public/images/wind/blue/(.+?).svg" .+?', DOTALL)
        wind = str(fulltext.findall(html)[0])
    except:
        wind = er

    try:
        fulltext = compile(r'<span class="value wind wind_kmh">(.+?) kmh.+?', DOTALL)
        wind_speed = str(fulltext.findall(html)[0])
    except:
        wind_speed = er

    try:
        fulltext = compile(r'<span class="value wind wind_kmh"><em>(.+?)</em> kmh.+?', DOTALL)
        wind_gust = str(fulltext.findall(html)[0])
    except:
        wind_gust = er

    try:
        fulltext = compile(r'<span class="value rain rain_mm"><em>(.+?)</em> mm</span> .+?', DOTALL)
        rain_mm = str(fulltext.findall(html)[0])
    except:
        rain_mm = er

    try:
        fulltext = compile(r'<div class="rhum center"><p><em>(.+?)</em>.+?', DOTALL)
        hum = str(fulltext.findall(html)[0])
    except:
        hum = er

    try:
        fulltext = compile(r'<span class="value pres pres_mmhg"><em>(.+?)</em> .+?', DOTALL)
        pressure = str(fulltext.findall(html)[0])
    except:
        pressure = er

    try:
        fulltext = compile(r',"defaultCountryName":"(.+?)",', DOTALL)
        country = str(fulltext.findall(html)[0])
    except:
        country = er

    try:
        fulltext = compile(r'lon: (.+?),.+?', DOTALL)
        lon = str(fulltext.findall(html)[0])
    except:
        lon = er

    try:
        fulltext = compile(r'lat: (.+?),.+?', DOTALL)
        lat = str(fulltext.findall(html)[0])
    except:
        lat = er

    try:
        fulltext = compile(r'class="row sun details">.+?<span class="value time time_24h">(.+?)</span></em>.+?', DOTALL)
        sunrise = str(fulltext.findall(html)[0])
    except:
        sunrise = er

    try:
        fulltext = compile(r'<div class="daylen center"><em>(.+?)</em><br>.+?', DOTALL)
        daylen = str(fulltext.findall(html)[0])
    except:
        daylen = er

    try:
        fulltext = compile(r'<div class="sunset right"><em>.+?<span class="value time time_24h">(.+?)</span></em><br>Sunset</div>.+?', DOTALL)
        sunset = str(fulltext.findall(html)[0])
    except:
        sunset = er

    mylogwrite(town + ' ' + cur_temp + ' ' + fl_temp + ' ' + dewpoint + ' ' + pic + ' ' + wind + ' ' + wind_speed + ' ' + wind_gust + ' ' + rain_mm + ' ' + hum + ' ' + pressure + ' ' + country + ' ' + lon + ' ' + lat + ' ' + sunrise + ' ' + daylen + ' ' + sunset)
    return town, cur_temp, fl_temp, dewpoint, pic, wind, wind_speed, wind_gust, rain_mm, hum, pressure, country, lon, lat, sunrise, daylen, sunset


def first_start():
    MAIN_PAGE_F = 'https://www.foreca.com/100457954/Liep%c4%81ja-Latvia'
    mytown, mycur_temp, myfl_temp, mydewpoint, mypic, mywind, mywind_speed, mywind_gust, myrain_mm, myhum, mypressure, mycountry, mylon, mylat, mysunrise, mydaylen, mysunset = getPageF(MAIN_PAGE_F)

    print(mytown)
    print(mycur_temp)
    print(myfl_temp)
    print(mydewpoint)
    print(mypic)
    print(mywind)
    print(mywind_speed)
    print(mywind_gust)
    print(myrain_mm)
    print(myhum)
    print(mypressure)
    print(mycountry)
    print(mylon)
    print(mylat)
    print(mysunrise)
    print(mydaylen)
    print(mysunset)

# first_start()
