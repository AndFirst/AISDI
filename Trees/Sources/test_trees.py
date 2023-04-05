from trees import BST, AVL, Node_AVL

def test_create_bst():
    values = [4, 1, 2, 6, 7, 5]
    tree = BST(values)
    assert tree.root.value == 4
    assert tree.root.left_child.value == 1
    assert tree.root.right_child.value == 6
    assert tree.root.left_child.right_child.value == 2
    assert tree.root.right_child.right_child.value == 7
    assert tree.root.right_child.left_child.value == 5


def test_bst_search():
    values = [4, 1, 2, 6, 7, 5]
    tree = BST(values)
    find = tree.search(6)
    assert find.parent.value == 4
    assert find.left_child.value == 5
    assert find.right_child.value == 7
    assert find.value == 6

def test_successor():
    values = [4, 1, 2, 6, 7, 5]
    tree = BST(values)
    node = tree.root
    find = tree.successor(node)
    assert find.value == 5

def test_bst_insert():
    values = [4, 1, 2, 6, 7, 5]
    tree = BST(values)
    tree.insert(3)
    assert tree.root.left_child.right_child.right_child.value == 3
    assert tree.root.left_child.right_child.right_child.parent.value == 2
    assert tree.root.left_child.right_child.right_child.left_child is None
    assert tree.root.left_child.right_child.right_child.right_child is None

def test_delete_bst_leaf():
    values = [4, 1, 2, 6, 7, 5]
    tree = BST(values)
    node = tree.delete(2)
    assert tree.root.left_child.right_child is None

def test_delete_bst_with_left_child():
    values = [4, 2, 1, 6, 7, 5]
    tree = BST(values)
    node = tree.delete(2)
    assert tree.root.left_child.value == 1
    assert node.value == 2

def test_delete_bst_with_right_child():
    values = [4, 1, 2, 6, 7, 5]
    tree = BST(values)
    node = tree.delete(1)
    assert tree.root.left_child.value == 2
    assert node.value == 1

def test_delete_bts_with_two_children():
    values = [4, 1, 2, 6, 7, 5]
    tree = BST(values)
    node = tree.delete(6)
    assert tree.root.right_child.value == 7
    assert tree.root.right_child.left_child.value == 5
    assert tree.root.right_child.right_child is None
    assert node.value == 7

def test_tree_minimum_all():
    values = [4, 2, 1, 6, 7, 5]
    tree = BST(values)
    node = tree.tree_minimum(tree.root)
    assert tree.root.left_child.left_child == node
    assert node.value == 1

def test_tree_minimum_some_node():
    values = [4, 2, 1, 6, 7, 5]
    tree = BST(values)
    node = tree.tree_minimum(tree.root.right_child)
    assert node.value == 5

def test_create_avl():
    numbers = [3, 2, 5, 1, 4, 6, 7]
    tree = AVL(numbers)
    assert tree.root.value == 3
    assert tree.root.left_child.value == 2
    assert tree.root.right_child.value == 5
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.right_child.left_child.value == 4
    assert tree.root.right_child.right_child.value == 6
    assert tree.root.right_child.right_child.right_child.value == 7

def test_create_avl_sorted():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    tree = AVL(numbers)
    assert tree.root.value == 4
    assert tree.root.left_child.value == 2
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.right_child.value == 3
    assert tree.root.right_child.value == 6
    assert tree.root.right_child.left_child.value == 5
    assert tree.root.right_child.right_child.value == 7

def test_rotate_right():
    root = [3]
    tree = AVL(root)
    tree.root.left_child = Node_AVL(2)
    tree.root.left_child.left_child = Node_AVL(1)
    tree.rotate_right(tree.root)
    assert tree.root.value == 2
    assert tree.root.left_child.value == 1
    assert tree.root.right_child.value == 3

def test_rotate_left():
    root = [1]
    tree = AVL(root)
    tree.root.right_child = Node_AVL(2)
    tree.root.right_child.right_child = Node_AVL(3)
    tree.rotate_left(tree.root)
    assert tree.root.value == 2
    assert tree.root.left_child.value == 1
    assert tree.root.right_child.value == 3

def test_predecessor_avl():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    tree = AVL(numbers)
    assert tree.root.value == 4
    node = tree.predecessor(tree.root)
    assert node.value == 3

def test_delete_leaf_no_rotation():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    tree = AVL(numbers)
    assert tree.root.right_child.right_child.value == 7
    tree.delete(7)
    assert tree.root.right_child.right_child is None

def test_delete_root():
    numbers = [3, 2, 5, 1, 4, 6, 7]
    tree = AVL(numbers)
    assert tree.root.value == 3
    tree.delete(3)
    assert tree.root.value == 5
    assert tree.root.left_child.value == 2
    assert tree.root.right_child.value == 6
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.right_child.value == 4
    assert tree.root.right_child.right_child.value == 7
