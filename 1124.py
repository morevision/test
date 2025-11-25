# 계산 목록 (숫자1, 연산자, 숫자2)
calculations = [
    (10, '+', 5),
    (20, '-', 8),
    (6, '*', 7),
    (15, '/', 3),
    (8, '/', 0),    # 0으로 나누기
    (12, '%', 5),   # 잘못된 연산자
]
print("계산 결과:")

# 리스트에서 값을 꺼내며 반복 
for num1, op, num2 in calculations:
    # 덧셈
    if op == '+':
        print(num1, "+", num2, "=", num1 + num2)

    # 뺄셈
    elif op == '-':
        print(num1, "-", num2, "=", num1 - num2)

    # 곱셈
    elif op == '*':
        print(num1, "*", num2, "=", num1 * num2)

    # 나눗셈
    elif op == '/':
        if num2 == 0:
            print("0으로 나눌 수 없습니다")
        else:
            # 결과 이미지에 5.0으로 되어 있으므로 int() 없이 계산
            print(num1, "/", num2, "=", num1 / num2)

    # 그 외 연산자 (%)
    else:
        print("잘못된 연산자입니다")