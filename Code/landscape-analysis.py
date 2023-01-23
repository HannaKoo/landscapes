import numpy as np
import pandas as pd
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
Esim. dict of lists,
tai list of dicts
"""
# data = {'nr':[], 'landsc':[], 'iss-stat':[], 'iss_gen':[]}
# data = [{'nr': '01', 'gender': 'm', 'n_landscapes': 4}]

# doc.issuer.gender
# doc.issuer.status
# doc.elements.sum

# amounts = []
data = []

for doc in root:
  data.append({'nr': doc.get('nr'), 'iss_gen': None, 'landscapes': 0})
  for j in doc.iter('issuer'):
    old = data[-1]['iss_gen']
    if old == None:
      data[-1]['iss_gen'] = j.get('gender')
    elif old != j.get('gender'):
      data[-1]['iss_gen'] = 'both'
    # (else do nothing)

    # None,m -> m
    # None,f -> f
    # both -> both
    # m,m -> m
    # f,f -> f
    # m,f -> both
    # f,m -> both
    # Does undefined something when gender != None/'f'/'m'/'both'

  for j in doc.iter('landscape'):
    data[-1]['landscapes'] += 1
  
for i in data:
  print(i)
