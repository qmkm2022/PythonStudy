import pymysql

db = None
try:
    # DB 호스트 정보에 맞게 입력해주세요
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='0000',
        db='test_db',
        port= 3309 ,
        charset='utf8'
    )

    # 데이터 삭제 sql 정의
    id = 1  # 데이터 id (PK)
    sql = '''
        DELETE from tb_student where id=%d
        ''' % id

    # 데이터 삭제
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()


except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()