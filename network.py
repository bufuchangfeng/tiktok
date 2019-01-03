import networkx
import matplotlib.pyplot as plt

plt.figure(figsize=(19.2, 10.8))

G = networkx.Graph()

f = open('20155324-node-list.txt', 'r')

for line in f.readlines():
    line = line.strip('<')
    node1 = line.split(',')[0]
    node2 = line.split(',')[1].split('>')[0]

    print(node1, node2)
    G.add_edge(node1, node2)

f.close()

networkx.draw(G, node_color='red', edge_color='black', font_size=20, node_size =300, width=1, with_labels=False)

plt.savefig('temp.png',bbox_inches='tight')

plt.show()