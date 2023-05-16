# Count types by status.
# Not inside titles.
    # type    noble eccles  burgher peasant several
    # river     x       y       z       w       v

from collections import Counter
# import lxml.etree as ET
import xml.etree.ElementTree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

types = {'noble': [], 'eccle': [], 'burgh': [], 'peasa': [], 'sever': []}
for doc in root:
    # get issuer statuses and combine into one status:
    statuses = set()
    for issuer in doc.iter('issuer'):
        status = issuer.get('status')[:5]
        statuses.add(status)
        if len(statuses) > 1:
            status = 'sever'

    # get landscape types to types[status]:
    for landscape in doc.iterfind('edition/p/landscape'):
        types[status].append(landscape.get('type'))
    for landscape in doc.iterfind('edition/landscape'):
        types[status].append(landscape.get('type'))

counts = {}
for status in types:
    counts[status] = Counter(types[status])

typeset = set()
for status in types:
    typeset.update(types[status])
print (typeset)


with open('Results/from_scripts/types-by-status.txt', 'w', encoding='utf8') as f:
    for status in ('eccle', 'noble', 'burgh', 'peasa', 'sever'):
        print(status+":", file=f)
        print(counts[status], file=f)
