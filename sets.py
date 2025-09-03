a = {1, 2, 3 }
b = {3, 4, 5}


print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric difference → {1, 2, 4, 5}

b.add(8)          # {4, 5, 6, 7, 8}
b.remove(8)       # 4, 5, 6, 7
b.discard(9)      # safe remove, no error if not found
b.pop()           # removes a random element
b.clear()
print()
print(a)

"""
add(x) → Add an element.

remove(x) → Remove element (error if not found).

discard(x) → Remove element (no error if not found).

pop() → Remove and return a random element.

clear() → Remove all elements.

union(other_set) → Combine sets.

intersection(other_set) → Common elements.

difference(other_set) → Elements not in the other.

issubset(other_set) → Check subset.

issuperset(other_set) → Check superset.
"""