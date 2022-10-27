from Card import Card

class AceCard(Card):
    def __init__(self, suit): 
        ace_values = (1, 11)
        super().__init__(self, ace_values, suit)


# IMPORTANT THINGS TO REMEMBER ABOUT INHERITANCE
# 1. NEEDS TO IMPORT THE PARENT CLASS
# 2. IT NEEDS TO PASS IN THE PARENT CLASS IN THE CLASS DEFINITION
# 3. USE THE SUPER() INITIALIZER