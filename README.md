# DA5300 Mid-Semester Exam Preparation

This repository is a structured preparation pack for the **DA5300: Data Structures for Data Science** mid-semester examination at IIT Madras.

It reorganizes the currently available course material into a dependency-based learning order and provides a practical revision system. Additional material can be inserted later without changing the overall workflow.

## Start here

Do not begin by reading every PDF from beginning to end. Use this order:

1. Open [study_plan/STUDY_PLAN.md](study_plan/STUDY_PLAN.md).
2. Complete one learning session at a time.
3. Mark the topic in [study_plan/TOPIC_CHECKLIST.md](study_plan/TOPIC_CHECKLIST.md).
4. Revise operation costs from [study_plan/COMPLEXITY_CHEATSHEET.md](study_plan/COMPLEXITY_CHEATSHEET.md).
5. Use [study_plan/PRACTICE_BLUEPRINT.md](study_plan/PRACTICE_BLUEPRINT.md) for dry runs and exam-style practice.
6. Record repeated errors in [notes/MISTAKE_LOG.md](notes/MISTAKE_LOG.md).

## Current syllabus map

The supplied material contains **22 PDFs** in three broad course units. The recommended study order is:

The original-to-organized filename mapping is recorded in [materials/SOURCE_MANIFEST.md](materials/SOURCE_MANIFEST.md).

| Phase | Topics | Main outcome |
|---:|---|---|
| 1 | Python strings, lists, tuples and dictionaries | Be comfortable reading course code |
| 2 | Efficiency, algorithm analysis, asymptotic notation and insertion sort | Calculate and compare running times |
| 3 | Arrays and linked lists | Understand storage, operations, pointers/references and trade-offs |
| 4 | Stacks, queues and their applications | Implement ADTs and solve expression/stock-span problems |
| 5 | Priority queues and heaps | Perform heap operations and explain their complexity |
| 6 | BST, successor/predecessor, AVL and Red-Black Trees | Perform search-tree operations and balancing dry runs |
| 7 | Mixed revision and mock practice | Retrieve concepts without using notes |

## Material in chronological order

### Phase 1: Python foundations

1. [Strings examples](materials/01_python_foundations/01_strings_examples.pdf)
2. [Lists, tuples and dictionaries](materials/01_python_foundations/02_lists_tuples_dictionaries.pdf)

Treat these as prerequisite revision. Focus on indexing, slicing, mutability, list operations, aliasing, sorting, tuples, dictionaries and comprehensions.

### Phase 2: Algorithm analysis and sorting

1. [Why efficiency matters](materials/02_algorithm_analysis/01_why_efficiency_matters.pdf)
2. [Analysis of algorithms](materials/02_algorithm_analysis/02_analysis_of_algorithms.pdf)
3. [Comparing orders of magnitude](materials/02_algorithm_analysis/03_comparing_orders_of_magnitude.pdf)
4. [Calculating complexity](materials/02_algorithm_analysis/04_calculating_complexity.pdf)
5. [Insertion sort](materials/02_algorithm_analysis/05_insertion_sort.pdf)

You must know input size, best/average/worst case, Big-O, Big-Omega, Big-Theta, iterative complexity, basic recurrences, insertion-sort dry runs and insertion-sort complexity.

### Phase 3: Arrays and linked lists

1. [Array-based sequences](materials/03_arrays_linked_lists/01_array_based_sequences.pdf)
2. [Designing a flexible list](materials/03_arrays_linked_lists/02_designing_a_flexible_list.pdf)
3. [Linked lists textbook slides](materials/03_arrays_linked_lists/03_linked_lists_textbook.pdf)
4. [Linked-list Python notebook](materials/03_arrays_linked_lists/04_linked_list_python_notebook.pdf)

Know contiguous versus linked storage, dynamic-array resizing, singly and doubly linked lists, node structure, traversal, search, insertion and deletion. Be able to draw every pointer/reference change.

### Phase 4: Stacks and queues

1. [Queues and stacks textbook slides](materials/04_stacks_queues/01_queues_stacks_textbook.pdf)
2. [Evaluating an infix expression](materials/04_stacks_queues/02_evaluating_infix_expression.pdf)
3. [Stock span problem](materials/04_stacks_queues/03_stock_span_problem.pdf)

Know FIFO versus LIFO, all core operations, array and linked implementations, circular queues, parentheses matching, expression evaluation and the stack-based stock-span solution.

### Phase 5: Priority queues and heaps

1. [Priority queues](materials/05_priority_queues_heaps/01_priority_queues.pdf)
2. [Heaps](materials/05_priority_queues_heaps/02_heaps.pdf)

Understand the sorted-list/unsorted-list trade-off, complete binary trees, heap property, array representation, bubble-up, bubble-down, `delete_max`, and why bottom-up heapify is `O(n)`.

### Phase 6: Search trees and balanced trees

1. [Binary search trees](materials/06_search_balanced_trees/01_binary_search_trees.pdf)
2. [BST successor and predecessor](materials/06_search_balanced_trees/02_bst_successor_predecessor.pdf)
3. [AVL and balanced search trees](materials/06_search_balanced_trees/03_avl_balanced_search_trees.pdf)
4. [Red-Black Tree versus AVL Tree](materials/06_search_balanced_trees/04_red_black_vs_avl.pdf)
5. [Red-Black Tree insertion](materials/06_search_balanced_trees/05_red_black_tree_insertion.pdf)
6. [Red-Black Tree deletion](materials/06_search_balanced_trees/06_red_black_tree_deletion.pdf)

