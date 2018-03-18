# Heap

## Properties
- There are 2 types min & max
- all parent node >= to child nodes (max heap)
- all parent node <= to child nodes (min heap)
- partial sort
- good for retrieve min, max -> priority queue --> [double endded priority queue](https://en.wikipedia.org/wiki/Double-ended_priority_queue)
- can implement using array
  - node i has 
      - left child = 2i + 1
      - right child = 2i + 2 

- Build steps
  - loop from *back* to front
  - compare node and its children (left, right)
  - if the node is not the largest (max-heap) or smallest(min-heap)
    - swap and run fix against the swap node


## Heap Sort

- given a heap we can contruct sorted result
  - min heap -> sort asc
  - max heap -> sort desc
- Steps

  - swap arr[0] to arr[length-1] --> this essentially swaps a known value (min or max) back to the end of array. note length will be smaller on each iteration
  - fix the heap (root node potentially messed up from the previous swap) --> don't forget to limit the fix to length - 2 (last element is now sorted)
  - repeat until end of array