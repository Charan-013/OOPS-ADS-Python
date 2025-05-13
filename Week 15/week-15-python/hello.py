class PageRank:
    def __init__(self, graph):
        self.graph = graph
        # self.l = len(graph)
        self.prValues = {}
        # for i in range(len(self.l)):
        #     self.prValues[i] = 1.0 / self.l
        
        e = self.graph.graph
        lenth = len(e)

        if lenth == 0:
            self.prValues[0] = 1
        else:
            score = 1 / lenth
            for i in e:
                s_node = i[0]
                if s_node not in self.prValues:
                    self.prValues[s_node] = score

    def get_pr(self, v):
        if v in self.prValues:
            return self.prValues[v]
        else:
            return 1

    def __str__(self):
        result = []
        for v, pr in sorted(self.prValues.items()):
            result.append(f"{v} - {pr:.6f}")
        return "\n".join(result)

    



class Digraph:
    def __init__(self, num):
        self.num = num
        self.graph = []

    def add_edge(self, from_ver, to_ver):
        data = [from_ver, to_ver]
        self.graph.append(data)



def read_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        content = f.readline()
    return content


class WebSearch:
    def __init__(self, pr, filename):
        self.lookup_table = pr
        raw_data = read_file(filename)
        keyword_map = {}

        for i in raw_data:
            # print(i)
            s = i.strip()
            # print(s)
            if ': ' in s:
                print('aaaaaaaa')
                info = s.split(': ')
                # print(info)
                num = int(info[0])
                lst = info[1].split()
                keyword_map[num] = lst

        self.lookup_table = keyword_map

    def i_am_feeling_lucky(self, query):
        for doc_id,keyword in self.lookup_table.items():
            if query in keyword:
                return int(doc_id)
        return -1
    