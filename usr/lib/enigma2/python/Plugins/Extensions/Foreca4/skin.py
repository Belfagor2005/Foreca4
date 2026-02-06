#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created (C) Evg77734, 2025

ForecaPreview_4_FHD = """
<screen name="ForecaPreview_4_FHD" position="0,0" size="1920,1080" title="Foreca Weather Preview" flags="wfNoBorder" backgroundColor="transparent">
  <ePixmap name="" position="205,140" size="400,86" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/forecalogo.png" zPosition="3" scale="1" transparent="1"/>
  <widget source="mytitel2" render="Label" position="245,1005" size="300,43" font="Regular;32" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
  <widget source="mytitel1" render="Label" position="30,26" size="750,56" font="Regular;34" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
  <widget source="Titel" render="Label" position="848,26" size="985,56" font="Regular;34" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center"/>
  <widget source="Titel2" render="Label" position="1398,26" size="985,56" font="Regular;34" foregroundColor="black" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="right"/>
  <widget name="town" position="155,260" size="500,40" zPosition="3" font="Regular;28" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="cur_temp" position="60,370" size="200,70" zPosition="3" font="Regular;50" backgroundColor="black" transparent="1" valign="center"/>
  <widget name="fl_temp" position="40,575" size="300,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center"/>
  <widget name="pressure_pic" position="371,695" size="48,48" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
  <widget name="rain_mm_pic" position="112,695" size="48,48" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
  <widget name="hum_pic" position="665,695" size="48,48" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
  <widget name="description_w" position="40,510" size="730,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="dewpoint" position="40,630" size="300,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center"/>
  <widget name="pic" position="355,355" size="100,100" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
  <widget name="sun" position="295,827" size="200,63" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
  <widget name="wind" position="592,385" size="40,41" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on"/>
  <widget name="wind_speed" position="440,575" size="330,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center"/>
  <widget name="wind_gust" position="440,630" size="330,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center"/>
  <widget name="rain_mm" position="50,765" size="170,40" zPosition="3" font="Regular;26" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="hum" position="610,765" size="160,40" zPosition="3" font="Regular;26" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="pressure" position="270,765" size="250,40" zPosition="3" font="Regular;24" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="day_len" position="270,900" size="250,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="sunrise_text" position="50,900" size="170,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="sunrise_val" position="50,850" size="170,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="sunset_text" position="570,900" size="160,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <widget name="sunset_val" position="570,850" size="160,38" zPosition="3" font="Regular;22" backgroundColor="black" transparent="1" valign="center" halign="center"/>
  <eLabel name="new eLabel3" position="100,1005" size="150,43" transparent="1" backgroundColor="#000080" text="Ext info" foregroundColor="#0053a9ff" font="Regular;32" zPosition="3" valign="center"/>
  <eLabel name="new eLabel" position="665,1005" size="120,43" transparent="1" backgroundColor="#000080" text="Help+" foregroundColor="#0053a9ff" font="Regular;32" zPosition="3" valign="center"/>
  <eLabel position="598,315" size="28,28" transparent="1" backgroundColor="#000080" text="N" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center"/>
  <eLabel position="598,471" size="28,28" transparent="1" backgroundColor="#000080" text="S" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center"/>
  <eLabel position="673,391" size="28,28" transparent="1" backgroundColor="#000080" text="E" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center"/>
  <eLabel position="523,391" size="28,28" transparent="1" backgroundColor="#000080" text="W" foregroundColor="#0053a9ff" font="Regular;18" zPosition="3" halign="center" valign="center"/>
  <eLabel name="new eLabel" position="555,1005" size="110,43" transparent="1" backgroundColor="black" text=" Help " foregroundColor="white" font="Regular;32" zPosition="3" borderColor="black" valign="center"/>
  <eLabel name="new eLabel2" position="30,1005" size="70,43" transparent="1" backgroundColor="black" text="Ok" foregroundColor="white" font="Regular;32" zPosition="3" borderColor="black" valign="center"/>
  <widget name="plate1" zPosition="1" size="1100,960" position="810,110" backgroundColor="#000050ef" cornerRadius="50"/>
  <widget name="plate11" size="1080,940" zPosition="2" position="820,120" backgroundColor="#40000000" cornerRadius="50"/>
  <widget name="plate2" size="790,860" zPosition="1" position="10,110" backgroundColor="#000050ef" cornerRadius="50"/>
  <widget name="plate22" size="770,840" zPosition="2" position="20,120" backgroundColor="#40000000" cornerRadius="50"/>
  <widget name="plate3" size="790,90" zPosition="1" position="10,980" backgroundColor="#000050ef" cornerRadius="50"/>
  <widget name="plate33" size="770,70" zPosition="2" position="20,990" backgroundColor="#40000000" cornerRadius="50"/>
  <widget name="plate4" size="1100,90" zPosition="1" position="810,10" backgroundColor="#000050ef" cornerRadius="50"/>
  <widget name="plate5" size="790,90" zPosition="1" position="10,10" backgroundColor="#000050ef" cornerRadius="50"/>
  <widget name="plate44" size="1080,70" zPosition="2" position="820,20" backgroundColor="#40000000" cornerRadius="50"/>
  <widget name="plate55" size="770,70" zPosition="2" position="20,20" backgroundColor="#40000000" cornerRadius="50"/>
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
  <widget name="plate1"  position="20,20" backgroundColor="#40000000" size="1120,900" zPosition="2" cornerRadius="30"/>
  <eLabel position="45,40" text="Color selection" font="Regular;32" valign="center" halign="center" size="1070,42" zPosition="3" transparent="1"/>
</screen>"""

