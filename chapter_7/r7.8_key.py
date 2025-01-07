"""Describe a nonrecursive method for finding, by link hopping, the middle node of a doubly linked list with header and trailer sentinels. In the case of an even number of nodes, report the node slightly left of center as the “middle.” (Note: This method must only use link hopping; it cannot use a counter.) What is the running time of this method?"""

def find_middle_node(head):

    tracker_1 = head
    tracker_2 = head


    while tracker_1._next != None and tracker_1.next.next != None:
        tracker_1 = tracker_1._next.next
        tracker_2 = tracker_2.next

    # tracker_1 is at the position of the Trailer Sentinel, it's .next == None

    return tracker_2