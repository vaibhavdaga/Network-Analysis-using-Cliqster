import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
# change the random percenttage
def generate(N, M, E1, E2):
	G = nx.Graph()

	Edges_in_N = N*(N-1)/2
	Edges_in_M = M*(M-1)/2

	percent_N = E1
	percent_M = E2

	edges_to_remove_N = (int)(Edges_in_N * percent_N)
	edges_to_remove_M = (int)(Edges_in_M * percent_M)
	
	for i in range(1,N+1):
		for j in range(i+1,N+1):
			if ((random.random() > 0.8) and (edges_to_remove_N > 0)):
				edges_to_remove_N = edges_to_remove_N - 1
				continue
			G.add_edge(i,j)

	for i in range(N+1,N+M+1):
		for j in range(i+1,N+M+1):
			if ((random.random() > 0.8) and (edges_to_remove_M > 0)):
				edges_to_remove_M = edges_to_remove_M - 1
				continue
			G.add_edge(i,j)
	
	print 'initial graph made...'
	last = N+1
	for i in range(1,N+1):
		if last>M+N:
			break
		n = min(1000,random.sample(range(1,M+N+1-last+1),1)[0])
		#print n
		while n>0 and last<=M+N:
			G.add_edge(i,last)
			last = last+1
			n = n-1

	print 'graph completed...'
	return G
