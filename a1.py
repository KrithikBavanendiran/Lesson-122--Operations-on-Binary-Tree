#from binarytree import Node
class Node:
    def  __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                print(f"Inserted {data} to the left of {self.data}.")
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                print(f"Inserted {data} to the right of {self.data}.")
            else:
                self.right.insert(data)
        else:
            print(f"{data} already exists in the tree.")

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()

if __name__ == "__main__":
    n=Node(12)
    n.insert(6)
    n.insert(14)
    n.insert(3)

    n.print_tree()
