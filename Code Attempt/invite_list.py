friends = ['Lanyi_adict', 'Joyang_Mecon', 'xKwin', 'XBear', 'Foxi']
take_part_01 = friends[0] + " can take part in the dinner."
print(take_part_01)

not_take_part = friends[2] + " could not take part in the dinner."
print(not_take_part)

del(friends[2])

friends.insert(2,"YiQing")

print(friends)

friends.append("Xuanyun")
print("I am sorry about that.")

del_name = friends.pop() + " I am sorry about that."
print(del_name)

del(friends)
