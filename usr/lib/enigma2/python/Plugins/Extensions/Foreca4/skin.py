#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created (C) Evg77734, 2025

ForecaPreview_4_FHD = """
<screen name="ForecaPreview_4_FHD" position="0,0" size="1920,1080" title="Foreca Weather Preview" flags="wfNoBorder" backgroundColor="transparent">
    <ePixmap name="" position="205,140" size="400,86" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/forecalogo.png" zPosition="3" scale="1" transparent="1" />
    <widget source="mytitel2" render="Label" position="245,1005" size="300,43" font="Regular;32" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center" />
    <widget source="mytitel1" render="Label" position="30,26" size="750,56" font="Regular;34" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center" />
    <widget source="Titel" render="Label" position="848,26" size="985,56" font="Regular;34" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center" />
    <widget source="Titel2" render="Label" position="1398,26" size="985,56" font="Regular;34" foregroundColor="black" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="right" />
    <widget name="town" position="155,260" size="500,40" zPosition="3" font="Regular;28" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="cur_temp" position="60,395" size="200,70" zPosition="3" font="Regular;50" backgroundColor="black" transparent="1" valign="center" />
    <widget name="fl_temp" position="40,575" size="300,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" />
    <widget name="pressure_pic" position="371,695" size="48,48" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
    <widget name="rain_mm_pic" position="112,695" size="48,48" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
    <widget name="hum_pic" position="665,695" size="48,48" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
    <widget name="description_w" position="40,510" size="730,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="dewpoint" position="40,630" size="300,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" />
    <widget name="pic" position="355,380" size="100,100" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
    <widget name="sun" position="295,827" size="200,63" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
    <widget name="wind" position="592,385" size="40,41" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
    <widget name="wind_speed" position="440,575" size="330,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" />
    <widget name="wind_gust" position="440,630" size="330,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" />
    <widget name="rain_mm" position="50,765" size="170,40" zPosition="3" font="Regular;26" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="hum" position="610,765" size="160,40" zPosition="3" font="Regular;26" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="pressure" position="270,765" size="250,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="day_len" position="270,900" size="250,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="sunrise_text" position="50,900" size="170,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="sunrise_val" position="50,850" size="170,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="sunset_text" position="570,900" size="160,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <widget name="sunset_val" position="570,850" size="160,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center" />
    <ePixmap name="" position="48,323" size="48,48" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/observation.png" zPosition="3" scale="1" transparent="1" />
    <widget name="station" position="100,325" size="400,48" font="Regular;24" halign="left" backgroundColor="black" transparent="1" valign="center" zPosition="3" />
    <ePixmap position="65,1004" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png" scale="1" zPosition="3" />
    <ePixmap position="150,1004" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png" scale="1" zPosition="3" />
    <ePixmap position="555,1004" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png" scale="1" zPosition="3" />
    <ePixmap position="640,1004" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_help.png" scale="1" zPosition="3" />
    <!--
    <eLabel name="new eLabel" position="555,1005" size="110,43" transparent="1" backgroundColor="black" text=" Help " foregroundColor="white" font="Regular;32" zPosition="3" borderColor="black" valign="center" />
    <eLabel name="new eLabel" position="665,1005" size="120,43" transparent="1" backgroundColor="#000080" text="Help+" foregroundColor="#0053a9ff" font="Regular;32" zPosition="3" valign="center" />
    <eLabel name="new eLabel2" position="30,1005" size="70,43" transparent="1" backgroundColor="black" text="Ok" foregroundColor="white" font="Regular;32" zPosition="3" borderColor="black" valign="center" />
    <eLabel name="new eLabel3" position="100,1005" size="150,43" transparent="1" backgroundColor="#000080" text="Ext info" foregroundColor="#0053a9ff" font="Regular;32" zPosition="3" valign="center" />
    -->
    <eLabel position="598,315" size="28,28" transparent="1" backgroundColor="#000080" text="N" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center" />
    <eLabel position="598,471" size="28,28" transparent="1" backgroundColor="#000080" text="S" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center" />
    <eLabel position="673,391" size="28,28" transparent="1" backgroundColor="#000080" text="E" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center" />
    <eLabel position="523,391" size="28,28" transparent="1" backgroundColor="#000080" text="W" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center" />
    <widget name="plate1" zPosition="1" size="1100,960" position="810,110" backgroundColor="#000050ef" cornerRadius="50" />
    <widget name="plate11" size="1080,940" zPosition="2" position="820,120" backgroundColor="#40000000" cornerRadius="50" />
    <widget name="plate2" size="790,860" zPosition="1" position="10,110" backgroundColor="#000050ef" cornerRadius="50" />
    <widget name="plate22" size="770,840" zPosition="2" position="20,120" backgroundColor="#40000000" cornerRadius="50" />
    <widget name="plate3" size="790,90" zPosition="1" position="10,980" backgroundColor="#000050ef" cornerRadius="50" />
    <widget name="plate33" size="770,70" zPosition="2" position="20,990" backgroundColor="#40000000" cornerRadius="50" />
    <widget name="plate4" size="1100,90" zPosition="1" position="810,10" backgroundColor="#000050ef" cornerRadius="50" />
    <widget name="plate5" size="790,90" zPosition="1" position="10,10" backgroundColor="#000050ef" cornerRadius="50" />
    <widget name="plate44" size="1080,70" zPosition="2" position="820,20" backgroundColor="#40000000" cornerRadius="50" />
    <widget name="plate55" size="770,70" zPosition="2" position="20,20" backgroundColor="#40000000" cornerRadius="50" />
    <widget source="menu" render="Listbox" position="833,143" size="1055,885" scrollbarMode="showOnDemand" zPosition="3" transparent="1" backgroundColor="black">
        <convert type="TemplatedMultiContent">
      {"template": [
          MultiContentEntryText(pos = (40, 49), size = (90, 30), font=0, flags = RT_HALIGN_LEFT, text = 0),
          MultiContentEntryText(pos = (270, 20), size = (120, 30), font=0, flags = RT_HALIGN_LEFT, text = 1),
          MultiContentEntryPixmapAlphaTest(pos = (155, 24), size = (70, 70), png = 2),
          MultiContentEntryText(pos = (270, 64), size = (120, 30), font=0, flags = RT_HALIGN_LEFT, text = 3),
          MultiContentEntryPixmapAlphaTest(pos = (390, 41), size = (27, 28), png = 4),
          MultiContentEntryText(pos = (455, 20), size = (120, 30), font=0, flags = RT_HALIGN_LEFT, text = 5),
          MultiContentEntryText(pos = (455, 64), size = (120, 30), font=0, flags = RT_HALIGN_LEFT, text = 6),
          MultiContentEntryText(pos = (580, 1), size = (470, 30), font=0, flags = RT_HALIGN_LEFT, text = 7),
          MultiContentEntryText(pos = (580, 31), size = (470, 24), font=1, flags = RT_HALIGN_LEFT, text = 8),
          MultiContentEntryText(pos = (580, 56), size = (470, 24), font=1, flags = RT_HALIGN_LEFT, text = 9),
          MultiContentEntryText(pos = (580, 81), size = (470, 24), font=1, flags = RT_HALIGN_LEFT, text = 10),
          ],
      "fonts": [gFont("Regular", 26),gFont("Regular", 20)],
      "itemHeight": 110
      }
                  </convert>
    </widget>
</screen>"""

