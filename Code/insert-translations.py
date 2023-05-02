# Insert lemma translations from landscape_lemmas.txt
# Read xml from Data directory, write to Results directory.
# Read landscape lemmas into dictionary {lemma: translation, ...}

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

with open('Data/landscape_lemmas.txt', 'r', encoding="utf-8") as f:
  lemmas = f.read().splitlines()
lemmas = [i.split(',') for i in lemmas]

# for lemma in lemmas:
#     print(lemma[1] + ': ' + lemma[2])

translations={}
for lemma in lemmas:
   translations[lemma[1]] = lemma[2]

print(translations)

with open('Data/dataset_landscape.xml', 'r', encoding="utf-8") as f:
  data = f.read()

for landscape in root.iter('landscape'):
   print(translations[landscape.get('lemma')])
   landscape.set( "translation", translations[landscape.get('lemma')] )
   
tree.write("Results/dataset_landscape.xml", encoding="utf-8", xml_declaration=True)
#, short_empty_elements=False) # short=False pidentää kaikki lyhyet tägit, True lyhentää titlet ja lisää välilyönnin lyhyisiin tägeihin.
# CDATAoista jää vain sisältö jäljelle -> ei validi.
# xsd- ym. linkit jää pois alusta myös declarationin kanssa
# lxml ilmeisesti ratkaisee osan näistä.