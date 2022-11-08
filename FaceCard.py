from Card import Card # capitalization does matter here!

class FaceCard(Card):
    def __init__(self, face, suit):
        self.face = face

        default_face_value = 10
        # THIS IS THE SAME AS: 
        super().__init__(default_face_value, suit)

        #  DOING THIS FROM CARD.PY
        # self.value = 10
        # self.suit = suit

        # pass also works!
        # Use the pass keyword when you do
        # not want to add any other properties
        # or methods to the class.
        # this works the same as super(): Card.__init__(self, value, suit)

    def __str__(self):
        return f"{self.face} of {self.suit}"


