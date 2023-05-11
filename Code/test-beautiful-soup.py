import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

tree = ET.parse('Data/dataset_landscape.xml')
root = tree.getroot()

with open('Data/dataset_landscape.xml', 'r', encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'xml')

print(soup.landscapes.document)
