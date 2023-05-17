# Count edition texts and words by language

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

langs = {'la':0, 'sv':0}
words = {'la':0, 'sv':0}
unique_words = set()

# .get() does not work with xml:lang, relevant search terms: 
#  namespace, nsmap

# Counting words with .itertext includes child elements, eg. landscape 
# elements (and notes!), but not tags or other markup.
# Language is counted per edition, so titles are counted in the language 
# that the document is in.
with open('Results/from_scripts/count-lang.txt', 'w', encoding="utf8") as f:
  for doc in root:
    print(doc.tag, doc.get('nr'), end=" ", file=f)
    for edition in doc.iter('edition'):
      lang = edition.attrib['{http://www.w3.org/XML/1998/namespace}lang']
      text = "".join(edition.itertext()).split()
      print(lang, file=f)
      wordcount = len(text)
      print(wordcount, file=f)
      if lang[:2] == 'la':
        langs['la'] += 1
        words['la'] += wordcount
      elif lang[:2] == 'sv':
        langs['sv'] += 1
        words['sv'] += wordcount
      else:
        print("Found", lang, file=f)
        print("Found", edition.attrib, file=f)

  print('langs:', langs, ', sum:', sum(langs.values()), file=f)
  print('words:', words, ', sum:', sum(words.values()), file=f)

  print("Averages:", file=f)
  print("All:", (words['la']+words['sv'])/(langs['la']+langs['sv']), file=f)
  for i in langs:
    print(i, end=": ", file=f)
    print(words[i]/langs[i], file=f)
