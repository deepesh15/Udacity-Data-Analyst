import wptools as wpt
 
page = wpt.page("E.T. the Extra-Terrestrial").get()
print(page.data['image'])