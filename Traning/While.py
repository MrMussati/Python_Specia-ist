 

1  import datetime
2  current_date = datetime.date.today()
3
4  str_due_date = input("Enter a date for the project in dd/mm/yyyy format:")
5  due_date = datetime.datetime.strptime(str_due_date, "%d/%m/%Y").date()
6
7  days_left = due_date - current_date
8
9  print(f"You have {days_left} days left to finish your project.")
10