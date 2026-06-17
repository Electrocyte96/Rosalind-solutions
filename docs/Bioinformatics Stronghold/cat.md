#   Catalan Numbers and RNA Secondary Structures (ID: CAT)

This problem just like any other problem with recursion took me some time but at the very end I was able to crack it. Also this problem strongly forces you to implement some sort of memoization. At first everything looks right when using Rosalind's sample dataset, but when it comes down to use the dataset to pass the problem in the platform, at least for me memoization is needed because finding the solution takes more (way more) than 5:00 minutes.

Just to be clear the function `count_structures(rna:str)` recives a string and calls `is_complement(first_base, rna[i]` function that recives two strings, ideally characters i.e. `'A'` and `'U'`, and returns a boolean if the pairing is possible in a biological transcription context.  

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