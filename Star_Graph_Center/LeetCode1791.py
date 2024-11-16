'''
There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n - 1 edges
that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates 
that there is an edge between the nodes ui and vi. 

Return the center of the given star graph.

'''

from typing import List

class Solution:
    def findCenterTraditional(self, edges: List[List[int]]) -> int:
        # Traditional Approach: Count occurrences of nodes from both edges
        # Combine the two edges into one list
        combined_nodes = edges[0] + edges[1]
        
        # Check which node appears twice, indicating it is the center
        for node in combined_nodes:
            if combined_nodes.count(node) == 2:
                return node
        
        return -1  # In case no center node is found (though this shouldn't happen in a valid star graph)

    def findCenterOptimized(self, edges: List[List[int]]) -> int:
        # Optimized Approach: Directly check for the common node between the first two edges
        # Since it's a star graph, the center will be the common node between the first two edges
        node1, node2 = edges[0]
        node3, node4 = edges[1]
        
        # Check if node1 is the center or node2 is the center
        if node1 == node3 or node1 == node4:
            return node1
        return node2  # If node1 is not the center, then node2 must be

# Example usage and comparison of both approaches:
edges = [[1, 2], [2, 3]]

solution = Solution()

# Traditional approach output
traditional_result = solution.findCenterTraditional(edges)
print("Traditional Approach Output:", traditional_result)  # Expected output: 2

# Optimized approach output
optimized_result = solution.findCenterOptimized(edges)
print("Optimized Approach Output:", optimized_result)  # Expected output: 2
