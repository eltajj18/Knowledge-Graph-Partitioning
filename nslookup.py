import xml.etree.ElementTree as ET
tree = ET.parse("/home/eltaj-amirli/Downloads/koralLocalConfig.xml")
root = tree.getroot()
for prop in root.findall('property'):
    name = prop.find('name').text
    if name == 'master':
        x=(prop.find('value').text)
        print(x)
        