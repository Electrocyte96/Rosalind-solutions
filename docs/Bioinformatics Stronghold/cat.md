#   Catalan Numbers and RNA Secondary Structures (ID: CAT)

This problem just like any other problem with recursion took me some time but at the very end I was able to crack it. Also this problem strongly forces you to implement some sort of memoization. At first everything looks right when using Rosalind's sample dataset, but when it comes down to use the dataset to pass the problem in the platform, at least for me memoization is needed because finding the solution takes more (way more) than 5:00 minutes.

Just to be clear the function `count_structures(rna)` recives a string and calls `is_complement(first_base, rna[i]` function that recives two strings, ideally characters i.e. `'A'` and `'U'`, and returns a boolean if the pairing is possible in a biological transcription context.  

The main idea of the `count_structures(rna)` function is to pair compatible nucleotides and if so, take those nucleotides and divide  rna secuence in two parts,  `inner =  rna[1:i]` and `outer = rna[i+1:]`. Let's say that we have the sequence `'AUAUAU'` and if we pair ``A[0]`` and ``U[3]`` then  ``inner = "UA"`` and ``outer = "AU"``. And then apply `count_structures(rna)` on both inner and outer and so on. The goal of `count_structures(rna)` is to get all inner structures * outer structures. 

Full code bellow:
```
def count_structures(rna:str)->int:
    if rna in memo:
        return memo[rna]
    if rna == '':
        return 1
    if len(rna) % 2 != 0:
        return 0
    if rna.count('A') != rna.count('U') or rna.count('C') != rna.count('G'):
        return 0
    total,n = 0,len(rna)
    first_base = rna[0]
    for i in range(1, n, 2):
        if is_complement(first_base, rna[i]):
            inner, outer = rna[1:i], rna[i+1:]
            inner_seqs, outer_seqs = (count_structures(inner)), (count_structures(outer))
            total += inner_seqs * outer_seqs
    memo[rna] = total
    return totalx
```

Now let's take a look on the base cases:  
When the given string is empty returns 1 because the string given is already forming a valid structure.
```
if rna == "":
    return 1
```

Also the problem requires perfect matchings, meaning that every nucleotide has a complement. So if the ``rna`` length is odd or the number of  `'A' != 'U'` or `'G' != 'C'` the function returns 0.

```
if len(rna) % 2 != 0:
        return 0
    if rna.count('A') != rna.count('U') or rna.count('C') != rna.count('G'):
        return 0
```

Following that idea we can note that for-loop starts at one and only iterates through odd numbers, because given a odd rna sequence then the inner sequence will be lenght even and therefore might be perfect.

```
for i in range(1, n, 2):
```

Let´s make a brief example of `count_structures(rna)` using the sequence ``'AUAUAU'``, with html tables made by ChatGPT because i'm so done doing it by hand at this point. 

<div align='center'>
<h3>Example: AUAUAU</h3>
<p>
RNA sequence:
</p>
<pre>
A U A U A U
0 1 2 3 4 5
</pre>
<p>
The first nucleotide (A at position 0) can pair with U at position 1, 3, or 5.
For each valid pairing, the sequence is split into an inner and an outer region.
</p>

<table>
    <thead>
        <tr>
            <th>Pairing</th>
            <th>Inner Region</th>
            <th>Outer Region</th>
            <th>count(inner)</th>
            <th>count(outer)</th>
            <th>Contribution</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>A[0] ↔ U[1]</td>
            <td>""</td>
            <td>"AUAU"</td>
            <td>1</td>
            <td>2</td>
            <td>1 × 2 = 2</td>
        </tr>
        <tr>
            <td>A[0] ↔ U[3]</td>
            <td>"UA"</td>
            <td>"AU"</td>
            <td>1</td>
            <td>1</td>
            <td>1 × 1 = 1</td>
        </tr>
        <tr>
            <td>A[0] ↔ U[5]</td>
            <td>"UAUA"</td>
            <td>""</td>
            <td>2</td>
            <td>1</td>
            <td>2 × 1 = 2</td>
        </tr>
        <tr>
            <td colspan="5"><strong>Total Structures</strong></td>
            <td><strong>5</strong></td>
        </tr>
    </tbody>
</table>
</div>

Then why `count("AUAU") = 2`?

<div align='center'>
    <h4>Subproblem: AUAU</h4>
    <table>
        <thead>
            <tr>
                <th>Pairing</th>
                <th>Inner Region</th>
                <th>Outer Region</th>
                <th>Contribution</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>A[0] ↔ U[1]</td>
                <td>""</td>
                <td>"AU"</td>
                <td>1 × 1 = 1</td>
            </tr>
            <tr>
                <td>A[0] ↔ U[3]</td>
                <td>"UA"</td>
                <td>""</td>
                <td>1 × 1 = 1</td>
            </tr>
            <tr>
                <td colspan="3"><strong>Total Structures</strong></td>
                <td><strong>2</strong></td>
            </tr>
        </tbody>
    </table>
</div>

Notes about memoization

<div align='center'>
    <h4>Why Memoization Helps</h4>
    <table>
        <thead>
            <tr>
                <th>Subsequence</th>
                <th>Occurrences</th>
                <th>Computed Once?</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>"AUAU"</td>
                <td>Multiple recursive branches</td>
                <td>Yes (stored in memo)</td>
            </tr>
            <tr>
                <td>"UA"</td>
                <td>Multiple recursive branches</td>
                <td>Yes (stored in memo)</td>
            </tr>
            <tr>
                <td>""</td>
                <td>Many recursive branches</td>
                <td>Yes (base case)</td>
            </tr>
        </tbody>
    </table>
</div>
