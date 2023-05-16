# Count types by status. Not inside titles.
    # type    noble eccles  burgher peasant several
    # river     x       y       z       w       v

import lxml.etree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

for doc in root:
    pass


with open('Results/from_scripts/types-by-status.txt', 'w', encoding='utf8') as f:
    pass
