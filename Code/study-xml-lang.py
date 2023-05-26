import lxml.etree as ET
# import xml.etree.ElementTree as ET
import re

data = '''
<project>
<doc xml:lang="la">
  <title>Lorem <important>ipsum</important></title>
  dolor <important>sit</important> amet.
</doc>
<doc xml:lang="sv">
  <title xml:lang="la">Consectetur <important>adipiscing</important> elit</title>
  Viterligit <note>what does this mean?</note> warj allom them som <important>thetta breff</important> see.
</doc>
</project>'''

'''
<project>
<doc xml:lang="la">
  <title>Lorem <important>ipsum</important></title>
  dolor <important>sit</important> amet.
  </doc>
  <doc xml:lang="sv">
    <title xml:lang="la">Consectetur <important>adipiscing</important> elit</title>
    Viterligit <important>thetta breff</important> see.
  </doc>
</project>
'''
root = ET.fromstring(data)

# importants = {'la': [], 'sv': []}
# for important in root.iter('important'):
#     lang = important.xpath("ancestor-or-self::*[@xml:lang][1]/@xml:lang")[0]
#     importants[lang].append(important.text)
# print(importants)

# for note in root.iter('note'):
#     print(note)
#     note.getparent().remove(note)  # Removes also tail :(
#     print(ET.tostring(root))

# Is it easiest to remove <note> +++ </note> using regex?