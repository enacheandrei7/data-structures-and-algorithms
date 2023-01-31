"""
Implementation of trees in Python
"""

class TreeNode:
    """ Creates a simple Tree"""
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self, child):
        """Adds a child to the Tree"""
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
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""

        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Lenovo"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("IPhone"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Google Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

root = build_product_tree()
# print(root.get_level())
root.print_tree()
