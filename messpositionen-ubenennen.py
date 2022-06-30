# -*- coding: utf-8 -*-

import gom
Name_alt="Position-kopie"
Name_neu="Position "
i=1#alte Nummer
a=5#neue Nummer
n=12#letzte Nummer


while i<=n:
	gom.script.sys.edit_properties (
	data=[gom.app.project.inspection[Name_alt+str(i)]], 
	elem_name=Name_neu+str(a))
	i = i + 1
	a = a + 1
