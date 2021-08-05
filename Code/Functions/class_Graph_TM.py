import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.community as nxcom
from Functions.class_TM import TM

class Graph_TM:
    def __init__(self):
        self.Graph = nx.Graph()
        self.edges2add = []
        self.communities = None
        
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
                     plot_size = (15, 10),
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
            plt.savefig(f'../TeX/img/{filename}.png')
            print(f'Graph saved as ../TeX/img/{filename}.png')

    def find_communities(self):
        self.communities = sorted(nxcom.greedy_modularity_communities(self.Graph), key = len, reverse = True)
        
        return self.communities
    
    '''Next 3 functions are from https://orbifold.net/default/community-detection-using-networkx/'''
    def set_node_community(self):
        '''Add community to node attributes'''
        if self.communities == None:
            _ = self.find_communities()
        for c, v_c in enumerate(self.communities):
            for v in v_c:
                # Add 1 to save 0 for external edges
                self.Graph.nodes[v]['community'] = c + 1

    def set_edge_community(self):
        '''Find internal edges and add their community to their attributes'''
        for v, w, in self.Graph.edges:
            if self.Graph.nodes[v]['community'] == self.Graph.nodes[w]['community']:
                # Internal edge, mark with community
                self.Graph.edges[v, w]['community'] = self.Graph.nodes[v]['community']
            else:
                # External edge, mark as 0
                self.Graph.edges[v, w]['community'] = 0

    def get_color(self, i, r_off = 1, g_off = 1, b_off = 1):
        '''Assign a color to a vertex.'''
        r0, g0, b0 = 0, 0, 0
        n = 16
        low, high = 0.1, 0.9
        span = high - low
        r = low + span * (((i + r_off) * 3) % n) / (n - 1)
        g = low + span * (((i + g_off) * 5) % n) / (n - 1)
        b = low + span * (((i + b_off) * 7) % n) / (n - 1)
        return (r, g, b)
    
    '''Next function is for plotting using the above functions (using same reference)'''
    def plot_communities(self,
                         edge_color = 'darkgray',
                         k = 0.001,
                         width = 0.01,
                         node_size = 3,
                         plot_size = (15, 10),
                         max_connected_components = 1,
                         filename = ''):
        if self.communities == None:
            _ = self.find_communities()
        
        G = Graph_TM()
        connected_components = list(nx.connected_components(self.Graph))
        if type(max_connected_components) == int and len(connected_components) > max_connected_components:
            subgraph_nodes = connected_components[0]
            for connected_component in connected_components[1:max_connected_components]:
                subgraph_nodes = subgraph_nodes.union(connected_component)
                
            G.Graph = nx.subgraph(self.Graph, subgraph_nodes)
        elif max_connected_components == 'all':
            G.Graph = self.Graph
        else:
            G.Graph = self.Graph        
        
        G.set_node_community()
        G.set_edge_community()

        node_color = [G.get_color(G.Graph.nodes[v]['community']) for v in G.Graph.nodes]
        external = [(v, w) for v, w in G.Graph.edges if G.Graph.edges[v, w]['community'] == 0]
        internal = [(v, w) for v, w in G.Graph.edges if G.Graph.edges[v, w]['community'] > 0]
        internal_color = ['black' for e in internal]
        plt.figure(figsize = plot_size)
        pos = nx.spring_layout(G.Graph, k = k)
        
        nx.draw_networkx_edges(G.Graph,
                               pos = pos,
                               edgelist = external,
                               width = width,
                               edge_color = edge_color)
        
        nx.draw_networkx_edges(G.Graph,
                               pos = pos,
                               edgelist = internal,
                               width = width,
                               edge_color = edge_color)

        nx.draw(G.Graph,
                pos = pos,
                node_color = node_color,
                edge_color = edge_color,
                node_size = node_size,
                width = width)
        
        if filename != '':
            plt.savefig(f'../TeX/img/{filename}.png')
            print(f'Graph saved as ../TeX/img/{filename}.png')