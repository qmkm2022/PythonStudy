import pymysql
import os
import sys
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '0000',
    'database' : 'test_db',
    'port' : 3309,
    'charset' : 'utf8',
    'use_unicode' : True
}

# goods 테이블 생성
def tableCreate() :
    try :
        print("----->")
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        sql = """create table  if not exists goods(
            code int primary key,
            name varchar(30) not null,
            su int default 0,
            dan int default 0
            )"""
        cursor.execute(sql)
        conn.commit()
    except Exception as e :
        print("오류 : ",e)
        conn.rollback()
    finally :
        conn.close()
        cursor.close()


# 상품 등록 기능
def add_pd() :
    try:
        # db 연동 객체
        conn = pymysql.connect(**config)

        # sql 실행 객체
        cursor = conn.cursor()

        # 중복방지를 위한 이름 조회
        print("<<<상품 등록입니다)>>>")
        ap_name = input("상품 이름을 입력해주세요 : ")

        # 테이블의 같은 상품이 있는지 조회
        if ap_name:
            ap_n = f"select * from goods where name like '%{ap_name}%'"
            cursor.execute(ap_n)
            ap_rows = cursor.fetchall()

            # 있을 시
            if len(ap_rows) > 0:
                print('이미 존재하는 상품입니다. 다시 입력해주세요.')

            # 없을 시 등록 진행
            else:
                ap_code = int(input('코드를 입력해주세요 : '))
                ap_su = int(input('수량을 입력해주세요 : '))  
                ap_dan = int(input('단가를 입력해주세요 : ')) 
                ap_s = f"insert into goods values({ap_code},'{ap_name}',{ap_su},{ap_dan})"
                cursor.execute(ap_s) # 레코드 추가
                conn.commit()
                print("상품등록을 성공했습니다.")

        # 이름을 입력 안했을 시 = null(False)
        else :
            print("상품등록을 위해 이름을 입력해 주세요")
    
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()


def all_pd() : 
    try:
        # db 연동 객체
        conn = pymysql.connect(**config)
        # sql 실행 객체
        cursor = conn.cursor()

        # 모든 레코드 조회
        cursor.execute("select * from goods")
        ap_rows = cursor.fetchall()

        print("<<<상품 목록 조회입니다)>>>")
        print("===goods 테이블 조회1===")
        print("(CODE, NAME, SU, DAN )")
        for r in ap_rows :
            print('%d  %s  %d  %d'%r)

    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 

    finally:
        cursor.close()
        conn.close()


# 코드별 조회 기능
def search_code_pd():
    try:
        # db 연동 객체
        conn = pymysql.connect(**config)
        # sql 실행 객체
        cursor = conn.cursor()

        # 회원 개별 조회
        print("<<<상품 개별 조회(코드)입니다)>>>")
        ap_code = int(input("조회할 코드를 입력하세요 : "))
        pm = f"select * from goods where code like {ap_code}"
        cursor.execute(pm) # 조회
        pm_rows = cursor.fetchall()

        # (9-1) 조회 결과가 있을 시
        if pm_rows : # null = false
            for row in pm_rows :
                print('조회결과는 코드:',row[0],', 이름:',row[1],', 수량:',row[2],', 단가:',row[3], '입니다.')
        
        # (9-2) 조회 결과가 없을 시
        else :
            print('해당상품 없음')

    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 

    finally:
        cursor.close()
        conn.close()


# 상품명별 조회 기능
def search_name_pd():
    try:
        # db 연동 객체
        conn = pymysql.connect(**config)
        # sql 실행 객체
        cursor = conn.cursor()

        # 회원 개별 조회
        print("<<<상품 개별 조회(상품명)입니다)>>>")
        ap_name = input("조회할 상품명을 입력하세요 : ")
        pm = f"select * from goods where name like '%{ap_name}%'"
        cursor.execute(pm) # 조회
        pm_rows = cursor.fetchall()

        # (9-1) 조회 결과가 있을 시
        if pm_rows : # null = false
            for row in pm_rows :
                print('조회결과는 코드:',row[0],', 이름:',row[1],', 수량:',row[2],', 단가:',row[3], '입니다.')
        
        # (9-2) 조회 결과가 없을 시
        else :
            print('해당상품 없음')

    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__" : # 소스코드가 시작하는 지점
    while True: # while True == 무한반복문으로 breark절이 나타날때까지 계속반복함
        os.system('cls')
        print("---상품관리---")
        print("상품    등록 : 1 ")
        print("상품목록조회 : 2 ")
        print("코드별  조회 : 3 ")
        print("상품명별조회 : 4 ")
        print("상품    수정 : 5 ")
        print("상품    삭제 : 6 ")
        print("상품관리종료 : 9 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            add_pd()
            os.system("pause")
        elif sel == 2 :
            all_pd()
            os.system("pause")
        elif sel == 3 :
            search_code_pd()
            os.system("pause")
        elif sel == 4 :
            search_name_pd()
            os.system("pause")
        elif sel == 5 :
            print("상품수정기능은 준비중입니다. ")
            os.system("pause")
        elif sel == 6 :
            print("상품삭제기능은 준비중입니다. ")
            os.system("pause")
        elif sel == 9 :
            print("상품관리를 종료합니다.")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 입력하셨습니다. ")
            os.system("pause")