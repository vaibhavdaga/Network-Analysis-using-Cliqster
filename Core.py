import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import generator
def generator_size(g):
    return sum(1 for x in g)

def error(originalgraph, constructedgraph):
    err = 0
    n = constructedgraph[0].size
    for edge in originalgraph.edges():
        if constructedgraph[int(edge[0]),int(edge[1])]==0:
            err = err+1
    return (err/float(originalgraph.number_of_edges()))*100

def error1(originalgraph, constructedgraph):
    err = 0
    n = constructedgraph[0].size
    for i in range(n):
        for j in range(n):
            #print i,j,originalgraph.has_edge(i,j)
            if originalgraph.has_edge(i,j) and constructedgraph[i,j]==0:
                err = err+1
    return err/2

def varycliques(G, g, n):
    k = 0.5
    K = g.size
    xcord = []
    ycord = []
    while k<=1.01:
        bases = []
        x = int(K*k)
        i = K - 1
        while x>0:
            bases.append(g[i])
            i = i-1
            x = x-1
        newgraph = reconstruct(bases, n)
        err = error(G, newgraph)
        print k, err
        xcord.append(k)
        ycord.append(err)
        k = k+0.01
    plt.plot(xcord, ycord)
    plt.show()

def reconstruct(bases,vertices):
    graph = np.zeros((vertices+1,vertices+1),dtype = float)
    for comp in bases:
        clique = comp[1]
        mu = comp[0]
        for i in clique:
            for j in clique:
                if i!=j:
                    graph[int(i),int(j)] = graph[int(i),int(j)] + mu
    return graph

def graphplot(arr,c):
    xcord = []
    ycord = []
    k = 0
    for i in arr :
        xcord.append(k)
        k=k+1
        ycord.append(i);
        print k,i
    plt.plot(xcord,ycord,c)
    plt.grid()

def cliqstr(g):
    #print "Starting Cliqster ..."
    # finding the maximal cliques using bron kerbosch algorithm in networkx 
    vertices = g.number_of_nodes()
    cliq = nx.find_cliques(g)
    # converting the generator type to a 2d list
    cliques_size = 0
    cliques = []

    #print "Writing cliques..."
    for i in cliq:
        if len(i)>1:
            cliques.append(i)
            cliques_size += 1

    #print "---Done writing cliques---"
    print "Number of cliques: " + str(cliques_size)
    #assert cliques_size == cliques_size
    vecd = np.zeros(cliques_size)
    A = np.zeros((cliques_size, cliques_size))
    # Calculating matX and vector D in the formula
    sumA = np.zeros((cliques_size,cliques_size))
    for i in range(cliques_size):
        for j in range(cliques_size):
            A[i,j] = len(set(cliques[i]).intersection(cliques[j]))*(len(set(cliques[i]).intersection(cliques[j])) -1)/2
        A[i,i] = len(cliques[i]) * (len(cliques[i]) - 1) / 2
        sumA = sumA + A
        for j in cliques[i]:
            for k in cliques[i]:
                if j!=k:
                    if g.has_edge(j,k):
                         vecd[i] += 1
    vecd /= 2
    #print "---Solving for Mu---"
    Mu = np.linalg.tensorsolve(A,vecd)
    
    dtype = [('mu',float), ('cliques',list), ('size',int)]
    components = []
    for i in range(0,cliques_size):
        components.append((Mu[i],cliques[i],len(cliques[i])))

    decomposition = np.array(components, dtype=dtype)
    decomposition = np.sort(decomposition, order='mu')

    return decomposition

def process(N,M,K,p1,p2):
    G = generator.generate(N,M,K,p1,p2);
    return cliqstr(G)[::-1]

def go(c,N,M):
    p1 = input()
    p2 = input()
    p3 = input()

    mu_arr = []
    for i in range(500):
        mu_arr.append(0)

    for i in range(100):
        print i
        cur_arr = process(N,M,p1,p2)
            if j<len(cur_arr):
                mu_arr[j] = mu_arr[j]+(cur_arr[j]['mu']/100.0)
    graphplot(mu_arr,c)

def run(N, M):
    go('r',N,M)
    plt.axis([0,25,-0.1,1.2])
    plt.xlabel("Index")
    plt.ylabel("Amplitude")
    s = str(raw_input("file name: "))
    plt.savefig(''+s)