# Insert lemma translations from landscape_lemmas.txt

# import xml.etree.ElementTree as ET
from lxml import etree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

with open('Data/landscape_lemmas.txt', 'r', encoding="utf-8") as f:
  lemmas = f.read().splitlines()
lemmas = [i.split(',') for i in lemmas]

# Read landscape lemmas into dictionary {lemma: translation, ...}
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
#, short_empty_elements=False) 
# short=False pidentää kaikki lyhyet tägit, True lyhentää titlet ja lisää välilyönnin lyhyisiin tägeihin.
# CDATAt korvautuvat &amp; -merkityillä, jolloin linkki ei toimi vscodesta.
# xsd- ym. linkit tulevat mukaan lxml:llä.
# lxml ilmeisesti ratkaisee osan näistä.
