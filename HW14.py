import random

user_select = input("Введи 'Камінь', 'Ножиці' чи 'Папір': ")
print(user_select)

list_of_selection = ["Камінь", "Ножиці", "Папір"]

if user_select not in list_of_selection:
    print("Не правильне значення")
    exit()

random_select = random.choice(list_of_selection)
print(random_select)

if user_select == random_select:
    print("Нічия")
elif user_select == ("Ножиці") and random_select == ("Папір"):
    print("Ти виграв")
elif user_select == ("Камінь") and random_select == ("Ножиці"):
    print("Ти виграв")
elif user_select == ("Папір") and random_select == ("Камінь"):
    print("Ти виграв")
else:
    print("Ти програв")



