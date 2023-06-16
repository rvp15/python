x = int(input('How many candies?'))

ava = 4
i = 1
while i <= x:
    print('candy', i)
    i += 1
    if i > ava:
        print('out of stock')
        break
print('enjoy your treat')


