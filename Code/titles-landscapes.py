# List landscape and transaction contents in titles

import xml.etree.ElementTree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

for doc in root:
  print(doc.tag, doc.get('nr'))#, end=" ")

  for title in doc.iter('title'):
    print("".join(title.itertext()))

    for landscape in title.iter('landscape'):
      everything = "".join(landscape.itertext())
      beginning = landscape.text
      if  everything == beginning:
        print("LANDSCAPE: ", everything)
      else:
        print("WARNING:", everything, "=!", beginning)

    for transaction in title.iter('transaction'):
      everything = "".join(transaction.itertext())
      beginning = transaction.text
      if  everything == beginning:
        print("TRANSACTION: ", everything)
      else:
        print("WARNING:", everything, "=!", beginning)

  print()
