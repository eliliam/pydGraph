import math
import matplotlib.pyplot as plt
import networkx as nx

class DGraph:
    def __init__(self, typeList:list):
        self.typeList = typeList
        if not all(x in typeList for x in ["undirected", "directed"]):
            self.typeList.append("undirected")
        if "simple" in typeList:
            self.typeList = ["undirected", "simple", "unweighted"]
            self.Graph = nx.Graph()
        if "undirected" not in typeList and "directed" not in typeList:
            typeList.append("undirected")
            self.Graph = nx.Graph()
        if "directed" in typeList:
            self.Graph = nx.DiGraph()
        else:
            self.Graph = nx.Graph()
    def add_node(self, node):
        self.Graph.add_node(node)

    def add_multiple_nodes(self, nodes:list):
        self.Graph.add_nodes_from(nodes)

    def add_edge(self, connectingNodes, weight=None):
        if "undirected" in self.typeList:
            self.Graph.add_edge(connectingNodes[0], connectingNodes[1], weight=weight)

    def add_multiple_edges(self, edges:list):
        self.Graph.add_edges_from(edges)

    def add_multiple_weighted_edges(self, edges:dict):
        self.add_multiple_edges(list(edges.keys()))
        if "weighted" in self.typeList:
            nx.set_edge_attributes(self.Graph, edges)

    def remove_edge(self, connectingNodes):
        self.Graph.remove_edge(connectingNodes[0], connectingNodes[1])

    def remove_node(self, node):
        self.Graph.remove_node(node)

    def list_nodes(self):
        return self.Graph.nodes()

    def shortest_path(self, start, goal, weight=None, type="shortest"):
        if type is "shortest":
            return nx.shortest_path(self.Graph, start, goal, weight=weight)
        elif type is "dijkstra":
            return nx.dijkstra_path(self.Graph, start, goal, weight=weight)

    def show_path(self, route):
        pos = nx.spring_layout(self.Graph)
        labels = {}
        for node in self.Graph.nodes():
            labels[node] = node

        nx.draw_networkx_nodes(self.Graph,pos=pos)
        nx.draw_networkx_labels(self.Graph,pos=pos, labels=labels)
        route_edges = [(route[n], route[n + 1]) for n in range(len(route) - 1)]
        nx.draw_networkx_edges(self.Graph, pos)
        nx.draw_networkx_edges(self.Graph, pos=pos, edgelist=route_edges, edge_color='r', width=10)
        plt.show()

    def show(self):
        arrows = True if "directed" in self.typeList else False
        pos = nx.spring_layout(self.Graph)
        labels = {}
        for node in self.Graph.nodes():
            labels[node] = node
        nx.draw_networkx_nodes(self.Graph, pos)
        nx.draw_networkx_edges(self.Graph, pos)
        nx.draw_networkx_labels(self.Graph, pos, labels, font_size=14, font_color="white", font_weight="bold", arrows=arrows, k=3)
        nx.draw(self.Graph, pos)
        plt.show()

dg = DGraph(["undirected", "weighted"])
values = {
    (1,2):{"weight":0.1},
    (2,3):{"weight":0.1},
    (3,4):{"weight":0.1},
    (4,5):{"weight":0.1},
    (2,4):{"weight":0.1},
    (3,5):{"weight":1.1},
    (3,1):{"weight":1.1}}
dg.add_multiple_weighted_edges(values)
dRoute = dg.shortest_path(1,5,weight="weight",type="shortest")
print(dRoute)
dg.show_path(dRoute)
# dg.show_path(dRoute)