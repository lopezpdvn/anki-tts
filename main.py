import xml.etree.ElementTree as ET
tree = ET.parse('example_tmpl.xml')
root = tree.getroot()

p = ET.SubElement(root, 'p')
s = ET.SubElement(p, 's')
s.text = 'To encourage, support, or cheer for someone or something; to wish the best for someone or something in an endeavor or activity.'

brk = ET.SubElement(p, 'break', strength='none', time='4s')

s = ET.SubElement(p, 's')
s.text = 'root for'

ET.dump(root)
