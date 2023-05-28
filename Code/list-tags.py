import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

tags = set()
for elem in root.iter():
    tags.add(elem.tag)

with open('Results/from_scripts/list-tags.txt', 'w', encoding='utf8') as f:
    f.write(str(sorted(tags)))
