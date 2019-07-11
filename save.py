import xml.etree.ElementTree as et
import xml.dom.minidom as minidom


def save(field, level, lines, score, block, next_block):
    root = et.Element("tetris")

    et.SubElement(root, "level").text = str(level)
    et.SubElement(root, "lines").text = str(lines)
    et.SubElement(root, "score").text = str(score)

    blk = et.SubElement(root, "block")
    et.SubElement(blk, "shape").text = block.shape
    et.SubElement(blk, "orientation").text = str(block.orientation)

    next_blk = et.SubElement(root, "nextblock")
    et.SubElement(next_blk, "shape").text = next_block.shape
    et.SubElement(next_blk, "orientation").text = str(next_block.orientation)

    for y in range(len(field)):
        row = et.SubElement(root, "row")
        for x in range(len(field[y])):
            tile = et.SubElement(row, "tile")
            tile.text = str(field[y][x])

    data = et.tostring(root)
    data = minidom.parseString(data)
    file = open("save.xml", "w")
    file.write(data.toprettyxml(indent="    "))
