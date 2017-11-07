import BadProgram


class Edge:
    # from 'left' fo 'right' by 'symbol'
    def __init__(self, left, right, symbol):
        self.left = left
        self.right = right
        self.symbol = symbol

    def shift(self, shift):
        self.left += shift
        self.right += shift


class Automate:
    def __init__(self, symbol):
        # number of vertexes
        self.number_vertexes = 1
        if symbol != '#':
            self.number_vertexes += 1

        # vertex 0 is start
        # terminal vertexes
        self.terminal_vertexes = [self.number_vertexes - 1]

        # edge
        if symbol != '#':
            self.edges = [Edge(0, 1, symbol)]

    def shift_edges(self, shift):
        for edge in self.edges:
            edge.shift(shift)

    def merge(self, another):
        if type(another) == Automate:
            # edges
            another.shift_edges(self.number_vertexes)
            self.edges += another.edges
            for term in self.terminal_vertexes:
                self.edges.append(Edge(term, self.number_vertexes, '#'))

            # terminals
            self.terminal_vertexes = []
            for term in another.terminal_vertexes:
                self.terminal_vertexes.append(term + self.number_vertexes)

            # vertexes
            self.number_vertexes += another.number_vertexes

        else:
            raise BadProgram.BadProgram("Automate.merge")
        return self

    def add(self, another):
        if type(another) == Automate:
            # edges
            self.shift_edges(1)
            another.shift_edges(self.number_vertexes + 1)
            self.edges += another.edges
            self.edges.append(Edge(0, 1, '#'))
            self.edges.append(Edge(0, self.number_vertexes + 1, '#'))

            # terminals
            for i in range(len(self.terminal_vertexes)):
                self.terminal_vertexes[i] += 1
            for term in another.terminal_vertexes:
                self.terminal_vertexes.append(term + self.number_vertexes + 1)

            # vertexes
            self.number_vertexes += another.number_vertexes + 1

        else:
            raise BadProgram.BadProgram("Automate.add")
        return self

    def star(self):
        # edges
        self.shift_edges(1)
        self.edges.append(Edge(0, 1, '#'))
        for term in self.terminal_vertexes:
            self.edges.append(Edge(term + 1, 0, '#'))

        # terminals
        self.terminal_vertexes = [0]

        # vertexes
        self.number_vertexes += 1
        return self
