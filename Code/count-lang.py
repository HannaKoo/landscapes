# Count edition texts and words by language
# TODO: - exclude notes etc.
#       - count titles in the language they are in, or leave them out?
# include_tags = (p, landscape, transaction, issuer, ...)
# exclude_tags = (note, scilicet, ...)
# Warn about tags not found.

import xml.etree.ElementTree as ET

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

langs = {'la':0, 'sv':0}
words = {'la':0, 'sv':0}
unique_words = {'la': set(), 'sv': set()}

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
      textlist = "".join(edition.itertext()).split()
      print(lang, file=f)
      wordcount = len(textlist)
      print(wordcount, file=f)
      if lang[:2] == 'la':
        langs['la'] += 1
        words['la'] += wordcount
        unique_words['la'].update(textlist)
      elif lang[:2] == 'sv':
        langs['sv'] += 1
        words['sv'] += wordcount
        unique_words['sv'].update(textlist)
      else:
        print("Found", lang, file=f)
        print("Found", edition.attrib, file=f)

  print("Languages are counted per document, so 'la' titles inside 'sv' documents are counted as 'sv'. Also <note>s and everything is counted.", file=f)
  print(" ", 'latina', 'ruotsi', 'yhteensä', sep='\t', file=f)
  print('dokumentteja', langs['la'], langs['sv'], sum(langs.values()), sep='\t', file=f)
  print('sanat', words['la'], words['sv'], sum(words.values()), sep='\t', file=f)
  print('uniikit sanat', len(unique_words['la']), len(unique_words['sv']), 
        (len(unique_words['la']) + len(unique_words['sv'])), sep='\t', file=f)

  print("Averages:", file=f)
  print("All:", (words['la']+words['sv'])/(langs['la']+langs['sv']), file=f)
  for i in langs:
    print(i, end=": ", file=f)
    print(words[i]/langs[i], file=f)
