# Find the sum of all the multiples of 3 or 5 below 1000.


num_list = range(50)

def multiples(collection):
    for num in collection:
        if num % 3 == 0:
            print(f"""{num} is a multiple of 3
            """)
        elif num % 5 == 0:
            print(f"""{num} is a multiple of 5
            """)

multiples(num_list)