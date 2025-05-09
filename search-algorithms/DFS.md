# Depth first search

In Depth First Search (or DFS) for a graph, we traverse all adjacent vertices one by one. When we traverse an adjacent vertex, we completely finish the traversal of all vertices reachable through that adjacent vertex. This is similar to a tree, where we first completely traverse the left subtree and then move to the right subtree. The key difference is that, unlike trees, graphs may contain cycles (a node may be visited more than once). To avoid processing a node multiple times, we use a boolean visited array.

## Example

Note : There can be multiple DFS traversals of a graph according to the order in which we pick adjacent vertices. Here we pick vertices as per the insertion order.


1. Input: adj =  [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
    ![Undirected graph](https://media.geeksforgeeks.org/wp-content/uploads/20240809162859/Input_undirected_Graph.webp)
    Explanation:  The source vertex s is 0. We visit it first, then we visit an adjacent. 
    ```
    Start at 0: Mark as visited. Output: 0
    Move to 1: Mark as visited. Output: 1 
    Move to 2: Mark as visited. Output: 2 
    Move to 3: Mark as visited. Output: 3 (backtrack to 2)
    Move to 4: Mark as visited. Output: 4 (backtrack to 2, then backtrack to 1, then to 0)
    ```


Not that there can be more than one DFS Traversals of a Graph. For example, after 1, we may pick adjacent 2 instead of 0 and get a different DFS. Here we pick in the insertion order.


2. Input: [[2,3,1], [0], [0,4], [0], [2]]
    ![Undirected graph](https://media.geeksforgeeks.org/wp-content/uploads/20240809162955/Input_undirected_Graph2.webp)
    Output: [0 2 4 3 1]
    Explanation: DFS Steps:


``` 
    Start at 0: Mark as visited. Output: 0
    Move to 2: Mark as visited. Output: 2
    Move to 4: Mark as visited. Output: 4 (backtrack to 2, then backtrack to 0)
    Move to 3: Mark as visited. Output: 3 (backtrack to 0)
    Move to 1: Mark as visited. Output: 1 (backtrack to 0)
```

## DFS from a Given Source of Undirected Graph
The algorithm starts from a given source and explores all reachable vertices from the given source. It is similar to [Preorder Tree Traversal](https://www.geeksforgeeks.org/preorder-traversal-of-binary-tree/) where we visit the root, then recur for its children. In a graph, there might be loops. So we use an extra visited array to make sure that we do not process a vertex again.

The following illustration might be helpful to understand DFS.
![Step 1](https://media.geeksforgeeks.org/wp-content/uploads/20250328131732463659/DFS-for-a-Graph-1.webp)

![Step 2](https://media.geeksforgeeks.org/wp-content/uploads/20250328131732267102/DFS-for-a-Graph-2.webp)

![Step 3](https://media.geeksforgeeks.org/wp-content/uploads/20250328131732134563/DFS-for-a-Graph-3.webp)

![Step 4](https://media.geeksforgeeks.org/wp-content/uploads/20250328131731956858/DFS-for-a-Graph-4.webp)

![Step 5](https://media.geeksforgeeks.org/wp-content/uploads/20250328131731689576/DFS-for-a-Graph-5.webp)

![Step 6](https://media.geeksforgeeks.org/wp-content/uploads/20250328131731493168/DFS-for-a-Graph-6.webp)

![Step 7](https://media.geeksforgeeks.org/wp-content/uploads/20250328131731320781/DFS-for-a-Graph-7.webp)

![Step 8](https://media.geeksforgeeks.org/wp-content/uploads/20250328131731182475/DFS-for-a-Graph-8.webp)

![Step 9](https://media.geeksforgeeks.org/wp-content/uploads/20250328131731022549/DFS-for-a-Graph-9.webp)

![Step 10](https://media.geeksforgeeks.org/wp-content/uploads/20250328131730828908/DFS-for-a-Graph-10.webp)

<br>

###### Continue reading here
[geeksforgeeks.org](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)