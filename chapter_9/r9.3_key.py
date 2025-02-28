"""What does each remove min call return within the following sequence ofpriority queue ADT methods: 

1. add(5,A) PQ = [(5,A)]
2. add(4,B) PQ = [(4,B), (5,A)]
3. add(7,F) PQ = [(4,B), (5,A), (7,F)]
4. add(1,D) PQ = [(1,D), (4,B), (5,A), (7,F)]
5. remove min() PQ = [(4,B), (5,A), (7,F)] --> return (1, D) 
6. add(3,J) PQ = [(3,J), (4,B), (5,A), (7,F)]
7. add(6,L) PQ = [(3,J), (4,B), (5,A), (6,L), (7,F)]
8. remove min() PQ = [(4,B), (5,A), (6,L), (7,F)] --> return (3,J)
9. remove min() PQ = [(5,A), (6,L), (7,F)] --> return (4,B)
10. add(8,G) PQ = [(5,A), (6,L), (7,F), (8,G)]
11. remove min() PQ = [(6,L), (7,F), (8,G)] --> return (5,A)
12. add(2,H) PQ = [(2,H), (6,L), (7,F), (8,G)]
13. remove min() PQ = [(6,L), (7,F), (8,G)] --> return (2,H)
14. remove min() PQ = [(7,F), (8,G)] --> return (6,L)
"""