# List lemmas of all landscape elements

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

for landscape in root.iter('landscape'):
  print(landscape.get('lemma'))