ColorSelect_FHD = """
<screen name="ColorSelect_FHD" position="center,center" backgroundColor="transparent" size="1160,940" flags="wfNoBorder">
    <widget name="Clist" itemHeight="35" position="45,105" size="1070,596" enableWrapAround="1" scrollbarMode="showOnDemand" valign="center" font="Console;28" transparent="1" backgroundColor="black" zPosition="3"/>
    <widget name="colordatas" position="45,850" size="1070,42" font="Regular;32" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black"/>
    <widget name="colorname" position="45,790" size="1070,42" font="Regular;32" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black"/>
    <widget position="45,720" name="pic1" zPosition="3" size="1070,50" scale="1" transparent="1" backgroundColor="black"/>
    <widget name="plate0" position="10,10" backgroundColor="#000050ef" size="1140,920" zPosition="1" cornerRadius="30"/>
    <widget name="plate1" position="20,20" backgroundColor="#40000000" size="1120,900" zPosition="2" cornerRadius="30"/>
    <eLabel position="45,40" text="Color selection" font="Regular;32" valign="center" halign="center" size="1070,42" zPosition="3" transparent="1"/>
</screen>"""

About_Foreca4_FHD = """
<screen name="About_Foreca4_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="960,450">
    <widget position="center,100" size="750,42" zPosition="3" font="Regular;32" source="ver" render="Label" transparent="1" valign="center" halign="center"/>
    <eLabel position="280,155" size="400,42" zPosition="3" font="Regular;32" text="Create by @Bauernbub" transparent="1" halign="center" valign="center"/>
    <eLabel position="280,200" size="400,42" zPosition="3" font="Regular;32" text="mod Evg77734, 2025" transparent="1" halign="center" valign="center"/>
    <eLabel position="280,245" size="400,42" zPosition="3" font="Regular;32" text="mod Lululla, 2026" transparent="1" halign="center" valign="center"/>
    <eLabel name="" position="280,290" size="400,42" zPosition="3" font="Regular;32" text="https://gisclub.tv" transparent="1" halign="center" valign="center"/>
    <eLabel name="" position="280,330" size="400,42" zPosition="3" font="Regular;32" text="https://linuxsat-support.com" transparent="1" halign="center" valign="center"/>
    <widget name="plate1" size="930,370" zPosition="2" position="15,15" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="960,400" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
</screen>"""

ExtInfo_Foreca4_FHD = """
<screen name="ExtInfo_Foreca4_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="1380,900">
    <widget position="860,70" size="473,42" zPosition="3" font="Regular;32" source="title1" render="Label" transparent="1" valign="center"/>
    <widget position="30,70" size="800,42" zPosition="3" font="Regular;32" source="title3" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="30,528" size="800,150" zPosition="3" font="Regular;28" source="text2" render="Label" transparent="1"/>
    <widget position="30,125" size="800,150" zPosition="3" font="Regular;28" source="text1" render="Label" transparent="1"/>
    <widget position="30,475" size="800,42" zPosition="3" font="Regular;32" source="title4" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="30,282" size="200,42" zPosition="3" font="Regular;32" source="mo1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="30,427" size="200,42" zPosition="3" font="Regular;32" source="mo1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="30,832" size="200,42" zPosition="3" font="Regular;32" source="mo2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="30,685" size="200,42" zPosition="3" font="Regular;32" source="mo2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="230,282" size="200,42" zPosition="3" font="Regular;32" source="af1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="230,427" size="200,42" zPosition="3" font="Regular;32" source="af1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="230,832" size="200,42" zPosition="3" font="Regular;32" source="af2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="230,685" size="200,42" zPosition="3" font="Regular;32" source="af2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="430,282" size="200,42" zPosition="3" font="Regular;32" source="ev1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="430,427" size="200,42" zPosition="3" font="Regular;32" source="ev1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="430,832" size="200,42" zPosition="3" font="Regular;32" source="ev2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="430,685" size="200,42" zPosition="3" font="Regular;32" source="ev2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="630,282" size="200,42" zPosition="3" font="Regular;32" source="ov1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="630,427" size="200,42" zPosition="3" font="Regular;32" source="ov1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="630,832" size="200,42" zPosition="3" font="Regular;32" source="ov2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="1155,760" size="180,42" zPosition="3" font="Regular;32" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="915,760" size="180,42" zPosition="3" font="Regular;32" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="630,685" size="200,42" zPosition="3" font="Regular;32" source="ov2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="30,20" size="800,42" zPosition="3" font="Regular;32" source="title2" render="Label" transparent="1" valign="center" halign="center"/>
    <widget name="plate1" size="1360,880" zPosition="2" position="10,10" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="1380,900" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="860,125" size="473,578" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5"/>
    <widget name="pic_af1" position="295,340" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_af2" position="295,745" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ev1" position="495,340" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ev2" position="495,745" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ov1" position="695,340" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ov2" position="695,745" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lot" position="1100,760" size="42,42" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lat" position="860,760" size="42,42" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_mo1" position="95,340" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_mo2" position="95,745" size="70,70" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
</screen>"""

ExtInfo_2_Foreca4_FHD = """
<screen name="ExtInfo_2_Foreca4_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="575,860">
    <widget position="50,50" size="473,42" zPosition="3" font="Regular;32" source="title1" render="Label" transparent="1" valign="center"/>
    <widget position="342,760" size="180,42" zPosition="3" font="Regular;32" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="100,760" size="180,42" zPosition="3" font="Regular;32" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget name="plate1" size="555,840" zPosition="2" position="10,10" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="575,860" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="50,125" size="473,578" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5"/>
    <widget name="pic_lot" position="295,760" size="42,42" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lat" position="50,760" size="42,42" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
</screen>"""

Transparency_Foreca4_FHD = """
<screen name="Transparency_Foreca4_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="865,660">
    <widget position="100,50" size="650,42" zPosition="3" font="Regular;32" source="text1" render="Label" transparent="1" valign="center" halign="center"/>
    <widget name="plate1" size="835,630" zPosition="2" position="15,15" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="865,660" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="list" position="100,122" size="650,468" itemHeight="52" valign="center" font="Regular;32" zPosition="3" transparent="1"/>
</screen>"""

Meteogram_Foreca4_FHD = """
<screen name="Meteogram_Foreca4_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="1570,910">
    <widget position="50,50" size="1000,42" zPosition="3" font="Regular;32" source="title1" render="Label" transparent="1" valign="center"/>
    <widget name="plate1" size="1550,890" zPosition="2" position="10,10" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="1570,910" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="50,125" size="1470,735" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5"/>
</screen>"""

ForecaMapsMenu_FHD = """
<screen name="ForecaMapsMenu_FHD" position="center,center" size="1200,900" title="Select Region">
    <widget name="list" position="100,100" size="1000,700" itemHeight="35" font="Regular;32" enableWrapAround="1" scrollbarMode="showOnDemand"/>
</screen>"""

ForecaSlideshow_FHD = """
<screen name="ForecaSlideshow_FHD" position="0,0" size="1920,1080" flags="wfNoBorder">
    <widget name="image" position="0,0" size="1920,1080" zPosition="1" scale="1" />
    <widget name="title" position="50,50" size="1820,60" font="Regular;40" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" valign="center" zPosition="3" />
    <widget name="info" position="50,970" size="1820,40" font="Regular;30" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />

    <!-- Pulsanti Play/Pause -->
    <widget name="pauseButton" position="380,1015" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/pause.png" zPosition="2" />
    <widget name="playButton" position="380,1015" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/play.png" zPosition="2" />
    <!-- Etichette pulsanti colorati -->
    <eLabel position="445,1020" size="40,40" backgroundColor="red" zPosition="3" />
    <eLabel position="690,1020" size="40,40" backgroundColor="green" zPosition="3" />
    <eLabel position="950,1020" size="40,40" backgroundColor="yellow" zPosition="3" />
    <eLabel position="1210,1020" size="40,40" backgroundColor="blue" zPosition="3" />

    <widget name="key_red" position="492,1015" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_green" position="740,1015" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_yellow" position="1001,1015" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_blue" position="1263,1015" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <ePixmap position="1554,1015" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1" zPosition="3" />
    <ePixmap position="1470,1015" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1" zPosition="3" />

</screen>"""

