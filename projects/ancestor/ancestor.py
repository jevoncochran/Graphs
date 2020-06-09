
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue(starting_node)
    # start with starting_node
    # does it have parents?
    n = q.dequeue()
    for item in ancestors:
        if item[-1] == starting
    # if it does have parents, get them
    # does its parents have parents
    # stop when there are no more "parents"
    # if there are multiple "parents," return lowest numeric ID
    # if it does not have parents, return -1