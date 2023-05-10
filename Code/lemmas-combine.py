# List lemmas and amounts of all landscape elements

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

lemmas = {}

for landscape in root.iter('landscape'):
  lemma = landscape.get('lemma')
  if lemma in lemmas:
    lemmas[lemma] += 1
  else: 
    lemmas[lemma] = 1

with open("Results/from_scripts/lemmas-combine.txt", 'w', encoding='utf8') as f:
  for lemma in lemmas:
    f.write(lemma +"\t" + str(lemmas[lemma]) + '\n')
