# word cloud program
# go through columns and print the second column and the word in it as many times as the 
# number in column 3 indicates

# open the file


with open('Data/lemmas-combine_suomeksi.txt', 'r', encoding='utf8') as f:
    data = f.readlines()
print(data)

table = []

for line in data:
    table.append(line.split(sep='\t'))
print()

print(table)


with open ('Results/from_scripts/HM_word_cloud.txt', 'w', encoding='utf8') as f:
    for line in table:
        print((line[1] + '\n')*int(line[2]), file=f)
