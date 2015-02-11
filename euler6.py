n = 100
total = ((n+1)*n)/2
squared_total = total**2

 
sum_of_squares = 0
for i in range(n + 1):
    sum_of_squares += i**2

print (squared_total - sum_of_squares)