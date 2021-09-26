import xml.etree.ElementTree as ET

REVIEW_BREAK_STRENGTH = 'none'
REVIEW_BREAK_TIME = '4s'
CARD_BREAK_STRENGTH = 'none'
CARD_BREAK_TIME = '2s'

def get_cards_fs(filepath = './anki_exports/Default.txt', card_sep_char = '\t'):
    with open(filepath, mode='r') as f:
        for line in f.readlines():
            yield line.split(card_sep_char)

def get_cards():
    from random import shuffle
    x = [*get_cards_fs()]
    shuffle(x)
    return x

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
