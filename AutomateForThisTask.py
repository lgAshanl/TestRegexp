import asyncio.queues
import BadProgram


class AutomateForThisTask:
    def __init__(self, automate, symbol):
        # vertexes
        self.number_vertexes = automate.number_vertexes

        # edges
        self.e_edges = []
        self.x_edges = []
        for i in range(self.number_vertexes):
            self.e_edges.append([])
            self.x_edges.append([])

        for edge in automate.edges:
            if edge.symbol == '#':
                self.e_edges[edge.left].append(edge.right)
            if edge.symbol == symbol:
                self.x_edges[edge.left].append(edge.right)
        pass

    def search(self, symbol, n):
        mark = []
        for i in range(self.number_vertexes):
            mark.append(n + 1)

        q = asyncio.queues.Queue()
        q.put_nowait([0, n])
        while not q.empty():
            l = q.get_nowait()
            v = l[0]
            count = l[1]
            if count == 0:
                return True
            if mark[v] > count:
                mark[v] = count
            else:
                continue

            for u in self.x_edges[v]:
                if mark[u] >= count:
                    q.put_nowait([u, count - 1])

            for u in self.e_edges[v]:
                if mark[u] > count:
                    q.put_nowait([u, count])

        return False
