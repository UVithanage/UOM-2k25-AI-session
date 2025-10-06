# Problem 1
print(sum(i for i in range(1000) if i%3==0 or i%5==0))



# Problem 2
a,b=1,2
s=0
while a<=4000000:
    if a%2==0:
        s+=a
    a,b=b,a+b
print(s)




# Problem 3
n=600851475143
i=2
last=1
while i*i<=n:
    if n%i==0:
        last=i
        n//=i
    else:
        if i==2:
            i=3
        else:
            i+=2
if n>1:
    last=n
print(last)



# Problem 4
maxp=0
for i in range(100,1000):
    for j in range(i,1000):
        p=i*j
        s=str(p)
        if s==s[::-1] and p>maxp:
            maxp=p
print(maxp)







# Problem 5
import math
from functools import reduce
print(reduce(lambda a,b:a*b//math.gcd(a,b), range(1,21), 1))





# Problem 6
n=100
print(sum(range(1,n+1))**2 - sum(i*i for i in range(1,n+1)))






# Problem 7
def nth_prime(n):
    count=0
    i=2
    while True:
        isprime=True
        r=int(i**0.5)
        for p in range(2,r+1):
            if i%p==0:
                isprime=False
                break
        if isprime:
            count+=1
            if count==n:
                return i
        i+=1
print(nth_prime(10001))




# Problem 8
num="""73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n","")
k=13
best=0
for i in range(len(num)-k+1):
    block=num[i:i+k]
    if '0' in block:
        continue
    prod=1
    for ch in block:
        prod*=int(ch)
    if prod>best:
        best=prod
print(best)







# Problem 9
for a in range(1,1000):
    for b in range(a+1,1000):
        c=1000-a-b
        if a*a+b*b==c*c:
            print(a*b*c)
            raise SystemExit








# Problem 10
limit=2000000
sieve=[True]*limit
sieve[0]=sieve[1]=False
for i in range(2,int(limit**0.5)+1):
    if sieve[i]:
        for j in range(i*i,limit,i):
            sieve[j]=False
print(sum(i for i,prime in enumerate(sieve) if prime)



























