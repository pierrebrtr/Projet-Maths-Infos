from math import *
import math
import random



class GPoly():

    def __init__(self,n):
        self.n = n

    def generate(self,n):
        x = []
        y = []
        for i in range(n):
            x.append(random.randint(1,500 -1))
            y.append(random.randint(1,500 -1))

        xc = 0
        yc = 0
        for i in range(n):
            xc = xc + x[i]
            yc = yc + y[i]
        xc = xc/n
        yc = yc / n
        center = (xc,yc)
        angles = []
        for i in range(n):
            angles.append(math.atan2(x[i]-center[0],y[i] - center[1]))
        ##sorting the points:
        sort_tups = sorted([(i,j,k) for i,j,k in zip(x,y,angles)], key = lambda t: t[2])

        ##making sure that there are no duplicates:
        if len(sort_tups) != len(set(sort_tups)):
            raise Exception('two equal coordinates -- exiting')

        x,y,angles = zip(*sort_tups)
        x = list(x)
        y = list(y)

        m = self.merge(x,y)
        print("SAVE",m)
        return m

    def merge(self,list1, list2):

        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
        return merged_list
