import csv
class ExpenseSplitter:
    def __init__(self):
        self.expenses={}

    def add_expense(self,payer,amount,participants):
        share = amount/len(participants)

        if payer not in self.expenses:
            self.expenses[payer] = 0
        self.expenses[payer] += amount

        for person in participants:
            if person not in self.expenses:
                self.expenses[person]=0
            self.expenses[person] -= share

    def show_balance(self):
        print("\nCurrent Balances:")

        for person, balance in self.expenses.items():
            print(f"{person}: {'Owes' if balance < 0 else 'Gets'} {abs(balance):.2f}")

    def settle_expenses(self):
        print("\nSettling Expense")

        g = self.expenses.copy()  #g = expense_dict

        sorted_balances = sorted(self.expenses.items(), key=lambda x:x[1]) #sorting and comparing elements at position 1 of tuples ie. money

        while sorted_balances[0][1] < 0:
            debtor, debt_amount = sorted_balances[0]
            creditor, creditor_amount = sorted_balances[-1]

            amount_to_settle = min(-debt_amount, creditor_amount)

            print(f"{debtor} pays {amount_to_settle:.2f} to {creditor}")

            g[debtor] += amount_to_settle
            g[creditor] -= amount_to_settle
            
            sorted_balances = sorted(g.items(), key=lambda x:x[1])

        print("Debt after settling: ",g)

    def reset_expenses(self):
        self.expenses.clear()

        print("Data cleared")

    def load_file(self,filename):
        a = input("Do you want to load data?(yes or no): ")

        if a == 'yes':
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                

                for row in reader:
                    payer = row[1]
                    amount = row[2]
                    participants = row[3]
                    self.add_expense(payer, float(amount), participants.split(","))

    def add_expense_and_save(self,event,payer,amount,participants):
        share = amount/len(participants)

        if payer not in self.expenses:
            self.expenses[payer] = 0
        self.expenses[payer] += amount

        for person in participants:
            if person not in self.expenses:
                self.expenses[person]=0
            self.expenses[person] -= share
                        
        with open("mydata.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([event, payer, amount, ",".join(participants)])


    def menu(self):
        while True:
            print("\nSmart Expense Splitter")
            print("1. Add budget")
            print("2. Add Ticket Expenses")
            print("3. Add Expense")
            print("4. Show Balance")
            print("5. Settle Expense")
            print("6. Reset Expense")
            print("7. Load Expense")
            print("8. Add Expense and Save")

            choice = input("Enter num:")

            if choice == '3':
                payer = input("Payer name:")
                amount = float(input("Amount:"))
                participants = input("Enter names of participants:").split(',')

                self.add_expense(payer.strip(), amount, [p.strip() for p in participants])
                print("Expense Added")

            elif choice == '4':
                self.show_balance()

            elif choice == '5':
                self.settle_expenses()

            elif choice == '6':
                self.reset_expenses()
            
            elif choice == '2':
                k = input("Enter names of participants:").split(',')
                contris = [p.strip() for p in k]

                for i in range(len(contris)):
                    j = float(input(f"Ticket cost for {contris[i]}: "))
                    if contris[i] not in self.expenses:
                        self.expenses[contris[i]] = 0
                    self.expenses[contris[i]] -= j

            elif choice == '1':
                k = input("Enter names of contributers:").split(',')
                contris = [p.strip() for p in k]

                for i in range(len(contris)):
                    j = float(input(f"Amount contributed by {contris[i]}: "))
                    if contris[i] not in self.expenses:
                        self.expenses[contris[i]] = 0
                    self.expenses[contris[i]] += j
            
            elif choice == '7':
                self.load_file("mydata.csv")

            elif choice == '8':
                payer = input("Payer name:")
                amount = float(input("Amount:"))
                participants = input("Enter names of participants:").split(',')
                event = input("Enter Event: ")

                self.add_expense_and_save(event, payer.strip(), amount, [p.strip() for p in participants])
                print("Expense Added and Saved")
                
                
            else:
                print("Invalid, try again")

if __name__ == "__main__":
    app = ExpenseSplitter()
    app.menu()
