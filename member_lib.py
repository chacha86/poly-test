members = []
no = 1
logined_member = None 

# 함수 완성하기2
def signup() :
  print("==== 회원 가입을 진행합니다 ====")

  print("회원가입이 완료되었습니다.")
  
def login() :
    global logined_member
    
    login_id = input("아이디 : ")
    login_pw = input("비밀번호 : ") 

    member = get_member_by_id_and_pw(login_id, login_pw)
    
    if member == None :
        print("잘못된 회원정보입니다.")
        return

    # 빈칸 채우기4
    _______________ = member
    print("{}님! 반갑습니다!!".format(member["nickname"]))
        
    
def get_member_by_id_and_pw(login_id, login_pw) :
    member = __________________(login_id)  # 빈칸 채우기5
    
    if member == None :
        return None
    
    if member["login_pw"] == login_pw :
        return member
        
            
def get_member_by_id(login_id) :
    for member in members :
        if member["login_id"] == login_id :
            return member