# import numpy as np
# import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

""" 
doc   iss.gender   iss.status landscape-elements
01    m            ecc        4
02    both         burg       3
"""


""" Numbers by document:
     noble ecc   burg  peas
m     
f     
both  
"""

""" Python tabular data
pandas https://outerbounds.com/docs/python-tabular-data-structures/ 
Esim. dict of lists
"""
data = {'nr':[], 'landsc':[], 'iss-stat':[], 'iss-gen':[]}

# doc.issuer.gender
# doc.issuer.status
# doc.elements.sum

amounts = []

for doc in root:
  amounts.append(0)
  print(doc.get('nr'))
  print(doc.tag, doc.get('nr'), end = ' ')
  for j in doc.iter('landscape'):
    amounts[len(amounts)-1] += 1
  print()
  
print(amounts)