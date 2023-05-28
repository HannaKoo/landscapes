# Remove <note> tags and others, using naive simple regexes: remove from <note> to first </note>.
# Does not work for:
#  - <note> tags inside comments,
#  - <note> tags inside other <note> tags. 
#  - empty tags: <note type="FIXME"/>,
#  - etc?

import re

def remove_tag(tag, data):
    p = re.compile('<' + tag + '.*?</' + tag + '>', re.DOTALL)
    # The ? makes the regex lazy instead of greedy.
    return p.sub('', data)

to_remove = ['note']

with open("Data/dataset_landscape.xml", 'r', encoding='utf8') as f:
    data = f.read()

for tag in to_remove:
    data = remove_tag(tag, data)

with open('Data/dataset_landscape_remove-note.xml', 'w', encoding='utf8') as f:
    f.write(data)
