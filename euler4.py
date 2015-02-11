largestPalindrome = 0
    for i in range(100,1000):
        for j in range(i + 1, 1000): 
            product = a*b
            if product > largestPalindrome and str(product)==(str(product)[::-1]):
                largestPalindrome = product
    return largestPalindrome