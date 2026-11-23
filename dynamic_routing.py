import networkx as nx
import matplotlib.pyplot as plt
import random

# Create network with individual attributes
network = nx.Graph()
network.add_node("A", failure_prob=0.0)
network.add_node("B", failure_prob=0.15)
network.add_node("C", failure_prob=0.10)
network.add_node("D", failure_prob=0.25)
network.add_node("E", failure_prob=0.20)
network.add_node("F", failure_prob=0.10)
network.add_node("G", failure_prob=0.05)
network.add_node("H", failure_prob=0.0)

network.add_edge("A", "B", failure_prob=0.05)
network.add_edge("A", "C", failure_prob=0.10)
network.add_edge("B", "D", failure_prob=0.15)
network.add_edge("C", "D", failure_prob=0.05)
network.add_edge("C", "E", failure_prob=0.10)
network.add_edge("D", "F", failure_prob=0.20)
network.add_edge("E", "F", failure_prob=0.10)
network.add_edge("E", "G", failure_prob=0.05)
network.add_edge("F", "H", failure_prob=0.15)
network.add_edge("G", "H", failure_prob=0.05)

positions = nx.spring_layout(network, seed=42)
source = "A"
destination = "H"

def find_path(graph, label):
    print(f"\n--- {label} ---")
    try:
        path = nx.shortest_path(graph, source, destination)
        print("Path found:", " -> ".join(path))
        return path
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        print("No available path due to network failures!")
        return None

# 1. Baseline: Before Failure
initial_path = find_path(network, "BEFORE FAILURE")

# 2. Dynamic Failure Simulation (Replacing hardcoded node D)
faulty_network = network.copy()
failed_components = []

# Evaluate node failures dynamically
for router, data in list(faulty_network.nodes(data=True)):
    if router not in [source, destination]:
        if random.random() < data["failure_prob"]:
            faulty_network.remove_node(router)
            failed_components.append(router)

# Evaluate link failures dynamically
for u, v, data in list(faulty_network.edges(data=True)):
    if u in faulty_network and v in faulty_network:
        if random.random() < data["failure_prob"]:
            faulty_network.remove_edge(u, v)
            failed_components.append(f"Link({u},{v})")

print("Failures detected at runtime:", failed_components)

# 3. Adaptive Routing: Recalculate path on the dynamically damaged network
adapted_path = find_path(faulty_network, "AFTER DYNAMIC FAILURE & ADAPTATION")
