import xml.etree.ElementTree as ET

tree = ET.parse('../Data/dataset_landscape.xml')
root = tree.getroot()

for i in root:
  print(i.tag, i.get('nr'), end = ' ')
  for j in i.iter(issuer):
    print(j.tag, end = ' ')
  print()
