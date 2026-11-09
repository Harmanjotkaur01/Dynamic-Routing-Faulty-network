import networkx as nx
import random

# Step 1: Create the original network
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

# Step 2: Set failure probabilities
router_failure = 0.20
link_failure = 0.10

# Recovery probability
recovery_probability = 0.50

# Start with all routers working
active_network = network.copy()

# Step 3: Run 10 simulation rounds
for round_number in range(1, 11):

    print("\n------------------------")
    print("Simulation Round:", round_number)

    # Step 4: Random router failures
    for router in list(active_network.nodes()):

        if router not in [source, destination]:

            if random.random() < router_failure:
                active_network.remove_node(router)
                print("Router failed:", router)

    # Step 5: Random link failures
    for link in list(active_network.edges()):

        if random.random() < link_failure:
            active_network.remove_edge(*link)
            print("Link failed:", link)

    # Step 6: Recover failed routers
    for router in network.nodes():

        if router not in active_network:

            if random.random() < recovery_probability:
                active_network.add_node(router)
                print("Router recovered:", router)

    # Step 7: Recover failed links
    for link in network.edges():

        a, b = link

        if a in active_network and b in active_network:

            if not active_network.has_edge(a, b):

                if random.random() < recovery_probability:
                    active_network.add_edge(a, b)
                    print("Link recovered:", link)

    # Step 8: Find available path
    try:
        path = nx.shortest_path(
            active_network,
            source,
            destination
        )

        print("Available Path:", " -> ".join(path))

    except nx.NetworkXNoPath:
        print("No available path!")

    print("Round completed!")

print("\nSimulation finished!")