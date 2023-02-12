# Count documents by decade

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

dates = []
for doc in root:
  print(doc.tag, doc.get('nr'), doc.get('when'))
  dates.append(doc.get('when')[:3])
print(sorted(dates))

for i in range(137,152):
  print(i*10, ':', dates.count(str(i)))
