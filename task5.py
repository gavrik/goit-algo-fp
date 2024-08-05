import numpy as np
import heapq
from task4 import draw_tree, build_heap_tree
from collections import deque


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def generate_color(layer, count_layers):
    base_color = [135, 206, 250]
    arr = np.linspace(0.2, 0.9, count_layers)
    # arr = arr[::-1]
    darken_factor = arr[layer]
    new_color = [int(val * darken_factor) for val in base_color]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs_visualisation(root):
    visited = set()
    stack = [root]
    step = 0
    step_count = count_nodes(root)
    while stack:
        node = stack.pop()
        if node not in visited:
            # print(node.val, end=' ')
            node.color = generate_color(step, step_count)
            visited.add(node)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        step += 1
    return visited


def bfs_visualisation(root):
    visited = set()
    queue = deque([root])
    step = 0
    step_count = count_nodes(root)
    while queue:
        next_nodes = []
        node = queue.popleft()
        if node not in visited:
            # print(node.val, end=' ')
            node.color = generate_color(step, step_count)
            visited.add(node)
            if node.left is not None:
                next_nodes.append(node.left)
            if node.right is not None:
                next_nodes.append(node.right)
            if node.right is not None or node.left is not None:
                queue.extend(set(next_nodes) - visited)
        step += 1
    return visited


if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)
    print(heap_list)
    root = build_heap_tree(heap_list)
    print("\n Origin tree Visualisation \n")
    draw_tree(root)
    print("\n DFS Visualisation \n")
    res = dfs_visualisation(root)
    for r in res:
        print(r.val, end=" ")
    draw_tree(root)
    print("\n BFS Visualisation \n")
    res = bfs_visualisation(root)
    for r in res:
        print(r.val, end=" ")
    draw_tree(root)
