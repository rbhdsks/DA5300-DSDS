# DA5300 Complexity Cheat Sheet

## Growth-rate order

From slower to faster growth:

```text
O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)
```

## Asymptotic notation

| Notation | Meaning |
|---|---|
| `O(g(n))` | Asymptotic upper bound |
| `Omega(g(n))` | Asymptotic lower bound |
| `Theta(g(n))` | Matching upper and lower bound |

Drop constant factors and lower-order terms:

```text
7n + 20              -> Theta(n)
3n^2 + 5n + 9        -> Theta(n^2)
n log n + 100n       -> Theta(n log n)
```

## Common code patterns

| Pattern | Complexity |
|---|---:|
| One loop over `n` items | `O(n)` |
| Two full nested loops | `O(n^2)` |
| Three full nested loops | `O(n^3)` |
| Repeatedly divide `n` by 2 | `O(log n)` |
| Outer `n`, inner `log n` | `O(n log n)` |
| Two sequential phases | Maximum/dominant phase |

## Python sequence operations

| Operation | Typical complexity |
|---|---:|
| List/string index access | `O(1)` |
| List append | Amortized `O(1)` |
| Insert/delete at list beginning | `O(n)` |
| List membership/search | `O(n)` |
| Dictionary lookup/insert/delete | Average `O(1)` |

## Arrays and linked lists

| Operation | Dynamic array | Singly linked list |
|---|---:|---:|
| Access by position | `O(1)` | `O(n)` |
| Search by value | `O(n)` | `O(n)` |
| Insert/delete at head | `O(n)` | `O(1)` |
| Append | Amortized `O(1)` | `O(1)` with tail, otherwise `O(n)` |
| Delete at tail | `O(1)` | `O(n)` |

## Stack and queue

| Operation | Complexity |
|---|---:|
| Stack `push`, `pop`, `top` | `O(1)` |
| Queue `enqueue`, `dequeue`, `first` | `O(1)` with a proper implementation |
| Parentheses matching | `O(n)` time, `O(n)` space |
| Stack-based stock span | `O(n)` time, `O(n)` space |

## Sorting

| Algorithm | Best | Average | Worst | Extra space |
|---|---:|---:|---:|---:|
| Insertion sort | `O(n)` | `O(n^2)` | `O(n^2)` | `O(1)` |

Insertion sort is in-place and stable in its standard implementation.

## Priority queues

| Representation | Insert | Delete maximum |
|---|---:|---:|
| Unsorted list | `O(1)` | `O(n)` |
| Sorted list | `O(n)` | `O(1)` |
| Heap | `O(log n)` | `O(log n)` |

## Max heap

| Operation | Complexity |
|---|---:|
| Read maximum | `O(1)` |
| Insert/bubble-up | `O(log n)` |
| Delete maximum/bubble-down | `O(log n)` |
| Bottom-up heapify | `O(n)` |
| Process all elements | `O(n log n)` |

For zero-based array indexing:

```text
left child  = 2*i + 1
right child = 2*i + 2
parent      = (i - 1) // 2
```

## Search trees

| Structure/operation | Average or balanced | Worst |
|---|---:|---:|
| Ordinary BST search | `O(log n)` | `O(n)` |
| Ordinary BST insert | `O(log n)` | `O(n)` |
| Ordinary BST delete | `O(log n)` | `O(n)` |
| AVL search/insert/delete | `O(log n)` | `O(log n)` |
| Red-Black search/insert/delete | `O(log n)` | `O(log n)` |

BST operations are fundamentally `O(h)`, where `h` is tree height.

