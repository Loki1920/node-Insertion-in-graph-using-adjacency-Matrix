# inserting node in graph using adjacency matrix

def add_node(v):
    global node_count
    if v in nodes:
        print(v," present in graph.")
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def print_graph():
    print("print adjacency matrix form:")
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end = ' ')
        print()


nodes = []
graph = []
node_count = 0
print("before adding node:")
print("nodes :",nodes)
print("graph :",graph)

add_node("A")
add_node("B")

print("After adding node:")
print("nodes :",nodes)
print("graph :",graph)

print_graph()

