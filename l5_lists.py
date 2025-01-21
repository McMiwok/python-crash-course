#
#
# OS
# Virtual Memory - roughly speaking its intent to map Hardware memory to an application
#
# | text fragments | 0xFFF
# |                |
# |                |
# |                |
# |                |
# |                |
# |      ^         |
# |     Heap       | 0xB0
# |     Stack      | 0xAF
# |                |
#
# Garbage Collector
# Reference Counter
#
# PYTHON STORES ALL THE VARIABLES ON THE HEAP!!!
#
# l = [1, 2, 3]
# stack: [{
#    ref *l (pointer to the object on the heap),
#    rc: int  <--- how many pointers to the object currently exists in memory. If rc == 0 then drop(l) else rc -= 1
# }
#
#
# a = 0
# stack: [{
#    ref *a,
#    rc: int
# }]
#
# One of Python optimizations.
# It pre-allocates small values like
# - None
# - ()
# - ""
# - True, False
# - [0..255]
#

if __name__ == "__main__":
    # Dynamic arrays.
    # Stored in the heap
    # May be modified during runtime

    # How to create a list
    # 1. Use []
    l = [1, 2, 3, "hjh", "rr", 3.54, 3 + 2j, None]

    # 2. Use list()
    l = list()

    # 2.1. Use list() to cast object into list
    s = "aba"
    l = list(s)
    # Usually, generators are cast to lists

    # 3. List comprehension
    #    [
    #        <element to be written to each block of list>
    #        for v in range(1, 10)
    #        {optional if <expr>}
    #    ]
    l = [v for v in range(1, 10)]
    l = [None for _ in range(1, 10)]
    l = [v for v in range(1, 10) if v != 5]

    # Python supports negative indexing
    # Get last element as
    last = l[-1]

    # Set element as
    l[0] = 999

    # Basic functions
    l.append(192)  # add to the end
    l.pop()  # delete from the end

    # List support concatenation
    l = [1, 2, 3] + [4, 5, 6]

    # Extend one from another
    l.extend([8, 9, 10])

    # Reverse and sort are in-place
    l.reverse()  # or l[::-1] but it creates a copy
    l.sort()  # Quick Sort

    # Functions
    len(l)
    sum(l)
    min(l), max(l)

    # Slice
    # SLICE CREATES SHALLOW COPY OF A COLLECTION!!

    for v in l:
        print(v)
