import requests
from bs4 import BeautifulSoup as bs

# 크롤링을 이용한 환률 계산기 : 다른 나라의 통화를 원으로 계산 -> 원을 다른 나라 통화로 계산 변경

# step 01) 환률 계산할 금액을 입력해주세요. (단위 :원) >> 10000
# step 02) 원하시는 국가를 선택해 주세요.
# 1. 미국
# 2. 일본
# 3. 유럽
# 4. 중국
# ============
# 선택 >> 1
# step 03) 10000원은 달러로 환전하면 7.543753771876887달러입니다.

def get_exchange_rate(menu: int) -> float:  # 원하는 환율을 가져옴
    url = 'https://finance.naver.com/marketindex'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    exchange_rates = soup.select('#exchangeList > li > a.head > div > span.value')
    exchange_rate: float = float(exchange_rates[menu -1].text.replace(",", ""))
    # 금액 숫자 중 ,가 들어가 변환이 안되는 이유 replace로 제거
    return exchange_rate

money = int(input('step 01) 환율 계산할 금액을 입력해주세요. (단위 :원) >> '))
print('step 02) 원하시는 국가를 선택해 주세요.')
print('1. 미국')
print('2. 일본')
print('3. 유럽')
print('4. 중국')
print('==========')
menu = int(input('선택 >> '))
unit = ['달러', '엔', '유로', '위안']

if menu == 2:
    trans_money = money / get_exchange_rate(menu) * 100
else:
    trans_money = money / get_exchange_rate(menu)

print(f'{money}원은 {unit[menu-1]}로 환전하면 {trans_money}{unit[menu-1]}입니다.')
