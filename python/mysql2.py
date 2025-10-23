import pymysql

# MySQL 연결
conn = pymysql.connect(
    host='127.0.0.1',        # DB 서버 주소
    user='root',             # 사용자 계정
    password='mysql',# 사용자 비밀번호
    db='python',             # 사용할 DB 이름
    charset='utf8mb4'        # 문자 인코딩
)

# 커서 객체 생성 (쿼리 실행에 사용)
cur = conn.cursor()

try:
    print("💸 잘못된 송금 시도 (트랜잭션 시작)")

    # 트랜잭션 명시적 시작
    conn.begin()

    # user1에게서 300원 차감
    cur.execute(
        "UPDATE accounts SET balance = balance - 300 WHERE user_id = %s",
        ('user1',)
    )

    # ❌ 존재하지 않는 사용자에게 입금 시도 → 에러 발생 예정!
    cur.execute(
        "UPDATE accounts SET balance = balance + 300 WHERE user_id = %s",
        ('non_exist_user',)  # 존재하지 않는 ID
    )

    # 여기에 도달하면 안 됨 (예외 발생해야 정상)
    conn.commit()
    print("❌ 이 메시지가 출력되면 안 됩니다.")

except Exception as e:
    # 예외 발생 시 롤백 → 모든 변경사항 취소됨
    conn.rollback()
    print("🚨 에러 발생! 트랜잭션 롤백 처리")
    print("에러 내용:", e)

finally:
    # 리소스 정리
    cur.close()
    conn.close()
    print("🔚 연결 종료")
