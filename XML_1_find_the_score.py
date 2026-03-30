def get_attr_number(node):
    score = len(node.attrib)
    for child in node.iter():
        if child != node:
            score += len(child.attrib)
    return score
