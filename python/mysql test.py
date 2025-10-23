import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='mysql', db='python', charset='utf8mb4')
cur = conn.cursor()

try:
    print("💸 송금 시작 (트랜잭션 시작)")
    conn.begin()  # 트랜잭션 시작

    # user1 → user2에게 300원 송금
    cur.execute("UPDATE accounts SET balance = balance - 300 WHERE user_id = %s", ('user1',))
    cur.execute("UPDATE accounts SET balance = balance + 300 WHERE user_id = %s", ('user2',))

    conn.commit()  # 모두 성공 시 저장
    print("✅ 송금 완료! COMMIT")

except Exception as e:
    conn.rollback()  # 하나라도 실패 시 되돌리기
    print("❌ 에러 발생! ROLLBACK")
    print("에러 내용:", e)

finally:
    cur.close()
    conn.close()
