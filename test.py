import pydotplus as pdp

 # Create test graph
test_graph = pdp.graphviz.Graph(graph_name='test_graph',
                                        graph_type='graph',
                                        simplify=True)

# Create test nodes
test_node_one = pdp.graphviz.Node(name='1')
test_node_two = pdp.graphviz.Node(name='2')

# Create test edges
test_edge = pdp.graphviz.Edge(src='1', dst='2')

# Add nodes and edges to graph
test_graph.add_node(test_node_one)
test_graph.add_node(test_node_two)
test_graph.add_edge(test_edge)

# Print graph
print(test_graph.to_string())