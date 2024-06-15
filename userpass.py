userpass = {   
    "username":"password" ,
    "amirhossein":'12345",
    "hooshang":"009922" ,
    "manizhe":"00000" ,
    "mahsa":"m11m3" }
x=int(0)

while x<3 :
    x = int(input("Enter 1 to login.\nEnter 2 to register.\nEnter 0 to exit. "))
    if x==1 :
        username = input("Enter your username : ") 
        password = input("Enter your password : ")
        if username in userpass and userpass [username] == password :
            print ("That's Right.")
            break
        else :
            print ("The username or password is wrong.")
            continue
    if x==2 :
        username = input("Enter your username : ") 
        if username in userpass :
            print("\nThis username is available\n")
            continue
        password = input("Enter your password : ")
        userpass.update({username:password})
        continue
    if x==0 :
        exit()
