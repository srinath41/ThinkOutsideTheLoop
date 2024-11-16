# Problem Analysis - LeetCode 1791: Find Center of Star Graph

## Problem Statement

You are given an **undirected star graph** consisting of `n` nodes labeled from `1` to `n`. A **star graph** is a graph where there is one **center node** and exactly `n - 1` edges that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [ui, vi]` indicates that there is an edge between the nodes `ui` and `vi`. Your task is to return the **center node** of the given star graph.

---

### Example 1:
```plaintext
Input: edges = [[1, 2], [2, 3]]
Output: 2
Explanation: The center of the star graph is node 2 because it is the only node that appears in both edges.
```

### Example 2:
```plaintext
Input: edges = [[1, 3], [2, 3]]
Output: 3
Explanation: The center of the star graph is node 3 because it is the only node that appears in both edges.
```

### Constraints:
- `2 <= n <= 100`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`
- The graph is a star graph, meaning there is exactly one center node.

---

## Approach 1: **Traditional Approach (Counting Occurrences)**

### **Method**:
- In the traditional approach, we can combine the first two edges of the graph and check which node appears in both edges. This node is the center of the star graph.
- To achieve this, we can concatenate the nodes of the first two edges and count the occurrences of each node.
- The node that appears twice will be the center of the graph.

### **Time Complexity**:
- **Time Complexity**: O(n), where `n` is the number of nodes. This is due to the `count()` operation which runs in O(n) time for each node, resulting in O(n) total time for the two edges.
- **Space Complexity**: O(n), due to the storage of the combined list of nodes.

### **Code Implementation**:
```python
from typing import List

class Solution:
    def findCenterTraditional(self, edges: List[List[int]]) -> int:
        # Traditional Approach: Count occurrences of nodes from both edges
        combined_nodes = edges[0] + edges[1]
        
        # Check which node appears twice, indicating it is the center
        for node in combined_nodes:
            if combined_nodes.count(node) == 2:
                return node
        
        return -1  # In case no center node is found
```

---

## Approach 2: **Optimized Approach (Direct Comparison)**

### **Method**:
- In the optimized approach, we directly compare the first two edges. Since it is a star graph, the center node will appear in both of these edges.
- We can simply compare the first node of the first edge with the nodes in the second edge. If they match, that node is the center; otherwise, the other node in the first edge is the center.

### **Time Complexity**:
- **Time Complexity**: O(1), as we only need to compare the first two edges, making the approach very efficient.
- **Space Complexity**: O(1), as no additional space is needed for storing nodes.

### **Code Implementation**:
```python
from typing import List

class Solution:
    def findCenterOptimized(self, edges: List[List[int]]) -> int:
        # Optimized Approach: Directly check for the common node between the first two edges
        node1, node2 = edges[0]
        node3, node4 = edges[1]
        
        # Check if node1 is the center or node2 is the center
        if node1 == node3 or node1 == node4:
            return node1
        return node2  # If node1 is not the center, then node2 must be
```

---

## Performance Comparison:

| **Approach**              | **Time Complexity** | **Space Complexity** | **Explanation**                                |
|---------------------------|---------------------|----------------------|------------------------------------------------|
| **Traditional Approach**   | O(n)                | O(n)                 | Combines the first two edges and counts nodes |
| **Optimized Approach**     | O(1)                | O(1)                 | Compares the first two edges directly         |

- **Optimized Approach** is clearly the better option in terms of both time and space efficiency, with O(1) time and space complexity.

---

## Conclusion

- The problem can be solved effectively using either approach, but the **optimized approach** is far superior in terms of performance.
- The **traditional approach** provides a simple solution but is less efficient due to the use of the `count()` operation on the combined list.
- The **optimized approach** achieves constant time complexity by leveraging the structure of the star graph, where the center node is common to all edges.

---

## LeetCode Profile

Check out my LeetCode profile for more solutions:  
[LeetCode Profile - srinathdev](https://leetcode.com/srinathdev/)

---
