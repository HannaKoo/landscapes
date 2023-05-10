# List lemmas of all landscape elements

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

with open("Results/from_scripts/lemmas.txt", 'w', encoding='utf8') as f:
  for landscape in root.iter('landscape'):
    # print(landscape.get('lemma'))
    f.write(landscape.get('lemma') + '\n')
