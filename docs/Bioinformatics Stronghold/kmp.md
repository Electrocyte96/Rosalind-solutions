#   Speeding Up Motif Finding (ID:KMP)

This problem introduced me to another way of finding motifs in a sequence, until now I was pretty familiar with the idea of a "sliding-window" algorithm, but never crossed my mind that this classic solution finds motifs in a $\textit{O(n*m)}$ complexity and that is easily improved with the Knuth-Morris-Pratt algorithm or KMP, this other algorithm solves the problem in $\textit{O(n+m)}$ time complexity. 

The algoritm is pretty straightforward until we reach `ls_prefix` list and `j = ls_prefix[j-1]` part.

First I will explain the `ls_prefix` structure, the idea of this list is to save the lenght of the best matching subchain from `s` at any given `i`. For example:

<div align='center'>
    <table>
        <tbody>
            <tr>
                <td><small>index </small></td>
                <td><small>0</small></td>
                <td><small>1 </small></td>
                <td><small> 2</small></td>
                <td><small>3 </small></td>
                <td><small>4</small></td>
                <td><small>5 </small></td>
                <td><small>6 </small></td>
                <td><small>7 </small></td>
                <td><small>8 </small></td>
            </tr>
            <tr>
                <td>s</td>
                <td>A</td>
                <td>A</td>
                <td>G</td>
                <td>A</td>
                <td>A</td>
                <td>T</td>
                <td>G</td>
                <td>A</td>
                <td>A</td>
            </tr>
            <tr>
                <td>ls_prefix</td>
                <td>0</td>
                <td>1</td>
                <td>0</td>
                <td>1</td>
                <td>2</td>
                <td>0</td>
                <td>0</td>
                <td>1</td>
                <td>2</td>
            </tr>
        </tbody>
    </table>
</div>

As I described before, each character (nucleotide) of `s` corresponds a element of `ls_prefix` that tells you how many concatenaded nucleotides match with the `s` prefix. Let's say we take `i = 4` we take `s_sub = s[:i+1] -> [A A G A A]` and we look at `ls_prefix[i] = 2 ` this means that there are two nucleotides that match with the prefix of `s`. This idea repeats for each elemens of `ls_prefix`.  

Now I'll cover all iterations of the code using `s = 'ABACABAB'` and `ls_prefix = [0,0,0,0,0,0,0,0]`
<div align='center'>
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if s[i] == s[j]</th>
                <th>j+=1</th>
                <th>ls_prefix[i] = j</th>
                <th>i+=1 </th>
                <th>if j==0</th>
                <th>i+=1 </th>
                <th>j = ls_prefix[j-1]</th>
                <th>ls_prefix</th>                
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>0</td>
                <td>B == A</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>True</td>
                <td>2</td>
                <td>-</td>
                <td>[0,0,0,0,0,0,0,0]</td>
            </tr>
            <tr>
                <td>2</td>
                <td>0</td>
                <td>A == A</td>
                <td>1</td>
                <td>ls_prefix[2] = 1</td>
                <td>3</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>[0,0,1,0,0,0,0,0]</td>
            </tr>
            <tr>
                <td rowspan='2'>3</td>
                <td>1</td>
                <td>C == B</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>0 = ls_prefix[1-1]</td>
                <td>[0,0,1,0,0,0,0,0]</td>
            </tr>
            <tr>
                <td>0</td>
                <td>C == A</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>True</td>
                <td>4</td>
                <td>-</td>
                <td>[0,0,1,0,0,0,0,0]</td>
            </tr>
            <tr>
                <td>4</td>
                <td>0</td>
                <td>A == A</td>
                <td>1</td>
                <td>ls_prefix[4] = 1</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
</div>


