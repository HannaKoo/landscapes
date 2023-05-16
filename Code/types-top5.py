# Most frequent landscape element types, top5 per category (built/natural)
# Include titles and editions (everything)
# Separate languages (la/sv-x-old)
    # type    sv-x-old    la
    # Natural
    # river     %          %
    # ...       %          %
    # Built
    # lot       %          %
    # ...       %          %
# TODO: Calculate percentages (now done in Excel)

import lxml.etree as ET
# import xml.etree.ElementTree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

def to_frequency_table(data):
    frequencytable = {}
    for key in data:
        if key in frequencytable:
            frequencytable[key] += 1
        else:
            frequencytable[key] = 1
    return frequencytable

data = {'sv-x-old': {'natural':[], 'built':[]}, 
              'la': {'natural':[], 'built':[]}}

for landscape in root.iter('landscape'):
    lang = landscape.xpath("ancestor-or-self::*[@xml:lang][1]/@xml:lang")[0]
    cat = landscape.get('cat')
    data[lang][cat].append(landscape.get('type'))

sv_nat = to_frequency_table(data['sv-x-old']['natural'])
sv_built = to_frequency_table(data['sv-x-old']['built'])
la_nat = to_frequency_table(data['la']['natural'])
la_built = to_frequency_table(data['la']['built'])

sv_nat_sorted   =   sorted(sv_nat.items(), key=lambda x:x[1], reverse=True)
sv_built_sorted = sorted(sv_built.items(), key=lambda x:x[1], reverse=True)
la_nat_sorted   =   sorted(la_nat.items(), key=lambda x:x[1], reverse=True)
la_built_sorted = sorted(la_built.items(), key=lambda x:x[1], reverse=True)

with open('Results/from_scripts/types-top5.txt', 'w', encoding='utf8') as f:
    print(' --- sv, natural', file=f)
    for i in sv_nat_sorted:
        print(i[0] +'\t'+ str(i[1]), file=f)
    print(' --- la, natural', file=f)
    for i in la_nat_sorted:
        print(i[0] +'\t'+ str(i[1]), file=f)
    print(' --- sv, built', file=f)
    for i in sv_built_sorted:
        print(i[0] +'\t'+ str(i[1]), file=f)
    print(' --- la, built', file=f)
    for i in la_built_sorted:
        print(i[0] +'\t'+ str(i[1]), file=f)
