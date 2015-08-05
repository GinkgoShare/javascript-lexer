# Write a procedure nfsmaccepts() that takes four
# arguments corresponding to a non-derministic finite state machine:
#   the start (or current) state
#   the edges (encoded as a mapping)
#   the list of accepting states
#   a list of states already visited (starts empty) 

# If the finite state machine accepts any string, your procedure must
# return one such string (your choice!). Otherwise, if the finite state
# machine is empty, your procedure must return None (the value None, not
# the string "None"). 
#
# For example, this non-deterministic machine ...
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 2],
          (4, 'c') : [5] }
accepting = [5] 
# ... accepts exactly one string: "abc". By contrast, this
# non-deterministic machine: 
edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }
accepting2 = [2] 
# ... accepts no strings (if you look closely, you'll see that you cannot
# actually reach state 2 when starting in state 1).

def nfsmaccepts(current, edges, accepting, visited): 
    if current in accepting:
        return ""
    elif current in visited:
        return None
    else:
        new_visited = visited + [current]
        for edge in edges:
            if edge[0] == current:
                for state in edges[edge]:
                    foo = nfsmaccepts(state, edges, accepting, new_visited)
                    if foo != None:
                        return edge[1] + foo
    return None
                

        

# This problem includes some test cases to help you tell if you are on
# the right track. You may want to make your own additional tests as well.
print "Test 1: " + str(nfsmaccepts(1, edges, accepting, []) == "abc") 
print "Test 2: " + str(nfsmaccepts(1, edges, [4], []) == "ab") 
print "Test 3: " + str(nfsmaccepts(1, edges2, accepting2, []) == None) 
print "Test 4: " + str(nfsmaccepts(1, edges2, [1], []) == "")
print "hello"