
import math
from hello import PageRank, Digraph, WebSearch

EPS = 1e-4

def check(name, cond):
    if cond:
        print(f"{name} passed")
    else:
        print(f"{name} FAILED")

def main():
    g0 = Digraph(1)
    pr0 = PageRank(g0)
    check("Test1 SingleNode", abs(pr0.get_pr(0) - 1.0) < EPS)

    g1 = Digraph(2)
    g1.add_edge(0, 1)
    g1.add_edge(1, 0)
    pr1 = PageRank(g1)
    check("Test2 PR0", abs(pr1.get_pr(0) - 0.5) < EPS)
    check("Test2 PR1", abs(pr1.get_pr(1) - 0.5) < EPS)

    g2 = Digraph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)
    pr2 = PageRank(g2)
    for i in range(3):
        check(f"Test3 PR{i}", abs(pr2.get_pr(i) - 1/3) < EPS)


    ws = WebSearch(pr2, "WebContent.txt")
    check("Test5 algorithm", ws.i_am_feeling_lucky("algorithm") == 0)
    check("Test5 mining",    ws.i_am_feeling_lucky("mining") == 2)
    check("Test5 none",      ws.i_am_feeling_lucky("none") == -1)

if __name__ == "__main__":
    main()
