# List issuers by document:
# document 02 {'status': 'burgher', 'gender': 'm', 'onlyone': 'n'} {'status': 'burgher wife', 'gender': 'f', 'onlyone': 'n'} 
# document 07 {'status': 'ecclesiastic', 'gender': 'm', 'onlyone': 'y'}
# ...

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

for i in root:
  print(i.tag, i.get('nr'), end = ' ')
  for j in i.iter('issuer'):
    print(j.attrib, end = ' ')
  print()
