# Count edition texts and words by language

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

langs = {'la':0, 'sv':0}
words = {'la':0, 'sv':0}

# .get() does not work with xml:lang, relevant search terms: 
#  namespace, nsmap

# Counting words with .itertext includes child elements, eg. landscape 
# elements (and notes!), but not tags or other markup.
# Language is counted per edition, so titles are counted in the language 
# that the document is in.

for doc in root:
  print(doc.tag, doc.get('nr'), end=" ")
  for edition in doc.iter('edition'):
    lang = edition.attrib['{http://www.w3.org/XML/1998/namespace}lang']
    print(lang)
    wordcount = len("".join(edition.itertext()).split())
    print(wordcount)
    if lang[:2] == 'la':
      langs['la'] += 1
      words['la'] += wordcount
    elif lang[:2] == 'sv':
      langs['sv'] += 1
      words['sv'] += wordcount
    else:
      print("Found", lang)
      print("Found", edition.attrib)

print(langs)
print(words)

print("Averages:")
print("All:", (words['la']+words['sv'])/(langs['la']+langs['sv']))
for i in langs:
  print(i, end=": ")
  print(words[i]/langs[i])
