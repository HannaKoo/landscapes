# import xml.etree.ElementTree as ET

# tree = ET.parse('Data/dataset_landscape.xml')
# root = tree.getroot()

# # replaces CDATA's with &amp;'s but 
# https://stackoverflow.com/questions/55217892/keeping-cdata-sections-while-parsing-through-xml
# tree.write("Data/dataset_test_etree.xml", encoding="UTF-8", short_empty_elements=False)

lemmaFile = open('Data/landscape_lemmas.txt', 'r', encoding="utf-8")

lemmas = lemmaFile.read().split('\n')
lemmas = [i.split(',') for i in lemmas]

# https://docs.python.org/3/howto/regex.html#modifying-strings

for i in lemmas:
  print(i)

# lemmas[0] -> lemma="lemmas[1]"

# for lemma in lemmas:
