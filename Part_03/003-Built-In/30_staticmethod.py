'''
    Returns a static method for a given function.
'''
class TestDate:
    def __init__(self, date):
        self.date = date
        
    def get_date(self):
        return self.date

    @staticmethod
    def to_dash(date):
        return date.replace("/", "-")
    
date = TestDate("18-10-1986")

date_db = "18/10/1986"

print(date.get_date(), TestDate.to_dash(date_db), sep = "\n")