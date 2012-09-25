class Node:
    __init__(self, node_type, string="")
        self.node_type = node_type
        self.string = string
        self.children = []

    add_child(self, child):
        self.children.append(child)

    children(self):
        return self.children


def parse_file(filename):
    f = open(filename)
    lines = open(filename).readlines()
    f.close()

    print lines;

parse_file("2012-09-25.note")
