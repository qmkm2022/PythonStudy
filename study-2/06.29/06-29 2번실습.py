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
    print("DB 연결 성공")


except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB 연결 닫기 성공")