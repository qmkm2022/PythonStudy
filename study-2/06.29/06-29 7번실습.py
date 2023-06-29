import pymysql
import pandas as pd
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

# 테이블 생성
def tableCreate() :
    try :
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


# 기본 데이터 정의
def dataSet() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        print("기본 데이터를 복구합니다.")
        students = [
            {'name': 'Kei', 'age': 36, 'address' : 'PUSAN'},
            {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
            {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
            {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
            {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
        ]
    # 데이터 db에 추가
        for s in students:
            with conn.cursor() as cursor:
                sql = '''
                        insert tb_student(name, age, address) values("%s",%d,"%s")
                        ''' % (s['name'], s['age'], s['address'])
                cursor.execute(sql)
        conn.commit() # 커밋
    except Exception as e :
        print("오류 : ",e)
        conn.rollback()
    finally :
        conn.close()
        cursor.close()


# 30대 학생만 조회
def search30() :
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        cond_age = 30
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = ''' 
            select * from tb_student where age > %d
            ''' % cond_age
            cursor.execute(sql)
            results = cursor.fetchall()
        print(results)
    except Exception as e :
        print("오류 : ",e)
        conn.rollback()
    finally :
        conn.close()
        cursor.close()


# 이름 검색
def searchname() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        os.system('cls')
        in_name = input("조회할 이름을 입력하세요 : ")
        sql = f"select * from tb_student where name = '{in_name}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) > 0 :
            for row in rows :
                print(row[1],row[2])
        else:
            print("조회결과 입력한 이름에 맞는 학생이 없습니다")
           
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close()


# 모든 로우 삭제
def delall() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        os.system('cls')
        print("모든 학생항목을 삭제합니다.")
        sql = ''' 
        TRUNCATE tb_student
        '''
        cursor.execute(sql)
        conn.commit
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close()


# 전체 학생 조회
def searchall() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        os.system('cls')
        cursor.execute("select * from tb_student")
        rows = cursor.fetchall()
        print("===학생 전체 명단 조회===")
        print("(id, name, age, adress)")
        for row in rows :
            print(row)
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__" : # 시작점
    tableCreate()
    while True:
        os.system('cls')
        print("---학생관리---")
        print("30대이상 학생 조회 : 1 ")
        print("이름 검색 : 2 ")
        print("모든 항목 삭제 : 3 ")
        print("기본 데이터 복구 : 4")
        print("전체 학생 조회 : 5")
        print("상품관리종료 : 9 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            search30()
            os.system("pause")
        elif sel == 2 :
            searchname()
            os.system("pause")
        elif sel == 3 :
            delall()
            os.system("pause")
        elif sel == 4 :
            dataSet()
            os.system("pause")
        elif sel == 5 :
            searchall()
            os.system("pause")
        elif sel == 9 :
            print("프로그램을 종료합니다. ")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")