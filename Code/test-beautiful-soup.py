import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

with open('Data/dataset_landscape.xml', 'r', encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'xml')

print(soup.landscapes.document.regesta.get('editor'))
print(soup.landscapes.document.regesta.get('{http://www.w3.org/XML/1998/namespace}lang'))
print(soup.landscapes.document.regesta.get('xml:lang'))
print(soup.landscapes.document.regesta.attrs)
print(soup.landscapes.document.regesta.folio.get('xml:lang'))
print(soup.landscapes.document.regesta.folio.attrs)
