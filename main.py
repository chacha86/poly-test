import article_lib as al

# 1. 빈칸채우기1
import _________________

al.init()
command = ""
    
while command != "exit" :
    # 빈칸 채우기2
    if ________________ == None:
        command = input("명령어: ") 
    else :
        command = input("명령어[{}({})]: ".
                        format(ml.logined_member["nickname"],
                               ml.logined_member["login_id"])) 
    
    if command == "exit" :
        print("프로그램이 종료됩니다.")
    
    elif command == "help" :
        al.print_help()
        
    elif command == "add" :
        al.add_article()
              
    elif command == "list" :

        # 빈칸 채우기 3
        al.print_article_list(____________)
      
    elif command == "update" :
        al.update_article()
    
    elif command == "delete" :
        al.delete_article()
    
    elif command == "read" :
        al.read_article()
        
    elif command == "signup" :
        ml.signup()
        
    elif command == "login" :
        ml.login()        
