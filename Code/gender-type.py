# List landscape @types by issuer gender, only in edition, skip titles

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

data = []
# types = {'f': [], 'm': [], 'both': []}


for doc in root:
  
  data.append({'nr': doc.get('nr'), 'iss_gen': None, 'types': []})
  # 'types_f': [], 'types_m': [], 'types_both': []})

  for issuer in doc.iter('issuer'):
    old = data[-1]['iss_gen']
    if old == None:
      data[-1]['iss_gen'] = issuer.get('gender')
    elif old != issuer.get('gender'):
      data[-1]['iss_gen'] = 'both'
  
  for landscape in doc.iter('landscape'):
    (data[-1]['types']).append(landscape.get('type'))
  

### Write file; analyse data:

with open('Results/from_scripts/gender-type.txt', 'w', encoding='utf8') as f:
    f.write("in development: includes titles\n\n")

    for i in data:
        f.write(str(i) + '\n')

    f.write('\n')
    f.write("documents:" + str(len(data)))


    f.write('\n'*2)
    f.write("types by gender:\n")

    types = {'f': [], 'm': [], 'both': []}
    for i in data:
        types[i.get('iss_gen')].append(i.get('types'))

    f.write('f: ' + str(types['f']) + '\n')
    f.write(str(sum(map(len, (types['f'])))) + '\n'*2)

    f.write('m: ' + str(types['m']) + '\n')
    f.write(str(sum(map(len, (types['m'])))) + '\n'*2)

    f.write('both: ' + str(types['both']) + '\n')
    f.write(str(sum(map(len, (types['both'])))) + '\n')
