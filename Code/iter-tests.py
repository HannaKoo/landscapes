# Test and list different iteration methods

import xml.etree.ElementTree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

# (Counting words with .itertext does not include child elements, eg. landscape elements
# But it seems to!)

for doc in root:  # all elements directly under root, in our case they are documents
  print(doc.tag, doc.get('nr'), end=" ")
  for title in doc.iter('title'):  # All titles anywhere under document
    print("".join(title.itertext()))
    # includes landscapes, notes and everything inside tags
    # it's an iterator:
    print(title.itertext())
    # how it works:
    print(list(title.itertext()))
  print()
