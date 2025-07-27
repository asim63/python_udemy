class User:
    def __init__(self,username,user_id):  #constructor
        print("new user being created....")
        self.name = username
        self.id = user_id
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following +=1
# user_1 = User()

# user_1.id = "001"
# user_1.username = "asim"

# print(user_1.id)

user_3 = User('Asim',78)
print(user_3.name)
print(user_3.id)

user_1 = User('Bigay',56)

user_1.follow(user_3)

print(user_1.followers)
print(user_1.following)
print(user_3.followers)
print(user_3.following)

