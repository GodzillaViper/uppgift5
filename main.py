def is_prime(number):# Funktion för att kontrollera om ett tal är ett primtal
    # Om talet är mindre än 2 är det inte ett primtal
    if number < 2:
        return False
    # Kontrollerar för faktorer från 2 till kvadratroten av talet
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    # Om inga faktorer hittas, är talet ett primtal
    return True

# Funktion för att räkna antalet primtalsdelsträngar i ett givet tal
def count_primes_in_number(number):
    # Konverterar talet till en sträng
    str_number = str(number)
    # En uppsättning för att lagra primtalsdelsträngar
    primes = set()
    # Iterera genom alla möjliga delsträngar
    for i in range(len(str_number)):
        for j in range(i + 1, len(str_number) + 1):
            # Extraherar delsträngen och konvertera den till ett heltal
            substring = int(str_number[i:j])
            # Kontrollerar om delsträngen är ett primtal och lägger till den i uppsättningen
            if is_prime(substring):
                primes.add(substring)
    # Skriver ut listan med primtalsdelsträngar
    print(list(primes))
    # Returnerar antalet unika primtalsdelsträngar
    return len(primes)

# Hämtar användarinput för ett tal
user_input = int(input("Ange ett heltal: "))
# Anropar funktionen för att räkna primtalsdelsträngar och spara resultatet
count = count_primes_in_number(user_input)
# Skriver ut antalet primtalsdelsträngar
print(count)
