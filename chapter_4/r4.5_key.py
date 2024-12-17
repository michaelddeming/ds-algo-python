"""Draw the recursion trace for the execution of function PuzzleSolve(3,S,U)
(Code Fragment 4.14), where S is empty and U= {a,b,c,d}."""

                                                                # P(3, [], {a,b,c,d})

                    # P(2, [a], {b,c,d})            # P(2, [b], {a,c,d})        # P(2, [c], {a,b,d})        # P(2, [d], {a,b,c})   

                    # P(1, [a,b], {c,d})            # P(1, [b,a], {c,d})        # P(1, [c,a], {b,d})        # P(1, [d,a], {b,c})  
                    # P(1, [a,c], {b,d})            # P(1, [b,c], {a,d})        # P(1, [c,b], {a,d})        # P(1, [d,b], {a,c})   
                    # P(1, [a,d], {b,c})            # P(1, [b,d], {a,c})        # P(1, [c,d], {a,b})        # P(1, [d,c], {a,b})       