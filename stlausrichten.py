# -*- coding: utf-8 -*-

import gom


stl='Dateiname'
von='Verzeichnis'
nach='Ausgabe-Verzeichnis'
ausrichtung='gxyz' # für Dateianhang (siehe Zeile 34)


gom.script.sys.import_stl (
	bgr_coding=True, 
	files=[von+"/"+stl+".stl"], 
	import_mode='replace_elements', 
	length_unit='mm', 
	stl_color_bit_set=False, 
	target_type='mesh')

print(stl+' ist importiert,...')


gom.script.sys.recalculate_project (with_reports=False)

print('...neu berechnet und...')

gom.script.sys.export_stl (
	bgr_coding=False, 
	binary=True, 
	color=False, 
	elements=[gom.app.project.actual_elements[stl]], 
	export_in_one_file=True, 
	file=nach+'/'+stl+'-'+ausrichtung+'.stl', 
	length_unit='default', 
	set_stl_color_bit=True)

print('...exportiert')
print('')
print('FERTIG')
