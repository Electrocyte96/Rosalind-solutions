#   Speeding Up Motif Finding (ID:KMP)

This problem introduced me to another way of finding motifs in a sequence, until now I was pretty familiar with the idea of a "sliding-window" algorithm, but never crossed my mind that this classic solution finds motifs in a $\textit{O(n*m)}$ complexity and that is easily improved with the Knuth-Morris-Pratt algorithm or KMP, this other algorithm solves the problem in $\textit{O(n+m)}$ time complexity. 

First we need to address some specifics of this problem, because if we look for some information of the KMP algorithm 