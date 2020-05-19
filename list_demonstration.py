#codehs link: https://codehs.com/share/list_demo_8DGt3T

while True:
    user_list = input("Give me four words, each seperated by a space (e.g. \"Here are four words\"): ")
    if len(user_list.split()) == 4: break
    else: print("Please give me four words >:(")
user_list = user_list.split()
print(user_list)
user_list.reverse()
print(user_list)