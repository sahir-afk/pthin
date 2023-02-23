class College:
    def __init__(self, ac, mr, location):
        self.chance = ac
        self.rating = mr
        self.location = location
        print("Created")
    def visit(self, time):
        print("visited on", time)

Uchicago = College(38, 10, "chicago")
Uchicago.rating = 9

cmu = College(38, 9, "pittsburgh")

rice = College(13, 10, "houston")

rice.visit("9/10")