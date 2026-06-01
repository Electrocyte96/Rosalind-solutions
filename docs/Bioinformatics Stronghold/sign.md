#   Enumerating Oriented Gene Orderings(ID: SIGN)

This problem is a extension for `perm.py` and just like any other recursion problem, it took me a while but I managed to figure it out. 

The problem separates in two parts: `sign_combs(n)` and `sign_and_perms(n)`, first one being the generation of the all the combination of signs $+/-$ given a positive value of $n\leq{6}$ and the second one being the product of one list containig the permutations of $1 ... n$ values and the list of lists containing all the combinations of symbols $+/-$. For example: 

<div align="center">
    <table>
        <thead>
            <tr>
                <th>First permutation when n=2</th>
                <th>First combination of +/- </th>
                <th>Product</th>
            <tr>
        <thead>
        <tbody>
            <tr>
                <td>[1, 2]</td>
                <td>[[1, 1], [-1, 1], [1, -1], [-1, -1]]</td>
                <td>[[1, 2], [-1, 2], [1, -2], [-1, -2]]</td>
            <tr>
        </tbody>
    </table>
</div>

To make it more clear I will go through each iteration for both functions, starting with `sign_combs(n)` when $n = 3$:

```
def sign_combs(n: int) -> list[list[int]]:
    if n == 1:
        return [[1], [-1]]
    sign_position = []
    for i in sign_combs(n-1):
        sign_position.append([1] + i)
        sign_position.append([-1] + i)
    return sign_position
```

The first thing that caught my attention was the use of `sign_combs(n-1)` as an iterable. Since the function returns a list it is possible.

<div align='center'>
    <table>
        <thead>
            <tr>
                <th>sign_combs(1)</th>
                <th>i</th>
                <th>.append[1]</th>
                <th>.append[-1]</th>
                <th>sign_position</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan='2'>[[1], [-1]]</td>
                <td>[1]</td>
                <td>[1]+i</td>
                <td>[-1]+i</td>
                <td>[[1, 1], [-1, 1]]</td>
            </tr>
            <tr>
                <td>[-1]</td>
                <td>[-1]+i</td>
                <td>[-1]+i</td>
                <td>[[1, 1], [-1, 1], [1, -1], [-1, -1]]</td>
            </tr>
        </tbody>
    </table>
</div>

<div align='center'>
    <table>
        <thead>
            <tr>
                <th>sign_combs(2)</th>
                <th>i</th>
                <th>.append[1]</th>
                <th>.append[-1]</th>
                <th>sign_position</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan='4'>[[1, 1], [-1, 1], [1, -1], [-1, -1]]</td>
                <td>[1, 1]</td>
                <td>[1]+i</td>
                <td>[-1]+i</td>
                <td>[[1, 1, 1], [-1, 1, 1]]</td>
            </tr>
            <tr>
                <td>[-1, 1]</td>
                <td>[1]+i</td>
                <td>[-1]+i</td>
                <td>[[1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1]]</td>
            </tr>
            <tr>
                <td>[1, -1]</td>
                <td>[1]+i</td>
                <td>[-1]+i</td>
                <td>[[1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1], [1, 1, -1], [-1, 1, -1]</td>
            </tr>
            <tr>
                <td>[-1, -1]</td>
                <td>[1]+i</td>
                <td>[-1]+i</td>
                <td>[[1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1], [1, 1, -1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]]</td>
            </tr>
        </tbody>
    </table>
</div>

So we end having all sign combinations given an  $n\leq{6}$. This is a subroutine for `sign_and_perms(n)`, let´s see this other function.

```
def sign_and_perms(n:int)->list:
    sign_w_perms = []
    n_list = [x for x in range(1,n+1)]
    permutations = permutation(n_list)
    for perm in permutations:
        for sign in sign_combs(n):
            sign_perm = []
            for i in range(n):
                sign_perm.append(sign[i]*perm[i])
            sign_w_perms.append(sign_perm)
    return sign_w_perms
```



