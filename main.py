import xml.etree.ElementTree as ET

tree = ET.parse('example_tmpl.xml')
root = tree.getroot()

p = ET.SubElement(root, 'p')
s = ET.SubElement(p, 's')
s.text = 'To encourage, support, or cheer for someone or something; to wish the best for someone or something in an endeavor or activity.'
brk = ET.SubElement(p, 'break', strength='none', time='4s')
s = ET.SubElement(p, 's')
s.text = 'root for'

brk = ET.SubElement(p, 'break', strength='none', time='2s')

p = ET.SubElement(root, 'p')
s = ET.SubElement(p, 's')
s.text = 'To be or become distracted, preoccupied, or unfocused from the present moment or the task at hand. Example: I love looking out the window on the train and just ___ for a few minutes.'
brk = ET.SubElement(p, 'break', strength='none', time='4s')
s = ET.SubElement(p, 's')
s.text = 'space out'

brk = ET.SubElement(p, 'break', strength='none', time='2s')

p = ET.SubElement(root, 'p')
s = ET.SubElement(p, 's')
s.text = 'To question or interrogate someone intensely and relentlessly (about something)'
brk = ET.SubElement(p, 'break', strength='none', time='4s')
s = ET.SubElement(p, 's')
s.text = 'grill (someone) (about something)'

ET.dump(root)
