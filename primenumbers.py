def sieve_of_erastothenes():

    print("Erastothenes")

    #initially all marked true (prime)

    a = [True for i in range(7920)]    #7919 is the 1000th prime number
    j = 2

    while j*j <= 7920:

        if a[j] == True:
            k = j**2

            for k in range(j**2, 7920, j):
                a[k] = False

        j += 1

    for l in range(2, 7920):

        if a[l] == True:
            print(l)


def sieve_of_atkin():

    print("Atkin")

    #more optimised
    #all initially marked false (not prime)
    """sieve of atkin uses mod 60 but all those divisible by 5
       are marked not prime, so mod 12 is being used here"""

    a = [False for i in range(7920)]

    print(2)
    print(3)

    #2 and 3 are prime

    x = 1

    while x * x < 7920:
        y = 1
        while y * y < 7920:

            p = 4 * x * x + y * y

            if (p % 12 == 1 or p % 12 == 5) and p < 7920:
                a[p] = True

            p = 3 * x * x + y * y

            if p % 12 == 7 and p < 7920:
                a[p] = True

            p = 3 * x * x - y * y

            if p % 12 == 11 and x > y and p < 7920:
                a[p] = True

            y += 1

        x += 1

    z = 5

     #marking multiples of squares of primes as non prime

    while z * z < 7920:
         if a[z] == True:
             for q in range(z * z, 7920, z * z):
                 a[q] = False

         z += 1

    for i in range(5, 7920):
        if a[i] == True:
            print(i)


sieve_of_atkin()
sieve_of_erastothenes()         
    
    

    

