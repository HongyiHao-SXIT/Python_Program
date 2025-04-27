set01 = set("qianfeng") 
set02 = set(("Xiaowan", "Xiaofeng")) 
set03 = set(["Xiaowan", "Xiaofeng"]) 
set04 = set({"Xiaowan": 19, "Xiaofeng": 18}) 
print("set01:", set01) 
print("set02:", set02) 
print("set03:", set03) 
print("set04:", set04) 

language_set = {"Chinese", "English", "French"} 
language_set.add("Russian") 
print(language_set) 
language_set.discard("English") 
print(language_set) 
language_set.remove("French") 
print(language_set) 

lst = [1, 3, 5, 3, 4, 4, 2, 9, 6, 7] 
set_lst = set(lst)  
if len(set_lst) == len(lst): 
    print('The elements in the list are all unique!')
else:
    print('There are duplicate elements in the list!')