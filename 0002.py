import math

prime_list = [2]

for i in range(3, 32_000,2):
    is_prime = True
    search_end = int(math.sqrt(i)) + 1
    for j in prime_list:
        if (j >= search_end):
            break
        elif (i%j == 0):
            is_prime = False
            break
    if (is_prime):
        prime_list.append(i)

total_line = int(input())
output = ""
for t in range (total_line):
    if (t>0):
        output += "\n"
    start_n, end_n = input().split(' ')
    start_n = int(start_n)
    end_n = int(end_n)
    search_end = int(math.sqrt(end_n)) + 1
    
    if (start_n < 2):
        start_n = 2

    is_prime = [True] * 100_001
    for i in prime_list:
        if (i >= search_end):
            break

        if (i >= start_n):
            start_p = i*2
        
        else:
            start_p = start_n + ((i - start_n % i) %i)

        false_mask = [False] * len (is_prime[start_p - start_n : end_n +1 - start_n : i])
        is_prime[start_p - start_n: end_n + 1 - start_n :i] = false_mask

    for i in range (start_n, end_n + 1):
        if (is_prime[i - start_n] == True):
            output += str(i) + "\n"

print (output[:-1])