ForecaMapMenu_FHD = """
<screen name="ForecaMapMenu_FHD" position="center,center" size="800,700" title="Foreca Live Maps">
    <widget name="list" position="46,7" size="700,650" itemHeight="35" font="Regular;32" scrollbarMode="showNever"/>
    <widget name="info" position="50,665" size="700,30" font="Regular;24" halign="center"/>
</screen>"""

ForecaMapViewer_FHD = """
<screen name="ForecaMapViewer_FHD" position="center,center" size="1920,1080" flags="wfNoBorder">
    <widget name="map" position="0,0" size="1920,1080" zPosition="1" scale="1" />
    <widget name="title" position="50,5" size="1820,50" font="Regular;40" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" valign="center" zPosition="3" />
    <widget name="time" position="50,1000" size="1820,50" font="Regular;30" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
    <widget name="info" position="50,1050" size="1820,30" font="Regular;24" foregroundColor="#c0c0c0" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
    <widget name="layerinfo" position="60,55" size="1800,40" font="Regular;28" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
</screen>"""

ForecaStations_FHD = """
<screen name="ForecaStations_FHD" position="center,center" size="820,560" title="Station Observations">
    <widget name="list" position="10,10" size="800,180" scrollbarMode="showOnDemand" font="Regular; 30" itemHeight="40" transparent="0"/>
    <widget name="distance" position="10,200" size="800,30" font="Regular;26"/>
    <widget name="details" position="10,240" size="800,280" font="Regular;24"/>
    <widget name="info" position="10,530" size="800,30" font="Regular;24"/>
</screen>"""

CityPanel4_FHD = """
<screen name="CityPanel4_FHD" position="center,center" size="1200,720" title="Select a city">
    <!-- Separator -->
    <eLabel backgroundColor="#fe00" position="10,80" size="1180,2" />
    <eLabel backgroundColor="#fe00" position="10,615" size="1180,2" />
    <!-- City list -->
    <widget name="Mlist" position="21,98" size="1156,511" font="Regular; 30" itemHeight="40" scrollbarMode="showOnDemand" transparent="0" />
    <widget name="description" position="9,619" size="1178,56" zPosition="3" font="Regular;34" foregroundColor="white" backgroundColor="red" transparent="0" valign="center" halign="center" />
    <!-- Button icons -->
    <ePixmap position="100,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png" scale="1" />
    <ePixmap position="180,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png" scale="1" />
    <ePixmap position="260,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png" scale="1" />
    <ePixmap position="340,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_text.png" scale="1" />
    <ePixmap position="420,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/volumeDown.png" scale="1" />
    <ePixmap position="500,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/volumeUp.png" scale="1" />
    <ePixmap position="580,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png" scale="1" />
    <ePixmap position="660,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1" />
    <ePixmap position="740,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1" />
    <ePixmap position="820,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_up.png" scale="1" />
    <ePixmap position="900,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ch+.png" scale="1" />
    <ePixmap position="980,675" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ch-.png" scale="1" />
    <!-- Button widgets with unified colors -->
    <widget source="key_red" render="Label" position="10,5" size="295,70" backgroundColor="key_red" font="Regular;28" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide" />
    </widget>
    <widget source="key_green" render="Label" position="305,5" size="295,70" backgroundColor="key_green" font="Regular;28" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide" />
    </widget>
    <widget source="key_yellow" render="Label" position="600,5" size="295,70" backgroundColor="key_yellow" font="Regular;28" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide" />
    </widget>
    <widget source="key_blue" render="Label" position="895,5" size="295,70" backgroundColor="key_blue" font="Regular;28" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide" />
    </widget>
</screen>
"""
UnitSettingsSimple_FHD = """
<screen name="UnitSettingsSimple_FHD" position="center,center" size="1200,700" title="Unit Settings">
    <widget name="title" position="20,20" size="780,50" font="Regular;32" halign="center" />
    <widget name="info" position="20,90" size="780,40" font="Regular;26" halign="center" />
    <!-- Button widgets with unified colors -->
    <ePixmap name="red" position="25,485" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_red.png" alphatest="on" />
    <ePixmap name="green" position="580,485" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_green.png" alphatest="on" />
    <widget name="key_red" position="80,485" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_green" position="635,485" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" />
    <widget name="option_metric" position="120,180" size="500,50" font="Regular;30" halign="left" />
    <widget name="metric_details" position="150,230" size="470,40" font="Regular;22" halign="left" />
    <widget name="option_imperial" position="120,300" size="500,50" font="Regular;30" halign="left" />
    <widget name="imperial_details" position="150,350" size="470,40" font="Regular;22" halign="left" />
    <widget name="check_metric" position="70,180" size="40,40" alphatest="on" scale="1" />
    <widget name="check_imperial" position="70,300" size="40,40" alphatest="on" scale="1" />
</screen>
"""
DailyForecast_FHD = """
<screen name="DailyForecast_FHD" position="center,center" size="1200,700" title="Weekly Forecast">
    <widget name="title" position="20,20" size="1150,40" font="Regular;32" halign="center" zPosition="3" />
    <widget name="info" position="20,70" size="1150,30" font="Regular;24" halign="center" zPosition="3" />
    <widget name="forecast_text" position="20,110" size="1150,529" font="Regular;26" zPosition="3" />
</screen>
"""
# -----------------------------------------------------------------------

