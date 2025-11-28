import streamlit as st

st.title("진법 변환기 (2, 8, 10, 16)")

# 지원 진법
supported_bases = [2, 8, 10, 16]

# 입력 진법 선택
bef_b = st.selectbox('입력할 수의 진법을 선택하세요', supported_bases)

# 숫자 선택 범위 설정
if bef_b == 16:
    digits = [str(i) for i in range(10)] + list('A B C D E F'.split())
else:
    digits = [str(i) for i in range(bef_b)]

# 자리수 선택
num_digits = st.number_input('자리수 선택', min_value=1, max_value=8, value=4, step=1)

# 숫자 선택 박스 생성
bef_n = []
for i in range(num_digits):
    bef_n.append(st.selectbox(f'{i+1}번째 자리', digits, key=f'digit_{i}'))

# 선택한 숫자를 10진수로 변환
bef_n_int = []
for d in bef_n:
    if bef_b == 16:
        bef_n_int.append(int(d, 16))
    else:
        bef_n_int.append(int(d))

# 출력 진법 선택
aft_b = st.selectbox('출력할 수의 진법을 선택하세요', supported_bases, key='output_base')

# 변환 버튼
if st.button('변환'):
    # 입력 검증
    for digit in bef_n_int:
        if digit >= bef_b:
            st.error(f"입력 숫자 {digit}가 입력 진법 {bef_b}보다 큽니다!")
            st.stop()

    # 10진수로 변환
    n = sum(bef_n_int[i] * (bef_b ** (len(bef_n_int) - i - 1)) for i in range(len(bef_n_int)))

    # 출력 진법으로 변환
    if n == 0:
        aft_n = [0]
    else:
        aft_n = []
        while n > 0:
            aft_n.append(n % aft_b)
            n //= aft_b
        aft_n.reverse()

    # 결과 문자열 만들기
    if aft_b == 16:
        hex_map = "0123456789ABCDEF"
        res = ''.join(hex_map[d] for d in aft_n)
    else:
        res = ''.join(str(d) for d in aft_n)

    st.success(f"변환 결과: {res}")
