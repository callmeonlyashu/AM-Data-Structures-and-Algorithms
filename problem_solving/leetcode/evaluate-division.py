""" Link: https://leetcode.com/problems/evaluate-division/"""

from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        def build_graph(equations, values):
            # Helper to add a directed, weighted edge from 'f' to 't' in the graph
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
            
            # For each equation like a/b = value, build a weighted graph:
            # an edge a -> b with weight 'value' (since a = value * b)
            # and the reverse edge b -> a with weight 1/value (since b = (1/value) * a)
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1 / value)

        def find_path(query):
            b, e = query  # b = start variable, e = end variable (we want b / e)
            
            # If either variable was never seen in any equation, the answer is undefined
            if b not in graph or e not in graph:
                return -1.0
            
            # BFS from 'b', tracking the running product of edge weights along the path
            # Each queue element is (current_node, product_of_weights_so_far)
            q = collections.deque([(b, 1.0)])
            visited = set()
            
            while q:
                front, cur_product = q.popleft()
                
                # Reached the target variable: cur_product is b/e
                if front == e:
                    return cur_product
                
                visited.add(front)
                
                # Explore neighbors, multiplying the accumulated ratio along the way
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product * value))
            
            # No path found between b and e -> undefined ratio
            return -1.0

        # Build the weighted graph from all given equations/values
        build_graph(equations, values)

        # Answer every query by finding a path (product of ratios) in the graph
        return [find_path(q) for q in queries]