ForecaPreview_4_HD = """
<screen name="ForecaPreview_4_HD" position="0,0" size="1280,720" title="Foreca Weather Preview" flags="wfNoBorder" backgroundColor="transparent">
    <ePixmap name="" position="137,93" size="267,57" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/forecalogo.png" zPosition="3" scale="1" transparent="1"/>
    <widget source="mytitel2" render="Label" position="163,670" size="200,29" font="Regular;21" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
    <widget source="mytitel1" render="Label" position="20,17" size="500,37" font="Regular;23" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
    <widget source="Titel" render="Label" position="565,17" size="657,37" font="Regular;23" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
    <widget source="Titel2" render="Label" position="932,17" size="657,37" font="Regular;23" foregroundColor="black" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="right"/>
    <widget name="town" position="103,173" size="333,27" zPosition="3" font="Regular;19" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="cur_temp" position="40,262" size="133,47" zPosition="3" font="Regular;33" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="fl_temp" position="27,383" size="200,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="pressure_pic" position="247,463" size="32,32" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="rain_mm_pic" position="75,463" size="32,32" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="hum_pic" position="443,463" size="32,32" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="description_w" position="27,340" size="487,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="dewpoint" position="27,420" size="200,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="pic" position="237,247" size="67,67" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="sun" position="197,551" size="133,42" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="wind" position="395,257" size="27,27" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="wind_speed" position="293,383" size="220,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="wind_gust" position="293,420" size="220,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="rain_mm" position="33,510" size="113,27" zPosition="3" font="Regular;17" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="hum" position="407,510" size="107,27" zPosition="3" font="Regular;17" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="pressure" position="180,510" size="167,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="day_len" position="180,600" size="167,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunrise_text" position="33,600" size="113,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunrise_val" position="33,567" size="113,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunset_text" position="380,600" size="107,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunset_val" position="380,567" size="107,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <ePixmap name="" position="28,210" size="32,32" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/observation.png" zPosition="3" scale="1" transparent="1"/>
    <widget name="station" position="60,210" size="320,32" font="Regular; 16" halign="left" backgroundColor="black" transparent="1" valign="center" zPosition="3"/>
    <eLabel position="399,210" size="19,19" transparent="1" backgroundColor="#000080" text="N" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center"/>
    <eLabel position="399,314" size="19,19" transparent="1" backgroundColor="#000080" text="S" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center"/>
    <eLabel position="449,261" size="19,19" transparent="1" backgroundColor="#000080" text="E" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center"/>
    <eLabel position="349,261" size="19,19" transparent="1" backgroundColor="#000080" text="W" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center"/>
    <ePixmap position="75,676" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png" scale="1" zPosition="3"/>
    <ePixmap position="115,676" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png" scale="1" zPosition="3"/>
    <ePixmap position="370,676" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png" scale="1" zPosition="3"/>
    <ePixmap position="410,676" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_help.png" scale="1" zPosition="3"/>
    <!--
    <eLabel name="new eLabel" position="370,670" size="73,29" transparent="1" backgroundColor="black" text=" Help " foregroundColor="white" font="Regular;21" zPosition="3" borderColor="black" valign="center"/>
    <eLabel name="new eLabel2" position="20,670" size="47,29" transparent="1" backgroundColor="black" text="Ok" foregroundColor="white" font="Regular;21" zPosition="3" borderColor="black" valign="center"/>
    <eLabel name="new eLabel3" position="67,670" size="100,29" transparent="1" backgroundColor="#000080" text="Ext info" foregroundColor="#0053a9ff" font="Regular;21" zPosition="3" valign="center"/>
    <eLabel name="new eLabel" position="443,670" size="80,29" transparent="1" backgroundColor="#000080" text="Help+" foregroundColor="#0053a9ff" font="Regular;21" zPosition="3" valign="center"/>
    -->
    <widget name="plate1" zPosition="1" size="733,640" position="540,73" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate11" size="720,627" zPosition="2" position="547,80" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate2" size="527,573" zPosition="1" position="7,73" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate22" size="513,560" zPosition="2" position="13,80" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate3" size="527,60" zPosition="1" position="7,653" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate33" size="513,47" zPosition="2" position="13,660" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate4" size="733,60" zPosition="1" position="540,7" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate5" size="527,60" zPosition="1" position="7,7" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate44" size="720,47" zPosition="2" position="547,13" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate55" size="513,47" zPosition="2" position="13,13" backgroundColor="#40000000" cornerRadius="50"/>
    <widget source="menu" render="Listbox" position="555,95" size="703,590" scrollbarMode="showOnDemand" zPosition="3" transparent="1" backgroundColor="black">
        <convert type="TemplatedMultiContent">
      {"template": [
          MultiContentEntryText(pos = (27, 33), size = (60, 20), font=0, flags = RT_HALIGN_LEFT, text = 0),
          MultiContentEntryText(pos = (180, 13), size = (80, 20), font=0, flags = RT_HALIGN_LEFT, text = 1),
          MultiContentEntryPixmapAlphaTest(pos = (103, 16), size = (47, 47), png = 2, flags=BT_SCALE),
          MultiContentEntryText(pos = (180, 43), size = (80, 20), font=0, flags = RT_HALIGN_LEFT, text = 3),
          MultiContentEntryPixmapAlphaTest(pos = (260, 27), size = (18, 19), png = 4, flags=BT_SCALE),
          MultiContentEntryText(pos = (303, 13), size = (80, 20), font=0, flags = RT_HALIGN_LEFT, text = 5),
          MultiContentEntryText(pos = (303, 43), size = (80, 20), font=0, flags = RT_HALIGN_LEFT, text = 6),
          MultiContentEntryText(pos = (387, 1), size = (313, 20), font=0, flags = RT_HALIGN_LEFT, text = 7),
          MultiContentEntryText(pos = (387, 21), size = (313, 16), font=1, flags = RT_HALIGN_LEFT, text = 8),
          MultiContentEntryText(pos = (387, 37), size = (313, 16), font=1, flags = RT_HALIGN_LEFT, text = 9),
          MultiContentEntryText(pos = (387, 54), size = (313, 16), font=1, flags = RT_HALIGN_LEFT, text = 10),
          ],
      "fonts": [gFont("Regular", 17),gFont("Regular", 13)],
      "itemHeight": 73
      }
                  </convert>
    </widget>
</screen>"""

ColorSelect_HD = """
<screen name="ColorSelect_HD" position="center,center" backgroundColor="transparent" size="773,627" flags="wfNoBorder">
    <widget name="Clist" itemHeight="35" position="30,70" size="713,397" enableWrapAround="1" scrollbarMode="showOnDemand" valign="center" font="Console;19" transparent="1" backgroundColor="black" zPosition="3"/>
    <widget name="colordatas" position="30,567" size="713,28" font="Regular;21" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black"/>
    <widget name="colorname" position="30,527" size="713,28" font="Regular;21" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black"/>
    <widget position="30,480" name="pic1" zPosition="3" size="713,33" scale="1" transparent="1" backgroundColor="black"/>
    <widget name="plate0" position="7,7" backgroundColor="#000050ef" size="760,613" zPosition="1" cornerRadius="30"/>
    <widget name="plate1" position="13,13" backgroundColor="#40000000" size="747,600" zPosition="2" cornerRadius="30"/>
    <eLabel position="30,27" text="Color selection" font="Regular;21" valign="center" halign="center" size="713,28" zPosition="3" transparent="1"/>
</screen>"""

About_Foreca4_HD = """
<screen name="About_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="640,267">
    <widget position="70,22" size="500,28" zPosition="3" font="Regular;21" source="ver" render="Label" transparent="1" valign="center" halign="center"/>
    <eLabel position="120,50" size="400,42" zPosition="3" font="Regular;21" text="Create by @Bauernbub" transparent="1" halign="center" valign="center"/>
    <eLabel position="120,90" size="400,42" zPosition="3" font="Regular;21" text="mod Evg77734, 2025" transparent="1" halign="center" valign="center"/>
    <eLabel position="120,130" size="400,42" zPosition="3" font="Regular;21" text="mod Lululla, 2026" transparent="1" halign="center" valign="center"/>
    <eLabel name="" position="120,170" size="400,42" zPosition="3" font="Regular;21" text="https://gisclub.tv" transparent="1" halign="center" valign="center"/>
    <eLabel name="" position="120,210" size="400,42" zPosition="3" font="Regular;21" text="https://linuxsat-support.com" transparent="1" halign="center" valign="center"/>
    <widget name="plate1" size="620,247" zPosition="2" position="10,10" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="640,267" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
</screen>"""

ExtInfo_Foreca4_HD = """
<screen name="ExtInfo_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="920,600">
    <widget position="573,47" size="315,28" zPosition="3" font="Regular;21" source="title1" render="Label" transparent="1" valign="center"/>
    <widget position="20,47" size="533,28" zPosition="3" font="Regular;21" source="title3" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="20,352" size="533,100" zPosition="3" font="Regular;19" source="text2" render="Label" transparent="1"/>
    <widget position="20,83" size="533,100" zPosition="3" font="Regular;19" source="text1" render="Label" transparent="1"/>
    <widget position="20,317" size="533,28" zPosition="3" font="Regular;21" source="title4" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="20,188" size="133,28" zPosition="3" font="Regular;21" source="mo1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="20,285" size="133,28" zPosition="3" font="Regular;21" source="mo1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="20,555" size="133,28" zPosition="3" font="Regular;21" source="mo2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="20,457" size="133,28" zPosition="3" font="Regular;21" source="mo2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="153,188" size="133,28" zPosition="3" font="Regular;21" source="af1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="153,285" size="133,28" zPosition="3" font="Regular;21" source="af1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="153,555" size="133,28" zPosition="3" font="Regular;21" source="af2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="153,457" size="133,28" zPosition="3" font="Regular;21" source="af2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="287,188" size="133,28" zPosition="3" font="Regular;21" source="ev1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="287,285" size="133,28" zPosition="3" font="Regular;21" source="ev1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="287,555" size="133,28" zPosition="3" font="Regular;21" source="ev2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="287,457" size="133,28" zPosition="3" font="Regular;21" source="ev2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="420,188" size="133,28" zPosition="3" font="Regular;21" source="ov1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="420,285" size="133,28" zPosition="3" font="Regular;21" source="ov1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="420,555" size="133,28" zPosition="3" font="Regular;21" source="ov2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="770,507" size="120,28" zPosition="3" font="Regular;21" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="610,507" size="120,28" zPosition="3" font="Regular;21" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="420,457" size="133,28" zPosition="3" font="Regular;21" source="ov2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="20,13" size="533,28" zPosition="3" font="Regular;21" source="title2" render="Label" transparent="1" valign="center" halign="center"/>
    <widget name="plate1" size="907,587" zPosition="2" position="7,7" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="920,600" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="573,83" size="315,385" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5"/>
    <widget name="pic_af1" position="197,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_af2" position="197,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ev1" position="330,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ev2" position="330,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ov1" position="463,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ov2" position="463,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lot" position="733,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lat" position="573,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_mo1" position="63,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_mo2" position="63,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
</screen>"""

