import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create the network
network = nx.Graph()

# Step 2: Connect the routers
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

# Step 3: Find the original shortest path
source = "A"
destination = "H"

original_path = nx.shortest_path(network, source, destination)

print("BEFORE FAILURE")
print("Original Path:", original_path)

# Step 4: Simulate router failure
failed_router = "D"
network.remove_node(failed_router)

print("\nRouter D has failed!")

# Step 5: Find a new path
print("\nAFTER FAILURE")

try:
    new_path = nx.shortest_path(network, source, destination)
    print("New Path:", new_path)
    print("Network successfully rerouted!")

except nx.NetworkXNoPath:
    print("No available path!")

# Step 6: Draw the network
nx.draw(
    network,
    with_labels=True,
    node_color="lightblue",
    node_size=1500,
    edge_color="gray"
)

plt.title("Network After Router Failure")
plt.savefig("network_after_failure.png")

print("\nNetwork diagram saved!")
