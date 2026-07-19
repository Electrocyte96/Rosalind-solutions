#   Speeding Up Motif Finding (ID:KMP)

This problem introduced me to another way of finding motifs in a sequence, until now I was pretty familiar with the idea of a "sliding-window" algorithm, but never crossed my mind that this classic solution finds motifs in a $\textit{O(n*m)}$ complexity and that is easily improved with the Knuth-Morris-Pratt algorithm or KMP, this other algorithm solves the problem in $\textit{O(n+m)}$ time complexity. 

The algorithm is pretty straightforward until we reach `ls_prefix` list and `j = ls_prefix[j-1]` part.

First I will explain the `ls_prefix` structure, the idea of this list is to save the length of the best matching subchain from `s` at any given `i`. For example:

<div align='center'>
    <table>
        <tbody>
            <tr>
                <td><small>index </small></td>
                <td><small>0</small></td>
                <td><small>1</small></td>
                <td><small>2</small></td>
                <td><small>3</small></td>
                <td><small>4</small></td>
                <td><small>5</small></td>
                <td><small>6</small></td>
                <td><small>7</small></td>
                <td><small>8</small></td>
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

As I described before, each character (nucleotide) of `s` corresponds a element of `ls_prefix` that tells you how many concatenaded nucleotides match with the `s` prefix. Let's say we take `i = 4` we take `s_sub = s[:i+1] -> [A A G A A]` and we look at `ls_prefix[i] = 2 ` this means that there are two nucleotides that match with the prefix of `s` and also is worth noting that this two in this nucleotides are at the end of the subchain. This idea repeats for each element of `ls_prefix`, then intrinsically this algorithm searches coincidences in prefixes and suffixes.

Now I'll cover all iterations of the code using `s = 'ABACABAB'`, `ls_prefix = [0,0,0,0,0,0,0,0]` and ``n = len(s) = 8``
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
                <td>5</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>[0,0,1,0,1,0,0,0]</td>
            </tr>
            <tr>
                <td>5</td>
                <td>1</td>
                <td>B == B</td>
                <td>2</td>
                <td>ls_prefix[5] = 2</td>
                <td>6</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>[0,0,1,0,1,2,0,0]</td>
            </tr>
            <tr>
                <td>6</td>
                <td>2</td>
                <td>A == A</td>
                <td>3</td>
                <td>ls_prefix[6] = 3</td>
                <td>7</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>[0,0,1,0,1,2,3,0]</td>
            </tr>
            <tr>
                <td rowspan='2'>7</td>
                <td>3</td>
                <td>B == C</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>1 = ls_prefix[3-1]</td>
                <td>[0,0,1,0,1,2,3,0]</td>
            </tr>
            <tr>
                <td>1</td>
                <td>B == B</td>
                <td>2</td>
                <td>ls_prefix[7] = 2</td>
                <td>8</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>[0,0,1,0,1,2,3,2]</td>
            </tr>
            <tr>
                <td colspan='11', align='center'> i < n => 8 < 8. False, so loop breaks</td>
            </tr>
        </tbody>
    </table>
</div>

As showed before, when two nucleotides are equal `s[i] == s[j]` then `j` increases one to compare the element next after the iteration, (note that this has to be before than) and you save the value of  `ls_prefix[i] = j` and finally `i` increases one to compare the element next. But if `s[i] != s[j]` then first you check if `j == 0`, if is then `i+=1` you move to the next element. but if `j != 0` then you assign the previous value of ``j`` in `ls_prefix` to `j`. This line is confusing and at the same time is brilliant because of a simple fact, and is this is: "The end of one streak can be the beginning of a new one". Lets try to see it more clearly with the next example

<div align='center'>
    <table>
        <tbody>
            <tr>
                <td><small>index </small></td>
                <td><small>0</small></td>
                <td><small>1</small></td>
                <td><small>2</small></td>
                <td><small>3</small></td>
                <td><small>4</small></td>
                <td><small>5</small></td>
                <td><small>6</small></td>
                <td><small>7</small></td>
                <td><small>8</small></td>
            </tr>
            <tr>
                <td>s</td>
                <td>A</td>
                <td>A</td>
                <td>G</td>
                <td>A</td>
                <td>A</td>
                <td>A</td>
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
                <td>2</td>
                <td>3</td>
                <td>4</td>
                <td>5</td>
            </tr>
        </tbody>
    </table>
</div>

Lets take a look of what is happening in each iteration when comparing indexes `i` and `j` in the `s` above.

<div align='center'>
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>match(?)</th>
            <tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>0</td>
                <td align='center'>✓</td>
            </tr>
            <tr>
                <td>2</td>
                <td>1</td>
                <td align='center'>✗</td>
            </tr>
            <tr>
                <td>2</td>
                <td>0</td>
                <td align='center'>✗</td>
            </tr>
            <tr>
                <td>3</td>
                <td>0</td>
                <td align='center'>✓</td>
            </tr>
            <tr>
                <td>4</td>
                <td>1</td>
                <td align='center'>✓</td>
            </tr>
            <tr>
                <td>5</td>
                <td>2</td>
                <td align='center'>✗</td>
            </tr>
            <tr>
                <td>5</td>
                <td>1</td>
                <td align='center'>✓</td>
            </tr>
            <tr>
                <td>6</td>
                <td>2</td>
                <td align='center'>✓</td>
            </tr>
            <tr>
                <td>7</td>
                <td>3</td>
                <td align='center'>✓</td>
            </tr>
            <tr>
                <td>8</td>
                <td>4</td>
                <td align='center'>✓</td>
            </tr>
        </tbody>
    </table>
</div>

As we can see when `i = 3` and `j = 0` we start a streak first with: $$A_3 == A_0✓$$  
then `i = 4` and `j = 1` $$A_4 == A_1 ✓ $$
but when `i = 5` and `j = 2` $$A_5 == G_2✗$$ we encounter a problem with becuse both nucleotides are different and since `j != 0` we enter to the `j = ls_prefix[j-1]` line. Is here when the sentence: "The end of one streak can be the beginning of a new one" makes sense. And this is when doing `j = ls_prefix[j-1]` we are checking in the next iteration if the previous value `s[j-1]` matches `s[i]` creating some sort of "mirror". And actually in the given `s` there is one. Also if there is no previous value of `s[j]` that matches `s[i]`, then ``j`` can go to 0 and after that, well you know...  

We continue with `i = 5` and `j = 1` $$A_5 == A_1 ✓$$
After this point we continue normally until `i<n == False`. 