About_Foreca4_FHD = """
<screen name="About_Foreca4_FHD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="960,400">
  <widget position="center,100" size="750,42" zPosition="3" font="Regular;32" source="ver" render="Label" transparent="1" valign="center" halign="center"/>
  <eLabel position="center,180" size="400,42" zPosition="3" font="Regular;32" text="(C) Evg77734, 2025" transparent="1" halign="center" valign="center"/>
  <eLabel name="" position="center,260" size="400,42" zPosition="3" font="Regular;32" text="https://gisclub.tv" transparent="1" halign="center" valign="center"/>
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

# -----------------------------------------------------------------------

ForecaPreview_4_HD = """
<screen name="ForecaPreview_4_HD" position="0,0" size="1280,720" title="Foreca Weather Preview" flags="wfNoBorder" backgroundColor="transparent" >
  <ePixmap name="" position="137,93" size="267,57" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/Foreca4/images/forecalogo.png" zPosition="3" scale="1" transparent="1" />
  <widget source="mytitel2" render="Label" position="163,670" size="200,29" font="Regular;21" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center" />
  <widget source="mytitel1" render="Label" position="20,17" size="500,37" font="Regular;23" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center" />
  <widget source="Titel" render="Label" position="565,17" size="657,37" font="Regular;23" foregroundColor="#0053a9ff" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="center" />
  <widget source="Titel2" render="Label" position="932,17" size="657,37" font="Regular;23" foregroundColor="black" backgroundColor="black" transparent="1" valign="center" zPosition="3" halign="right" />
  <widget name="town" position="103,173" size="333,27" zPosition="3" font="Regular;19" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="cur_temp" position="40,247" size="133,47" zPosition="3" font="Regular;33" backgroundColor="black" transparent="1" valign="center" />
  <widget name="fl_temp" position="27,383" size="200,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" />
  <widget name="pressure_pic" position="247,463" size="32,32" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="rain_mm_pic" position="75,463" size="32,32" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="hum_pic" position="443,463" size="32,32" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="description_w" position="27,340" size="487,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="dewpoint" position="27,420" size="200,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" />
  <widget name="pic" position="237,237" size="67,67" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="sun" position="197,551" size="133,42" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="wind" position="395,257" size="27,27" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="wind_speed" position="293,383" size="220,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" />
  <widget name="wind_gust" position="293,420" size="220,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" />
  <widget name="rain_mm" position="33,510" size="113,27" zPosition="3" font="Regular;17" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="hum" position="407,510" size="107,27" zPosition="3" font="Regular;17" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="pressure" position="180,510" size="167,27" zPosition="3" font="Regular;16" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="day_len" position="180,600" size="167,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="sunrise_text" position="33,600" size="113,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="sunrise_val" position="33,567" size="113,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="sunset_text" position="380,600" size="107,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <widget name="sunset_val" position="380,567" size="107,25" zPosition="3" font="Regular;15" backgroundColor="black" transparent="1" valign="center" halign="center" />
  <eLabel name="new eLabel3" position="67,670" size="100,29" transparent="1" backgroundColor="#000080" text="Ext info" foregroundColor="#0053a9ff" font="Regular;21" zPosition="3" valign="center" />
  <eLabel name="new eLabel" position="443,670" size="80,29" transparent="1" backgroundColor="#000080" text="Help+" foregroundColor="#0053a9ff" font="Regular;21" zPosition="3" valign="center" />
  <eLabel position="399,210" size="19,19" transparent="1" backgroundColor="#000080" text="N" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center" />
  <eLabel position="399,314" size="19,19" transparent="1" backgroundColor="#000080" text="S" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center" />
  <eLabel position="449,261" size="19,19" transparent="1" backgroundColor="#000080" text="E" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center" />
  <eLabel position="349,261" size="19,19" transparent="1" backgroundColor="#000080" text="W" foregroundColor="#0053a9ff" font="Regular;12" zPosition="3" halign="center" valign="center" />
  <eLabel name="new eLabel" position="370,670" size="73,29" transparent="1" backgroundColor="black" text=" Help " foregroundColor="white" font="Regular;21" zPosition="3" borderColor="black" valign="center" />
  <eLabel name="new eLabel2" position="20,670" size="47,29" transparent="1" backgroundColor="black" text="Ok" foregroundColor="white" font="Regular;21" zPosition="3" borderColor="black" valign="center" />
  <widget name="plate1" zPosition="1" size="733,640" position="540,73" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="plate11" size="720,627" zPosition="2" position="547,80" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate2" size="527,573" zPosition="1" position="7,73" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="plate22" size="513,560" zPosition="2" position="13,80" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate3" size="527,60" zPosition="1" position="7,653" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="plate33" size="513,47" zPosition="2" position="13,660" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate4" size="733,60" zPosition="1" position="540,7" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="plate5" size="527,60" zPosition="1" position="7,7" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="plate44" size="720,47" zPosition="2" position="547,13" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate55" size="513,47" zPosition="2" position="13,13" backgroundColor="#40000000" cornerRadius="50" />
  <widget source="menu" render="Listbox" position="555,95" size="703,590" scrollbarMode="showOnDemand" zPosition="3" transparent="1" backgroundColor="black" >
    <convert type="TemplatedMultiContent" >
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
</screen >"""

ColorSelect_HD = """
<screen name="ColorSelect_HD" position="center,center" backgroundColor="transparent" size="773,627" flags="wfNoBorder" >
  <widget name="Clist" itemHeight="35" position="30,70" size="713,397" enableWrapAround="1" scrollbarMode="showOnDemand" valign="center" font="Console;19" transparent="1" backgroundColor="black" zPosition="3" />
  <widget name="colordatas" position="30,567" size="713,28" font="Regular;21" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black" />
  <widget name="colorname" position="30,527" size="713,28" font="Regular;21" transparent="1" zPosition="3" halign="center" valign="center" backgroundColor="black" />
  <widget position="30,480" name="pic1" zPosition="3" size="713,33" scale="1" transparent="1" backgroundColor="black" />
  <widget name="plate0" position="7,7" backgroundColor="#000050ef" size="760,613" zPosition="1" cornerRadius="30" />
  <widget name="plate1"  position="13,13" backgroundColor="#40000000" size="747,600" zPosition="2" cornerRadius="30" />
  <eLabel position="30,27" text="Color selection" font="Regular;21" valign="center" halign="center" size="713,28" zPosition="3" transparent="1" />
