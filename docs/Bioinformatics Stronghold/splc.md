#   RNA Splicing  (ID:SPLC)

The solution of this problem was pretty straightforward. My approach was to create a "sliding window" and compare strings. If both of the substring matched then I modify the counter in the loop, but then I encountered a problem when trying to modify the counter, let's say, `i` in a classic for loop. It turns out that is not possible to change the value of the counter, save it in `i` and keep it for the next iteration.  
Let's say that we have the next loop and we want to modify the counter when it's value is equal to 7
```
for i in range(10):  
    if i == 7:
        i += i*2
    print(i)
```
The output will be:

<div align='center'>
    <table>
        <thead>
            <tr>
            <th>Iteration</th>
            <th>i</th>
            </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>0</td>
        </tr>
        <tr>
            <td>2</td>
            <td>1</td>
        </tr>
        <tr>
            <td>3</td>
            <td>2</td>
        </tr>
        <tr>
            <td>4</td>
            <td>3</td>
        </tr>
        <tr>
            <td>5</td>
            <td>4</td>
        </tr>
        <tr>
            <td>6</td>
            <td>5</td>
        </tr>
        <tr>
            <td>7</td>
            <td>6</td>
        </tr>
        <tr>
            <td>8</td>
            <td>21</td>
        </tr>
        <tr>
            <td>9</td>
            <td>8</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
        </tr>
        </tbody>
    </table>
</div>

At the seventh iteration the condition becomes `True` so the `i` value is modified, but when that iteration ends `i` value return to 8 according to the, let's say, "original plan" and end the loop properly.  

So we need to use another type of loop, fortunately a while loop get's the job done, because is the type of loop in which you have to, let's say, "manually" initialize and change the value of the counter at the end of each iteration. 

```
i = 0
while i < 25:
    if i == 7:
        i += i*2
        print(i)
    else:
        print(i)
        i += 1
```

<div align='center'>
    <table>
        <thead>
            <tr>
            <th>Iteration</th>
            <th>i</th>
            </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
        </tr>
        <tr>
            <td>3</td>
            <td>3</td>
        </tr>
        <tr>
            <td>4</td>
            <td>4</td>
        </tr>
        <tr>
            <td>5</td>
            <td>5</td>
        </tr>
        <tr>
            <td>6</td>
            <td>6</td>
        </tr>
        <tr>
            <td>7</td>
            <td>21</td>
        </tr>
        <tr>
            <td>8</td>
            <td>22</td>
        </tr>
        <tr>
            <td>9</td>
            <td>23</td>
        </tr>
        <tr>
            <td>10</td>
            <td>24</td>
        </tr>
        <tr>
            <td>11</td>
            <td>25</td>
        </tr>
        </tbody>
    </table>
</div>

I remember to look for while and for loop differences before the AI boom and I don't remember finding this difference, or at least i can't remember it.

Finally, this problem can be solved with the following one-liner, probably the most pythonic way but it is good to have a glance of what is happening under the rug or at least to be know how to solve this problem "from scratch".

`s_1 = s.replace(sub_s[0], '').replace(sub_s[1], '')`