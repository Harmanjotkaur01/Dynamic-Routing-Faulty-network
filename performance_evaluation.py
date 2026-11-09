import networkx as nx
import random

# Create network
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

source = "A"
destination = "H"

# Simulation settings
total_rounds = 100
router_failure = 0.20
link_failure = 0.10

# Store results
successful_routes = 0
failed_routes = 0
total_path_length = 0

# Run simulation
for round_number in range(1, total_rounds + 1):

    faulty_network = network.copy()

    # Random router failures
    for router in list(faulty_network.nodes()):

        if router not in [source, destination]:

            if random.random() < router_failure:
                faulty_network.remove_node(router)

    # Random link failures
    for link in list(faulty_network.edges()):

        if random.random() < link_failure:
            faulty_network.remove_edge(*link)

    # Check whether a path exists
    if nx.has_path(faulty_network, source, destination):

        path = nx.shortest_path(
            faulty_network,
            source,
            destination
        )

        successful_routes += 1
        total_path_length += len(path) - 1

    else:
        failed_routes += 1

# Calculate results
reliability = (successful_routes / total_rounds) * 100

if successful_routes > 0:
    average_path = total_path_length / successful_routes
else:
    average_path = 0

# Display results
print("\nNETWORK PERFORMANCE RESULTS")
print("----------------------------")

print("Total Rounds:", total_rounds)
print("Successful Routes:", successful_routes)
print("Failed Routes:", failed_routes)
print("Network Reliability:", round(reliability, 2), "%")
print("Average Path Length:", round(average_path, 2))

print("\nEvaluation completed!")