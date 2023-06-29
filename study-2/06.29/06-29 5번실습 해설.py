#예제 7-5 삭제
import pymysql
db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='root1234',
        db='test_db',
        charset='utf8'
    )
    ## 데이터 삭제 sql 정의 백업본 
    #id = 1  # 데이터 id (PK)
    #sql = '''
    #    DELETE from tb_student where id=%d
    #    ''' % id
    ## 
    #id = 1  # 데이터 id (PK)
    sql = '''                   ##### 테이블의 모든 로우를 삭제함 
        DELETE from tb_student
        '''
    # 
    # 데이터 삭제
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()