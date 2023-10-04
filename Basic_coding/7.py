# not done
#Python program for n-th Fibonacci number

a = int(input('Insert a number:'))
f = [0,1]
fib = []
for i in range(0,a+1):
    fib = f[i]+f[i+1]
    f = f.append(fib)

    print(f'{f}')