# Landscape elements by gender
# ... and decade

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

""" 
doc   iss.gender   iss.status landscape-elements
01    m            ecc        4
02    both         burg       3
"""

""" Numbers by document:
     noble ecc   burg  peas
m     
f     
both  
"""

# dict of lists vs list of dicts:
# data = {'nr':[], 'landsc':[], 'iss-stat':[], 'iss_gen':[]}
# data = [{'nr': '01', 'gender': 'm', 'n_landscapes': 4}]

data = []

### Collect all data:
for doc in root:
  
  data.append({'nr': doc.get('nr'), 'lang': None, 'when': doc.get('when'),
               'words': 0, 'iss_gen': None, 'landscapes': 0})

  for edition in doc.iter('edition'):
    data[-1]['lang'] = edition.attrib['{http://www.w3.org/XML/1998/namespace}lang']

  for issuer in doc.iter('issuer'):
    old = data[-1]['iss_gen']
    if old == None:
      data[-1]['iss_gen'] = issuer.get('gender')
    elif old != issuer.get('gender'):
      data[-1]['iss_gen'] = 'both'
    # (else do nothing)

    # None,m -> m
    # None,f -> f
    # both -> both
    # m,m -> m
    # f,f -> f
    # m,f -> both
    # f,m -> both
    # Does undefined something when:
    #   gender != None/'f'/'m'/'both'
    # eg. 'm','m?' -> 'both'

  for edition in doc.iter('edition'):
    data[-1]['words'] += len("".join(edition.itertext()).split())

  for landscape in doc.iter('landscape'):
    data[-1]['landscapes'] += 1
  

### Print and analyse data:
for i in data:
  print(i)

print()
print("documents:", len(data))

print()
print("Documents by gender:")

doc_sums = {}
for i in data:
  if i.get('iss_gen') in doc_sums:
    doc_sums[i.get('iss_gen')] += 1
  else:
    doc_sums[i.get('iss_gen')] = 1
print(doc_sums)


print()
print("Landscapes by gender:")

landscape_sums = {'all': 0}
for i in data:
  landscape_sums['all'] += i.get('landscapes')
  if i.get('iss_gen') in landscape_sums:
    landscape_sums[i.get('iss_gen')] += i.get('landscapes')
  else:
    landscape_sums[i.get('iss_gen')] = i.get('landscapes')
print(landscape_sums)

print()
print('Landscape means:')
print("'f': ", landscape_sums['f']/doc_sums['f'])
print("'m': ", landscape_sums['m']/doc_sums['m'])
print("'both': ", landscape_sums['both']/doc_sums['both'])
print("'all':", landscape_sums['all']/len(data))


decades = {}
for i in range(137, 152):
  decades[str(i*10)] = {'words': {'la': 0, 'sv': 0}, 'landscapes': 0}

for doc in data:
  decade = doc['when'][:3]+'0'
  decades[decade]['landscapes'] += doc['landscapes']
  if doc['lang'] == 'la':
    decades[decade]['words']['la'] += doc['words']
  elif doc['lang'][:2] == 'sv':
    decades[decade]['words']['sv'] += doc['words']
  else:
    print("Found", doc['lang'])

print("\ndecades:")
print(decades)
# for decade in decades:
#   print(decade, ':', decade['words'], decade['landscapes'])
