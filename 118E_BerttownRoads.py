
from collections import defaultdict

def dfs_rec(graph, root, seen=defaultdict(bool), edges=[]):
    seen[root] = True
    for neighbour in graph[root]:
        if not seen[neighbour]:
            edges.append( (root,neighbour) ) 
            seen[neighbour] = True
            dfs_rec(graph, neighbour, seen, edges)
            
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

def all_children(graph,u,tree_edges):
    children = [edge[1] for edge in tree_edges if edge[0] == u]
    return flatten(children + [all_children(graph,v,tree_edges) for v in children])

def dp(graph, u, tree_edges, back_edges):
    if not u:
        return 0
    children = [edge[1] for edge in tree_edges if edge[0] == u]
    up_backedges = [edge for edge in back_edges
                    if (edge[0] == u and edge[1] not in all_children(graph, u, tree_edges))
                    or (edge[1] == u and edge[0] not in all_children(graph, u, tree_edges))
                    ]
    down_backedges = [edge for edge in back_edges
                      if (edge[0] == u and edge[1] in all_children(graph, u, tree_edges))
                      or (edge[1] == u and edge[0] in all_children(graph, u, tree_edges))
                      ]
    return len(up_backedges)//2-len(down_backedges)//2 + sum(dp(graph, v, tree_edges, back_edges) for v in children)
            
def main():
    n, m = map(int, input().split(' '))
    nodelist = list(range(1,n+1))
    edgelist_input = []
    for _ in range(m):
        a, b = map(int, input().split(' '))
        edgelist_input.append( (a,b) ) # directed edges
    # make graph
    graph = defaultdict(list)
    edgelist = [] # undirected edges
    for s,t in edgelist_input:
        graph[s].append(t)
        graph[t].append(s)
        edgelist.append( (s,t) )
        edgelist.append( (t,s) )
    # make dfs tree
    tree_edges=[]
    root = 1
    dfs_rec(graph , root , defaultdict(bool), tree_edges )
    # find backedges
    tree_edges_full = tree_edges + [ (t,s) for s,t in tree_edges ]
    back_edges = set(edgelist)-set(tree_edges_full)
    span_edges = set(edgelist) - back_edges
    
    def anybridge(graph):
        return not all( [dp(graph, u, tree_edges, back_edges) for u in range(2,n+1)]  )
    #print({u : dp(graph, u, tree_edges, back_edges) for u in graph} )    
    if anybridge(graph): 
        print(0)
    else:
        up_backedges = []
        for node in graph:
            up_backedges = up_backedges + [edge for edge in back_edges
                    if (edge[0] == node and edge[1] not in all_children(graph, node, tree_edges))
                    ]
        for s,t in tree_edges + up_backedges:
            print(str(s)+' '+str(t))

if __name__=='__main__':
     main()



