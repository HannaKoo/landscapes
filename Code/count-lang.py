# Count edition texts and words by language
# TODO: [x] exclude notes & translations etc.
#       [x] count titles in the language they are in
#       - list of word counts
#       - strip at least '(',')','[',']' from the words, intelligently: Petä[s]mä(s)ki
#         - duobus (ͻ: duabus) -> 'duobus', '(ͻ:', 'duabus)',
# include_tags = ((landscapes, document, edition), p, landscape, transaction, issuer, place, title)
# exclude_tags = ((regesta, folio, scilicet), note, translation)
# Warn about tags not found.

# import xml.etree.ElementTree as ET
import lxml.etree as ET
from collections import Counter

# subtract lists: a-b
# https://stackoverflow.com/a/57827145/10216585
def subtract(a,b):
  remaining = Counter(b)
  result = []
  for val in a:
    if remaining[val]:
      remaining[val] -= 1
    else:
      result.append(val)
  return result

tree = ET.parse('Data/dataset_landscape_remove-note,translation.xml')
root = tree.getroot()

# See about mixed-content documents: https://lxml.de/tutorial.html#elements-contain-text

langs = {'la':0, 'sv':0}
words = {'la':0, 'sv':0}
unique_words = {'la': set(), 'sv': set()}

with open('Results/from_scripts/count-lang.txt', 'w', encoding="utf8") as f:
  for edition in root.iter('edition'):
    # Print document info like in the previous version:
    document = edition.getparent()
    print(document.tag, document.get('nr'), end=" ", file=f)
    
    # print(ET.tostring(edition, method="text", encoding="unicode"))
    edition_lang = edition.xpath("ancestor-or-self::*[@xml:lang][1]/@xml:lang")[0]
    # TODO: What is this, could it help with the lang namespaces?
    #   find = etree.ETXPath("//{ns}b")
    #  https://lxml.de/xpathxslt.html#etxpath
    edition_textlist = ET.tostring(edition, method="text", encoding="unicode").split() 
    # Whatabout .tail?
    print(edition_lang, file=f)
    edition_wordcount = len(edition_textlist)
    print(edition_wordcount, file=f)

    title_wordcount = 0
    title_lang = edition_lang
    title_textlist = []
    for title in edition.iter('title'):
      title_lang = title.xpath("ancestor-or-self::*[@xml:lang][1]/@xml:lang")[0]
      title_textlist.extend(ET.tostring(title, method="text", with_tail=False,
                            encoding="unicode").split())
      title_wordcount += len(title_textlist)
    print('title words:', title_wordcount, file=f)
    
    if edition_lang == title_lang == 'la':
      langs['la'] += 1
      words['la'] += edition_wordcount
      unique_words['la'].update(edition_textlist)
    elif edition_lang == title_lang == 'sv-x-old':
      langs['sv'] += 1
      words['sv'] += edition_wordcount
      unique_words['sv'].update(edition_textlist)
    elif edition_lang == 'sv-x-old' and title_lang == 'la':
      langs['sv'] += 1
      words['sv'] += edition_wordcount - title_wordcount
      words['la'] += title_wordcount
      unique_words['la'].update(title_textlist)
      # print(subtract(edition_textlist, title_textlist))
      unique_words['sv'].update(subtract(edition_textlist, title_textlist))
    else:
      print("Found ed-lang:", edition_lang, 'title-lang:', title_lang, file=f)
      print("Found", edition.attrib, file=f)

  print("Hopefully: document language is counted from edition, <note>s and <translation>s are not counted.", file=f)
  print(" ", 'latina', 'ruotsi', 'yhteensä', sep='\t', file=f)
  print('dokumentteja', langs['la'], langs['sv'], sum(langs.values()), sep='\t', file=f)
  print('sanat', words['la'], words['sv'], sum(words.values()), sep='\t', file=f)
  print('uniikit sanat', len(unique_words['la']), len(unique_words['sv']), 
        (len(unique_words['la']) + len(unique_words['sv'])), sep='\t', file=f)

  print("Averages: (all latin in titles included, crap)", file=f)
  print("All:", (words['la']+words['sv'])/(langs['la']+langs['sv']), file=f)
  for i in langs:
    print(i, end=": ", file=f)
    print(words[i]/langs[i], file=f)
