# DA5300 Practice Blueprint

Use these question patterns after learning each topic. Do not immediately look at code or slides.

## Pattern 1: Definition and comparison

Answer in three to five lines.

1. Why is algorithm analysis expressed using input size?
2. Differentiate Big-O, Big-Omega and Big-Theta.
3. Compare arrays and linked lists.
4. Compare stacks and queues.
5. Compare sorted and unsorted priority-queue implementations.
6. Compare a BST, AVL Tree and Red-Black Tree.

## Pattern 2: Complexity calculation

For every answer, write the counted operation and number of repetitions.

1. Analyse a single loop over `n` elements.
2. Analyse two nested loops over `n` elements.
3. Analyse a loop in which `n` is divided by 2 each iteration.
4. Analyse one `O(n)` phase followed by one `O(n^2)` phase.
5. Explain the Towers of Hanoi recurrence.
6. Explain why bottom-up heapify is `O(n)`.

## Pattern 3: Array and linked-list tracing

1. Insert a value at the beginning of an array and list every shifted element.
2. Insert a node at the head of a singly linked list.
3. Insert a node between two existing nodes.
4. Delete the tail of a singly linked list.
5. Delete a middle node of a doubly linked list.
6. Identify the incorrect pointer update in a broken implementation.

## Pattern 4: Stack and queue tracing

1. Show the stack after every symbol in `([{}])`.
2. Find the first mismatch in `([)]`.
3. Evaluate `3 + 5 * 2` using value and operator stacks.
4. Evaluate `(8 - 2) * (3 + 1)` using two stacks.
5. Trace enqueue/dequeue operations in a circular queue.
6. Solve stock span for `[100, 80, 60, 70, 60, 75, 85]`.

## Pattern 5: Heap dry runs

1. Decide whether a given tree is complete.
2. Decide whether a complete tree satisfies the max-heap property.
3. Insert `77` into a supplied max heap and show each swap.
4. Delete the maximum and show each bubble-down step.
5. Convert an unsorted array into a heap.
6. State the array index of a node's parent and children.

## Pattern 6: BST operations

Construct a BST by inserting:

```text
50, 30, 70, 20, 40, 60, 80
```

Then:

1. Write its inorder traversal.
2. Find minimum and maximum.
3. Search for `40` and show the path.
4. Delete leaf `20`.
5. Delete a node with one child after modifying the tree appropriately.
6. Delete node `50`, which has two children.
7. Find successor and predecessor of different nodes.

## Pattern 7: AVL rotations

Identify the case and correct the tree:

| Insertion order | Expected imbalance |
|---|---|
| `30, 20, 10` | LL |
| `10, 20, 30` | RR |
| `30, 10, 20` | LR |
| `10, 30, 20` | RL |

After every correction, recompute the balance factors.

## Pattern 8: Red-Black Trees

1. State all Red-Black Tree properties.
2. Explain why a new node is initially red.
3. Insert when the parent is black.
4. Repair an insertion when the parent and uncle are red.
5. Repair LL/RR and LR/RL cases when the uncle is black.
6. Explain why deleting a black node may create double black.
7. Compare the role of the uncle in insertion with the sibling in deletion.

## Three-pass practice rule

For every dry run:

1. **Guided:** solve while looking at one worked example.
2. **Closed-book:** solve a new example without notes.
3. **Timed:** solve another new example under an exam-style time limit.

Only the third pass shows whether the topic is ready for the exam.

