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

    def move_money_category(self, first_category, amount, second_category):
        first_loop = False
        second_loop = False
        list_categories = []
        for i in self.categories:
            list_categories.append(i['category'])

        if second_category in list_categories:
            for first_dict in self.categories:
                if first_category == first_dict['category']:
                    less_amount = int(first_dict['amount'])-int(amount)
                    first_dict['amount'] = str(less_amount)
                    first_loop = True


        if first_category in list_categories:
            for second_dict in self.categories:
                if second_category == second_dict['category']:
                    new_amount = int(second_dict['amount']) + int(amount)
                    second_dict['amount'] = str(new_amount)
                    second_loop = True
            
        if second_loop and first_loop:
            self.write_csv()
        else:
            print('Invalid Entry')

    def moving_money_income(self,category,amount):
        try:    
            not_category = True
            real_amount = int(amount)
            if (real_amount) <= self.income-self.sub_():
                for categories in self.categories:
                    if categories['category'] == category:
                        not_category = False
                        category_amount = int(categories['amount'])
                        category_amount += real_amount
                        categories['amount'] = str(category_amount)
            else:
                print('You dont have enough for that')
            if not_category:
                print('This is not a category')
            self.write_csv()
        except:
            print('invalid entry')

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

        text = f'What would you like to do?\n1. Add a New Category\n2. Move Money into Category from Income\n3. Move Money from Category into Another Category\n4. View Budget\n5. Exit\n'

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
                print(f'{self.income-self.sub_()} here is how much money you have')
                user_amount = input('choose a whole number amount less than the money you have free\n')

                self.moving_money_income(user_category,user_amount)
                user_answer = input(text)
            #move category moneys
            elif user_answer == '3':
                for i in self.categories:
                    category = i['category']
                    money = i['amount']
                    print(f'{category} is a category with {money} Dollars')
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


