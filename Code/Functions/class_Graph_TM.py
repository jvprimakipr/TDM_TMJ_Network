import networkx as nx
from Functions.class_TM import TM
import matplotlib.pyplot as plt

class Graph_TM:
    def __init__(self):
        self.Graph = nx.Graph()
        self.edges2add = []
        
    def data2insert(self, file):
        cb = TM()
        cb.unpack(file)
        weights = []
        
        for row in cb.data.iterrows():
            for i in range(1, len(row[1])):
                if row[1][i] == '':
                    break
                for j in range(i + 1, len(row[1])):
                    if row[1][j] == '':
                        break
                    if [row[1][i], row[1][j]] in self.edges2add:
                        index = self.edges2add.index([row[1][i], row[1][j]])
                        weights[index] += 1
                    elif [row[1][j], row[1][i]] in self.edges2add:
                        index = self.edges2add.index([row[1][j], row[1][i]])
                        weights[index] += 1
                    else:
                        self.edges2add.append([row[1][i], row[1][j]])
                        weights.append(1)

        for i in range(len(self.edges2add)):
            self.edges2add[i].append(weights[i])
            self.edges2add[i] = tuple(self.edges2add[i])
    
    def insert_cb(self, file):
        self.data2insert(file)
        inserting = []
        for u, v, w in self.edges2add:
            if (u, v) in self.Graph.edges():
                self.Graph[u][v]['weight'] += w
            else:
                inserting.append((u, v, w))
        
        self.Graph.add_weighted_edges_from(inserting)
        self.edges2add = []
        
    def insert_cbs(self, list_of_files):
        for file in list_of_files:
            self.insert_cb(file)
            
    def plot_network(self,
                     node_color = 'steelblue',
                     edge_color = 'darkgray',
                     k = 0.001,
                     max_width = 10,
                     max_node_size = 100,
                     plot_size = (15, 8),
                     highlight = ['Mônica', 'Cebolinha', 'Cascão', 'Magali', 'Chico Bento'],
                     highlight_color = 'red',
                     max_connected_components = 1,
                     filename = ''):
        
        connected_components = list(nx.connected_components(self.Graph))
        if type(max_connected_components) == int and len(connected_components) > max_connected_components:
            subgraph_nodes = connected_components[0]
            for connected_component in connected_components[1:max_connected_components]:
                subgraph_nodes = subgraph_nodes.union(connected_component)
                
            G = nx.subgraph(self.Graph, subgraph_nodes)
        elif max_connected_components == 'all':
        	G = self.Graph
        else:
            G = self.Graph
        
        pos = nx.spring_layout(G, k = k)
        plt.figure(figsize = plot_size)
        node_colors = []
        degrees = list(dict(nx.degree(G)).values())
        node_size = [max_node_size * degree / max(degrees) for degree in degrees]
        width = [G[u][v]['weight'] for u, v in G.edges()]
        width = [max_width * v / max(width) for v in width]

        for node in G.nodes():
            if node in highlight:
                node_colors.append(highlight_color)
            else:
                node_colors.append(node_color)

        nx.draw_networkx_edges(G,
                               pos = pos,
                               edgelist = G.edges(),
                               width = width,
                               edge_color = edge_color)

        nx.draw(G,
                pos = pos,
                node_color = node_colors,
                edge_color = edge_color,
                node_size = node_size)
        
        if filename != '':
            plt.savefig('../TeX/img/{}.png'.format(filename))
            print('Graph saved as ../TeX/img/{}.png'.format(filename))
