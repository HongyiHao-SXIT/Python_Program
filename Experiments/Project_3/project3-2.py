run_list = ["0 minutes", "20 minutes", "40 minutes", "60 minutes"]
swim_list = ["0 meters", "200 meters", "400 meters", "600 meters"]
calories_list = []

for i in range(len(run_list)):
    for j in range(len(swim_list)):
        calories_list.append(i * 200 + j * 100)

print("Calorie list: ", calories_list)
print(f"The maximum calories burned in the exercise plan is {max(calories_list)}, and the minimum is {min(calories_list)}.")