ExtInfo_2_Foreca4_HD = """
<screen name="ExtInfo_2_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="383,573">
    <widget position="33,33" size="315,28" zPosition="3" font="Regular;21" source="title1" render="Label" transparent="1" valign="center"/>
    <widget position="228,507" size="120,28" zPosition="3" font="Regular;21" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="67,507" size="120,28" zPosition="3" font="Regular;21" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget name="plate1" size="370,560" zPosition="2" position="7,7" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="383,573" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="33,83" size="315,385" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5"/>
    <widget name="pic_lot" position="197,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lat" position="33,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
</screen>"""

Transparency_Foreca4_HD = """
<screen name="Transparency_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="577,440">
    <widget position="67,33" size="433,28" zPosition="3" font="Regular;21" source="text1" render="Label" transparent="1" valign="center" halign="center"/>
    <widget name="plate1" size="557,420" zPosition="2" position="10,10" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="577,440" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="list" position="67,81" size="433,312" itemHeight="52" valign="center" font="Regular;21" zPosition="3" transparent="1"/>
</screen>"""

Meteogram_Foreca4_HD = """
<screen name="Meteogram_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="1047,607">
    <widget position="33,33" size="667,28" zPosition="3" font="Regular;21" source="title1" render="Label" transparent="1" valign="center"/>
    <widget name="plate1" size="1033,593" zPosition="2" position="7,7" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="1047,607" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="33,83" size="980,490" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5"/>
</screen>"""

ForecaSlideshow_HD = """
<screen name="ForecaSlideshow_HD" position="0,0" size="1280,720" flags="wfNoBorder">
    <widget name="image" position="0,0" size="1280,720" zPosition="1" />
    <widget name="title" position="30,30" size="1220,40" font="Regular;28" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" valign="center" zPosition="3" />
    <widget name="info" position="30,625" size="1220,30" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
    <!-- Pulsanti Play/Pause -->
    <widget name="pauseButton" position="50,660" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/pause.png" zPosition="2" />
    <widget name="playButton" position="50,660" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/play.png" zPosition="2" />
    <!-- Etichette pulsanti colorati -->
    <eLabel position="110,665" size="40,40" backgroundColor="red" zPosition="3" />
    <eLabel position="362,665" size="40,40" backgroundColor="green" zPosition="3" />
    <eLabel position="616,665" size="40,40" backgroundColor="yellow" zPosition="3" />
    <eLabel position="864,665" size="40,40" backgroundColor="blue" zPosition="3" />

    <widget name="key_red" position="160,660" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_green" position="413,660" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_yellow" position="666,660" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_blue" position="915,660" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <ePixmap position="1186,665" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1" zPosition="3" />
    <ePixmap position="1100,665" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1" zPosition="3" />
</screen>"""

ForecaMapsMenu_HD = """
<screen name="ForecaMapsMenu_HD" position="center,center" size="800,600" title="Select Region">
    <widget name="list" position="50,50" size="700,500" itemHeight="35" font="Regular;24" enableWrapAround="1" scrollbarMode="showOnDemand"/>
</screen>"""

ForecaMapMenu_HD = """
<screen name="ForecaMapMenu_HD" position="center,center" size="800,700" title="Foreca Live Maps">
    <widget name="list" position="46,7" size="700,650" itemHeight="35" font="Regular;32" scrollbarMode="showNever"/>
    <widget name="info" position="50,665" size="700,30" font="Regular;24" halign="center"/>
</screen>"""

ForecaMapViewer_HD = """
<screen name="ForecaMapViewer_HD" position="center,center" size="1280,720" flags="wfNoBorder">
    <widget name="map" position="0,0" size="1280,720" zPosition="1" />
    <widget name="title" position="30,10" size="1220,35" font="Regular;28" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" valign="center" zPosition="3" />
    <widget name="time" position="30,665" size="1220,30" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
    <widget name="info" position="30,695" size="1220,20" font="Regular;20" foregroundColor="#c0c0c0" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
    <widget name="layerinfo" position="29,50" size="1220,40" font="Regular;24" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
</screen>"""

ForecaStations_HD = """
<screen name="ForecaStations_HD" position="center,center" size="620,460" title="Station Observations">
    <widget name="list" position="10,10" size="600,150" scrollbarMode="showOnDemand" font="Regular; 24" itemHeight="35" transparent="0"/>
    <widget name="distance" position="10,170" size="600,25" font="Regular;22"/>
    <widget name="details" position="10,200" size="600,230" font="Regular;22"/>
    <widget name="info" position="10,440" size="600,20" font="Regular;22"/>
</screen>"""

CityPanel4_HD = """
<screen name="CityPanel4_HD" position="560,240" size="800,600" title="Select a city">
    <!-- Separator -->
    <eLabel backgroundColor="#fe00" position="5,53" size="785,1"/>
    <eLabel backgroundColor="#fe00" position="5,513" size="785,1"/>
    <!-- City list -->
    <widget name="Mlist" position="6,60" size="786,443" font="Regular;24" itemHeight="30" enableWrapAround="1" scrollbarMode="showOnDemand" transparent="0"/>
    <widget name="description" position="5,517" size="787,35" zPosition="3" font="Regular; 22" foregroundColor="white" backgroundColor="red" transparent="0" valign="center" halign="center"/>
    <!-- Button icons -->
    <ePixmap position="140,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png" scale="1"/>
    <ePixmap position="180,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png" scale="1"/>
    <ePixmap position="220,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png" scale="1"/>
    <ePixmap position="260,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_text.png" scale="1"/>
    <ePixmap position="300,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/volumeDown.png" scale="1"/>
    <ePixmap position="340,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/volumeUp.png" scale="1"/>
    <ePixmap position="380,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png" scale="1"/>
    <ePixmap position="420,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1"/>
    <ePixmap position="460,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1"/>
    <ePixmap position="500,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_up.png" scale="1"/>
    <ePixmap position="540,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ch+.png" scale="1"/>
    <ePixmap position="580,576" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ch+.png" scale="1"/>
    <!-- Button widgets with unified colors -->
    <widget source="key_red" render="Label" position="6,3" size="196,46" backgroundColor="key_red" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
    <widget source="key_green" render="Label" position="203,3" size="196,46" backgroundColor="key_green" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
    <widget source="key_yellow" render="Label" position="400,3" size="196,46" backgroundColor="key_yellow" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
    <widget source="key_blue" render="Label" position="596,3" size="196,46" backgroundColor="key_blue" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
</screen>"""
# UnitSettingsSimple
UnitSettingsSimple_HD = """
<screen name="UnitSettingsSimple_HD" position="center,center" size="620,450" title="Unit Settings">
    <widget name="title" position="16,15" size="580,40" font="Regular;28" halign="center" />
    <widget name="info" position="20,70" size="580,30" font="Regular;22" halign="center" />
    <!-- Button widgets with unified colors -->
    <ePixmap name="red" position="35,390" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_red.png" alphatest="on" />
    <ePixmap name="green" position="389,390" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_green.png" alphatest="on" />
    <widget name="key_red" position="88,390" size="150,50" font="Regular;24" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_green" position="439,390" size="150,50" font="Regular;24" halign="left" valign="center" backgroundColor="black" transparent="1" />
    <widget name="option_metric" position="100,150" size="400,40" font="Regular;26" halign="left" />
    <widget name="metric_details" position="120,190" size="380,30" font="Regular;20" halign="left" />
    <widget name="option_imperial" position="100,250" size="400,40" font="Regular;26" halign="left" />
    <widget name="imperial_details" position="120,290" size="380,30" font="Regular;20" halign="left" />
    <widget name="check_metric" position="60,150" size="32,32" alphatest="on" scale="1" />
    <widget name="check_imperial" position="60,250" size="32,32" alphatest="on" scale="1" />
</screen>
"""

