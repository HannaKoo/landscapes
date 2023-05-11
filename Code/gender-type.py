# List landscape @types by issuer gender, only in edition, skip titles
# Landscapes found at least in edition/landscape and edition/p/landscape,
# others? 
# TODO: How to list where landscapes are found? landscape.parent(.tag)...?

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

# Flatten a list of lists, goes only two levels deep.
def flatten(list):
    flattened = []
    for sublist in list:
        for item in sublist:
            flattened.append(item)
    return flattened

        # Counts for types:
        # type   f  m both
        # river 11 22 14

data = []  # tobe a list of dicts
for doc in root:
    data.append({'nr': doc.get('nr'), 'iss_gen': None, 'types': []})
    for issuer in doc.iter('issuer'):
        old = data[-1]['iss_gen']
        if old == None:
            data[-1]['iss_gen'] = issuer.get('gender')
        elif old != issuer.get('gender'):
            data[-1]['iss_gen'] = 'both'
    
    for landscape in doc.iterfind('edition/p/landscape'):
        (data[-1]['types']).append(landscape.get('type'))
    for landscape in doc.iterfind('edition/landscape'):
        (data[-1]['types']).append(landscape.get('type'))

typeset = set()
for i in data:
    for type in i.get('types'):
        typeset.add(type)
alltypes = dict.fromkeys(typeset, 0)

f_types = alltypes.copy()
m_types = alltypes.copy()
both_types = alltypes.copy()
for i in data:
    if i.get('iss_gen') == 'f':
        for type in i.get('types'):
            f_types[type] += 1
    if i.get('iss_gen') == 'm':
        for type in i.get('types'):
            m_types[type] += 1
    if i.get('iss_gen') == 'both':
        for type in i.get('types'):
            both_types[type] += 1
    

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

    f.write('f:\n' + str(f_types) + '\n')
    f.write('m:\n' + str(m_types) + '\n')
    f.write('both:\n' + str(both_types) + '\n')
