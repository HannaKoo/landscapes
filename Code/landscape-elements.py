import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

keys = set()
cats = set()
types = set()
lemmas = set()

for i in root:
  print(i.tag, i.get('nr'), end = ' ')
  for j in i.iter('landscape'):
    print(j.attrib, end = ' ')
    keys.update(j.keys())
    cats.add(j.get("cat"))
    types.add(j.get("type"))
    lemmas.add(j.get("lemma"))
  print()

print()
print("cats: ", cats)
print("keys: ", keys)
print(len(types), "types: ", types)
print(len(lemmas), "lemmas: ", sorted(lemmas))
