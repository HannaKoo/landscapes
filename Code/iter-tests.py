# Test and list different iteration methods
# for i in root:
# .iter() käy läpi elementit rekursiivisesti
# .itertext() käy läpi textit rekursiivisesti
# root.findall() etsii kaikki ensin, voi käyttää poistamiseen.

import xml.etree.ElementTree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

for doc in root:  # all elements directly under root, in our case they are documents
  print(doc.tag, doc.get('nr'), end=" ")
  for title in doc.iter('title'):  # All titles anywhere under document
    print("".join(title.itertext()))
    # includes landscapes, notes and everything inside tags,
    # it's an iterator:
    print(title.itertext())
    # how it works:
    print(list(title.itertext()))
  print()
