import random
class Car_Detector:
    def __init__(self,n):
        self.size = n
        self.state = ["Red","Black",'White','Blue',"Green","Yellow","Orange","Pink"]
        self.weights=[3,3,4,2,1,1,1,1]
        self.count = -1

    def __iter__(self):
        self.count = -1 # reset the internal counter
        return self

    def __next__(self):
        self.count+=1
        if self.count < self.size:
            return random.choices(self.state,self.weights,k=1)[0]
        else:
            raise StopIteration()


