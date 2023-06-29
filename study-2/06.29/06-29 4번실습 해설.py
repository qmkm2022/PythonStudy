#예제 7-3 데이터 삽입
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
    # 데이터 삽입 sql 정의
    sql = '''
    INSERT tb_student(name, age, address) values('Kei', 35, 'Korea')
    '''
    # 데이터 삽입
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
