# Count edition texts and words by language
# TODO: [x] exclude notes & translations etc.
#       - count titles in the language they are in
#       - list of word counts
# include_tags = ((landscapes, document, edition), p, landscape, transaction, issuer, place, title,...)
# exclude_tags = ((regesta, folio, scilicet), note, translation,  ...)
# Warn about tags not found.

# import xml.etree.ElementTree as ET
import lxml.etree as ET

tree = ET.parse('Data/dataset_landscape_remove-note,translation.xml')
root = tree.getroot()

langs = {'la':0, 'sv':0}
words = {'la':0, 'sv':0}
unique_words = {'la': set(), 'sv': set()}

# Counting words with .itertext includes child elements, eg. landscape 
# elements (and notes!), but not tags or other markup.
# Language is counted per edition, so titles are counted in the language 
# that the document is in.

# See about mixed-content documents: https://lxml.de/tutorial.html#elements-contain-text

# with open('Results/from_scripts/count-lang.txt', 'w', encoding="utf8") as f:
for elem in root.iter():
  if elem.tag != 'landscapes' and elem.tag != 'document':
    if elem.tag == 'document':
      print(elem.tag, elem.get('nr'), end=" ") #, file=f)
    elif elem.tag != 'landscapes':
      print(elem.tag)
    lang = elem.xpath("ancestor-or-self::*[@xml:lang][1]/@xml:lang")[0]
    # print(ET.tostring(elem, method="text", encoding="utf8"))
    textlist = ET.tostring(elem, method="text", encoding="utf8").split()
    print(lang) #, file=f)
    wordcount = len(textlist)
    print(wordcount) #, file=f)
    if lang == 'la':
      langs['la'] += 1
      words['la'] += wordcount
      unique_words['la'].update(textlist)
    elif lang == 'sv-x-old':
      langs['sv'] += 1
      words['sv'] += wordcount
      unique_words['sv'].update(textlist)
    else:
      print("Found", lang) #, file=f)
      print("Found", elem.attrib) #, file=f)

print("Languages are counted per document, so 'la' titles inside 'sv' documents are counted as 'sv'. <note>s and <translation>s are not counted.") #, file=f)
print(" ", 'latina', 'ruotsi', 'yhteensä', sep='\t') #, file=f)
print('dokumentteja', langs['la'], langs['sv'], sum(langs.values()), sep='\t') #, file=f)
print('sanat', words['la'], words['sv'], sum(words.values()), sep='\t') #, file=f)
print('uniikit sanat', len(unique_words['la']), len(unique_words['sv']), 
      (len(unique_words['la']) + len(unique_words['sv'])), sep='\t') #, file=f)

print("Averages:") #, file=f)
print("All:", (words['la']+words['sv'])/(langs['la']+langs['sv'])) #, file=f)
for i in langs:
  print(i, end=": ") #, file=f)
  print(words[i]/langs[i]) #, file=f)
