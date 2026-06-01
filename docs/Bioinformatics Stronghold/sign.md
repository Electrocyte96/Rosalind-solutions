#   Enumerating Oriented Gene Orderings (ID: SIGN)

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

First you get all combinations for $n$ with `permutation(n_list)`. This function receives a list containing the elements and returns a list of lists, and each of them contains one of the possible combinations of all the elements, for example: $n=3$ the permutations would be:

<div  align='center'>
    <table>
    <thead>
        <tr>
        <th>Permutations when n=3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>[[1, 2, 3],</td>
        </tr>
        <tr>
        <td>[1, 3, 2],</td>
        </tr>
        <tr>
        <td>[2, 1, 3],</td>
        </tr>
        <tr>
        <td>[2, 3, 1],</td>
        </tr>
        <tr>
        <td>[3, 1, 2],</td>
        </tr>
        <tr>
        <td>[3, 2, 1]]</td>
        </tr>
    </tbody>
    </table>
</div>

Then we iterate through all the elements of `perms` and for each element we call our `sign_combs(n)` functions so we get all the combinations of signs and loop through all combinations. Finally we loop through the  elements of `perm` and multiply the $i-th$ element of `perms` vs the $i-th$ element of `signs`, like `.(signs[i]*perm[i])`. The main idea is that for each element of `perms` we create a new set of combinations with all signs combinations. 

¡Por supuesto! Para `n = 3`, tenemos 6 permutaciones (las formas de ordenar `[1, 2, 3]`) y 8 combinaciones de signos. Eso nos da un total de **48 iteraciones completas**.

Aquí tienes la tabla detallada en HTML, contenida en un contenedor centrado como lo solicitaste, donde puedes observar exactamente cómo se multiplica cada elemento índice por índice (`signs[i] * perm[i]`) antes de agregarse al resultado final.