DailyForecast_HD = """
<screen name="DailyForecast_HD" position="center,center" size="800,600" title="Weekly Forecast">
    <widget name="title" position="20,20" size="760,40" font="Regular;28" halign="center" zPosition="3" />
    <widget name="info" position="20,70" size="760,30" font="Regular;22" halign="center" zPosition="3" />
    <widget name="forecast_text" position="20,110" size="760,440" font="Regular;22" zPosition="3" />
    <ePixmap position="380,566" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png" scale="1" zPosition="3" />
    <ePixmap position="420,566" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1" zPosition="3" />
    <ePixmap position="460,566" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1" zPosition="3" />
    <ePixmap position="500,566" size="40,20" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_up.png" scale="1" zPosition="3" />
</screen>
"""

# -----------------------------------------------------------------------

ForecaPreview_4_UHD = """
<screen name="ForecaPreview_4_UHD" position="0,0" size="2560,1440" title="Foreca Weather Preview" flags="wfNoBorder" backgroundColor="transparent">
    <ePixmap name="" position="274,187" size="534,115" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/forecalogo.png" zPosition="3" scale="1" transparent="1"/>
    <widget source="mytitel2" render="Label" position="312,1340" size="420,58" font="Regular;43" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
    <widget source="mytitel1" render="Label" position="40,35" size="1000,75" font="Regular;46" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
    <widget source="Titel" render="Label" position="1131,35" size="1314,75" font="Regular;46" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
    <widget source="Titel2" render="Label" position="1864,35" size="1314,75" font="Regular;46" foregroundColor="black" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="right"/>
    <widget name="town" position="207,362" size="667,54" zPosition="3" font="Regular;38" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="cur_temp" position="80,494" size="267,94" zPosition="3" font="Regular;67" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="fl_temp" position="54,767" size="400,54" zPosition="3" font="Regular;32" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="pressure_pic" position="495,927" size="64,64" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="rain_mm_pic" position="150,927" size="64,64" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="hum_pic" position="887,927" size="64,64" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="description_w" position="54,680" size="974,54" zPosition="3" font="Regular;32" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="dewpoint" position="54,840" size="400,54" zPosition="3" font="Regular;32" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="pic" position="474,474" size="134,134" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="sun" position="394,1103" size="267,84" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="wind" position="790,514" size="54,55" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="wind_speed" position="587,767" size="440,54" zPosition="3" font="Regular;32" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="wind_gust" position="587,840" size="440,54" zPosition="3" font="Regular;32" backgroundColor="black" transparent="1" valign="center"/>
    <widget name="rain_mm" position="67,1020" size="227,54" zPosition="3" font="Regular;35" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="hum" position="814,1020" size="214,54" zPosition="3" font="Regular;35" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="pressure" position="360,1020" size="334,54" zPosition="3" font="Regular;32" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="day_len" position="360,1200" size="334,51" zPosition="3" font="Regular;30" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunrise_text" position="67,1200" size="227,51" zPosition="3" font="Regular;30" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunrise_val" position="67,1134" size="227,51" zPosition="3" font="Regular;30" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunset_text" position="760,1200" size="214,51" zPosition="3" font="Regular;30" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <widget name="sunset_val" position="760,1134" size="214,51" zPosition="3" font="Regular;30" backgroundColor="black" transparent="1" valign="center" halign="center"/>
    <eLabel position="798,420" size="38,38" transparent="1" backgroundColor="#000080" text="N" foregroundColor="#0053a9ff" font="Regular;24" zPosition="3" halign="center" valign="center"/>
    <eLabel position="798,628" size="38,38" transparent="1" backgroundColor="#000080" text="S" foregroundColor="#0053a9ff" font="Regular;24" zPosition="3" halign="center" valign="center"/>
    <eLabel position="898,522" size="38,38" transparent="1" backgroundColor="#000080" text="E" foregroundColor="#0053a9ff" font="Regular;24" zPosition="3" halign="center" valign="center"/>
    <eLabel position="698,522" size="38,38" transparent="1" backgroundColor="#000080" text="W" foregroundColor="#0053a9ff" font="Regular;24" zPosition="3" halign="center" valign="center"/>
    <ePixmap name="" position="53,613" size="52,52" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/observation.png" zPosition="3" scale="1" transparent="1"/>
    <widget name="station" position="109,614" size="650,52" font="Regular; 26" halign="left" backgroundColor="black" transparent="1" valign="center" zPosition="3"/>
    <ePixmap position="100,1342" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png" scale="1" zPosition="3"/>
    <ePixmap position="200,1342" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png" scale="1" zPosition="3"/>
    <ePixmap position="750,1342" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png" scale="1" zPosition="3"/>
    <ePixmap position="850,1342" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_hep.png" scale="1" zPosition="32"/>
    <!--
    <eLabel name="new eLabel3" position="134,1340" size="200,58" transparent="1" backgroundColor="#000080" text="Ext info" foregroundColor="#0053a9ff" font="Regular;43" zPosition="3" valign="center"/>
    <eLabel name="new eLabel" position="887,1340" size="160,58" transparent="1" backgroundColor="#000080" text="Help+" foregroundColor="#0053a9ff" font="Regular;43" zPosition="3" valign="center"/>
    <eLabel name="new eLabel" position="740,1340" size="147,58" transparent="1" backgroundColor="black" text=" Help " foregroundColor="white" font="Regular;43" zPosition="3" borderColor="black" valign="center"/>
    <eLabel name="new eLabel2" position="40,1340" size="94,58" transparent="1" backgroundColor="black" text="Ok" foregroundColor="white" font="Regular;43" zPosition="3" borderColor="black" valign="center"/>
    -->
    <widget name="plate1" zPosition="1" size="1467,1280" position="1080,147" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate11" size="1440,1254" zPosition="2" position="1094,160" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate2" size="1054,1147" zPosition="1" position="14,147" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate22" size="1027,1120" zPosition="2" position="27,160" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate3" size="1054,120" zPosition="1" position="14,1307" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate33" size="1027,94" zPosition="2" position="27,1320" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate4" size="1467,120" zPosition="1" position="1080,14" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate5" size="1054,120" zPosition="1" position="14,14" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="plate44" size="1440,94" zPosition="2" position="1094,27" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate55" size="1027,94" zPosition="2" position="27,27" backgroundColor="#40000000" cornerRadius="50"/>
    <widget source="menu" render="Listbox" position="1111,191" size="1407,1180" scrollbarMode="showOnDemand" zPosition="3" transparent="1" backgroundColor="black">
        <convert type="TemplatedMultiContent">
      {"template": [
          MultiContentEntryText(pos = (54, 66), size = (120, 40), font=0, flags = RT_HALIGN_LEFT, text = 0),
          MultiContentEntryText(pos = (360, 27), size = (160, 40), font=0, flags = RT_HALIGN_LEFT, text = 1),
          MultiContentEntryPixmapAlphaTest(pos = (207, 32), size = (94, 94), png = 2),
          MultiContentEntryText(pos = (360, 86), size = (160, 40), font=0, flags = RT_HALIGN_LEFT, text = 3),
          MultiContentEntryPixmapAlphaTest(pos = (520, 55), size = (36, 38), png = 4),
          MultiContentEntryText(pos = (607, 27), size = (160, 40), font=0, flags = RT_HALIGN_LEFT, text = 5),
          MultiContentEntryText(pos = (607, 86), size = (160, 40), font=0, flags = RT_HALIGN_LEFT, text = 6),
          MultiContentEntryText(pos = (774, 2), size = (627, 40), font=0, flags = RT_HALIGN_LEFT, text = 7),
          MultiContentEntryText(pos = (774, 42), size = (627, 32), font=1, flags = RT_HALIGN_LEFT, text = 8),
          MultiContentEntryText(pos = (774, 75), size = (627, 32), font=1, flags = RT_HALIGN_LEFT, text = 9),
          MultiContentEntryText(pos = (774, 108), size = (627, 32), font=1, flags = RT_HALIGN_LEFT, text = 10),
          ],
      "fonts": [gFont("Regular", 35),gFont("Regular", 27)],
      "itemHeight": 147
      }
                  </convert>
    </widget>
</screen>"""

