class User:
    def __init__(self,username,user_id):  #constructor
        print("new user being created....")
        self.name = username
        self.id = user_id
    
    
# user_1 = User()

# user_1.id = "001"
# user_1.username = "asim"

# print(int(user_1.id))

# user_2 = User()
# user_2.name = "jpt"

# print(user_2.name)

user_3 = User('Asim',78)
print(user_3.name)
print(user_3.id)