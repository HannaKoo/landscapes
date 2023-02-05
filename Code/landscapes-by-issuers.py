import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

def countLandscapes(doc):
  sum = 0
  for ls in doc.iter('landscape'):
    sum += 1
  return sum

sums = {'eccle': 0, 'noble': 0, 'burgh': 0, 'peasa': 0, 'sever': 0}

for doc in root:
  numLandscapes = countLandscapes(doc)
  print(numLandscapes)

  statuses = []
  print(doc.tag, doc.get('nr'), end = ' ')
  for issuer in doc.iter('issuer'):
    status = issuer.get('status')[:5]
    if status not in statuses:
        print(status, end=" ")
        statuses.append(status)
  if len(statuses) > 1:
    sums['sever'] += numLandscapes
  else:
    sums[status] += numLandscapes
  print()
  print(status)

print(sums)
