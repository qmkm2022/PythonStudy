# 구현 문제점
# - def로 함수 정의 후 기능별 구현이 가능하지만 하지 않았음
# - while True 문(무한반복문)을 통해 특정기능 실행 후 다른 기능들까지 반복실행시킬 수 있었지만 하지 않았음
# - 발코딩, 다른사람이 보고 한번에 이해가 가능하게 기능별로 정의가 되어있고 그 기능만 불러오고 수정 삭제가 가능하도록
#   간단하게 구성되어야함.

# 해결방법
# - 총 3개의 기능임. 전체조회, 회원등록, 개별조회, 이러한 기능을 함수로 정의
# - 소스코드는 if문으로 기능별 조건선택 및 while True 무한반복문으로 함수만 가져다 쓰기

# import 및 환경변수
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

    # 테이블은 이미 생성되어 있으니 주석처리
    # # (5) tb1 테이블 생성
    # ct = "create table if not exists tb1(name varchar(20), age int, num int);"
    # cursor.execute(ct)
    # conn.commit() # db 반영


# 회원 등록 기능
def sign_up() :
    try :
        # db 연동 객체
        conn = pymysql.connect(**config)
        # sql 실행 객체
        cursor = conn.cursor()

        # 중복방지를 위한 성명 조회
        su_name = input('회원님의 성명을 입력해주세요 : ')

        # 테이블에 같은 이름이 있는지 조회
        if su_name:
            su_n = f"select * from tb1 where name like '%{su_name}%'"
            cursor.execute(su_n)
            ci_rows = cursor.fetchall()
            
            # 있을 시
            if len(ci_rows) > 0:
                print('이미 존재하는 회원입니다. 다시 입력해주세요.')

            # 없을 시 등록 진행
            else:
                su_age = int(input('나이를 입력해주세요 : '))
                su_num = int(input('수량을 입력해주세요 : '))   
                su_s = f"insert into tb1 values('{su_name}',{su_age},{su_num})"
                cursor.execute(su_s) # 레코드 추가
                conn.commit()
                print("회원등록을 성공했습니다.")

        # 이름을 입력 안했을 시 = null(False)
        else :
            print("회원가입을 위해 이름을 입력해 주세요")

    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()


# 전체 회원 조회 기능
def all_mem():
    try :
        # db 연동 객체
        conn = pymysql.connect(**config)
        # sql 실행 객체
        cursor = conn.cursor()

        # 모든 레코드 조회
        cursor.execute("select * from tb1")
        am_rows = cursor.fetchall()
        print("===전체 회원 명단===")
        print("(NAME, AGE , NUM)")
        for row in am_rows :
            print(row)

    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 

    finally:
        cursor.close()
        conn.close()


# 개별 회원 조회 기능
def personal_mem() :
    try:
        # db 연동 객체
        conn = pymysql.connect(**config)
        # sql 실행 객체
        cursor = conn.cursor()

        # 회원 개별 조회
        pm_name = input("조회할 이름를 입력하세요 : ")
        pm = f"select * from tb1 where name like '%{pm_name}%'"
        cursor.execute(pm) # 조회
        pm_rows = cursor.fetchall()

        # (9-1) 조회 결과가 있을 시
        if pm_rows : # null = false
            for row in pm_rows :
                print('조회결과는 이름:',row[0],', 나이:',row[1],', 수량:',row[2], '입니다.')
        
        # (9-2) 조회 결과가 없을 시
        else :
            print('조회결과 입력한 이름에 맞는 회원이 없습니다.')

    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 

    finally:
        cursor.close()
        conn.close()



# 소스코드 시작

if __name__ == "__main__" : # 소스코드가 시작하는 지점
    while True: # while True == 무한반복문으로 breark절이 나타날때까지 계속반복함
        os.system('cls')
        print("---회원관리 프로그램---")
        print("회원    등록 : 1 ")
        print("전체회원조회 : 2 ")
        print("개별회원조회 : 3 ")
        print("회원    수정 : 4 ")
        print("회원    삭제 : 5 ")
        print("종        료 : 6 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            sign_up()
            os.system("pause")
        elif sel == 2 :
            all_mem()
            os.system("pause")
        elif sel == 3 :
            personal_mem()
            os.system("pause")
        elif sel == 4 :
            print("회원수정기능은 준비중입니다. ")
            os.system("pause")
        elif sel == 5 :
            print("회원삭제기능은 준비중입니다. ")
            os.system("pause")
        elif sel == 6 :
            print("프로그램을 종료합니다.")
            break
        else :
            print("잘못 입력하셨습니다. ")
            os.system("pause")