<div>
    <table>
    <thead>
    <tr>
        <th>Perm</th>
        <th>Sign</th>
        <th>(sign[i]*perm[i])</th>
        <th>sign_perm</th>
    <tr>
    <thead>
  <tr>
    <td rowspan="8"><strong>[1, 3, 2]</strong></td>
    <td>[1, 1, 1]</td>
    <td>(1 * 1), (1 * 3), (1 * 2)</td>
    <td><strong>[1, 3, 2]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, 1]</td>
    <td>(-1 * 1), (1 * 3), (1 * 2)</td>
    <td><strong>[-1, 3, 2]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, 1]</td>
    <td>(1 * 1), (-1 * 3), (1 * 2)</td>
    <td><strong>[1, -3, 2]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, 1]</td>
    <td>(-1 * 1), (-1 * 3), (1 * 2)</td>
    <td><strong>[-1, -3, 2]</strong></td>
  </tr>
  <tr>
    <td>[1, 1, -1]</td>
    <td>(1 * 1), (1 * 3), (-1 * 2)</td>
    <td><strong>[1, 3, -2]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, -1]</td>
    <td>(-1 * 1), (1 * 3), (-1 * 2)</td>
    <td><strong>[-1, 3, -2]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, -1]</td>
    <td>(1 * 1), (-1 * 3), (-1 * 2)</td>
    <td><strong>[1, -3, -2]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, -1]</td>
    <td>(-1 * 1), (-1 * 3), (-1 * 2)</td>
    <td><strong>[-1, -3, -2]</strong></td>
  </tr>

  <tr>
    <td rowspan="8"><strong>[2, 1, 3]</strong></td>
    <td>[1, 1, 1]</td>
    <td>(1 * 2), (1 * 1), (1 * 3)</td>
    <td><strong>[2, 1, 3]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, 1]</td>
    <td>(-1 * 2), (1 * 1), (1 * 3)</td>
    <td><strong>[-2, 1, 3]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, 1]</td>
    <td>(1 * 2), (-1 * 1), (1 * 3)</td>
    <td><strong>[2, -1, 3]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, 1]</td>
    <td>(-1 * 2), (-1 * 1), (1 * 3)</td>
    <td><strong>[-2, -1, 3]</strong></td>
  </tr>
  <tr>
    <td>[1, 1, -1]</td>
    <td>(1 * 2), (1 * 1), (-1 * 3)</td>
    <td><strong>[2, 1, -3]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, -1]</td>
    <td>(-1 * 2), (1 * 1), (-1 * 3)</td>
    <td><strong>[-2, 1, -3]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, -1]</td>
    <td>(1 * 2), (-1 * 1), (-1 * 3)</td>
    <td><strong>[2, -1, -3]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, -1]</td>
    <td>(-1 * 2), (-1 * 1), (-1 * 3)</td>
    <td><strong>[-2, -1, -3]</strong></td>
  </tr>

  <tr>
    <td rowspan="8"><strong>[2, 3, 1]</strong></td>
    <td>[1, 1, 1]</td>
    <td>(1 * 2), (1 * 3), (1 * 1)</td>
    <td><strong>[2, 3, 1]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, 1]</td>
    <td>(-1 * 2), (1 * 3), (1 * 1)</td>
    <td><strong>[-2, 3, 1]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, 1]</td>
    <td>(1 * 2), (-1 * 3), (1 * 1)</td>
    <td><strong>[2, -3, 1]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, 1]</td>
    <td>(-1 * 2), (-1 * 3), (1 * 1)</td>
    <td><strong>[-2, -3, 1]</strong></td>
  </tr>
  <tr>
    <td>[1, 1, -1]</td>
    <td>(1 * 2), (1 * 3), (-1 * 1)</td>
    <td><strong>[2, 3, -1]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, -1]</td>
    <td>(-1 * 2), (1 * 3), (-1 * 1)</td>
    <td><strong>[-2, 3, -1]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, -1]</td>
    <td>(1 * 2), (-1 * 3), (-1 * 1)</td>
    <td><strong>[2, -3, -1]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, -1]</td>
    <td>(-1 * 2), (-1 * 3), (-1 * 1)</td>
    <td><strong>[-2, -3, -1]</strong></td>
  </tr>

  <tr>
    <td rowspan="8"><strong>[3, 1, 2]</strong></td>
    <td>[1, 1, 1]</td>
    <td>(1 * 3), (1 * 1), (1 * 2)</td>
    <td><strong>[3, 1, 2]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, 1]</td>
    <td>(-1 * 3), (1 * 1), (1 * 2)</td>
    <td><strong>[-3, 1, 2]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, 1]</td>
    <td>(1 * 3), (-1 * 1), (1 * 2)</td>
    <td><strong>[3, -1, 2]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, 1]</td>
    <td>(-1 * 3), (-1 * 1), (1 * 2)</td>
    <td><strong>[-3, -1, 2]</strong></td>
  </tr>
  <tr>
    <td>[1, 1, -1]</td>
    <td>(1 * 3), (1 * 1), (-1 * 2)</td>
    <td><strong>[3, 1, -2]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, -1]</td>
    <td>(-1 * 3), (1 * 1), (-1 * 2)</td>
    <td><strong>[-3, 1, -2]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, -1]</td>
    <td>(1 * 3), (-1 * 1), (-1 * 2)</td>
    <td><strong>[3, -1, -2]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, -1]</td>
    <td>(-1 * 3), (-1 * 1), (-1 * 2)</td>
    <td><strong>[-3, -1, -2]</strong></td>
  </tr>

  <tr>
    <td rowspan="8"><strong>[3, 2, 1]</strong></td>
    <td>[1, 1, 1]</td>
    <td>(1 * 3), (1 * 2), (1 * 1)</td>
    <td><strong>[3, 2, 1]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, 1]</td>
    <td>(-1 * 3), (1 * 2), (1 * 1)</td>
    <td><strong>[-3, 2, 1]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, 1]</td>
    <td>(1 * 3), (-1 * 2), (1 * 1)</td>
    <td><strong>[3, -2, 1]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, 1]</td>
    <td>(-1 * 3), (-1 * 2), (1 * 1)</td>
    <td><strong>[-3, -2, 1]</strong></td>
  </tr>
  <tr>
    <td>[1, 1, -1]</td>
    <td>(1 * 3), (1 * 2), (-1 * 1)</td>
    <td><strong>[3, 2, -1]</strong></td>
  </tr>
  <tr>
    <td>[-1, 1, -1]</td>
    <td>(-1 * 3), (1 * 2), (-1 * 1)</td>
    <td><strong>[-3, 2, -1]</strong></td>
  </tr>
  <tr>
    <td>[1, -1, -1]</td>
    <td>(1 * 3), (-1 * 2), (-1 * 1)</td>
    <td><strong>[3, -2, -1]</strong></td>
  </tr>
  <tr>
    <td>[-1, -1, -1]</td>
    <td>(-1 * 3), (-1 * 2), (-1 * 1)</td>
    <td><strong>[-3, -2, -1]</strong></td>
  </tr>
</tbody>
    </table>
</div>



