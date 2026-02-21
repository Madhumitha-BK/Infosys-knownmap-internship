import spacy
import networkx as nx

nlp = spacy.load("en_core_web_sm")

def build_knowledge_graph(text: str):
    doc = nlp(text)
    G = nx.Graph()

    for ent in doc.ents:
        G.add_node(ent.text, label=ent.label_)

    return list(G.nodes)