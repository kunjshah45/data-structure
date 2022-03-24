class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = "    "*self.get_level()
        prefix = spaces + "|_" if self.parent else ""
        print(prefix, self.data)

        if(len(self.children)):
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = Treenode("Electrnoic")
    laptop = Treenode("Laptop")
    laptop.add_child(Treenode("Apple Mac"))
    laptop.add_child(Treenode("Microsoft Surface"))
    laptop.add_child(Treenode("Lenovo Thinkpad"))

    cellphone = Treenode("Cellphone")
    cellphone.add_child(Treenode("Apple Iphone"))
    cellphone.add_child(Treenode("Google Pixel"))
    cellphone.add_child(Treenode("Samsung"))

    tv = Treenode("TV")
    tv.add_child(Treenode("Apple TV"))
    tv.add_child(Treenode("Samsung"))
    tv.add_child(Treenode("Sony Bravia"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()

    root.print_tree()