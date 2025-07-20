akshay_list = [1,1,2,3,4,5,6,7,5,8,9]
removed_duplicates_values = []

for i in akshay_list:
    if i not in removed_duplicates_values:
        removed_duplicates_values.append(i)

print("The removed duplicate list: ",removed_duplicates_values)
