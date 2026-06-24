#   Longest Increasing Subsequence (ID: LGIS)

Each of the functions to solve this problem, `longest_increasing(perm, n)` and `longest_decreasing(perm, n)` are composed by two parts, the first one being the obtaining of the longest sequence for each element and the second one to ``i have to wite thiss``. 

Each of the functions recieve a list of elements and n,being the lenght of the list. Through this document I'm looking to document the iterations of all the loops and have a better understanding on how the functions are working.

I will illustrate the function `longest_increasing(perm, n)` with `perm = [1,10,5,2,7,8]` and `n = 6`. Also the function creates `longs = [1] * n`, a list with ``n`` ones because 1 is the minimal lenght of a increasing or decreasing sequence

<div align='center'>
    <h4>When i = 1, j ranges from 0 to 1 excluiding 1 </h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs<th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td >i = 1</td>
                <td>j = 0</td>
                <td> 1 < 10</td>
                <td> 1 = 1 + 1 </td>
                <td>[1,2,1,1,1,1]</td>
            </tr>
        </tbody>
    </table>
</div>

<div align='center'>
    <h4>When i = 2, j ranges from 0 to 2 excluiding 2 </h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs<th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td >i = 2</td>
                <td>j = </td>
                <td> </td>
                <td>  </td>
                <td></td>
            </tr>
        </tbody>
    </table>
</div>

<div align='center'>
    <h4>When i = , j ranges from 0 to  excluiding </h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs<th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td >i = </td>
                <td>j = </td>
                <td> </td>
                <td>  </td>
                <td></td>
            </tr>
        </tbody>
    </table>
</div>


<div align='center'>
    <table>
        <thead>
            <tr>
                <th>Titles</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Rows</td>
            </tr>
        </tbody>
    </table>
</div>