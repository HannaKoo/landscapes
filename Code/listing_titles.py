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
# Idea: remove all notes and translations first from root.
# for document in root.iter('document'):
#     root.remove(document)  # problem: removes during traversal
for note in root.findall('note'): # problem: not iterating
    print("findall", note)
    root.remove(note)
# for translation in root.iter('translation'):
#     root.remove(translation)  # problem: removes during traversal

for doc in root:
    print(doc.tag, doc.get('nr'), doc.get('when'))
    for title in doc.iter('title'):
        print("".join(title.itertext()))

# for title in root.iter('title'):
#     print("".join(title.itertext()))

#     print(ET.tostring(title, encoding='unicode', method='text'))
# Bugaa: tulostaa usein ylimääräistä titlen jälkeen, miksi?
