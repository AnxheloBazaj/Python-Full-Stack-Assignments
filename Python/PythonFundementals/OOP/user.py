class User:
    def __init__(self, first_name, last_name, email, age = 0, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f' first name: {self.first_name}\n last name: {self.last_name}\n email: {self.email}\n age: {self.age}\n points: {self.gold_card_points}')
    
    def enroll(self):
        if self.is_rewards_member == True:
            print( "User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"Enrolled status: {self.is_rewards_member}.\nGold card points: {self.gold_card_points}.")

    def spend(self, ammount=0):
        if ammount < self.gold_card_points:
            self.gold_card_points -= ammount
        else:
            print("Not enough points to spend!")
