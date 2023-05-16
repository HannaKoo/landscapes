# Count types by status.
# Not inside titles.
    # type    noble eccles  burgher peasant several
    # river     x       y       z       w       v

# import lxml.etree as ET
import xml.etree.ElementTree as ET
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
    for landscape in doc.iterfind('edition/p/landscape'):
        types[status].append(landscape.get('type'))
    for landscape in doc.iterfind('edition/landscape'):
        types[status].append(landscape.get('type'))



with open('Results/from_scripts/types-by-status.txt', 'w', encoding='utf8') as f:
    for status in ('eccle', 'noble', 'burgh', 'peasa', 'sever'):
        print(status, file=f)
        print(types[status], file=f)
