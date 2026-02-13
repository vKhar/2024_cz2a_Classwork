class Stack:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.items = [" " for _ in range(capacity) ]
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def get_capacity(self):
        return self.capacity

    def get_items(self):
        return self.items[::-1]

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.top]

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.items[self.top]
        self.items[self.top] = " "
        self.top -= 1
        return item

# %%
def initialise_game():
    """
    Creates three Stack objects and initialises the first two tubes.
    Returns a list containing the three Stack object
    """
    stack1 = Stack()
    stack1.push("B")
    stack1.push("B")
    stack1.push("R")
    
    stack2 = Stack()
    stack2.push("B")
    stack2.push("R")
    stack2.push("R")
    
    stack3 = Stack()
    
    return [stack1, stack2, stack3]

def display_game(tubes):
    c = tubes[0].capacity
    display = [[None for _ in range(c)] for _  in range(c)]
    for i in range(c):
        for j,item in enumerate(tubes[i].get_items()):
            display[j][i] = item
    for r in display:
        for i in range(len(r)):
            print(f"[{r[i]}]",end=" " )
        print()
    print(f"{'0':^3} {'1':^3} {'2':^3}" )


def valid_move(tubes, source, destination):
    no_tubes = len(tubes)
    if not ( (-1 < source < no_tubes) and ( -1 < destination < no_tubes) ) :
        return False
    else:
        source_colour = tubes[source].peek()
        if source_colour == None:
            return False
        if tubes[destination].is_full():
            return False
        destination_colour = tubes[destination].peek()
        if (destination_colour == source_colour) or destination_colour == None:
            return True
        else:
            return False


def move(tubes, source, destination):
    if not valid_move(tubes, source, destination):
        return False
    else:
        ball = tubes[source].pop()
        tubes[destination].push(ball)
        return True

def game_won(tubes):
    for tube in tubes:
        if tube.is_empty():
            continue
        items = [ x for x in tube.get_items() if x != " "]
        for item in items[1:]:
            if item != items[0]:
                return False
    return True
