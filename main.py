import xml.etree.ElementTree as ET

REVIEW_BREAK_STRENGTH = 'none'
REVIEW_BREAK_TIME = '4s'
CARD_BREAK_STRENGTH = 'none'
CARD_BREAK_TIME = '2s'

def get_cards():
    yield ('To encourage, support, or cheer for someone or something; to wish the best for someone or something in an endeavor or activity.',
            'root for')
    yield ('To be or become distracted, preoccupied, or unfocused from the present moment or the task at hand. Example: I love looking out the window on the train and just ___ for a few minutes.',
            'space out')
    yield ('To question or interrogate someone intensely and relentlessly (about something)',
            'grill (someone) (about something)')

tree = ET.parse('example_tmpl.xml')
root = tree.getroot()

first = True
for front, back in get_cards():
    if first:
        first = False
    else:
        brk = ET.SubElement(p, 'break', strength=CARD_BREAK_STRENGTH,
                                        time=CARD_BREAK_TIME)

    p = ET.SubElement(root, 'p')
    s = ET.SubElement(p, 's')
    s.text = front
    brk = ET.SubElement(p, 'break', strength=REVIEW_BREAK_STRENGTH,
                                    time=REVIEW_BREAK_TIME)
    s = ET.SubElement(p, 's')
    s.text = back

ET.dump(root)
