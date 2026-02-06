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
    with open('/tmp/foreca_tt_log.txt', 'a') as f:
        f.write(str(indata) + '\n')


def getPageTT(MAIN_PAGE, page=None):
    working = True
    if not page:
        page = ""
    url = "%s%s" % (MAIN_PAGE, page)
    try:
        req = Request(url, headers=HEADERS)
        resp = urlopen(req, timeout=10)
        return getForecaPageF(resp.read().decode('utf-8')
                              if PY3 else resp.read())
    except BaseException:
        return ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a', ' n/a'


def getForecaPageF(html):
    try:
        fulltext = compile(r'<h1>Weather in (.+?)</h1><h2', DOTALL)
        town = str('Weather in ' + fulltext.findall(html)[0])
    except BaseException:
        town = er

    try:
        fulltext = compile(
            r'<h2 class="simple">Weather today</h2><p class="wx">(.+?)<em>.+?',
            DOTALL)
        text1 = str(fulltext.findall(html)[0])
    except BaseException:
        text1 = er

    try:
        fulltext = compile(
            r'<h2 class="simple">Weather today</h2>.+?<span class="value temp temp_c">(.+?)&deg;</span>.+?',
            DOTALL)
        h_temp = str(fulltext.findall(html)[0])
    except BaseException:
        h_temp = er

    try:
        fulltext = compile(
            r'</em>and low <em>.+?<span class="value temp temp_c">(.+?)&deg;</span>.+?',
            DOTALL)
        l_temp = str('and low ' + fulltext.findall(html)[0])
    except BaseException:
        l_temp = er

    try:
        fulltext = compile(
            r'</em>. Total rain today <em>.+?<span class="value rain rain_mm">(.+?) mm</span>.+?',
            DOTALL)
        text2 = str('Total rain today ' + fulltext.findall(html)[0])
    except BaseException:
        text2 = er

    try:
        fulltext = compile(
            r'<h2 class="simple">Weather tomorrow</h2><p class="wx">(.+?)<em>.+?',
            DOTALL)
        text3 = str(fulltext.findall(html)[0])
    except BaseException:
        text3 = er

    try:
        fulltext = compile(
            r'<h2 class="simple">Weather tomorrow</h2>.+?<span class="value temp temp_c">(.+?)&deg;</span>.+?',
            DOTALL)
        h2_temp = str(fulltext.findall(html)[0])
    except BaseException:
        h2_temp = er

    try:
        fulltext = compile(
            r'</em>and low <em>.+?<span class="value temp temp_c">(.+?)&deg;</span>.+?',
            DOTALL)
        l2_temp = str('and low ' + fulltext.findall(html)[1])
    except BaseException:
        l2_temp = er

    try:
        fulltext = compile(
            r'</em>. Total rain today <em>.+?<span class="value rain rain_mm">(.+?) mm</span>.+?',
            DOTALL)
        text4 = str('Total rain today ' + fulltext.findall(html)[1])
    except BaseException:
        text4 = er

    # -------------------------------------------------------------------

    try:
        fulltext = compile(
            r'<h2 class="simple">Weather today</h2>.+?<img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_mo1 = str(fulltext.findall(html)[0])
    except BaseException:
        symb_mo1 = er

    try:
        fulltext = compile(
            r'<h2 class="simple">Weather tomorrow</h2>.+?<img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_mo2 = str(fulltext.findall(html)[0])
    except BaseException:
        symb_mo2 = er

    try:
        fulltext = compile(
            r'<h3>Morning</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_mo1 = str(fulltext.findall(html)[0])
    except BaseException:
        t_mo1 = er

    try:
        fulltext = compile(
            r'<h3>Morning</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_mo2 = str(fulltext.findall(html)[1])
    except BaseException:
        t_mo2 = er

    # -------------------------------------------------------------------

    try:
        fulltext = compile(
            r'<h3>Afternoon</h3><img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_af1 = str(fulltext.findall(html)[0])
    except BaseException:
        symb_af1 = er

    try:
        fulltext = compile(
            r'<h3>Afternoon</h3><img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_af2 = str(fulltext.findall(html)[1])
    except BaseException:
        symb_af2 = er

    try:
        fulltext = compile(
            r'<h3>Afternoon</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_af1 = str(fulltext.findall(html)[0])
    except BaseException:
        t_af1 = er

    try:
        fulltext = compile(
            r'<h3>Afternoon</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_af2 = str(fulltext.findall(html)[1])
    except BaseException:
        t_af2 = er

    # -------------------------------------------------------------------

    try:
        fulltext = compile(
            r'<h3>Evening</h3><img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_ev1 = str(fulltext.findall(html)[0])
    except BaseException:
        symb_ev1 = er

    try:
        fulltext = compile(
            r'<h3>Evening</h3><img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_ev2 = str(fulltext.findall(html)[1])
    except BaseException:
        symb_ev2 = er

    try:
        fulltext = compile(
            r'<h3>Evening</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_ev1 = str(fulltext.findall(html)[0])
    except BaseException:
        t_ev1 = er

    try:
        fulltext = compile(
            r'<h3>Evening</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_ev2 = str(fulltext.findall(html)[1])
    except BaseException:
        t_ev2 = er

    # -------------------------------------------------------------------

    try:
        fulltext = compile(
            r'<h3>Overnight</h3><img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_ov1 = str(fulltext.findall(html)[0])
    except BaseException:
        symb_ov1 = er

    try:
        fulltext = compile(
            r'<h3>Overnight</h3><img src="/public/images/symbols/(.+?).svg" .+?',
            DOTALL)
        symb_ov2 = str(fulltext.findall(html)[1])
    except BaseException:
        symb_ov2 = er

    try:
        fulltext = compile(
            r'<h3>Overnight</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_ov1 = str(fulltext.findall(html)[0])
    except BaseException:
        t_ov1 = er

    try:
        fulltext = compile(
            r'<h3>Overnight</h3>.+?</span> <span class="value temp temp_c">(.+?)&deg;.+?',
            DOTALL)
        t_ov2 = str(fulltext.findall(html)[1])
    except BaseException:
        t_ov2 = er

    # -------------------------------------------------------------------

    mylogwrite(
        town +
        ' ' +
        text1 +
        ' ' +
        h_temp +
        ' ' +
        l_temp +
        ' ' +
        text2 +
        ' ' +
        text3 +
        ' ' +
        h2_temp +
        ' ' +
        l2_temp +
        ' ' +
        text4 +
        ' ' +
        symb_mo1 +
        ' ' +
        symb_mo2 +
        ' ' +
        t_mo1 +
        ' ' +
        t_mo2 +
        ' ' +
        symb_af1 +
        ' ' +
        symb_af2 +
        ' ' +
        t_af1 +
        ' ' +
        t_af2 +
        ' ' +
        symb_ev1 +
        ' ' +
        symb_ev2 +
        ' ' +
        t_ev1 +
        ' ' +
        t_ev2 +
        ' ' +
        symb_ov1 +
        ' ' +
        symb_ov2 +
        ' ' +
        t_ov1 +
        ' ' +
        t_ov2)
    return town, text1, h_temp, l_temp, text2, text3, h2_temp, l2_temp, text4, symb_mo1, symb_mo2, t_mo1, t_mo2, symb_af1, symb_af2, t_af1, t_af2, symb_ev1, symb_ev2, t_ev1, t_ev2, symb_ov1, symb_ov2, t_ov1, t_ov2


def first_start():
    MAIN_PAGE_TT = 'https://www.forecaweather.com/100659935/Forssa-Finland'
    mytown, mytext1, myh_temp, myl_temp, mytext2, mytext3, myh2_temp, myl2_temp, mytext4, mysymb_mo1, mysymb_mo2, myt_mo1, myt_mo2, mysymb_af1, mysymb_af2, myt_af1, myt_af2, mysymb_ev1, mysymb_ev2, myt_ev1, myt_ev2, mysymb_ov1, mysymb_ov2, myt_ov1, myt_ov2 = getPageTT(
        MAIN_PAGE_TT)

    print(mytown)
    print(mytext1)
    print(myh_temp)
    print(myl_temp)
    print(mytext2)
    print(mytext3)
    print(myh2_temp)
    print(myl2_temp)
    print(mytext4)
    print(mysymb_mo1)
    print(mysymb_mo2)
    print(myt_mo1)
    print(myt_mo2)
    print(mysymb_af1)
    print(mysymb_af2)
    print(myt_af1)
    print(myt_af2)
    print(mysymb_ev1)
    print(mysymb_ev2)
    print(myt_ev1)
    print(myt_ev2)
    print(mysymb_ov1)
    print(mysymb_ov2)
    print(myt_ov1)
    print(myt_ov2)

# first_start()
