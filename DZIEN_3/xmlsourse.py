import xml.etree.ElementTree as ET

try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()

    for child in root:
        print(f"nazwa taga: {child.tag}, atrybuty: {child.attrib}")

    print(f"root: {root.tag}")

    print(root[0][1].text)
except Exception as ex:
    print(ex)
    
