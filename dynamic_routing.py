import networkx as nx
import matplotlib.pyplot as plt

# Create the network
network = nx.Graph()

# Connect routers
connections = [
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
]

network.add_edges_from(connections)

# Set router positions
positions = nx.spring_layout(network, seed=42)

source = "A"
destination = "H"

# Function to find shortest path
def find_path(graph):
    try:
        path = nx.shortest_path(graph, source, destination)
        print("Path:", " -> ".join(path))
        return path
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        print("No available path!")
        return None


# Function to draw network
def draw_network(graph, path, title, filename, failed=None):

    plt.figure(figsize=(9, 6))

    # Draw working routers
    nx.draw(
        graph,
        positions,
        with_labels=True,
        node_color="lightblue",
        node_size=1200,
        edge_color="gray"
    )

    # Highlight selected path
    if path:
        path_edges = list(zip(path, path[1:]))

        nx.draw_networkx_edges(
            graph,
            positions,
            edgelist=path_edges,
            edge_color="green",
            width=4
        )

    # Show failed router
    if failed:
        nx.draw_networkx_nodes(
            network,
            positions,
            nodelist=[failed],
            node_color="red",
            node_shape="X",
            node_size=1500
        )

        nx.draw_networkx_labels(
            network,
            positions,
            labels={failed: failed}
        )

    plt.title(title)
    plt.savefig(filename)
    plt.close()


# BEFORE FAILURE
print("BEFORE FAILURE")

original_path = find_path(network)

draw_network(
    network,
    original_path,
    "Network Before Failure",
    "before_failure.png"
)


# SIMULATE FAILURE
failed_router = "D"

faulty_network = network.copy()
faulty_network.remove_node(failed_router)

print("\nRouter D has failed!")


# AFTER FAILURE
print("\nAFTER FAILURE")

new_path = find_path(faulty_network)

draw_network(
    faulty_network,
    new_path,
    "Network After Failure",
    "after_failure.png",
    failed_router
)


print("\nSimulation completed!")