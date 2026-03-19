# Rabbits and Recurrence Relations (ID: FIB)

The algorithm used for this case was `F(n) = F(n-1) + k * F(n-2)` and it was implemented using an iterative approach `a, b = b, b + k * a` and using an auxiliar variable `aux` to handle values to `b` in each step and where `a = F(n-2)` and `b = F(n-1)`

<div>
    <table>
        <thead>
            <tr>
                <th>Month</th>
                <th>1</th>
                <th>2</th>
                <th>3</th>
                <th>4</th>
                <th>5</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan='3'> a = 1,<br> b = 1, <br> n = 5, <br> k = 3, <br>aux = Null</td>
                <td rowspan = '2'> 1 brp </td>
                <td rowspan = '2'>1 arp</td>
                <td>1 arp y 3 brp</td>
                <td>4 arp y 3 brp</td>
                <td>7 arp y 12 brp</td>
            </tr>
            <tr>
                <td>a = 1,<br> b = 4, <br> aux = 1+k*1</td>
                <td>a = 4,<br> b = 7, <br> aux = 4+k*1</td>
                <td>a = 7,<br> b = 19, <br> aux = 7+k*4</td>
            </tr>
        </tbody>
    </table>
    <small>Note* All numbers are rabbit pairs, more specifically:  arp = Adult rabbit pair, brp = Baby rabbit pair</small>
</div><br>

## Explanation
- The first month start with 1 pair of baby rabbits, since they are babies they can't reproduce
- The second month the pair of rabbits reaches the adulthood so they are ready to create offspring
- In the third month the pair of adult rabbits create 3 pairs of baby rabbits `k = 3`
- By the fourth month there are 4 adult rabbit pairs but just one of them was able to procreate another 3 pairs of baby rabbits since the other 3 pairs have reached the adulthood in that exact month
- In the fifth month there are 7 adult rabbit pairs from which 4 pairs are breeding pairs and those create 12 baby rabbit pairs.   

So for the rabbit pairs at a determined `n  = 5` and `k = 3` the total rabbit pairs is 19 
