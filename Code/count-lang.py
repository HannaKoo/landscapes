# Count edition texts and words by language

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

langs = {'la':0, 'sv':0}
words = {'la':0, 'sv':0}

# .get() does not work with xml:lang, relevant search terms: 
#  namespace, nsmap

for doc in root:
  print(doc.get('nr'), end=" ")
  for edition in doc.iter('edition'):
    lang = edition.attrib['{http://www.w3.org/XML/1998/namespace}lang']
    print(lang)
    if lang[:2] == 'la':
      langs['la'] += 1
      words['la'] += len("".join(edition.itertext()).split())
    elif lang[:2] == 'sv':
      langs['sv'] += 1
      words['sv'] += len("".join(edition.itertext()).split())
    else:
      print("Found", lang)
      print("Found", edition.attrib)

print(langs)
print(words)