ColorSelect_UHD = """
<screen name="ColorSelect_UHD" position="center,center" backgroundColor="transparent" size="1547,1254" flags="wfNoBorder">
    <widget name="Clist" itemHeight="47" position="60,140" size="1427,795" enableWrapAround="1" scrollbarMode="showOnDemand" valign="center" font="Console;38" transparent="1" backgroundColor="black" zPosition="3"/>
    <widget name="colordatas" position="60,1134" size="1427,56" font="Regular;43" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black"/>
    <widget name="colorname" position="60,1054" size="1427,56" font="Regular;43" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black"/>
    <widget position="60,960" name="pic1" zPosition="3" size="1427,67" scale="1" transparent="1" backgroundColor="black"/>
    <widget name="plate0" position="14,14" backgroundColor="#000050ef" size="1520,1227" zPosition="1" cornerRadius="30"/>
    <widget name="plate1" position="27,27" backgroundColor="#40000000" size="1494,1200" zPosition="2" cornerRadius="30"/>
    <eLabel position="60,54" text="Color selection" font="Regular;43" valign="center" halign="center" size="1427,56" zPosition="3" transparent="1"/>
</screen>"""

About_Foreca4_UHD = """
<screen name="About_Foreca4_UHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="1280,534">
    <widget position="140,54" size="1000,56" zPosition="3" font="Regular;43" source="ver" render="Label" transparent="1" valign="center" halign="center"/>
    <eLabel position="330,120" size="600,42" zPosition="3" font="Regular;43" text="Create by @Bauernbub" transparent="1" halign="center" valign="center"/>
    <eLabel position="330,175" size="600,42" zPosition="3" font="Regular;43" text="mod Evg77734, 2025" transparent="1" halign="center" valign="center"/>
    <eLabel position="330,220" size="600,42" zPosition="3" font="Regular;43" text="mod Lululla, 2026" transparent="1" halign="center" valign="center"/>
    <eLabel name="" position="330,281" size="600,42" zPosition="3" font="Regular;43" text="https://gisclub.tv" transparent="1" halign="center" valign="center"/>
    <eLabel name="" position="330,330" size="600,50" zPosition="3" font="Regular;43" text="https://linuxsat-support.com" transparent="1" halign="center" valign="center"/>
    <widget name="plate1" size="1240,494" zPosition="2" position="20,20" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="1280,534" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
</screen>"""

ExtInfo_Foreca4_UHD = """
<screen name="ExtInfo_Foreca4_UHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="1840,1200">
    <widget position="1147,94" size="631,56" zPosition="3" font="Regular;43" source="title1" render="Label" transparent="1" valign="center"/>
    <widget position="40,94" size="1067,56" zPosition="3" font="Regular;43" source="title3" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="40,704" size="1067,200" zPosition="3" font="Regular;38" source="text2" render="Label" transparent="1"/>
    <widget position="40,167" size="1067,200" zPosition="3" font="Regular;38" source="text1" render="Label" transparent="1"/>
    <widget position="40,634" size="1067,56" zPosition="3" font="Regular;43" source="title4" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="40,376" size="267,56" zPosition="3" font="Regular;43" source="mo1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="40,570" size="267,56" zPosition="3" font="Regular;43" source="mo1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="40,1110" size="267,56" zPosition="3" font="Regular;43" source="mo2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="40,914" size="267,56" zPosition="3" font="Regular;43" source="mo2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="307,376" size="267,56" zPosition="3" font="Regular;43" source="af1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="307,570" size="267,56" zPosition="3" font="Regular;43" source="af1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="307,1110" size="267,56" zPosition="3" font="Regular;43" source="af2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="307,914" size="267,56" zPosition="3" font="Regular;43" source="af2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="574,376" size="267,56" zPosition="3" font="Regular;43" source="ev1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="574,570" size="267,56" zPosition="3" font="Regular;43" source="ev1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="574,1110" size="267,56" zPosition="3" font="Regular;43" source="ev2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="574,914" size="267,56" zPosition="3" font="Regular;43" source="ev2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="840,376" size="267,56" zPosition="3" font="Regular;43" source="ov1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="840,570" size="267,56" zPosition="3" font="Regular;43" source="ov1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="840,1110" size="267,56" zPosition="3" font="Regular;43" source="ov2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="1540,1014" size="240,56" zPosition="3" font="Regular;43" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="1220,1014" size="240,56" zPosition="3" font="Regular;43" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="840,914" size="267,56" zPosition="3" font="Regular;43" source="ov2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center"/>
    <widget position="40,27" size="1067,56" zPosition="3" font="Regular;43" source="title2" render="Label" transparent="1" valign="center" halign="center"/>
    <widget name="plate1" size="1814,1174" zPosition="2" position="14,14" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="1840,1200" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="1147,167" size="631,771" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="7"/>
    <widget name="pic_af1" position="394,454" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_af2" position="394,994" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ev1" position="660,454" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ev2" position="660,994" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ov1" position="927,454" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_ov2" position="927,994" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lot" position="1467,1014" size="56,56" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lat" position="1147,1014" size="56,56" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_mo1" position="127,454" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_mo2" position="127,994" size="94,94" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
</screen>"""

ExtInfo_2_Foreca4_UHD = """
<screen name="ExtInfo_2_Foreca4_UHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="767,1147">
    <widget position="67,67" size="631,56" zPosition="3" font="Regular;43" source="title1" render="Label" transparent="1" valign="center"/>
    <widget position="456,1014" size="240,56" zPosition="3" font="Regular;43" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget position="134,1014" size="240,56" zPosition="3" font="Regular;43" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff"/>
    <widget name="plate1" size="740,1120" zPosition="2" position="14,14" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="767,1147" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="67,167" size="631,771" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="7"/>
    <widget name="pic_lot" position="394,1014" size="56,56" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
    <widget name="pic_lat" position="67,1014" size="56,56" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
</screen>"""

Transparency_Foreca4_UHD = """
<screen name="Transparency_Foreca4_UHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="1154,880">
    <widget position="134,67" size="867,56" zPosition="3" font="Regular;43" source="text1" render="Label" transparent="1" valign="center" halign="center"/>
    <widget name="plate1" size="1114,840" zPosition="2" position="20,20" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="1154,880" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="list" position="134,163" size="867,624" itemHeight="70" valign="center" font="Regular;43" zPosition="3" transparent="1"/>
</screen>"""

Meteogram_Foreca4_UHD = """
<screen name="Meteogram_Foreca4_UHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="2094,1214">
    <widget position="67,67" size="1334,56" zPosition="3" font="Regular;43" source="title1" render="Label" transparent="1" valign="center"/>
    <widget name="plate1" size="2067,1187" zPosition="2" position="14,14" backgroundColor="#40000000" cornerRadius="50"/>
    <widget name="plate0" size="2094,1214" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50"/>
    <widget name="pic" position="67,167" size="1960,980" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="7"/>
</screen>"""

ForecaPreview_4_UHD = """
<screen name="ForecaPreview_4_UHD" position="center,center" size="1600,1200" title="Select Region">
    <widget name="list" position="134,134" size="1334,934" itemHeight="47" font="Regular;43" enableWrapAround="1" scrollbarMode="showOnDemand"/>
</screen>
"""

