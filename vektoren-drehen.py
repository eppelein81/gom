# -*- coding: utf-8 -*-

import gom

Name="Vektorname "
i=0 #erste Nummer
n=999 #letzte Nummer

RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
' <title>Message</title>' \
' <style></style>' \
' <control id="YesNo"/>' \
' <position>center</position>' \
' <embedding>always_toplevel</embedding>' \
' <sizemode>automatic</sizemode>' \
' <size height="154" width="256"/>' \
' <content rows="1" columns="1">' \
'  <widget row="0" columnspan="1" column="0" rowspan="1" type="display::text">' \
'   <name>text</name>' \
'   <tooltip></tooltip>' \
'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
'p, li { white-space: pre-wrap; }' \
'&lt;/style>&lt;/head>&lt;body style="    ">' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1. Punkt in &lt;font color="#ff0000">&lt;b>'+Name+str(i)+'&lt;/b>&lt;/font> umbenannt?&lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> &lt;/p>' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">...wenn &amp;quot;Ja&amp;quot;, dann geht\'s los...&lt;/p>&lt;/body>&lt;/html></text>' \
'   <wordwrap>false</wordwrap>' \
'  </widget>' \
' </content>' \
'</dialog>')

while i<=n:
	
	print(Name+str(i))
	
	print("Vektor alt")
	print(gom.app.project.inspection[Name+str(i)].get ('normal.x'))
	print(gom.app.project.inspection[Name+str(i)].get ('normal.y'))
	print(gom.app.project.inspection[Name+str(i)].get ('normal.z'))
	
	print("Vektor neu")
	#Berechnung
	x=(gom.app.project.inspection[Name+str(i)].get ('normal.x'))*-1
	y=(gom.app.project.inspection[Name+str(i)].get ('normal.y'))*-1
	z=(gom.app.project.inspection[Name+str(i)].get ('normal.z'))*-1
	print(x)
	print(y)
	print(z)
	print(" ")
	
	gom.script.sys.edit_creation_parameters (
	auto_apply=True, 
	element=gom.app.project.inspection[Name+str(i)], 
	normal={'direction':  gom.Vec3d (x, y, z), 'inverted': True, 'point': gom.Vec3d (0.00000000e+00, 0.00000000e+00, 0.00000000e+00), 'type': 'projected'})
	i = i + 1

RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
' <title>Message</title>' \
' <style></style>' \
' <control id="OkCancel"/>' \
' <position>center</position>' \
' <embedding>always_toplevel</embedding>' \
' <sizemode>automatic</sizemode>' \
' <size width="281" height="168"/>' \
' <content columns="1" rows="1">' \
'  <widget column="0" rowspan="1" type="display::text" columnspan="1" row="0">' \
'   <name>text</name>' \
'   <tooltip></tooltip>' \
'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
'p, li { white-space: pre-wrap; }' \
'&lt;/style>&lt;/head>&lt;body style="    ">' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Fertig&lt;/p>&lt;/body>&lt;/html></text>' \
'   <wordwrap>false</wordwrap>' \
'  </widget>' \
' </content>' \
'</dialog>')
