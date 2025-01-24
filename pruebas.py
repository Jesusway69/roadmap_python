import pyjokes
import random
import os
os.system('cls')
# def dec_to_bin(dec):
#     bin = ""
#     while dec >0:
#         bin = f"{dec%2}{bin}"
#         dec//=2
#     return "0" if bin=="" else bin



# joke = pyjokes.get_joke(language='es', category='chuck')

# print(joke)


# for i in range(1,11):
#     print(dec_to_bin(i).zfill(8))



def choice_numbers()->tuple:
    numbers = []
    for i in range(5):
        number = random.randint(1,49)
        if number in numbers:
            i -=1
            continue
        numbers.append(number)
    complementary = random.randint(1,49)
    return numbers, complementary


sorted_list = sorted(choice_numbers()[0])
print("Números:", end=" ")
for number in sorted_list:
    print(number, end=" ")
print(f"\nComplemetario: {choice_numbers()[1]}")