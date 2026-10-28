#   Finding a Shared Spliced Motif  (ID: LCSQ)

When I was doing this exercise I faced a problem that caught my attention. This was that, when creating the list for filling the scores of alignment, just a list of list full of zeros.    

My first approach was to simply, create variables with the length of the sequences + 1. It is like that because the matrix dimensions $i,j$  must be number of rows +1 and columns +1, and also create the matrix elements, a list of lists. I made all of that with: 
```
a,b = 'AACCTTGG', 'ACACTGTGA'
a_len, b_len = len(a)+1 , len(b)+1

cols = [0 for i in range(b_len)]
M = [cols for i in range(a_len)] 
```
And of course the output is:

```
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
```

At this point this looks that is working perfectly fine but there is a major flaw with it and this happens when creating the list or matrix `M`. When doing this I assumed I was appending different lists to `M`. But instead I appended different references but from the same list, This is a problem because when finishing the matrix generation I ended with `M` being something like this:

```
[[0, 1, 2, 2, 3, 4, 5, 5, 6, 6],
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6],
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6], 
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6],
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6],
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6],
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6],
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6],
[0, 1, 2, 2, 3, 4, 5, 5, 6, 6]]
```

This is obviously incorrect and what is happening is that all changes you do in any element of any list are changes that get saved in the final list that typically is the last one to fill. Instead of having $i$ independent lists I am having $i$ references (pointers) to an only object in memory. 

So the correct procedure for creating the `M` list is:

```
M = [[0] * b_len  for i in range(a_len)]
```

Where you create a new  `[0]* b_len` list for each iteration across `a_len`
