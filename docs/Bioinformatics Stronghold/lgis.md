#   Longest Increasing Subsequence (ID: LGIS)

Each of the functions to solve this problem, `longest_increasing(perm, n)` and `longest_decreasing(perm, n)` are composed by two parts, the first one being the obtaining of the longest sequence for each element and the second one to ``i have to wite thiss``. 

Each of the functions recieve a list of elements and n,being the lenght of the list. Through this document I'm looking to document the iterations of all the loops and have a better understanding on how the functions are working.

I will illustrate the function `longest_increasing(perm, n)` with `perm = [1,10,5,2,7,8]` and `n = 6`. Also the function creates `longs = [1] * n`, a list with ``n`` ones because 1 is the minimal lenght of a increasing or decreasing sequence. Also we need to take a look of `padres = [-1,-1,-1,-1,-1,-1]`, the purpouse of padres is to store the index of all the numbers that 

<div align='center'>
    <h4>When i = 1, j ranges from 0 to 1 excluiding 1 </h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th> if longs[j] + 1 > long[i]</th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs</th>
                <th>padres[i] = j </th>
                <th>padres</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td >i = 1</td>
                <td>j = 0</td>
                <td> 1 < 10</td>
                <td> 1+1 > 1</td>
                <td> longs[1] = 1+1 </td>
                <td>[1,2,1,1,1,1]</td>
                <td>padres[1] = 0</td>
                <td>[-1,0,-1,-1,-1,-1]</td>
            </tr>
        </tbody>
    </table>
    <p>perm = [1,10,5,2,7,8] longs = [1,2,1,1,1,1] padres = [-1,0,-1,-1,-1,-1]</p>
    <hr></hr>
</div>

<div align='center'>
    <h4>When i = 2, j ranges from 0 to 2 excluiding 2 </h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th> if longs[j] + 1 > long[i]</th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs</th>
                <th>padres[i] = j </th>
                <th>padres</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="2">i = 2</td>
                <td>j = 0</td>
                <td> 1 < 5 </td>
                <td>1+1 > 1</td>
                <td>longs[2] = 1+1 </td>
                <td>[1,2,2,1,1,1]</td>
                <td>padres[2] = 0</td>
                <td>[-1,0,0,-1,-1,-1]</td>
            </tr>
            <tr>
                <td>j = 1</td>
                <td>10 < 5 </td>
                <td> - </td>
                <td>- </td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
            </tr>
        </tbody>
    </table>
    <p>perm = [1,10,5,2,7,8] longs = [1,2,2,1,1,1] padres = [-1,0,0,-1,-1,-1]</p>
    <hr></hr>
</div>

<div align='center'>
    <h4>When i = 3, j ranges from 0 to 3 excluiding 3</h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th> if longs[j] + 1 > long[i]</th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs</th>
                <th>padres[i] = j </th>
                <th>padres</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="3">i = 3</td>
                <td>j = 0</td>
                <td>1 < 2 </td>
                <td>1+1 > 1 </td>
                <td>longs[3] = 1+1</td>
                <td>[1,2,2,2,1,1]</td>
                <td>padres[3] = 0</td>
                <td>[-1,0,0,0,-1,-1]</td>
            </tr>
            <tr>
                <td>j = 1</td>
                <td> 10 < 2</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>j = 2</td>
                <td>5 < 2</td>
                <td> - </td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
            </tr>
        </tbody>
    </table>
    <p>perm = [1,10,5,2,7,8] longs = [1,2,2,2,1,1] padres = [-1,0,0,0,-1,-1]</p>
    <hr></hr>
</div>

<div align='center'>
    <h4>When i = 4, j ranges from 0 to 4 excluiding 4</h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th> if longs[j] + 1 > long[i]</th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs</th>
                <th>padres[i] = j </th>
                <th>padres</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan='4'>i = 4</td>
                <td>j = 0</td>
                <td>1 < 7 </td>
                <td> 1+1 > 1 </td>
                <td>longs[4] = 1+1</td>
                <td>[1,2,2,2,2,1]</td>
                <td>padres[4] = 0</td>
                <td>[-1,0,0,0,0,-1]</td>
            </tr>
            <tr>
                <td>j = 1</td>
                <td> 10 < 7 </td>
                <td>-  </td>
                <td>- </td>
                <td>-</td>
                <td>- </td>
                <td>-</td>
            </tr>
            <tr>
                <td>j = 2</td>
                <td> 5 < 7</td>
                <td> 2+1 < 2 </td>
                <td>longs[4] = 2+1</td>
                <td>[1,2,2,2,2,3,1]</td>
                <td>padres[4] = 2</td>
                <td>[-1,0,0,0,2,-1]</td>
            </tr>
            <tr>
                <td>j = 3</td>
                <td>2 < 7 </td>
                <td> 2+1 > 3 </td>
                <td>- </td>
                <td>-</td>
                <td>- </td>
                <td>-</td>
            </tr>
        </tbody>
    </table>
    <p>perm = [1,10,5,2,7,8] longs = [1,2,2,2,2,3,1] padres = [-1,0,0,0,2,-1] </p> 
</div>

I think here is worth mentioning the why on the second conditional `if longs[j] + 1 > longs[i]` because is here when the third iteration ends. It turns out that this control structure allow us to avoid entering the value assignation part. If we didn't have this code line we would assign `longs[4] = longs[2]+1` or `longs[4] = 2+1` but at this point `longs[4]` is already equal to 3. Without this check, the algorithm would overwrite a better solution with a worse one. Therefore, this conditional ensures that we only update our records when we find a strictly longer subsequence, preserving the optimal path found so far. 
<hr></hr>

<div align='center'>
    <h4>When i = 5, j ranges from 0 to 5 excluiding 5</h4> 
    <table>
        <thead>
            <tr>
                <th>i</th>
                <th>j</th>
                <th>if perm[j] < perm[i]: </th>
                <th> if longs[j] + 1 > long[i]</th>
                <th>longs[i] = longs[j]+1</th>
                <th>longs</th>
                <th>padres[i] = j </th>
                <th>padres</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan='5'>i = 5</td>
                <td>j = 0</td>
                <td>1 < 8 </td>
                <td> 1+1 > 1 </td>
                <td>longs[5] = 1+1</td>
                <td>[1,2,2,2,3,2]</td>
                <td>padres[5] = 0</td>
                <td>[-1,0,0,0,2,0]</td>
            </tr>
            <tr>
                <td>j = 1</td>
                <td>10 < 8 </td>
                <td>  </td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>j = 2</td>
                <td> 5 < 8</td>
                <td> 2+1 > 3</td>
                <td>longs[5] = 2+1</td>
                <td>[1,2,2,2,3,3]</td>
                <td>padres[5] = 2</td>
                <td>[-1,0,0,0,2,2]</td>
            </tr>
            <tr>
                <td>j = 3</td>
                <td>2 < 8</td>
                <td>2+1 > 3</td>
                <td>- </td>
                <td>-</td>
                <td>- </td>
                <td>-</td>
            </tr>
            <tr>
                <td>j = 4</td>
                <td>7 < 8 </td>
                <td> 3+1 > 3 </td>
                <td>longs[5] = 3+1</td>
                <td>[1,2,2,2,3,4]</td>
                <td>padres[5] = 4</td>
                <td>[-1,0,0,0,2,4]</td>
            </tr>
        </tbody>
    </table>
    <p>perm = [1,10,5,2,7,8] longs = [1,2,2,2,3,4] padres = [-1,0,0,0,2,4]</p>
    <hr></hr>
</div>

