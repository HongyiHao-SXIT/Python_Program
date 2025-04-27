class Staff:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def get_name(self):
        return self.name

    def get_wage(self):
        return self.wage

    def set_wage(self, new_wage):
        self.wage = new_wage


class Agroup(Staff):
    def __init__(self, name, wage, special_skill):
        super().__init__(name, wage)
        self.special_skill = special_skill

    def get_name(self):
        return super().get_name()

    def get_wage(self):
        return 1.5 * super().get_wage()

    def set_wage(self, new_wage):
        super().set_wage(new_wage)

    def show_special_skill(self):
        return self.special_skill


class Bgroup(Staff):
    def __init__(self, name, wage, project_experience):
        super().__init__(name, wage)
        self.project_experience = project_experience

    def get_name(self):
        return super().get_name()

    def get_wage(self):
        return 1.2 * super().get_wage()

    def set_wage(self, new_wage):
        super().set_wage(new_wage)

    def show_project_experience(self):
        return self.project_experience


class Cgroup(Staff):
    def __init__(self, name, wage, seniority):
        super().__init__(name, wage)
        self.seniority = seniority

    def get_name(self):
        return super().get_name()

    def get_wage(self):
        return 1.0 * super().get_wage()

    def set_wage(self, new_wage):
        super().set_wage(new_wage)

    def show_seniority(self):
        return self.seniority


if __name__ == "__main__":
    
    staff_member = Staff("John", 5000)
    print(f"Name: {staff_member.get_name()}")
    print(f"Wage: {staff_member.get_wage()}")


    staff_member.set_wage(6000)
    print(f"Modified Wage: {staff_member.get_wage()}")


    a_staff = Agroup("Alice", 5000, "Data Analysis")
    print(f"\nA Group Staff - Name: {a_staff.get_name()}")
    print(f"A Group Staff - Wage: {a_staff.get_wage()}")
    print(f"A Group Staff - Special Skill: {a_staff.show_special_skill()}")


    b_staff = Bgroup("Bob", 5000, "5 years of project experience")
    print(f"\nB Group Staff - Name: {b_staff.get_name()}")
    print(f"B Group Staff - Wage: {b_staff.get_wage()}")
    print(f"B Group Staff - Project Experience: {b_staff.show_project_experience()}")


    c_staff = Cgroup("Charlie", 5000, "3 years")
    print(f"\nC Group Staff - Name: {c_staff.get_name()}")
    print(f"C Group Staff - Wage: {c_staff.get_wage()}")
    print(f"C Group Staff - Seniority: {c_staff.show_seniority()}")
    