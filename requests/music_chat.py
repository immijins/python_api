import requests
from bs4 import BeautifulSoup as bs

from share import save_csv

# 1. 벅스 TOP 100 순위, 곡제목, 가수, 앨범 csv로 저장

# url 연결, html 태그 가져오기
url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# pprint.pprint(soup)

chart = soup.select('#CHARTrealtime > table > tbody > tr')
# pprint.pprint(chart)

# 소스 추출
dict_list: list[dict] = list()
for i, char in enumerate(chart):
    new_dict = dict()

    new_dict['순위'] = i + 1
    new_dict['곡제목'] = char.select_one('.title').text.strip()
    new_dict['가수'] = char.select_one('.artist').text.strip().replace("/", ",").replace("\n", "").replace("\r", "")
    new_dict['앨범'] = char.select_one('.album').text.strip()

    dict_list.append(new_dict)
print(dict_list)

save_csv('bugs.csv', dict_list)

# 2. 앨범 이미지 저장
# 파일명 순위_곡제목_가수.jpg
# bugs

# 이미지 태그
tag_img = soup.select('.thumbnail > img')
# print(tag_img)

# 이미지 저장 경로
dir_save = './output_image/bugs/'

for i, tag in enumerate(tag_img):
#    print(tag.attrs['src'])
    response = requests.get(tag.get('src'))

    with open(f'{dir_save}_{dict_list[i]["순위"]}_{dict_list[i]["곡제목"]}_{dict_list[i]["가수"]}.jpg', 'wb') as img_file:
        img_file.write(response.content)
        print(f'{i+1}/{len(tag_img)}')

