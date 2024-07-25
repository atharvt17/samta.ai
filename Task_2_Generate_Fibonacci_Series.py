def fibo(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

n = int(input("Enter the number of terms :- "))
if n <= 0:
    print("Please enter a positive number.")
else:
    fibonacci = fibo(n)
    print("Output:- ",fibonacci)