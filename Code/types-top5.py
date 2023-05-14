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
#
import xml.etree.ElementTree as ET
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

# Count landscape types per category, sort + TOP5
# [(cat, type)]  list of tuples
types = []
naturals = []
builts = []
for landscape in root.iter('landscape'):
    if landscape.get('cat') == 'natural':
        naturals.append(landscape.get('type'))
    elif landscape.get('cat') == 'built':
        builts.append(landscape.get('type'))
    else:
        print('Warning: cat', landscape.get('cat'), 'not expected.')

for i in naturals:
    print(i)
print()
for i in builts:
    print(i)

print()

natural_table = to_frequency_table(naturals)
for i in natural_table:
    print(i, natural_table[i])

print()
built_table = to_frequency_table(builts)
for i in built_table:
    print(i, built_table[i])

print()

sorted_naturals = sorted(natural_table.items(), key=lambda x:x[1], reverse=True)
for i in sorted_naturals:
    print(i[0] +'\t'+ str(i[1]))
print()
sorted_builts = sorted(built_table.items(), key=lambda x:x[1], reverse=True)
for i in sorted_builts:
    print(i[0] +'\t'+ str(i[1]))
