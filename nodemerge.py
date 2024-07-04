from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # Dummy node to handle edge cases
        current = dummy 
        segment_sum = 0
        node = head.next # Skip the initial 0 node

        while node is not None:
            if node.value == 0:
                # End of a segment
                if segment_sum != 0:
                    current.next = ListNode(segment_sum)
                    current = current.next
                segment_sum = 0 # Rest for the next segment
            else:
                segment_sum += node.val # Sum up the values in the segment
            node = node.next

        return dummy.next # Return the modfied list, skiipping the dummy node


# Helper function to print linked list (for testing purposes)
def print_linked_list(head: Optional[ListNode]):
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    print("->".join(map(str, nodes)))

    # Example usage:
    # Create the linked list: 0 -> 1 -> 2 -> 0 -> 3 -> 4 -> 0 -> 5 -> 0
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(0)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(0)

    # Process the linked list 

    solution Solution()

    new_head = solution.mergeNodes(head)

    # Print the modified linked list
    print_linked_listt(new_head)
