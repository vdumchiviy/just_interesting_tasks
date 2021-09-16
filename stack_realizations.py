# Write code that will implement a Stack
# Four functionalities should be available
# 1. Insert into begging of the stack
# 2. Remove items from the begging of the stack
# 3. Peek into current last item


# For example
# stack = Stack()
# stack.push(1)
# stack.peek()
# >> 1
# stack.push(2)
# stack.peek()
# >> 2
# stack.push(5)
# stack.push(10)
# stack.pop()
# >> 10
# stack.peek()
# >> 5

# Bonus 1 - don’t use any built in data sctructures.

# Bonus 2 - add additional method for return next item after specified index
# stack.get_next_after_ith(1) # 5 -> 2 -> 1
# >> 2

import copy
import queue


class Stack_with_List():
    """class realizes simple construction of stack using bulit-in type List
    """

    def __init__(self) -> None:
        self.st = []

    def push(self, new_value):
        self.st.append(new_value)

    def peek(self):
        if len(self.st) == 0:
            raise Exception('stack is empty')

        return self.st[-1]

    def pop(self):
        if len(self.st) == 0:
            raise Exception('stack is empty')

        val = self.peek
        self.st = self.st[0:len(self.st)-1]
        return val

    def get_next_after_ith(self, index):
        if len(self.st) == 0:
            raise Exception('stack is empty')
        if len(self.st) < index:
            raise Exception(f'element with index {index} absent')
        return self.st[index]

####


def raise_if_stack_empty(inner_method):
    def wrapper(self,  *args):
        if len(self.st) == 0:
            raise Exception('stack is empty')
        return inner_method(self, *args)
    return wrapper


def raise_if_out_of_index(inner_method):
    def wrapper(self, index):
        if len(self.st) < index:
            raise Exception(f'element with index {index} is absent')
        return inner_method(self, index)
    return wrapper


class Stack_with_wrapper():
    """class realize stack using wrapping and built-in type List
    """

    def __init__(self) -> None:
        self.st = []

    def push(self, new_value):
        self.st.append(new_value)

    @raise_if_stack_empty
    def peek(self):
        return self.st[-1]

    @raise_if_stack_empty
    def pop(self):

        val = self.peek
        self.st = self.st[0:len(self.st)-1]
        return val

    @raise_if_stack_empty
    @raise_if_out_of_index
    def get_next_after_ith(self, index):

        return self.st[index]






####
def raise_if_stack_empty(inner_method):
    def wrapper(self,  *args):
        if self.st.empty():
            raise Exception('stack is empty')
        return inner_method(self, *args)
    return wrapper


def raise_if_out_of_index(inner_method):
    def wrapper(self, index):
        if self.st.qsize() < index:
            raise Exception(f'element with index {index} is absent')
        return inner_method(self, index)
    return wrapper

class Stack_with_wrapper_and_queue():
    """class realize stack using wrapping and Lifoqueue instead of built-in type List
    ! But class also uses import - "queue" and "copy" 
    """

    def __init__(self) -> None:
        self.st = queue.LifoQueue()

    def __str__(self) -> str:
        tmp = queue.LifoQueue()
        tmp.queue = copy.deepcopy(self.st.queue)
        s = ""
        while not tmp.empty():
            val = tmp.get()
            s = s + "->" + str(val)
        return s

    def push(self, new_value):
        self.st.put(new_value)

    @raise_if_stack_empty
    def peek(self):
        val = self.st.get()
        self.push(val)
        return val

    @raise_if_stack_empty
    def pop(self):
        return self.st.get()

    @raise_if_stack_empty
    @raise_if_out_of_index
    def get_next_after_ith(self, index):
        tmp = queue.LifoQueue()
        tmp.queue = copy.deepcopy(self.st.queue)
        for _ in range(tmp.qsize() - index):
            val = tmp.get()
        return val


# For example
stack = Stack_with_wrapper_and_queue()
# stack.pop()
stack.push(1)
stack.peek()
stack.push(2)
stack.peek()
stack.push(5)
stack.push(10)
print(stack)
# stack.pop()
# stack.peek()
# print(stack)
print(stack.get_next_after_ith(1))
