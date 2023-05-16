# Count types by status.
# Not inside titles.
    # type    noble eccles  burgher peasant several
    # river     x       y       z       w       v

import lxml.etree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

types = {'eccle': [], 'noble': [], 'burgh': [], 'peasa': [], 'sever': []}
for doc in root:
    # get issuer statuses and combine into one status:
    statuses = set()
    for issuer in doc.iter('issuer'):
        status = issuer.get('status')[:5]
        statuses.add(status)
        if len(statuses) > 1:
            status = 'sever'
        print(statuses, status)

    # get landscape types to types[status]:
    for landscape in doc.iter('landscape'):
        types[status].append(landscape.get('type'))

for status in ('eccle', 'noble', 'burgh', 'peasa', 'sever'):
    print(status)
    print(types[status])

with open('Results/from_scripts/types-by-status.txt', 'w', encoding='utf8') as f:
    pass
