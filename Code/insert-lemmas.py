# import xml.etree.ElementTree as ET
import re

# tree = ET.parse('Data/dataset_landscape.xml')
# root = tree.getroot()

# # replaces CDATA's with &amp;'s but 
# https://stackoverflow.com/questions/55217892/keeping-cdata-sections-while-parsing-through-xml
# tree.write("Data/dataset_test_etree.xml", encoding="UTF-8", short_empty_elements=False)

lemmaFile = open('Data/landscape_lemmas.txt', 'r', encoding="utf-8")

lemmas = lemmaFile.read().splitlines()
lemmas = [i.split(',') for i in lemmas]

# https://docs.python.org/3/howto/regex.html#modifying-strings

# lemmas[0] -> lemma="lemmas[1]"
with open('Data/dataset_landscape.xml', 'r', encoding="utf-8") as f:
  data = f.read()

# regex: r'type="()">'+lemma+r'</landscape>'
# find type="church">kirkon</landscape>
# replace type="church" lemma="kirkko">kirkon</landscape>
# str.find(sub[, start[, end]]) 
# str.replace(old, new[, count]) 

for lemma in lemmas:
  print(lemma)


#  p = re.compile(r'type="()">') 
#  p.sub(, data, count=1)