</screen>"""

About_Foreca4_HD = """
<screen name="About_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="640,267" >
  <widget position="center,67" size="500,28" zPosition="3" font="Regular;21" source="ver" render="Label" transparent="1" valign="center" halign="center" />
  <eLabel position="center,120" size="267,28" zPosition="3" font="Regular;21" text="(C) Evg77734,2025" transparent="1" halign="center" valign="center" />
  <eLabel name="" position="center,173" size="267,28" zPosition="3" font="Regular;21" text="https://gisclub.tv" transparent="1" halign="center" valign="center" />
  <widget name="plate1" size="620,247" zPosition="2" position="10,10" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate0" size="640,267" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50" />
</screen>"""

ExtInfo_Foreca4_HD = """
<screen name="ExtInfo_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="920,600" >
  <widget position="573,47" size="315,28" zPosition="3" font="Regular;21" source="title1" render="Label" transparent="1" valign="center" />
  <widget position="20,47" size="533,28" zPosition="3" font="Regular;21" source="title3" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" />
  <widget position="20,352" size="533,100" zPosition="3" font="Regular;19" source="text2" render="Label" transparent="1" />
  <widget position="20,83" size="533,100" zPosition="3" font="Regular;19" source="text1" render="Label" transparent="1" />
  <widget position="20,317" size="533,28" zPosition="3" font="Regular;21" source="title4" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" />
  <widget position="20,188" size="133,28" zPosition="3" font="Regular;21" source="mo1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="20,285" size="133,28" zPosition="3" font="Regular;21" source="mo1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="20,555" size="133,28" zPosition="3" font="Regular;21" source="mo2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="20,457" size="133,28" zPosition="3" font="Regular;21" source="mo2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="153,188" size="133,28" zPosition="3" font="Regular;21" source="af1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="153,285" size="133,28" zPosition="3" font="Regular;21" source="af1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="153,555" size="133,28" zPosition="3" font="Regular;21" source="af2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="153,457" size="133,28" zPosition="3" font="Regular;21" source="af2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="287,188" size="133,28" zPosition="3" font="Regular;21" source="ev1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="287,285" size="133,28" zPosition="3" font="Regular;21" source="ev1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="287,555" size="133,28" zPosition="3" font="Regular;21" source="ev2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="287,457" size="133,28" zPosition="3" font="Regular;21" source="ev2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="420,188" size="133,28" zPosition="3" font="Regular;21" source="ov1" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="420,285" size="133,28" zPosition="3" font="Regular;21" source="ov1_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="420,555" size="133,28" zPosition="3" font="Regular;21" source="ov2_text" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="770,507" size="120,28" zPosition="3" font="Regular;21" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" />
  <widget position="610,507" size="120,28" zPosition="3" font="Regular;21" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" />
  <widget position="420,457" size="133,28" zPosition="3" font="Regular;21" source="ov2" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" halign="center" />
  <widget position="20,13" size="533,28" zPosition="3" font="Regular;21" source="title2" render="Label" transparent="1" valign="center" halign="center" />
  <widget name="plate1" size="907,587" zPosition="2" position="7,7" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate0" size="920,600" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="pic" position="573,83" size="315,385" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5" />
  <widget name="pic_af1" position="197,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_af2" position="197,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_ev1" position="330,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_ev2" position="330,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_ov1" position="463,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_ov2" position="463,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_lot" position="733,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_lat" position="573,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_mo1" position="63,227" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_mo2" position="63,497" size="47,47" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
