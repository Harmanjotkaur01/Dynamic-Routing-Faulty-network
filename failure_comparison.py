import networkx as nx
import matplotlib.pyplot as plt
import random

# Step 1: Create the network
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

# Step 2: Set source and destination
source = "A"
destination = "H"

# Step 3: Different failure conditions
tests = [
    (0.05, 0.05),
    (0.10, 0.10),
    (0.20, 0.10),
    (0.30, 0.20)
]

total_rounds = 1000

reliability_results = []
test_labels = []

# Step 4: Run each test
for router_failure, link_failure in tests:

    successful_routes = 0

    for round_number in range(total_rounds):

        # Start with a working network
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

        # Check if a route exists
        if nx.has_path(faulty_network, source, destination):
            successful_routes += 1

    # Calculate reliability
    reliability = (successful_routes / total_rounds) * 100

    reliability_results.append(reliability)

    label = f"{int(router_failure * 100)}% / {int(link_failure * 100)}%"
    test_labels.append(label)

    print("Router Failure:", int(router_failure * 100), "%")
    print("Link Failure:", int(link_failure * 100), "%")
    print("Network Reliability:", round(reliability, 2), "%")
    print("--------------------------")

# Step 5: Create comparison graph
plt.figure(figsize=(9, 5))

plt.bar(test_labels, reliability_results)

plt.xlabel("Router Failure % / Link Failure %")
plt.ylabel("Network Reliability (%)")
plt.title("Network Reliability Under Different Failure Conditions")

plt.ylim(0, 100)

# Show reliability above each bar
for i, value in enumerate(reliability_results):
    plt.text(i, value + 1, f"{value:.1f}%", ha="center")

plt.tight_layout()

# Save graph
plt.savefig("failure_comparison.png")

plt.close()

print("\nComparison graph saved!")
print("Simulation completed!")