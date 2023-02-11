with open('Data/landscape_lemmas.txt', 'r', encoding="utf-8") as f:
  lemmas = f.read().splitlines()
lemmas = [i.split(',') for i in lemmas]

# Remove duplicate lemmas. TODO: Give a warning when lemma[0] are same but rest of the lines differ.
lemmas = set(map(tuple, lemmas))

# for lemma in sorted(lemmas):
#   print(lemma)

with open('Data/dataset_landscape.xml', 'r', encoding="utf-8") as f:
  data = f.read()

# find type="church">kirkon</landscape>
# replace type="church" lemma="kirkko">kirkon</landscape>
# str.find(sub[, start[, end]]) 
# str.replace(old, new[, count]) 

# Warning: If there are lemma with the same lemma[0], but differences in lemma[1] or lemma[2], the lemmas will be added twice, so check for things like: 'lemma="gathan" lemma="gatan">'
for lemma in lemmas:
  data = data.replace('>'+lemma[0]+'</landscape>', ' lemma="'+lemma[1]+'">'+lemma[0]+'</landscape>')

# Warning: Overwrites your data, so have your git and backups ready!
with open('Data/dataset_landscape.xml', 'w', encoding="utf-8") as f:
  f.write(data)
