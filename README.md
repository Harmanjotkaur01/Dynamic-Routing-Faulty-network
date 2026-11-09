# Dynamic-Routing Mechanism Design in a Faulty Network

## Network Diagrams

### Network Before Failure

![Network Before Failure](before_failure.png)

### Network After Router Failure

![Network After Failure](after_failure.png)

### Network With Random Failures

![Random Network Failures](random_failure_network.png)
## Network Reliability Comparison

The network was tested under four different failure conditions.
Each test included 1,000 simulation rounds.

| Router Failure | Link Failure | Reliability |
|---|---|---|
| 5% | 5% | 95.3% |
| 10% | 10% | 81.4% |
| 20% | 10% | 68.0% |
| 30% | 20% | 35.2% |

### Reliability Comparison Graph

![Network Reliability Comparison](failure_comparison.png)

### Results

The results show that network reliability decreases as router
and link failure probabilities increase.

At low failure rates, the network maintained a working route
in most simulation rounds.

At higher failure rates, finding an available route became
more difficult.