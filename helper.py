expences=[]
def create_expence():
    title=input("Enter the expence title")
    amount=input("Enter the amount")
    dt=input("Enter the date")
    expences.append((title,amount,dt))
def display_expence():
    print(expences)
def delete_expence():
    #need to remove/delete record
    in1=int(input("Enter the index you want to remove"))
    del expences[in1]
def update_expence():
    in1=int(input("Enter the index you want to update"))
    title=input("Enter the expence title")
    amount=input("Enter the amount")
    dt=input("Enter the date")
    expences[in1]=(title,amount,dt)
def menu():
    print("Options")
    print("1-> For Insert a record")
    print("2-> For Show  records")
    print("3-> For Remove  records")
    print("4-> For Update  records")
    op=int(input("Enter Your Option"))
    return op
def get_expences():
    return expences
def set_expences(data):
    global expences
    expences=data