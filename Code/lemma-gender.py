# List lemmas by issuer gender

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

data = []
# lemmas = {'f': [], 'm': [], 'both': []}

for doc in root:
  
  data.append({'nr': doc.get('nr'), 'iss_gen': None, 'lemmas': []})
  # 'lemmas_f': [], 'lemmas_m': [], 'lemmas_both': []})

  for issuer in doc.iter('issuer'):
    old = data[-1]['iss_gen']
    if old == None:
      data[-1]['iss_gen'] = issuer.get('gender')
    elif old != issuer.get('gender'):
      data[-1]['iss_gen'] = 'both'
  
  for landscape in doc.iter('landscape'):
    (data[-1]['lemmas']).append(landscape.get('lemma'))
  

### Print and analyse data:
for i in data:
  print(i)

print()
print("documents:", len(data))


print()
print("Lemmas by gender:")

lemmas = {'f': [], 'm': [], 'both': []}

for i in data:
  lemmas[i.get('iss_gen')].append(i.get('lemmas'))
print(lemmas)
