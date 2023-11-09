class OneFactoriser:
    def __init__(self, n=8):
        self.n = n

    def oneFactorisations(self):
        self.createX1()
        self.initialSol = {frozenset(self.x1)}
        self._edgesToAdd = self.createEdges()
        self._oneFactors = self.createOneFactors()
        self._w1 = []
        self.createW1()
        self._x1Mappings = []
        self._oneFactorisations = []
        self._schedules = []
        self.createBaseOneFactorisations(self.getInitialSol())
        self.applyMappings()

    def createX1(self):
        self.x1 = set()
        for i in range(0, self.n, 2):
            self.x1.add(frozenset((i, i + 1)))

    def getW1(self):
        return self._w1[:]

    def getSchedules(self):
        return self._schedules[:]

    def getX1Mappings(self):
        return self._x1Mappings[:]

    def getOneFactorisations(self):
        return self._oneFactorisations[:]

    def getOneFactors(self):
        return self._oneFactors[:]

    def getInitialSol(self):
        return set(self.initialSol)

    def getEdges(self):
        return self._edgesToAdd[:]

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
                solution.append(set())
                oneFactor = set()
                oneFactor.add(frozenset({0, i + 2}))
                self.createOneFactors(solution, oneFactor, 1, i)

            for i in range(self.n - 2):
                solution[i] = frozenset(solution[i])

            return solution
        # recursive loop
        else:
            maxDepth = self.n // 2 - 1
            for edge in self._edgesToAdd:
                if edge.isdisjoint([number for pair in oneFactor for number in pair]):
                    oneFactor.add(edge)

                    if depth == maxDepth:
                        if oneFactor not in solution[i]:
                            solution[i].add(frozenset(oneFactor))
                        oneFactor.remove(edge)
                        break

                    self.createOneFactors(solution, oneFactor, depth + 1, i)
                    oneFactor.remove(edge)

    def createBaseOneFactorisations(self, currentSolution, depth=0):
        # generate all the one-factorisations containing x1
        maxDepth = self.n - 3
        for oneFactor in self.getOneFactors()[depth]:
            if oneFactor.isdisjoint(
                [pairing for oneFactor in currentSolution for pairing in oneFactor]
            ):
                currentSolution.add(oneFactor)

                # at this depth the one-factorisation is complete
                if depth == maxDepth:
                    self._oneFactorisations.append(frozenset(currentSolution))
                    currentSolution.remove(oneFactor)
                    break

                self.createBaseOneFactorisations(currentSolution, depth + 1)
                currentSolution.remove(oneFactor)

    def createW1(self, currentSol=None, depth=0):
        if self.n < 6:
            self._w1.append(self.x1)
            return

        if currentSol == None:
            currentSol = list(range(self.n))

        maxDepth = self.n - 4

        for i in range(depth + 3, self.n):
            currentSol[depth + 3], currentSol[i] = currentSol[i], currentSol[depth + 3]

            if depth == maxDepth:
                setSol = sorted(
                    [
                        sorted([currentSol[i], currentSol[i + 1]])
                        for i in range(0, self.n, 2)
                    ]
                )
                setSol = [i for sublist in setSol for i in sublist]
                if setSol not in self._w1:
                    self._w1.append(setSol[:])
            else:
                self.createW1(currentSol, depth + 1)
            currentSol[depth + 3], currentSol[i] = currentSol[i], currentSol[depth + 3]

    def getOneFactorisationsAsLists(self):
        result = self.getOneFactorisations()
        for i in range(len(result)):
            result[i] = list(result[i])
            for j in range(len(result[i])):
                result[i][j] = list(result[i][j])
                for k in range(len(result[i][j])):
                    result[i][j][k] = list(result[i][j][k])
                result[i][j].sort()
            result[i].sort()
        return result

    def applyMappings(self):
        w1 = self.getW1()[1:]

        for b1F in self.getOneFactorisationsAsLists():
            for mapping in w1:
                oneFactorisationToAdd = set()

                for onefactor in b1F:
                    oneFactorToAdd = set()

                    for pairing in onefactor:
                        pairingToAdd = set()

                        for team in pairing:
                            pairingToAdd.add(mapping[team])

                        oneFactorToAdd.add(frozenset(pairingToAdd))

                    oneFactorisationToAdd.add(frozenset(oneFactorToAdd))

                self._oneFactorisations.append(frozenset(oneFactorisationToAdd))
