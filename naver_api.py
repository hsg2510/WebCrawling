import requests
import dotenv
import os
import pprint

# 환경변수 불러오기
dotenv.load_dotenv()

client_id = os.getenv("NAVER_OPEN_API_CLIENT_ID")
client_secret = os.getenv("NAVER_OPEN_API_CLIENT_SECRET")

naver_open_api_url = (
    "https://openapi.naver.com/v1/search/news.json?query=펩트론&sort=sim"
)
header_params = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
}

res = requests.get(naver_open_api_url, headers=header_params)

if res.status_code == 200:
    json_data = res.json()
    # pprint.pprint(json_data)
    # print(json_data)
    # print(res.text)
else:
    print("Error Code:", res.status_code)


start, num = 1, 0
for index in range(1, 10):
    naver_open_api_shopping_url = (
        "https://openapi.naver.com/v1/search/shop.json?query=갤럭시노트&display=100&start="
        + str(start)
    )

    header_params = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    res = requests.get(naver_open_api_shopping_url, headers=header_params)
    if res.status_code == 200:
        json_data = res.json()
        for item in json_data["items"]:
            num += 1
            print(num, item["title"], item["link"], item["lprice"], item["hprice"])
    else:
        print("Error Code:", res.status_code)

    start += 100
