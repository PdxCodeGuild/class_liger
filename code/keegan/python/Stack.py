class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self):
        self.top_node = None
        self.__height = 0

    def push(self, value):
        '''add a node to the top'''
        # instantiate a new Node object
        new_node = Node(value)

        # if the Stack is empty, make the new_node the top_node
        # if self.top_node is None:
        if not self.top_node:
            self.top_node = new_node

        # otherwise, the new_node becomes the top and the previous top becomes the next value
        else:
            # point the new node at the current top_node
            new_node.next = self.top_node

            # put the new node on the top
            self.top_node = new_node

        # indicate that the height has increased
        self.__height += 1
    
    
    def pop(self):
        '''remove a node from the top'''

        if self.__height == 0:
            raise IndexError("pop from empty Stack")

        # create a temporary variable to store the top node
        temp = self.top_node

        # make the top_node's next node the new top_node
        self.top_node = temp.next

        # decrease the height property of the Stack
        self.__height -= 1

        # return the popped node
        return temp


    def peek(self):
        '''returns the top_node's value or None if the Stack is empty'''
        return self.top_node

    def clear(self):
        '''Continually pop nodes off the top of the stack until it is empty'''
        # while self.__height > 0:
        # while self.__height != 0:
        while self.__height:
            self.pop()


    def search(self, target):
        '''Look at each node and return the position of the node containing the desired value'''
        # start at the top_node
        current_node = self.top_node

        index = 0
        while current_node is not None:
            # check if the current_node's value is the target value
            # if str(current_node) == target:
            if current_node.value == target:
                # return the index of the current_node
                return index
            
            # increment the index
            index += 1

            # move the current_node to its next node
            current_node = current_node.next

        # if the loop runs all the way through,
        # the target value wasn't found
        return None


    def __len__(self):
        '''length representation of the stack'''
        return self.__height


    def __str__(self):
        '''Print a representation of the Stack'''
        if self.__height == 0:
            output = 'The stack is empty.'

        else:
            # start with a blank string
            output = '\n'

            # initialize the current_node as the top_node (i.e. start at the top)
            current_node = self.top_node

            # loop until the current_node is None
            while current_node is not None:
                # concatenate the current_node's value to the output string
                output += current_node.value + '\n'

                # move the current_node to its next node
                current_node = current_node.next


        return output
    


if __name__ == '__main__':
    # node_1 = Node('A')
    # node_2 = Node('B')

    # node_1.next = node_2
    # print(node_1.next) # 'B'

    # instantiate a Stack
    stack = Stack()

    # print(stack.top_node) # None
    # print(stack.__height) # Error, private attribute

    stack.push('A')
    stack.push('B')
    stack.push('C')

    # print(stack.peek()) # C

    # print(stack.pop()) # C
    # print(stack.peek()) # B
    print(stack)

    print(stack.search('B'))

    # print(len(stack)) # 3

    # stack.pop() # B
    # stack.pop() # A
    # stack.pop() # IndexError: pop from empty Stack

    # stack.clear()

    # print(stack)

