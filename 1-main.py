#!/usr/bin/python3

from linkedlist import LinkedList, Node

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.display()

linked_list.delete(2)
linked_list.display()
