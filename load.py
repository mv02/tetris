import xml.etree.ElementTree as et


def load():
    tree = et.parse("save.xml")
    root = tree.getroot()

    level = root[0].text
    lines = root[1].text
    score = root[2].text

    block = [root[3][0].text, root[3][1].text]
    next_block = [root[4][0].text, root[4][1].text]

    field = []
    for row in range(5, len(root)):
        field.append([])
        for column in range(len(root[row])):
            text = root[row][column].text
            if "(" in text:
                field[row - 5].append(eval(text))
            else:
                field[row - 5].append(text)

    return [level, lines, score, block, next_block, field]
