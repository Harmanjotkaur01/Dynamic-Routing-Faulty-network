import networkx as nx
import matplotlib.pyplot as plt
import random

# Create the network
network = nx.Graph()

network.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "F"),
    ("E", "F"),
    ("E", "G"),
    ("F", "H"),
    ("G", "H")
])

# Keep router positions the same
positions = nx.spring_layout(network, seed=42)

source = "A"
destination = "H"

# Failure probabilities
router_failure = 0.20
link_failure = 0.10

# Create a copy of the original network
active_network = network.copy()

# Function to draw the network
def draw_network(graph, title, filename):

    plt.figure(figsize=(9, 6))

    # Find shortest path
    try:
        path = nx.shortest_path(graph, source, destination)
        path_edges = list(zip(path, path[1:]))

        print(title)
        print("Path:", " -> ".join(path))

    except nx.NetworkXNoPath:
        path_edges = []
        print(title)
        print("No available path!")

    # Draw working routers and links
    nx.draw(
        graph,
        positions,
        with_labels=True,
        node_color="lightblue",
        node_size=1200,
        edge_color="gray"
    )

    # Highlight available path
    nx.draw_networkx_edges(
        graph,
        positions,
        edgelist=path_edges,
        edge_color="green",
        width=4
    )

    # Show failed routers
    failed_routers = set(network.nodes()) - set(graph.nodes())

    if failed_routers:
        nx.draw_networkx_nodes(
            network,
            positions,
            nodelist=list(failed_routers),
            node_color="red",
            node_shape="X",
            node_size=1200
        )

        nx.draw_networkx_labels(
            network,
            positions,
            labels={node: node for node in failed_routers}
        )

    plt.title(title)
    plt.savefig(filename)
    plt.close()


# Step 1: Draw original network
draw_network(
    active_network,
    "Original Network",
    "original_network.png"
)

# Step 2: Simulate random router failures
for router in list(active_network.nodes()):

    if router not in [source, destination]:

        if random.random() < router_failure:
            active_network.remove_node(router)
            print("Router failed:", router)

# Step 3: Simulate random link failures
for link in list(active_network.edges()):

    if random.random() < link_failure:
        active_network.remove_edge(*link)
        print("Link failed:", link)

# Step 4: Draw faulty network
draw_network(
    active_network,
    "Network After Random Failures",
    "random_failure_network.png"
)

print("\nVisualization completed!")