# Mathematical Constant (Euler's Number)
e = 2.7182818284590451

def variance(lon):
    assert(len(lon)>0)
    x = (sum(lon))/(len(lon))
    y = len(lon)
    answer = 0
    while len(lon) > 0:
        answer = answer + (x - lon[0])**2
        lon = lon[1:]
    return float(answer)/y

def stdev(lon):
    return (variance(lon))**(0.5)

def factorial(n):
    assert(n>=0)
    product = 1
    while (n!=0):
        product = product*n
        n = n - 1
    return product

def factors(n,k):
    assert(n>=k)
    assert(k>=0)
    assert(n>=1)
    answer = 1
    while (k!=0):
        answer = answer*n
        k = k - 1
        n = n - 1
    return answer

def choose(n,k):
    if (k == 0):
        return 1
    elif (k == 1):
        return n
    elif (k > n):
        return 0
    elif (k > n/2):
        return factors(n,n-k)/factorial(n-k)
    else:
        return factors(n,k)/factorial(k)

def binomial(n,p,x):
    return choose(n,x)*(p**x)*(1-p)**(n-x)

def nbinomial(k,p,x):
    return choose(x+k-1,x)*(p**k)*(1-p)**x

def geometric(p,x):
    return p*(1-p)**x

##u=np
def poisson(u,x):
    return (e**(-u)*(u**x))/factorial(x)

def hypergeometric(x,r,N,n):
    return float(choose(r,x)*choose(N-r,n-x))/choose(N,n)
    



        