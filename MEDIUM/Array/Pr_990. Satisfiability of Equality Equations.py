class UnionFind:
    def __init__(self):
        self.arr = [i for i in range(26)]
    
    def union(self, i, j):
        rootI = self.find(i)
        rootJ = self.find(j)
        for ind in range(len(self.arr)):
            if self.arr[ind] == rootJ:
                self.arr[ind] = rootI

    def find(self, i):
        return self.arr[i]

    def check(self, i, j):
        return self.arr[i] != self.arr[j]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eqEquations = [i for i in equations if i[1] == '=']
        neEquations = [i for i in equations if i[1] == '!']
        uf = UnionFind()
        for eq in eqEquations:
            uf.union(ord(eq[0])-97, ord(eq[-1])-97)

        for eq in neEquations:
            if uf.check(ord(eq[0])-97, ord(eq[-1])-97) == False:
                return False
        return True
