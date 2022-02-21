import os
import csv
import pandas as pd 

class Budget:
    def __init__(self, income):
        self.income = income
        self.categories = self.load_csv()
    
    def sub_(self):
        num = 0
        for category in self.categories:
            num += int(category['amount'])
        return num

    def add_category(self, dict_):
        self.categories.append(dict_)
        self.write_csv()

    def move_money_category(self, category, amount, category_new):
        for category in self.categories:
            if category == category['category']:
                new_amount = int(category['amount'])-int(amount)
                category['amount'] = str(new_amount)
        
        for category in self.categories:
            if category_new == category['category']:
                new_amount = int(category['amount']) + int(amount)
                category['amount'] = str(new_amount)
        self.write_csv()

    def moving_money_income(self,category,amount):
        not_category = True
        real_amount = int(amount)
        if (real_amount) <= self.income-self.sub_():
            for categories in self.categories:
                if categories['category'] == category:
                    not_category = False
                    categories['amount'] = amount
        
        else:
            print('You dont have enough for that')
        if not_category:
            print('This is not a category')
        self.write_csv()
        print(self.sub_())
    def show_categories(self):
        print('———— Here is your Budget ————')
        print(f'Your total monthly income is: {self.income} Dollars')
        for i in self.categories:
            category = i['category']
            amount = i['amount']
            print(f'for {category} you can spend {amount} Dollars')
        print(f'and you have {self.income - self.sub_()} Dollars left')
        print('——— END ———')
    
    def show_money_left(self):
        print(self.income - self.sub_())
    
    def load_csv(self):
        arr = []
        path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(path, 'data.csv')
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for dict_ in reader:
                arr.append(dict_)
        
        return arr

    def write_csv(self):
        df = pd.DataFrame.from_dict(self.categories)
        df.to_csv(r'data.csv', index = False, header = True)

    def menu(self):
        print('——— Welcome to Your Budget ———')

        text = f'What would you like to do?\n1. add a new category\n2. move money into category from income\n3. move money from category into another category\n4. View Budget\n5. Exit\n'

        user_answer = input(text)

        while True:
            #add a category
            if user_answer == '1':
                user_dict_ = {}
                user_dict_['category'] = input('what is the category\n')
                user_dict_['amount'] = 0
                self.add_category(user_dict_)                
                user_answer = input(text)
            #move money with income
            elif user_answer == '2':
                for i in self.categories:
                    category = i['category']
                    print(f'{category} is a category')
                user_category = input('choose a category from above\n')
                print(f'{self.income-self.sub_()} here is how much you have free')
                user_amount = input('choose an amount less than the money you have free\n')

                self.moving_money_income(user_category,user_amount)
                user_answer = input(text)
            #move category moneys
            elif user_answer == '3':
                user_category = input('choose category to take from\n')
                user_amount = input('choose a whole number amount\n')
                user_new_category = input('choose category to add to\n')
                self.move_money_category(user_category,user_amount,user_new_category)
                user_answer = input(text)
            #show categories/ turns into show budget eventually
            elif user_answer == '4':
                self.show_categories()
                user_answer = input(text)
  
            elif user_answer == '5':
                print('thank you come again')
                break
            else:
                print('that is not an option')
                user_answer = input(text)




