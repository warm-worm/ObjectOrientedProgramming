# first quadrant = both point coordinates are greater than 0
class C:
    def __init__(self, points):
        self.points = points
    def m(self, n):
        count = 0
        for point in self.points:
            if point[0] > 0 and point[1] > 0: #is it in the first quadrant
                count += 1
        return count >= n #true if there are at least n points in the first quadrant
    
c = C([[2,3],[1,8],[-6,4],[3,-7]])

print(c.m(2))
print(c.m(3))