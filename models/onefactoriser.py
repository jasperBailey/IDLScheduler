from itertools import combinations


class OneFactoriser:
    def __init__(self, n=8):
        self.n = n
        self.initialSol = self.createInitialSol()
        self.edgesToAdd = self.createEdges()
        self.oneFactors = self.createOneFactors()

    def getOneFactors(self):
        return self.oneFactors

    def getInitialSol(self):
        return set(self.initialSol)

    def getEdges(self):
        return self.edgesToAdd[:]

    def createInitialSol(self):
        result = set()
        for i in range(0, self.n, 2):
            result.add(frozenset((i, i + 1)))
        return result

    def createEdges(self):
        pairings = []

        # create list of possible matchups in each time period (week)
        for i in range(1, self.n):
            for j in range(i, self.n):
                if i == j or (not i % 2 and j == i + 1):
                    continue
                pairings.append(frozenset([i, j]))
        return pairings

    def createOneFactors(self, solution=None, oneFactor=None, depth=0, i=-1):
        # returns a list of n-2 lists, each sublist is the set of one-factors
        # containing {0, i+2}

        # initial setup
        if solution == None:
            solution = []
            for i in range(self.n - 2):
                solution.append([])
                oneFactor = set()
                oneFactor.add(frozenset({0, i + 2}))
                self.createOneFactors(solution, oneFactor, 1, i)

            return solution
        # recursive loop
        else:
            for edge in self.edgesToAdd:
                if edge.isdisjoint([number for pair in oneFactor for number in pair]):
                    oneFactor.add(edge)

                    if depth == self.n // 2 - 1:
                        if oneFactor not in solution[i]:
                            solution[i].append(set(oneFactor))
                        oneFactor.remove(edge)
                        break

                    self.createOneFactors(solution, oneFactor, depth + 1, i)
                    oneFactor.remove(edge)
