# haluan listan otsikoista
# ostikon lisäksi pitää tulostaa päivämäärä
# lisänä tieto dokumentista
# myös tieto kielestä
# järjestys suodattuu päivämäärän mukaan

# tuo kirjaston joka lukee/käsittelee xml:ää
#nimetään ET:ksi

import xml.etree.ElementTree as ET

# ladataan xml tiedosto ja parseroidaan se 

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

#tree on muuttuja ja siihen tallennetaan ET.parse
#parse on funktio

# root muuttujan kautta voidaan käsitellä xml tiedostoa

# Ongelma: tulostaa notet ja translationit mukaan.
# IDEA: remove all notes and translations first from root.

# for document in root.iter('document'):
#     root.remove(document)  # problem: removes during traversal

# https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support
# https://docs.python.org/3/library/xml.etree.elementtree.html#modifying-an-xml-file
# for note in root.findall('.//note'): 
#   # problem: not recursive, with XPath // it should be
#     print(note.tag, note.text)
#     print("findall", note)
#     root.remove(note)

for title in root.findall('.//title'):
    for note in title.findall('note'):
        title.remove(note)
# Seems to work!
# EXCEPT: For some reason doc 12 is missing the whole title after marking a <note> in the beginning. 
# Are there other problems like this? 
# Yes, doc 25 printing starts only from the first tag after the note(transaction)!
# TODO: remove translations, what else?

# for translation in root.iter('translation'):
#     root.remove(translation)  # problem: removes during traversal

for doc in root:
    print(doc.tag, doc.get('nr'), doc.get('when'))
    for title in doc.iter('title'):
        print("".join(title.itertext()))

# for title in root.iter('title'):
#     print("".join(title.itertext()))
#
#     print(ET.tostring(title, encoding='unicode', method='text'))
# Bugaa: tulostaa usein ylimääräistä titlen jälkeen, miksi?
# Onko se title.tail ? Eli ensimmäiseen tagiin asti editiota?
