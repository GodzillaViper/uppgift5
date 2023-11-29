def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_primes_in_number(number):
    str_number = str(number)
    count = 0
    primes=set()#ändring
    for i in range(len(str_number)):
        for j in range(i + 1, len(str_number) + 1):
            substring = int(str_number[i:j])
            if is_prime(substring):# ändring
                primes.add(substring) # ändring
    print(list(primes)) # ändring
    return len(primes) #ändring

# anger ett tal
user_input = int(input("Ange ett heltal: "))
count=count_primes_in_number(user_input)
print(count)