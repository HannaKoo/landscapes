# Count types by status. Not inside titles.
    # type    noble eccles  burgher peasant
    # river     x       y       z       w

import lxml.etree as ET
tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

