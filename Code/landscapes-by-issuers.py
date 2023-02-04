import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

""" 
{ecc: ##, noble: ##, burgher: ##, peasant: ##, several: ##}
 """

sums = {}

for i in root:
  print(i.tag, i.get('nr'), end = ' ')
  for j in i.iter('issuer'):
    if status[:5] in sums:  # Koko dokumentti pitää käsitellä kerralla landscapet ja issuer-statukset.
        sums[status[:5]] += landscapes
    else:
        sums[status[:5]] = landscapes
    print(j.attrib, end = ' ')
  print()
