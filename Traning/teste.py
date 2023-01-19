####### LOAN ########


kitty = 500

request = []

#loan = open('C:\\Users\\bruno\Desktop\\VSCODE\\IT_Specialist_python\\Ecollege\\loan_requests.txt','r') 
#print(loan.read())
    

loan = open ('C:\\Users\\bruno\Desktop\\VSCODE\\IT_Specialist_python\\Ecollege\\loan_requests.txt','a+') 
for i in loan:
    i = i.rstrip()
    print(i)
loan.write('was paid\n ')
print(loan.read())

loan.close

