# Διακριτά Μαθηματικά
## Εργασία 1 - Graph realization problem

>Υλοποίηση αλγορίθμου που θα αποφασίζει εάν κάποια ακολουθία ακέραιων αριθμών είναι γραφική ή όχι και θα επιστρέφει το γράφημα σε μορφή γειτονιών των κορυφών.

### Definition (Graphic Sequence)
---
A graphic sequence is a sequence of numbers which can be the degree sequence of some graph.

### Theorem (Erdős–Gallai)
---
A sequence of non-negative integers $d_1\geqslant\ldots\geqslant d_n$ can be represented as the degree sequence of a finite simple graph on $n$ vertices **if and only if** $d_1+\ldots+d_n$ is even and:

>$\displaystyle{\sum_{i=1}^{k}d_i\leqslant k(k-1)+\sum_{i=k+1}^{n}min(d_i,k)}$, is true for every $k$ in $1\leqslant k\leqslant n$.

### Code checking if a sequence is graphic or not
---

```python
# Check if a given sequence is graphic or not
# using the Erdős–Gallai theorem.
# Source: Choudum, S. A. (1986), "A simple proof of the Erdős–Gallai theorem on graph sequences", Bulletin of the Australian Mathematical Society

def contains_neg(lst):
    for i in range(len(lst)):
        if lst[i]<0:
            return True

def Er_Ga_inequality(k,n,lst):
    left_sum=0
    for i in range(0,k+1,1):
        left_sum=left_sum+lst[i]

    right_sigma=0
    #lists are zero-indexed. Thus in the mathematical expressions k must be replaced by k+1.
    for j in range(k+1,n,1):
        minimum=min(k+1,lst[j])
        right_sigma=right_sigma+minimum

    right_sum=right_sigma+(k+1)*((k+1)-1)
    if left_sum<=right_sum:
        return True

og_seq=[]
try:
    print("Enter a sequence of natural numbers (including zero). "
          "(Press \"Enter\" after each element and once more when "
          "you have entered all the elements)")
    while True:
        og_seq.append(int(input()))
# if the input is not-integer, just print the list
except:
    print("Your sequence is:",og_seq,".")

if len(og_seq)==0:
    print("The sequence has no elements.")
    quit()
    
sum=0
for i in range(len(og_seq)):
    sum=sum+og_seq[i]
if sum%2!=0 or contains_neg(og_seq)==True:
    print("The given sequence contains negative numbers or the sum "
    "of its elements is not even and therefore it is not graphic.")
    quit()

seq=list(og_seq)
seq.sort(reverse=True)
print("Your sequence sorted in descending order is:",seq,".")

k=0
while k<len(seq):
    if(Er_Ga_inequality(k,len(seq),seq))==True:
        k=k+1
    else:
        print("The enequality of the Erdős–Gallai theorem does not hold for k=",k+1,
              ". Thus, the sequence",seq,"is not graphic.")
        quit()
print("The sequence",seq,"is graphic.")
```

### Sources
---

+ https://mathworld.wolfram.com/GraphicSequence.html
+ A SIMPLE PROOF OF THE ERDOS-GALLAI THEOREM ON GRAPH SEQUENCES - S.A. CHOUDUM, School of Mathematical Sciences, Madurai Kamaraj University
+ https://en.wikipedia.org/wiki/Havel%E2%80%93Hakimi_algorithm
