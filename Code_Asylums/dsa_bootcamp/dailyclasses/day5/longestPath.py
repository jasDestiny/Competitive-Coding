def longestPath(graph, source):
    visited={}


graph={3:[2,4,6,7], 2:[1], 1:[], 4:[5], 5:[], 6:[],7:[8], 8:[9], 9:[]}
print(longestPath(graph, 3))