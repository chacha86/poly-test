no = 4
articles = []
# ====================================================================
# 이부분은 문제 범위가 아닙니다. 
def add_padding(pstr, width) :
    if str(type(pstr)) == "<class 'int'>" :
        pstr = str(pstr)
    
    cnt = 0
    for c in pstr :
        if 0 <= ord(c) and ord(c) <= 127 :
            cnt += 1
        else :
            cnt += 2
    
    pd_len = width - cnt
    for i in range(pd_len) :
        pstr += ' '
    
    return pstr

def f2(s1, s2, s3, s4, s5) :
    if len(s2) >= 10 :
        s2 = s2[:7] + "..."
    print(add_padding(s1, 3), end=" ")
    print(add_padding(s2, 20), end=" ")
    print(add_padding(s3, 10), end=" ")
    print(add_padding(s4, 12), end=" ")
    print(add_padding(s5, 0), end=" ")
    print()
    print("---------------------------------------------------------")

def print_article_list(articles) :
    f2("번호", "제목", "작성자", "작성일", "조회수")
    for a in articles :
        f2(a["no"], a["title"], a["writer"], str(a['regDate'])[:10], a['hit'])
# 이부분은 문제 범위가 아닙니다. 
# ====================================================================

def print_help() :
    print("add    : 게시물 등록")
    print("list   : 게시물 목록 조회")
    print("update : 게시물 수정")
    print("delete : 게시물 삭제")
    print("search : 게시물 검색")
    print("read   : 게시물 상세보기")
    print("signup : 회원가입")
    print("login  : 로그인")

# ====================================================================
def add_article() :
    no = 1
           
    title = input("제목을 입력해주세요 : ")

    body = input("내용을 입력해주세요 : ")

    import datetime as dt
    date = dt.datetime.now()
    date = date.strftime("%Y.%m.%d")

    article = {"no" : no, "title" : title, "body" : body,
               "writer" : "익명", "hit" : 0, "regDate" : date}
    
    articles.append(article)
    no += 1
    
    print("게시물이 저장되었습니다.")
        
# ====================================================================
def update_article() :
    no = int(input("수정할 게시물 번호 :")) 
  
    is_exist = 0 
  
    for i in range(len(articles)) :
        article = articles[i]
    
        if article["no"] == no :
            is_exist = 1
            title = input("새제목 : ")
            article["title"] = title
            body = input("새내용 : ")
            article["body"] = body
    
            print("수정 완료되었습니다")
            break
        
    if is_exist == 0:
      print("없는 게시물입니다.")  
    
    print_article_list(articles)
# ====================================================================
def delete_article() :
    no = int(input("삭제할 게시물 번호 :")) 
        
    is_exist = 0
  
    for i in range(len(articles)) :
        article = articles[i]
    
        if article["no"] == no :
            is_exist = 1
            del(articles[i])
            print("삭제가 완료되었습니다.")
            break   

    if is_exist == 0:
        print("없는 게시물입니다.") 
        
# ====================================================================    
# 함수 완성하기 2
def search_article() :
    keyword = input("검색 키워드를 입력해주세요 :") 
    
  
# ====================================================================
def init() :
  test_article1 = {"no" : 1, "title" : "제목1", "body" : "내용1", 
                   "writer" : "익명", "hit" : 0, "regDate" : "2022.04.04"}
  test_article2 = {"no" : 2, "title" : "제목2", "body" : "내용2",
                   "writer" : "익명", "hit" : 0, "regDate" : "2022.04.04"}
  test_article3 = {"no" : 3, "title" : "제목3", "body" : "내용3",
                   "writer" : "익명", "hit" : 0, "regDate" : "2022.04.04"}
  articles.append(test_article1)
  articles.append(test_article2)
  articles.append(test_article3)
  print("테스트 데이터 등록 완료.")  
# ====================================================================
    
def read_article() :
    
    no = int(input("상세보기할 게시물 번호 :"))
  
    article = get_article_by_no(no)    
    
    if article != None :
        article["hit"] + 1
        print_one_article(article)
        
    else :        
        print("없는 게시물입니다.") 
      
# ====================================================================
def print_one_article(article) :
    print("==== {}번 게시물 ====".format(article["no"]))
    print("번호 : {}".format(article["no"]))
    print("제목 : {}".format(article["title"]))
    print("-------------------")
    print("내용 : {}".format(article["body"]))
    print("-------------------")
    print("작성자 : {}".format(article["writer"]))
    print("등록날짜 : {}".format(article["regDate"]))
    print("조회수 : {}".format(article["hit"]))
    print("===================")

# ====================================================================
def get_article_by_no(no) :
    article = articles[no]
    if article["no"] == no :
        return article     


# ====================================================================
