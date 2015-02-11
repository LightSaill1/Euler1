firstTerm = 1
secondTerm = 1
total = 0
while firstTerm <= 4000000:
    if firstTerm % 2 == 0:
        total += firstTerm
        firstTerm = secondTerm
        secondTerm = firstTerm + secondTerm
print (total)