</screen>"""

ExtInfo_2_Foreca4_HD = """
<screen name="ExtInfo_2_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="383,573" >
  <widget position="33,33" size="315,28" zPosition="3" font="Regular;21" source="title1" render="Label" transparent="1" valign="center" />
  <widget position="228,507" size="120,28" zPosition="3" font="Regular;21" source="lon_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" />
  <widget position="67,507" size="120,28" zPosition="3" font="Regular;21" source="lat_val" render="Label" transparent="1" valign="center" foregroundColor="#0053a9ff" />
  <widget name="plate1" size="370,560" zPosition="2" position="7,7" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate0" size="383,573" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="pic" position="33,83" size="315,385" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5" />
  <widget name="pic_lot" position="197,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
  <widget name="pic_lat" position="33,507" size="28,28" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" />
</screen>"""

Transparency_Foreca4_HD = """
<screen name="Transparency_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="577,440" >
  <widget position="67,33" size="433,28" zPosition="3" font="Regular;21" source="text1" render="Label" transparent="1" valign="center" halign="center" />
  <widget name="plate1" size="557,420" zPosition="2" position="10,10" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate0" size="577,440" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="list" position="67,81" size="433,312" itemHeight="52" valign="center" font="Regular;21" zPosition="3" transparent="1" />
</screen>"""

Meteogram_Foreca4_HD = """
<screen name="Meteogram_Foreca4_HD" position="center,center" flags="wfNoBorder" backgroundColor="transparent" size="1047,607" >
  <widget position="33,33" size="667,28" zPosition="3" font="Regular;21" source="title1" render="Label" transparent="1" valign="center" />
  <widget name="plate1" size="1033,593" zPosition="2" position="7,7" backgroundColor="#40000000" cornerRadius="50" />
  <widget name="plate0" size="1047,607" zPosition="1" position="0,0" backgroundColor="#000050ef" cornerRadius="50" />
  <widget name="pic" position="33,83" size="980,490" scale="1" zPosition="3" backgroundColor="#40000000" transparent="1" alphatest="on" borderColor="#000050ef" borderWidth="5" />
</screen >"""
