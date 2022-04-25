import article_lib as al
import member_lib as ml

al.init()
command = ""
    
while command != "exit" :
    if ______________ == None:
        command = input("명령어: ") # 함수
    else :
        command = input("명령어[{}({})]: ".
                        format(ml.logined_member["nickname"],
                               ml.logined_member["login_id"])) # 함수
    
    if command == "exit" :
        print("프로그램이 종료됩니다.")
    
    elif command == "help" :
        al.print_help()
        
    elif command == "add" :
        al.add_article()
              
    elif command == "list" :
        
        al.print_article_list(al.articles)
    
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
    
    elif command == "search" :
        al.search_article()        
            
            
            
       