Know BST ordering, traversal, minimum/maximum, search, insertion, all deletion cases, successor/predecessor, tree height, AVL rotations, Red-Black properties, insertion cases and the purpose of double black during deletion.

## The correct way to study each topic

For every algorithm or data structure, complete these five layers:

1. **Meaning:** Explain it in two or three simple sentences.
2. **Diagram:** Draw the data before and after an operation.
3. **Operations:** State what each operation does.
4. **Complexity:** Give time and space costs with a short reason.
5. **Implementation:** Write or trace the relevant Python code without copying.

A topic is not complete merely because the slides have been read. It is complete when you can explain it, draw it, analyse it and solve one unseen question without notes.

## Recommended 90-minute routine

Use the same routine for every session:

| Time | Task |
|---:|---|
| 0-10 min | Recall the previous topic without opening notes |
| 10-35 min | Read the selected slides and identify the central idea |
| 35-55 min | Make a one-page handwritten summary |
| 55-75 min | Perform one dry run or write the core code |
| 75-85 min | Solve two short complexity/concept questions |
| 85-90 min | Update the checklist and mistake log |

If using two 90-minute slots in a day, use the first for **learning** and the second for **practice plus recall**.

## Plans based on time remaining

### If 14 or more days remain

- Complete one learning session per day.
- Use the second daily slot for practice and revision.
- Keep the final two days for mixed mocks and weak topics.

### If 7-13 days remain

- Complete two related sessions each day.
- Do not skip dry runs.
- Combine Python basics with algorithm analysis and combine Red-Black Tree comparison with insertion.

### If 4-6 days remain

- Prioritize complexity, linked lists, stacks/queues, heaps, BST deletion and AVL rotations.
- Study Red-Black deletion conceptually; do not memorize the full implementation.
- Perform one mixed recall test every night.

### If 3 days or fewer remain

1. Complexity, asymptotic notation and insertion sort
2. Linked lists, stacks, queues and stock span
3. Heap, BST deletion, successor/predecessor, AVL and Red-Black properties

Use the cheat sheet for rapid revision, but still perform at least one dry run per major structure.

## High-priority exam topics

- Big-O, Big-Omega and Big-Theta
- Complexity of iterative and recursive code
- Insertion-sort trace and complexity
- Array versus linked-list comparison
- Linked-list insertion/deletion and pointer changes
- Stack and queue implementations
- Parentheses matching, infix evaluation and stock span
- Priority-queue representation trade-offs
- Heap insertion, deletion and heapify
- BST search, insertion and three deletion cases
- Successor and predecessor
- AVL LL, RR, LR and RL rotations
- Red-Black Tree properties and insertion cases
- Conceptual Red-Black deletion and double black

## What not to spend excessive time memorizing

- Every basic string/list example
- The entire positional-list class
- Repeated progressive slides showing the same animation
- The full C++ implementation in the Red-Black deletion article
- Long blocks of code before understanding the associated diagram

The Red-Black deletion article is best used for cases and diagrams. The main lecture material is Python-oriented, so prepare exam implementations in the language used by the course.

## Exam-readiness test

Before calling a topic complete, answer all five questions:

- [ ] Can I define it without looking at the slide?
- [ ] Can I draw or dry-run an operation?
- [ ] Can I state the important complexities?
- [ ] Can I explain why those complexities occur?
- [ ] Can I write or trace the core Python implementation?

If any answer is no, mark the topic `Learning` or `Practised`, not `Revised`.

## Topics not present in the current material

The current pack does not contain dedicated teaching material for merge sort, quicksort, hashing, graphs, BFS/DFS, tries, disjoint sets or dynamic programming. Do not assume that these are excluded permanently; add them if the instructor provides more mid-semester material.

## Repository structure

```text
DA5300-midsem-prep/
├── README.md
├── materials/
│   ├── SOURCE_MANIFEST.md
│   ├── 01_python_foundations/
│   ├── 02_algorithm_analysis/
│   ├── 03_arrays_linked_lists/
│   ├── 04_stacks_queues/
│   ├── 05_priority_queues_heaps/
│   └── 06_search_balanced_trees/
├── notes/
│   └── MISTAKE_LOG.md
└── study_plan/
    ├── STUDY_PLAN.md
    ├── TOPIC_CHECKLIST.md
    ├── COMPLEXITY_CHEATSHEET.md
    └── PRACTICE_BLUEPRINT.md
```

## Adding new material

When new files are provided:

1. Place each file in the closest existing numbered folder.
2. Create a new numbered folder only if the topic is genuinely new.
3. Add the file link to this README.
4. Add its concepts to the topic checklist.
5. Insert a study session before mixed revision.
6. Commit with a clear message such as `add hashing lecture and practice checklist`.

## Suggested Git workflow

```bash
git init
git add .
git commit -m "organize DA5300 midsem preparation material"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Use small later commits, for example:

```text
complete algorithm analysis notes
add heap dry runs
revise BST deletion cases
add newly shared lecture material
```

## Important repository-visibility note

Some PDFs appear to be lecture slides, textbook extracts or saved webpages. Keep the GitHub repository **private** unless you have permission to redistribute every included document. If you want a public repository, publish only your own notes, checklists and code, and exclude the `materials/` directory.
