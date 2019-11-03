
import networkx as nx

def make_graph(data):
    net = nx.Graph()
    print(data)
    net.add_nodes_from(data.keys())

    edges = []
    
    return net 

if __name__=="__main__":
    from dataset import Dataset 
    data = Dataset()
    data = data.load()
    make_graph(data)
