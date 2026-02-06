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
    with open('/tmp/foreca_forecast_log.txt', 'a') as f:
        f.write(str(indata) + '\n')


def getPageF_F(MAIN_PAGE, page=None):
    working = True
    if not page:
        page = ""
    url = "%s%s" % (MAIN_PAGE, page)
    try:
        req = Request(url, headers=HEADERS)
        resp = urlopen(req, timeout=10)
        return getForecaPageF_F(resp.read().decode('utf-8') if PY3 else resp.read())
    except:
        return ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a'


def getForecaPageF_F(html):
    date = []
    mytime = []
    sb = []

    try:
        fulltext = compile(r',"defaultName":"(.+?)",".+?', DOTALL)
        town = str(fulltext.findall(html)[1])
        mylogwrite(town)
    except:
        town = er

    try:
        fulltext = compile(r'"time":"(.+?)",".+?', DOTALL)
        time = str(fulltext.findall(html))
        time1 = time.split("['24h', '")[1]
        time2 = time1.split("']")[0]
        time3 = time2.split("', '")

        for n in time3:
            date1 = n.split('T')[0]
            mt1 = n.split('T')[1]

            date.append(date1)
            mytime.append(mt1)
        mylogwrite(date)
        mylogwrite(mytime)
    except:
        mydate = er
        mytime = er

    try:
        fulltext = compile(r'"symb":"(.+?)",".+?', DOTALL)
        symb = str(fulltext.findall(html))
        symb1 = symb.split("['")[1]
        symb2 = symb1.split("']")[0]
        symb3 = symb2.split("', '")
        mylogwrite(symb3)
    except:
        symb3 = er

    try:
        fulltext = compile(r',"temp":(.+?),".+?', DOTALL)
        cur_temp = str(fulltext.findall(html))
        cur_temp1 = cur_temp.split("['")[1]
        cur_temp2 = cur_temp1.split("']")[0]
        cur_temp3 = cur_temp2.split("', '")
        mylogwrite(cur_temp3)
    except:
        cur_temp3 = er

    try:
        fulltext = compile(r',"flike":(.+?),".+?', DOTALL)
        flike_temp = str(fulltext.findall(html))
        flike_temp1 = flike_temp.split("['")[1]
        flike_temp2 = flike_temp1.split("']")[0]
        flike_temp3 = flike_temp2.split("', '")
        mylogwrite(flike_temp3)
    except:
        flike_temp3 = er

    try:
        fulltext = compile(r',"windd":(.+?),".+?', DOTALL)
        wind = str(fulltext.findall(html))
        wind1 = wind.split("['")[1]
        wind2 = wind1.split("']")[0]
        wind3 = wind2.split("', '")
        mylogwrite(wind3)
    except:
        wind3 = er

    """
    try:
        fulltext = compile(r',"winds":(.+?),".+?', DOTALL)
        wind_speed = str(fulltext.findall(html))
        wind_speed1 = wind_speed.split("['")[1]
        wind_speed2 = wind_speed1.split("']")[0]
        wind_speed3 = wind_speed2.split("', '")
        mylogwrite(wind_speed3)
    except:
        wind_speed3 = er
    """

    try:
        fulltext = compile(r',"windskmh":(.+?),".+?', DOTALL)
        wind_speed = str(fulltext.findall(html))
        wind_speed1 = wind_speed.split("['")[1]
        wind_speed2 = wind_speed1.split("']")[0]
        wind_speed3 = wind_speed2.split("', '")
        mylogwrite(wind_speed3)
    except:
        wind_speed3 = er

    try:
        fulltext = compile(r',"rainp":(.+?),".+?', DOTALL)
        precipitation = str(fulltext.findall(html))
        precipitation1 = precipitation.split("['")[1]
        precipitation2 = precipitation1.split("']")[0]
        precipitation3 = precipitation2.split("', '")
        mylogwrite(precipitation3)
    except:
        precipitation3 = er

    try:
        fulltext = compile(r',"rhum":(.+?),".+?', DOTALL)
        rel_hum = str(fulltext.findall(html))
        rel_hum1 = rel_hum.split("['")[1]
        rel_hum2 = rel_hum1.split("']")[0]
        rel_hum3 = rel_hum2.split("', '")
        mylogwrite(rel_hum3)
    except:
        rel_hum3 = er

    try:
        fulltext = compile(r'<div class="dayName">(.+?)</div>.+?', DOTALL)
        day = str(fulltext.findall(html)[0])
        mylogwrite(day)
    except:
        day = er

    return town, date, mytime, symb3, cur_temp3, flike_temp3, wind3, wind_speed3, precipitation3, rel_hum3, day


# -----------------------------------------------------------------------


def first_start(indata):
    # MAIN_PAGE = 'https://www.foreca.com/100659935/Forssa-Finland/hourly?day=' + str(indata)
    # MAIN_PAGE = 'https://www.foreca.com/100457954/Liep%c4%81ja-Latvia/hourly?day=' + str(indata)
    MAIN_PAGE = 'https://www.foreca.com/100688148/Yenakiyeve-Donetsk-Oblast-Ukraine/hourly?day=' + str(indata)
    mytown, mydate, mytime, mysymb, mycur_temp, myflike_temp, mywind, mywind_speed, myprecipitation, myrel_hum, myday = getPageF_F(MAIN_PAGE)
    print(mytown)
    print(mydate)
    print(mytime)
    print(mysymb)
    print(mycur_temp)
    print(myflike_temp)
    print(mywind)
    print(mywind_speed)
    print(myprecipitation)
    print(myrel_hum)
    print(myday)

# first_start(1)
