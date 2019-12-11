# testCase = int(input())

# for i in range(testCase):
#     print('Scenario #{}:'.format(i+1))
#     bugs, interactions = [int(x) for x in input().split()]
#     res = "No suspicious bugs found!"
#     sex = [0] * (bugs+1)
#     for i in range(interactions):
#         x, y = [int(z) for z in input().split()]
#         print(x, y)
#         print(bugs)
#         if x>bugs or y>bugs:
#             res = "Suspicious bugs found!"
#             break
#         elif sex[x] == 0 and sex[y] == 0:
#             sex[x] = 1
#             sex[y] = 2
#         elif sex[x] == 1 and sex[y] == 0:
#             sex[y] = 2
#         elif sex[x] == 2 and sex[y] == 0:
#             sex[y] = 1
#         elif sex[x] == 0 and sex[y] == 1:
#             sex[x] = 2
#         elif sex[x] == 0 and sex[y] == 2:
#             sex[x] = 1
#         elif (sex[x] == 1 and sex[y] == 1) or (sex[x] == 2 and sex[y] == 2):
#             print("entrou")
#             res = "Suspicious bugs found!"
#             break
#         print(sex)
#     print(res)

from collections import defaultdict


class Grafo(object):

    def __init__(self, arestas, direcionado=False):
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)


    def get_vertices(self):
        return list(self.adj.keys())


    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            self.adiciona_arco(u, v)
            
    def adiciona_arco(self, u, v):
        self.adj[u].add(v)
        # if not self.direcionado:
        #     self.adj[v].add(u)



testCase = int(input())
for i in range(testCase):
    bugs, interactions = [int(x) for x in input().split()]
    arestas = []
    for i in range(interactions):
        x, y = [int(z) for z in input().split()]
        arestas.append((x,y))

    grafo = Grafo(arestas, direcionado=True)
    print(grafo)
    print(arestas)
