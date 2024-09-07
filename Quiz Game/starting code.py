class User:

    def __init__(self, user_id, name, job_title):   # PART 1 setting Attributes
        self.user_id = user_id  # self.attribute = Parameter
        self.name = name
        self.job_title = job_title
        self.followers = 0  # Setting default value
        self.following = 0  # Setting default value

    def follow(self, user):
        user.followers += 1
        self.following += 1


employee_1 = User("8762835", "shay", "Developer")   # Creating Objects
employee_2 = User("3892787234", "Jack", "Senior Backend Developer") # Creating Objects

print(f"You're {employee_1.name}, Okay, so your User ID is {employee_1.user_id} and "
      f"your current job title is {employee_1.job_title}. Additionally, you'll work with {employee_2.name}")
