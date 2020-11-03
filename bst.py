# bst.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================


class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        return self.grade < kq.grade

    def __gt__(self, kq):
        return self.grade > kq.grade

    def __eq__(self, kq):
        return self.grade == kq.grade

    def __str__(self):
        if self.grade is not None:
            student_name = str(self.name)
            student_grade = str(self.grade)
            return student_name + " has a grade of " + student_grade

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """
        node = TreeNode(val)
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if node.val < current.val:
                current = current.left
            else:
                current = current.right
        if parent is None:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

    def in_order_traversal(self, cur_node=None, visited=None) -> []:
            """
            Perform in-order traversal of the tree and return a list of visited nodes
            """
            if visited is None:
                # first call to the function -> create container to store list of visited nodes
                # and initiate recursive calls starting with the root node
                visited = []
                self.in_order_traversal(self.root, visited)

            # not a first call to the function
            # base case - reached the end of current subtree -> backtrack
            if cur_node is None:
                return visited

            # recursive case -> sequence of steps for in-order traversal:
            # visit left subtree, store current node value, visit right subtree
            self.in_order_traversal(cur_node.left, visited)
            visited.append(cur_node.val)
            self.in_order_traversal(cur_node.right, visited)
            return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        if visited == None:
            visited = []
            self.pre_order_traversal(self.root, visited)

        if cur_node == None:
            return visited

        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left, visited)
        self.pre_order_traversal(cur_node.right, visited)
        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        if visited == None:
            visited = []
            self.post_order_traversal(self.root, visited)

        if cur_node == None:
            return visited

        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        visited.append(cur_node.val)
        return visited


    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """
        current = self.root
        while current != None:
            if current.val == kq:
                return True
            elif kq < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """
        while node.left != None:
            node = node.left
        return node

    def get_parent(self, node):
        """
        Accepts the node as an argument and finds its parent
        node and returns it.
        """

        if node is self.root:
            return None
        else:
            current = self.root
            while current != node:
                if node.val < current.val:
                    if current.left.val == node.val:
                        return current
                    else:
                        current = current.left
                else:
                    if current.right.val == node.val:
                        return current
                    else:
                        current = current.right

            return False
    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """
        if kq == self.root.val:
            self.remove_first()
            return

        if self.contains(kq):
            node = self.root
            while node.val != kq:
                if kq < node.val:
                    node = node.left
                else:
                    node = node.right

        else:
            return False

        kq_parent = self.get_parent(node)

        if node.left == None and node.right == None:
            if node.val < kq_parent.val:
                kq_parent.left = None
            else:
                kq_parent.right = None
        else:
            if node.right == None:
                next_node = node.left
                if node.val < kq_parent.val:
                    kq_parent.left = next_node
                else:
                    kq_parent.right = next_node

                node.left = None
                node.right = None
                return True
            else:
                next_node = self.left_child(node.right)

            next_node_parent = self.get_parent(next_node)
            next_node.left = node.left
            if next_node != node.right:
                next_node_parent = next_node.right
                next_node.right = node.right

            if node.val < kq_parent.val:
                kq_parent.left = next_node
            else:
                kq_parent.right = next_node

        node.left = None
        node.right = None
        return True

    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        if self.root == None:
            return None
        else:
            return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        if self.root == None:
            return False
        else:
            if self.root.left == None and self.root.right == None:
                self.root = None
                return True
            elif self.root.right == None:
                self.root = self.root.left
                return True
            else:
                next_node = self.left_child(self.root.right)

                next_node_parent = self.get_parent(next_node)
                if next_node_parent == self.root:
                    next_node.left = self.root.left
                    self.root = next_node
                    return True
                else:
                    next_node.left = self.root.left
                    next_node_parent.left = next_node.right
                    next_node.right = self.root.right
                    self.root = next_node
                    return True
