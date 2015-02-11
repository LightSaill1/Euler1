largest = 1
number = 600851475143
while number % 2 == 0:
        largest = 2
        number = number/2
thirdFactor = 3
while number != 1:
        while number % thirdFactor == 0:
            largest = thirdFactor
            number = number/thirdFactor
        thirdFactor = thirdFactor + 2
 
return largest