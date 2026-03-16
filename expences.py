from helper import *
from filehelper import *
data1=read_expences()
set_expences(data1)
is_continue=True
while(is_continue==True):
    opt=menu()
    if(opt==1):
       create_expence()
    if(opt==2):
       display_expence()
    if(opt==3):
       delete_expence()
    if(opt==4):
       update_expence() 
    is_continue=bool(input("Do you want to continue? Types True for Yes"))
    if not is_continue:
       data=get_expences()
       write_expences(data)
       