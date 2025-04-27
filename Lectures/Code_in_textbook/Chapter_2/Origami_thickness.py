initial_thickness = (1/200) * 10

def compute_thick(nums):
    final_thickness = initial_thickness * (2 ** nums)
    print(f"After folding {nums} times, the thickness of the paper is {final_thickness} millimeters, which is {final_thickness / 1000} meters.")


folds = int(input("Please enter the number of times you want to fold the paper: "))
compute_thick(folds)