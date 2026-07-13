#   Speeding Up Motif Finding (ID:KMP)

This problem introduced me to another way of finding motifs in a sequence, until now I was pretty familiar with the idea of a "sliding-window" algorithm, but never crossed my mind that this classic solution finds motifs in a $\textit{O(n*m)}$ complexity and that is easily improved with the Knuth-Morris-Pratt algorithm or KMP, this other algorithm solves the problem in $\textit{O(n+m)}$ time complexity. 

The algoritm is pretty straightforward until the functioning of the `ls_prefix` list and `j = ls_prefix[j-1]` part. The first one tells exactly you how many nucleotides at the end of `s` are a identical copy of the nucleotides from the begining of `s` 


cuántos nucleótidos al final de tu subcadena actual (s[:i+1]) son una copia idéntica de los nucleótidos al principio de toda tu secuencia s.

C A G C A T G G T A T C A C A G C A G A G  
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0