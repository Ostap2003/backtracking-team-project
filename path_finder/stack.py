class Stack:
    """Simple stack implementation"""
    def __init__(self):
        """Initialize empty stack"""
        self.elements = []
        self.el_num = 0

    def add(self, elem):
        """Add element to the stack"""
        self.elements.append(elem)
        self.el_num += 1

    def pop_el_from_stack(self):
        """Pop the last element from the stack"""
        assert self.el_num > 0, "stack is empty, nothing to remove"
        self.el_num -= 1
        return self.elements.pop()
    
    def peek(self):
        """Return last added element to the stack"""
        return self.elements[-1]

    def __len__(self):
        """Return number of elements in the stack"""
        return self.el_num

    def __str__(self):
        """String representation of the stack"""
        return ", ".join([str(el) for el in self.elements])

