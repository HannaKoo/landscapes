# Remove <note> elements and others, using naive simple regexes: remove from <note> to first </note>.
# Does not work for:
#  - <note> tags inside comments,
#  - <note> elements inside other <note> elements. 
#  - etc?

import re

def remove_tag(tag, data):
    p_empty = re.compile('<' + tag + '.*?/>')
    data = p_empty.sub('', data)
    p_normal = re.compile('<' + tag + '.*?</' + tag + '>', re.DOTALL)
    # The ? makes the regex lazy instead of greedy.
    data = p_normal.sub('', data)
    return data

to_remove = ['note', 'translation']

with open("Data/dataset_landscape.xml", 'r', encoding='utf8') as f:
    data = f.read()

for tag in to_remove:
    data = remove_tag(tag, data)

with open('Data/dataset_landscape_remove-note,translation.xml', 'w', encoding='utf8') as f:
    f.write(data)
