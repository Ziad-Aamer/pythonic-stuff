
def nth_prime_number(n):
    if n==1:
        return 2
    count = 1
    num = 1
    while(count < n):
        num +=2 #optimization
        if is_prime(num):
            count +=1
    return num

def is_prime(num):
    factor = 2
    while (factor * factor <= num):
        if num % factor == 0:
             return False
        factor +=1
    return True

def char_to_prime_hash(name: str):
    HASH_SIZE = 10
    sum = 0
    for char in name:
        char = char.lower()
        sum += nth_prime_number(ord(char) - ord('a') + 1)
    print('Sum', sum)
    sum %= HASH_SIZE

    return sum

def test_hash_function():
    """Test, whether a hash function has a good distribution (getting unique index per each different input)"""

    list1 = ["Esther", "Bob", "Ben", "Dan"]
    list2 = ["A", "AA", "AAA", "AAAA"]
    list3 = ["Maus", "Fun Home", "Watchmen"]

    list = list3
    for s in list:
        print(char_to_prime_hash(s))

def test_nth_prime_number():

    for i in range(1, 11):
        print(nth_prime_number(i))
