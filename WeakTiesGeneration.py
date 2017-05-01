import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def generate(N, M, K, p1, p2):

	G = nx.Graph()
	for i in range(1,N+1):
		for j in range(i+1,N+1):
			G.add_edge(i,j)

	for i in range(N+1,N+M+1):
		for j in range(i+1,N+M+1):
			G.add_edge(i,j)

	currentNode = N+1
	S2 = N + (M*p2)
	if S2 > int(S2):
		S2 = S2+1
	S2 = int(S2)
	S1 = (N+1)*p1
	if S1 > int(l):
		S1 = l+1;
	for i in range(1,int(S1)):
		if currentNode>S2:
			break
		n = min(100,random.sample(range(1,S2+1-currentNode+1),1)[0])
		while n>0 and currentNode<=S2:
			G.add_edge(i,currentNode)
			currentNode = currentNode+1
			n = n-1

	return G
