import streamlit as st

st.title("진법 변환기 (2, 8, 10, 16)")

# 지원 진법
supported_bases = [2, 8, 10, 16]

# 입력 진법 선택
bef_b = st.selectbox('입력할 수의 진법을 선택하세요', supported_bases)

# 입력 숫자
if bef_b == 16:
    bef_n_str = st.text_input('수를 입력해주세요 (0-9, A-F 사용)')
else:
    bef_n_str = st.text_input(f'수를 입력해주세요 (0~{bef_b-1} 사용)')

# 출력 진법 선택
aft_b = st.selectbox('출력할 수의 진법을 선택하세요', supported_bases, key='output_base')

# 변환 버튼
if st.button('변환'):
    try:
        # 입력 문자열을 10진수 숫자 리스트로 변환
        if bef_b == 16:
            bef_n = [int(ch, 16) for ch in bef_n_str.upper()]
        else:
            bef_n = [int(ch) for ch in bef_n_str]

        # 입력 검증
        for digit in bef_n:
            if digit >= bef_b:
                st.error(f"입력 숫자 {digit}가 입력 진법 {bef_b}보다 큽니다!")
                st.stop()

        # 10진수로 변환
        n = sum(bef_n[i] * (bef_b ** (len(bef_n) - i - 1)) for i in range(len(bef_n)))

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

    except ValueError:
        st.error("입력을 올바른 숫자 형식으로 입력해주세요.")

