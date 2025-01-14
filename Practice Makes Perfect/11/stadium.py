class C:
    def __init__(self, sectors):
        self.sectors = sectors
    def m1(self, s, n):
        self.sectors[s] = n #if sector exists updates n of fans, otherwise adds new sector with the n
    def m2(self, s): #calculate sum of fans in the sectors in the str s
        total_fans = 0
        for sector in s:
            if sector in self.sectors:
                total_fans += self.sectors[sector]
        return total_fans
    
stadium = C({"A":120,"D":150,"G":90,"K":110})
stadium.m1("G",130)

print(stadium.m2("GD"))
print(stadium.m2("KEJ"))