ForecaMapsMenu_UHD = """
<screen name="ForecaMapsMenu_UHD" position="center,center" size="1600,1200" title="Select Region">
    <widget name="list" position="134,134" size="1334,934" itemHeight="47" font="Regular;43" enableWrapAround="1" scrollbarMode="showOnDemand"/>
</screen>"""

ForecaSlideshow_UHD = """
<screen name="ForecaSlideshow_FHD" position="0,0" size="1840,1200" flags="wfNoBorder">
    <widget name="image" position="0,0" size="1840,1200" zPosition="1" scale="1" />
    <widget name="title" position="50,50" size="1820,60" font="Regular; 42" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" valign="center" zPosition="3" />
    <widget name="info" position="50,1020" size="1820,40" font="Regular;30" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" cornerRadius="0" zPosition="3" />
    <!-- Pulsanti Play/Pause -->
    <widget name="pauseButton" position="380,1090" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/pause.png" zPosition="2" />
    <widget name="playButton" position="380,1090" size="50,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/play.png" zPosition="2" />
    <!-- Etichette pulsanti colorati -->
    <eLabel position="445,1095" size="40,40" backgroundColor="red" zPosition="3" />
    <eLabel position="690,1095" size="40,40" backgroundColor="green" zPosition="3" />
    <eLabel position="950,1095" size="40,40" backgroundColor="yellow" zPosition="3" />
    <eLabel position="1210,1095" size="40,40" backgroundColor="blue" zPosition="3" />

    <widget name="key_red" position="492,1090" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_green" position="740,1090" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_yellow" position="1001,1090" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_blue" position="1263,1090" size="180,50" font="Regular;26" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <ePixmap position="1554,1095" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1" zPosition="3" />
    <ePixmap position="1470,1095" size="80,40" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1" zPosition="3" />
</screen>"""

ForecaMapMenu_UHD = """
<screen name="ForecaMapMenu_UHD" position="center,center" size="1067,934" title="Foreca Live Maps">
    <widget name="list" position="62,10" size="934,867" itemHeight="47" font="Regular;43" scrollbarMode="showNever"/>
    <widget name="info" position="67,887" size="934,40" font="Regular;32" halign="center"/>
</screen>"""

ForecaMapViewer_UHD = """
<screen name="ForecaMapViewer_UHD" position="center,center" size="2560,1440" flags="wfNoBorder">
    <widget name="map" position="0,0" size="2560,1440" zPosition="1" scale="1" />
    <widget name="title" position="67,15" size="2427,67" font="Regular;54" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" valign="center" zPosition="3" />
    <widget name="time" position="67,1334" size="2427,67" font="Regular;40" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
    <widget name="info" position="67,1400" size="2427,40" font="Regular;32" foregroundColor="#c0c0c0" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
    <widget name="layerinfo" position="66,83" size="2427,60" font="Regular;40" foregroundColor="#ffffff" backgroundColor="#40000000" transparent="1" halign="center" zPosition="3" />
</screen>"""

ForecaStations_UHD = """
<screen name="ForecaStations_UHD" position="center,center" size="1200,800" title="Station Observations">
    <widget name="list" position="20,20" size="1160,220" scrollbarMode="showOnDemand" font="Regular; 34" itemHeight="40" transparent="0"/>
    <widget name="distance" position="20,260" size="1160,40" font="Regular;32"/>
    <widget name="details" position="20,310" size="1160,430" font="Regular;32"/>
    <widget name="info" position="20,760" size="1160,40" font="Regular;30"/>
</screen>"""

CityPanel4_UHD = """
<screen name="CityPanel4_UHD" position="center,center" size="1600,1200" title="Select a city">
    <!-- Separator -->
    <eLabel backgroundColor="#fe00" position="0,107" size="1600,3"/>
    <eLabel backgroundColor="#fe00" position="0,1027" size="1600,3"/>
    <!-- City list -->
    <widget name="Mlist" position="14,120" size="1574,887" font="Regular;32" itemHeight="47" enableWrapAround="1" scrollbarMode="showOnDemand" transparent="0"/>
    <widget name="description" position="14,1060" size="1573,56" zPosition="3" font="Regular; 32" foregroundColor="white" backgroundColor="red" transparent="0" valign="center" halign="center"/>
    <!-- Button icons -->
    <ePixmap position="255,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ok.png" scale="1"/>
    <ePixmap position="355,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_menu.png" scale="1"/>
    <ePixmap position="455,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_info.png" scale="1"/>
    <ePixmap position="555,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_text.png" scale="1"/>
    <ePixmap position="655,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/volumeDown.png" scale="1"/>
    <ePixmap position="755,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/volumeUp.png" scale="1"/>
    <ePixmap position="855,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png" scale="1"/>
    <ePixmap position="955,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1"/>
    <ePixmap position="1055,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1"/>
    <ePixmap position="1155,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_up.png" scale="1"/>
    <ePixmap position="1255,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_ch.png" scale="1"/>
    <!-- Button widgets with unified colors -->
    <widget source="key_red" render="Label" position="14,7" size="394,94" backgroundColor="key_red" font="Regular; 32" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
    <widget source="key_green" render="Label" position="407,7" size="394,94" backgroundColor="key_green" font="Regular; 32" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
    <widget source="key_yellow" render="Label" position="800,7" size="394,94" backgroundColor="key_yellow" font="Regular;20" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
    <widget source="key_blue" render="Label" position="1194,7" size="394,94" backgroundColor="key_blue" font="Regular; 32" foregroundColor="#ffffff" halign="center" valign="center">
        <convert type="ConditionalShowHide"/>
    </widget>
</screen>"""

UnitSettingsSimple_UHD = """
<screen name="UnitSettingsSimple_UHD" position="410,190" size="1100,700" title="Unit Settings">
    <widget name="title" position="20,20" size="1060,70" font="Regular;42" halign="center" />
    <widget name="info" position="20,120" size="1060,50" font="Regular;32" halign="center" />
    <!-- Button widgets with unified colors -->
    <ePixmap name="red" position="45,625" size="60,60" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_red.png" alphatest="on" />
    <ePixmap name="green" position="744,625" size="60,60" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_green.png" alphatest="on" />
    <widget name="key_red" position="108,625" size="250,60" font="Regular;28" halign="left" valign="center" backgroundColor="black" transparent="1" zPosition="3" />
    <widget name="key_green" position="805,625" size="250,60" font="Regular;28" halign="left" valign="center" backgroundColor="black" transparent="1" />
    <widget name="option_metric" position="150,230" size="700,70" font="Regular;38" halign="left" />
    <widget name="metric_details" position="190,300" size="660,50" font="Regular;26" halign="left" />
    <widget name="option_imperial" position="150,380" size="700,70" font="Regular;38" halign="left" />
    <widget name="imperial_details" position="190,450" size="660,50" font="Regular;26" halign="left" />
    <widget name="check_metric" position="90,230" size="50,50" alphatest="on" scale="1" />
    <widget name="check_imperial" position="90,380" size="50,50" alphatest="on" scale="1" />
</screen>
"""

DailyForecast_FHD = """
<screen name="DailyForecast_FHD" position="center,center" size="1840,1200" title="Weekly Forecast">
    <widget name="title" position="17,20" size="1800,40" font="Regular; 38" halign="center" zPosition="3" />
    <widget name="info" position="20,68" size="1800,40" font="Regular; 32" halign="center" zPosition="3" />
    <widget name="forecast_text" position="20,110" size="1800,1005" font="Regular;26" zPosition="3" />
    <ePixmap position="855,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_next.png" scale="1" zPosition="3" />
    <ePixmap position="955,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_prev.png" scale="1" zPosition="3" />
    <ePixmap position="1055,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_down.png" scale="1" zPosition="3" />
    <ePixmap position="1155,1127" size="100,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/buttons/key_up.png" scale="1" zPosition="3" />
</screen>

"""
