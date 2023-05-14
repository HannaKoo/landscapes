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
for landscape in root.iter('landscape'):
    types.append((landscape.get('cat'), landscape.get('type')))
for i in types:
    print(i)
print()

table = to_frequency_table(types)
for i in table:
    print(i, table[i])

print()

sorted_table = sorted(table.items(), key=lambda x:x[1], reverse=True)
for i in sorted_table:
    print(i)
