# DA5300 Session-by-Session Study Plan

This roadmap uses 90-minute sessions. With two sessions per day, it takes approximately nine focused days; with one session per day, it takes approximately eighteen days.

## Phase 1: Foundation

### Session 1: Python sequences and mappings

- Read the strings and lists/tuples/dictionaries PDFs selectively.
- Revise indexing, slicing, mutability, list aliasing, sorting and dictionaries.
- Trace five short Python expressions by hand.
- Completion test: predict output correctly without running the code.

## Phase 2: Algorithm analysis

### Session 2: Why efficiency and input size

- Read `01_why_efficiency_matters.pdf` and `02_analysis_of_algorithms.pdf`.
- Understand time versus space, input size and hardware-independent analysis.
- Compare linear search with repeated halving.
- Completion test: explain why an algorithm can matter more than faster hardware.

### Session 3: Big-O, Omega and Theta

- Read `03_comparing_orders_of_magnitude.pdf`.
- Learn upper, lower and tight bounds.
- Order common growth rates:

  `1 < log n < n < n log n < n^2 < n^3 < 2^n < n!`

- Completion test: simplify ten complexity expressions.

### Session 4: Calculating complexity

- Read `04_calculating_complexity.pdf`.
- Analyse sequential loops, nested loops and loops that divide the input.
- Study the Towers of Hanoi recurrence.
- Completion test: derive the complexity of five unseen code snippets.

### Session 5: Insertion sort

- Read `05_insertion_sort.pdf`.
- Dry-run `[7, 4, 5, 2]` after every outer-loop iteration.
- Write iterative insertion sort from memory.
- Explain best, average and worst cases.

## Phase 3: Arrays and linked lists

### Session 6: Arrays and dynamic arrays

- Read the meaningful pages of `01_array_based_sequences.pdf`.
- Learn contiguous storage and shifting costs.
- Understand incremental growth versus doubling.
- Completion test: explain why append is amortized `O(1)`.

### Session 7: Singly linked lists

- Read `02_designing_a_flexible_list.pdf` and the singly linked-list portion of `03_linked_lists_textbook.pdf`.
- Draw insertion/deletion at head, tail and middle.
- State the cost of each operation with and without a tail pointer.

### Session 8: Linked-list implementation and doubly linked lists

- Study `04_linked_list_python_notebook.pdf`.
- Write `Node`, traversal, insert-at-head and delete-at-head from memory.
- Study doubly linked-list insertion and deletion.
- Completion test: correct a deliberately broken pointer update.

## Phase 4: Stacks and queues

### Session 9: Queue ADT

- Study the queue portion of `01_queues_stacks_textbook.pdf`.
- Learn array, circular-array and linked-list implementations.
- Practise front/rear index movement.
- Completion test: trace wrap-around in a circular queue.

### Session 10: Stack ADT and parentheses

- Study the stack and parentheses portions of the textbook PDF.
- Implement `push`, `pop`, `top` and `is_empty`.
- Solve three balanced-parentheses traces.

### Session 11: Infix evaluation and stock span

- Read `02_evaluating_infix_expression.pdf`.
- Trace value and operator stacks for one expression with parentheses.
- Compare the naive and stack solutions to stock span.
- Implement the `O(n)` stock-span algorithm.

## Phase 5: Priority queues and heaps

### Session 12: Priority queues

- Read `01_priority_queues.pdf`.
- Compare unsorted lists, sorted lists and heaps.
- Learn `insert` and `delete_max` costs.
- Completion test: select the correct implementation for three workloads.

### Session 13: Heap operations

- Study heap definition, completeness and max-heap property.
- Perform three insertions using bubble-up.
- Perform three deletions using bubble-down.
- Learn the array parent/child index relationships.

### Session 14: Heapify and mixed heap practice

- Study bottom-up heapify.
- Understand why heapify is `O(n)`, not `O(n log n)`.
- Build a heap manually from an unsorted array.
- Completion test: detect both completeness and heap-property violations.

## Phase 6: Search trees and balancing

### Session 15: Binary Search Trees

- Read `01_binary_search_trees.pdf`.
- Practise inorder traversal, search, min/max and insertion.
- Perform deletion of a leaf, a one-child node and a two-child node.
- Explain complexity using tree height.

### Session 16: Successor, predecessor and AVL trees

- Read `02_bst_successor_predecessor.pdf`.
- Find successor/predecessor with and without the relevant subtree.
- Begin `03_avl_balanced_search_trees.pdf`.
- Practise LL and RR rotations.

### Session 17: AVL and Red-Black Tree insertion

- Practise LR and RL rotations.
- Compare AVL and Red-Black Trees.
- Learn Red-Black Tree properties.
- Perform insertion cases for red uncle and black uncle.

### Session 18: Red-Black deletion and final tree review

- Study standard BST deletion as the first step.
- Understand red deletion, black deletion and double black.
- Classify sibling-colour and sibling-child cases.
- Do not memorize the full article implementation unless explicitly required.

## Final revision sessions

### Revision A: Complexity and linear structures

- 20-minute closed-book complexity test
- Insertion-sort dry run
- Array-versus-linked-list comparison
- One linked-list pointer question
- One stack and one queue trace

### Revision B: Heaps and search trees

- Heap insert/delete/heapify
- BST deletion
- Successor and predecessor
- All four AVL rotations
- Red-Black properties and one insertion dry run

### Revision C: Full mock and correction

- Attempt a timed mixed paper or self-made question set.
- Mark doubtful answers instead of checking notes immediately.
- Review only after the timer ends.
- Transfer every repeated error to the mistake log.

