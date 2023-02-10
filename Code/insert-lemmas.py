with open('Data/landscape_lemmas.txt', 'r', encoding="utf-8") as f:
  lemmas = f.read().splitlines()
lemmas = [i.split(',') for i in lemmas]

lemmas = set(map(tuple, lemmas))

# for lemma in sorted(lemmas):
#   print(lemma)

with open('Data/dataset_landscape.xml', 'r', encoding="utf-8") as f:
  data = f.read()

# find type="church">kirkon</landscape>
# replace type="church" lemma="kirkko">kirkon</landscape>
# str.find(sub[, start[, end]]) 
# str.replace(old, new[, count]) 

for lemma in lemmas:
  data = data.replace('>'+lemma[0]+'</landscape>', ' lemma="'+lemma[1]+'">'+lemma[0]+'</landscape>')

with open('Data/dataset_landscape.xml', 'w', encoding="utf-8") as f:
  f.write(data)
