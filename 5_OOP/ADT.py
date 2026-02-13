## using a list
def create_ADT():
    return []

def push_ADT(thing,item):
    thing.append(item)

def pop_ADT(thing):
    try :
        return thing.pop()
    except:
        return None
