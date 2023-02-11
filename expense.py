

class Expense:
    def __init__(self,expense_name = 'none') :
        self.expense_name = expense_name
        self.value = 0

    
    def withdraw(self,amount):
        self.value -= amount
        return self.value


    def deposit(self,amount):
        self.value += amount
        return self.value

        




    


    

        