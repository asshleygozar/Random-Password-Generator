import random


def characters():
    letters = "AaBbCcDdEeFfGgHh1iJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    lists_letters = list(letters)
    random.shuffle(lists_letters)
    shuffled_letters = "".join(lists_letters)
    return shuffled_letters

def special_characters():
    special_letters = "`~!@#$%^&*()_+-=][:;<,>.?/"
    lists_special_letters = list(special_letters)
    random.shuffle(lists_special_letters)
    shuffled_special_letters = "".join(lists_special_letters)
    return shuffled_special_letters

def number():
    num = random.randint(0,10000)
    final_number = str(num)
    return final_number

def generate_password():

   alphabets = characters()
   special_letters = special_characters()
   numbers = number()
   final_letters_result = []

   while True:
       try:
          print("Choose your password combination")
          print("Press 1: Characters + Special Characters")
          print("Press 2: Characters + Numbers")
          print("Press 3: Numbers + Special Characters")
          print("Press 4: Characters + Special Characters + Numbers")
          print("Press 5: Exit")
        
          user_input = int(input("Enter here: "))
          password_length = int(input("Enter your password length: "))

          match user_input:
                case 1:
                    combined_letters = alphabets + special_letters
                    convert_lists = list(combined_letters)
                    random.shuffle(convert_lists)
                    for i in range(password_length):
                        final_letters_result.append(convert_lists[i])
                    shuffled_characters = ''.join(final_letters_result)
                    print(shuffled_characters)
                    break
                case 2:
                    combined_alpha_numerical = alphabets + numbers
                    convert_lists_alpha = list(combined_alpha_numerical)
                    random.shuffle(convert_lists_alpha)
                    for i in range(password_length):
                        final_letters_result.append(convert_lists_alpha[i])
                    shuffled_alpha_numerical = ''.join(final_letters_result)
                    print(shuffled_alpha_numerical)
                    break
                case 3:
                    combined_special_letters_number = special_letters + numbers
                    convert_lists_special_number = list(combined_special_letters_number)
                    random.shuffle(convert_lists_special_number)
                    for i in range(password_length):
                        final_letters_result.append(convert_lists_special_number[i])
                    shuffled_special_number = ''.join(final_letters_result)
                    print(shuffled_special_number)
                    break
                case 4:
                    combined_all_characters = special_letters + numbers + alphabets
                    convert_lists_all = list(combined_all_characters)
                    random.shuffle(convert_lists_all)
                    for i in range(password_length):
                        final_letters_result.append(convert_lists_all[i])
                    shuffled_all_characters = ''.join(final_letters_result)
                    print(shuffled_all_characters)
                    break
                case 5:
                    print("Exiting!")
                    break
                case _:
                    print("Invalid Input!")
       except ValueError:
            print("Integer Number only!")

generate_password()


