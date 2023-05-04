# List landscape and transaction contents in titles

import xml.etree.ElementTree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

containing_tag = 'title'
tags_of_interest = ['landscape', 'transaction']

def print_content(elem):
  for tag in tags_of_interest:
    for j in elem.iter(tag):
      everything = "".join(j.itertext())
      beginning = j.text
      if  everything == beginning:
        print(tag+": ", everything)
      else:
        print("WARNING:", everything, "=!", beginning)

for doc in root:
  print(doc.tag, doc.get('nr'))#, end=" ")
  for containing_elem in doc.iter(containing_tag):
    print("".join(containing_elem.itertext()))
    print_content(containing_elem)
  print()
