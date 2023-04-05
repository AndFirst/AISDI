class BSTNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None

    def __str__(self, depth=0):
        output = ''
        if self.right_child:
            output += self.right_child.__str__(depth + 1)
        output += f"{' ' * (5 * depth)}>{self.value}\n"
        if self.left_child:
            output += self.left_child.__str__(depth + 1)
        return output


class BST:
    def __init__(self, values):
        self.root = BSTNode(values[0])
        for value in values[1:]:
            self.insert(value)

    def search(self, searched_value):
        current_node = self.root
        while current_node and current_node.value != searched_value:
            if searched_value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return current_node

    def insert(self, value):
        new_node = BSTNode(value)
        return self._insert(new_node)

    def _insert(self, new_node):
        current_node = self.root
        while not new_node.parent:
            if new_node.value < current_node.value:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    current_node.left_child = new_node
                    new_node.parent = current_node
            else:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    current_node.right_child = new_node
                    new_node.parent = current_node
        return new_node

    def delete(self, value):
        node = self.search(value)
        if node.left_child is None or node.right_child is None:
            pointer = node
        else:
            pointer = self.successor(node)
        if pointer.left_child:
            child = pointer.left_child
        else:
            child = pointer.right_child
        if child:
            child.parent = pointer.parent
        if pointer.parent is None:
            self.root = child
        else:
            if pointer == pointer.parent.left_child:
                pointer.parent.left_child = child
            else:
                pointer.parent.right_child = child
        if pointer != node:
            node.value = pointer.value
        return pointer

    def successor(self, node):
        if node.right_child:
            return self.tree_minimum(node.right_child)
        parent = node.parent
        while parent and node == parent.right_child:
            node = parent
            parent = parent.parent
        return parent

    def tree_minimum(self, node):
        while node.left_child:
            node = node.left_child
        return node

    def __str__(self):
        if not self.root:
            return ''
        return self.root.__str__()


class Node_AVL():
    def __init__(self, value, left_child=None, right_child=None, height=1, balance=0):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.height = height
        self.balance = balance

    def __str__(self, depth=0):
        output = ''
        if self.right_child:
            output += self.right_child.__str__(depth + 1)
        output += f"{' ' * (5 * depth)}>{self.value} {self.balance}\n"
        if self.left_child:
            output += self.left_child.__str__(depth + 1)
        return output


class AVL():
    def __init__(self, values):
        self.root = Node_AVL(values[0])
        for value in values[1:]:
            self.insert(self.root, value)

    def insert(self, parent, value):
        if not parent:
            return Node_AVL(value)
        if value < parent.value:
            parent.left_child = self.insert(parent.left_child, value)
        else:
            parent.right_child = self.insert(parent.right_child, value)

        self.update_height_balance(parent)
        if parent.balance > 1:
            if parent.right_child.value <= value:
                parent = self.rotate_left(parent)
            else:
                parent.right_child = self.rotate_right(parent.right_child)
                parent = self.rotate_left(parent)
        if parent.balance < -1:
            if parent.left_child.value <= value:
                parent.left_child = self.rotate_left(parent.left_child)
                parent = self.rotate_right(parent)
            else:
                parent = self.rotate_right(parent)
        return parent

    def search(self, searched_value):
        if self.root:
            current_node = self.root
            while current_node:
                if searched_value == current_node.value:
                    return current_node
                elif searched_value < current_node.value:
                    current_node = current_node.left_child
                else:
                    current_node = current_node.right_child

    def rotate_right(self, node):
        pivot = node.left_child.right_child
        swap_node = node.left_child
        node.left_child.right_child = node
        node.left_child = pivot
        self.update_height_balance(node)
        self.update_height_balance(swap_node)
        if node == self.root:
            self.root = swap_node
        return swap_node

    def rotate_left(self, node):
        pivot = node.right_child.left_child
        swap_node = node.right_child
        node.right_child.left_child = node
        node.right_child = pivot
        self.update_height_balance(node)
        self.update_height_balance(swap_node)
        if node == self.root:
            self.root = swap_node
        return swap_node

    def update_height_balance(self, node):
        l_height = 0
        r_height = 0
        if node.left_child is not None:
            l_height = node.left_child.height
        if node.right_child is not None:
            r_height = node.right_child.height
        node.height = 1 + max(r_height, l_height)
        node.balance = r_height - l_height

    def delete(self, number, node="root"):
        if not self.root:
            return
        if node == "root":
            node = self.root
        if not self.root.left_child  and not self.root.right_child:
            if self.root.value == number:
                self.root = None
        if node is None:
            return node
        elif number < node.value:
            node.left_child = self.delete(number, node.left_child)
        if number > node.value:
            node.right_child = self.delete(number, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                node = None
            elif node.right_child and node.left_child:
                predecessor = self.predecessor(node)
                node.value = predecessor.value
                node.left_child = self.delete(node.value, node.left_child)
            elif not node.left_child:
                node = node.right_child
            elif not node.right_child:
                node = node.left_child
        if not node:
            return node
        self.update_height_balance(node)
        l_height = 0
        r_height = 0
        if node.balance < -1:
            if node.left_child.left_child is not None:
                l_height = node.left_child.left_child.height
            if node.left_child.right_child is not None:
                r_height = node.left_child.right_child.height
            if r_height >= l_height:
                node.left_child = self.rotate_left(node.left_child)
                node = self.rotate_right(node)
            else:
                node = self.rotate_right(node)
        if node.balance > 1:
            if node.right_child.left_child is not None:
                l_height = node.right_child.left_child.height
            if node.right_child.right_child is not None:
                r_height = node.right_child.right_child.height
            if r_height >= l_height:
                node = self.rotate_left(node)
            else:
                node.right_child = self.rotate_right(node.right_child)
                node = self.rotate_left(node)
        return node

    def predecessor(self, node):
        current_node = node.left_child
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node

    def __str__(self):
        return self.root.__str__()



if __name__ == "__main__":
    from random import randint
    numbers = [1,2,3,4,5,6,7]
    tree = AVL(numbers)
    print(tree.__str__())
