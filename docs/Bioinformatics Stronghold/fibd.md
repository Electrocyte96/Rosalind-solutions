#   Mortal Fibonacci Rabbits (ID: FIBD)

The main idea of this algorithm is to create a list with $m-lenght$ in which each position of the list will be representing a stage of the life cycle of the rabbits.  

First we start with a setting up our list: <div style="text-align: center">edad = [1] [0]*(m-1) </div>  
Each index will represent the life stages of the rabbits. Starting with 1 at index edad[0] because the problem begins with 1 baby pair of rabbits. 

<div align="center">
    <table>
        <thead>
        <tr>
            <th>index</th>
            <th>age</th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <td>edad[0]</td>
                <td>Newborns</td>
            </tr>
            <tr>
                <td>edad[1]</td>
                <td>Adults (1 month)</td>
            </tr>
            <tr>
                <td>edad[2]</td>
                <td>Adults (2 months)</td>
            </tr>
            <tr>
                <td style="text-align: center" >...</td>
                <td style="text-align: center" ></td>
            </tr>
            <tr>
                <td>edad[m-1]</td>
                <td>Adults in their last month of life</td>
            </tr>
        </tbody>
    </table>
</div>

Each month new rabbits are born  <div style="text-align: center"> nuevos = sum(edad[1:]) </div>  
All adult rabbits starting at index edad[1:] mate  

Then some rabbits age and die <div style="text-align: center"> edad = [nuevos] + edad[:-1] </div>  
So let's see what's happening behind. This line: deletes the older rabbits, age every other rabbits and adds newborn rabbits. Let's look at an example.  
<div style="text-align: center"> edad = [a0, a1, a2, a3] </div> 

Where `m = 4`. <div style="text-align: center"> [a0, a1, a2] </div> 

This is equivalent to `edad[:-1]`, so we remove `edad[3]`.  <div style="text-align: center"> [nuevos] + [a0, a1, a2] = [nuevos, a0, a1, a2] </div> 

This last operations works like a concatenation, adding two lists results in a list with a combined length of the lists that were added, and the order of the addition determines the indices of each element

<div style="text-align: center"> nuevos = sum(edad[1:]) </div>  

It is also worth mentioning that we are not saving the total sum of rabbits, we are saving a distribution by age.  
Quick review from the rosalind example exercise 

<div align="center">
    <table>
        <thead>
        <tr>
            <th> n </th>
            <th> edad </th>
        <tr>
        </thead>
        <tbody>
            <tr>
                <td> 1 </td>
                <td> edad = [1, 0, 0] </td>
            </tr>
            <tr>
                <td> 2 </td>
                <td> edad = [0, 1, 0] </td>
            </tr>
            <tr>
                <td> 3 </td>
                <td> edad = [1, 0, 1] </td>
            </tr>
            <tr>
                <td> 4 </td>
                <td> edad = [1, 1, 0] </td>
            </tr>
            <tr>
                <td> 5 </td>
                <td> edad = [1, 1, 1] </td>
            </tr>
            <tr>
                <td colspan=2> nuevos = sum(edad[1:]) = 3 </td>
            </tr>
        </tbody>
    </table>
</div>