import networkx as nx
import matplotlib.pyplot as plt

def build_knowledge_graph(triples):
    """
    triples: list of (subject, relation, object)
    """
    G = nx.DiGraph()

    for subj, rel, obj in triples:
        G.add_node(subj)
        G.add_node(obj)
        G.add_edge(subj, obj, relation=rel)

    return G

def visualize_knowledge_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

# Example usage:
if __name__ == "__main__":
    triples = [
        ("AI", "transforms", "Healthcare"),
        ("Google", "invests_in", "AI"),
        ("India", "hosts", "Research Center")
    ]

    G = build_knowledge_graph(triples)
    print("Nodes:", G.nodes())
    print("Edges with relations:")
    for u, v, data in G.edges(data=True):
        print(f"{u} -[{data['relation']}]-> {v}")

    visualize_knowledge_graph(G)
