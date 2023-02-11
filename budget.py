import csv
import pandas as pd
from expense import Expense

"""
!add expenses to the expense list
"""

class Budget:
    def __init__(self, amount):
        self.total_amount = amount
        self.amount_left = amount
        self.expense_list = []
    def add_expense(self, expense_name):
        new_expense = Expense(expense_name)
        self.expense_list.append(new_expense)
        # print(self.expense_list)
        return self.expense_list
    """
    Here you need to move money from one expense to the other
    first you need to check to make sure the expenses exist in the list
    """
    def move_money(
        self, 
        first_category, 
        amount, 
        second_category
        ):
        pass
    def deposit_expense(self,expense_name,amount):
        does_not_exists = True
        amount = int(amount)
        for i in self.expense_list:
            if i.expense_name == expense_name:
                i.value += amount
                self.amount_left -= amount
                does_not_exists = False

        if(does_not_exists):
            print("<<< Not Here >>>")

        
            
        pass
    def show_budget(self):
        print(f"Budget Amount: {self.total_amount}")
        print(f"Amount Left: {self.amount_left}")
        for i in self.expense_list:
            print(i)

    def menu(self):
        print('——— Welcome to Your Budget ———')
        text = (
"""What would you like to do?
1. Show Budget
2. Add Expense
3. Deposit Money to Expense
4. Move Money from One Expense to Another
""")     
        user_answer = input(text)
        while True:
            #add a category
            if user_answer == '1':
                self.show_budget()
                pass
            elif user_answer == '2':
                # add expense
                new_expense = input("Expense name?\n")
                self.add_expense(new_expense)
                pass
            elif user_answer == '3':
                #deposit money into expense
                expense = input("choose expense\n")
                amount = input("choose an amount\n")
                self.deposit_expense(expense,amount)
                pass
            #show categories/ turns into show budget eventually
            elif user_answer == '4':           
                pass
            user_answer = input(text)




            


        
    
    
