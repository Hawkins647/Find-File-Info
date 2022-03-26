import os

path = "YourPathHere"

main_dict = {}
file_list = []


for val in os.listdir(path):
    if os.path.isdir(path + "/" + val):
        main_dict[val] = os.listdir(path + "/" + val)
    else:
        file_list.append(val)

print("Directories found in the path are: " + str(main_dict))
print("Files found in the path are: " + str(file_list))
