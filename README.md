# goit-algo-hw-04
Master of Science (Neoversity): Basic Algorithms and Data Structures - Homework №4

## Результати порівняння алгоритмів сортуванння:

- **Small dataset**:
`merge_sort`: 0.02639 seconds
`insertion_sort`: 0.03183 seconds
`timsort`: 0.00041 seconds

- **Medium dataset**:
`merge_sort`: 0.31863 seconds
`insertion_sort`: 2.70250 seconds
`timsort`: 0.00862 seconds

- **Large dataset**:
`merge_sort`: 3.53930 seconds
`insertion_sort`: 282.68993 seconds
`timsort`: 0.13267 seconds

З отриманих даних можна побачити, що timsort працює краще, ніж merge_sort і insertion_sort для всіх трьох наборів даних. В свою чергу merge_sort очікувано краще відпрацьовує за insertion_sort при чому зі збільшенням розміру масиву ця різниця більш помітна.
