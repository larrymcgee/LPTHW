from sys import argv

increment, limit = argv
numbers = []

def number_loop(increment, limit):
    i = 0
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

number_loop(increment, limit)

print "The numbers: "

for num in numbers:
    print num
