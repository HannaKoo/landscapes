# List landscape @types by issuer gender, only in edition, skip titles
# Landscapes found at least in edition/landscape and edition/p/landscape,
# others?

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

def flatten(list):
  flattened = []
  for sublist in list:
    for item in sublist:
        flattened.append(item)
  return flattened

data = []

for doc in root:
  
  data.append({'nr': doc.get('nr'), 'iss_gen': None, 'types': []})

  for issuer in doc.iter('issuer'):
    old = data[-1]['iss_gen']
    if old == None:
      data[-1]['iss_gen'] = issuer.get('gender')
    elif old != issuer.get('gender'):
      data[-1]['iss_gen'] = 'both'
  
  # Is there a way to do these in one go? 
  # 'edition//landscape' not working (gives also titles).
  # 'edition/*/landscape' does something weird.
  # union of the .iterfinds? Needs .findall?
  for landscape in doc.iterfind('edition/p/landscape'):
    (data[-1]['types']).append(landscape.get('type'))
  for landscape in doc.iterfind('edition/landscape'):
    (data[-1]['types']).append(landscape.get('type'))
#   for landscape in doc.iterfind('edition/*/landscape'):
#     (data[-1]['types']).append(landscape.get('type'))


###  Write file; analyse data:  ###

with open('Results/from_scripts/gender-type.txt', 'w', encoding='utf8') as f:
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
    f.write(str(sum(map(len, (types['both'])))) + '\n'*2)

    ## Flatten lists and count types

    f_flat = flatten(types['f'])
    m_flat = flatten(types['m'])
    both_flat = flatten(types['both'])

    # Counts for types:
    # type   f  m both
    # river 11 22 14

# def count_items(list):
    f_types = {}

    for type in f_flat:
      if type in f_types:
          f_types[type] += 1
      else:
          f_types[type] = 1
    f.write('f :' + str(f_types) + '\n')
