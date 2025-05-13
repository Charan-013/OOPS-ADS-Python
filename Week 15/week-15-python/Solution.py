class Digraph:
    def __init__(self, numV):
        self.numV = numV
        self.graph = []

    def add_edge(self, from_vertex, to_vertex):
        edge_data = [from_vertex, to_vertex]
        self.graph.append(edge_data)


class PageRank:
    def __init__(self, graph):
        self.graph = graph
        self.prValues = {}

        edge_list = self.graph.graph
        total_edges = len(edge_list)

        if total_edges == 0:
            self.prValues[0] = 1
        else:
            initial_score = 1 / total_edges
            for link in edge_list:
                source_node = link[0]
                if source_node not in self.prValues:
                    self.prValues[source_node] = initial_score

    def get_pr(self, value):
        if value in self.prValues:
            return self.prValues[value]
        else:
            return 1



def read_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        content_lines = f.readlines()
    return content_lines

class WebSearch:
    def __init__(self, pr, filename):
        self.lookupTable = pr
        raw_data = read_file(filename)
        doc_keyword_map = {}

        for entry in raw_data:
            cleaned_entry = entry.strip()
            if ": " in cleaned_entry:
                doc_info = cleaned_entry.split(": ")
                doc_num = int(doc_info[0])
                keyword_list = doc_info[1].split()
                doc_keyword_map[doc_num] = keyword_list

        self.lookupTable = doc_keyword_map

    def i_am_feeling_lucky(self, query):
        for document_id, keywords in self.lookupTable.items():
            if query in keywords:
                return document_id
        return -1
