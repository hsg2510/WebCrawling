import requests

from bs4 import BeautifulSoup

# res = requests.get("http://v.media.daum.net/v/20170615203441266")
# soup = BeautifulSoup(res.content, "html.parser")
html = """
<html> 
    <body> 
        <h1 id='title'>[1]크롤링이란?</h1> 
        <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> 
        <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> 
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# find는 조건에 맞는 데이터를 찾으면 이후 데이터는 찾지않고 그냥 첫번째 결과를 return 해버림.
mydata = soup.find("p", class_="cssstyle")
# mydata = soup.find("p", "cssstyle") 이렇게 써도 됌.
mydata2 = soup.find("p", attrs={"align": "center"})
mydata3 = soup.find("p", attrs={"id": "body", "align": "center"})
mydata4 = soup.find(id="body")
# print(mydata.get_text())
# print(mydata.string)
# print(mydata2.get_text())
# print(mydata3.get_text())
# print(mydata4.get_text())

# find_all은 조건에 맞는 데이터를 모두 찾아서 리스트로 return 해줌.
mydata5 = soup.find_all("p")
for item in mydata5:
    print(item.get_text())


res = requests.get("https://davelee-fun.github.io/blog/crawl_test")
soup = BeautifulSoup(res.content, "html.parser")

mydata6 = soup.find("ul", id="hobby_course_list")
mydata7 = mydata6.find_all("li", "course")
for item in mydata7:
    print(item.get_text())


mydata8 = soup.find("ul", id="dev_course_list")
mydata9 = mydata8.find_all("li", "course")
for item in mydata9:
    print(item.get_text())

# for index, title in enumerate(mydata9):
#     print(str(index + 1) + ".", title.get_text().split("-")[-1].split("[")[0].strip())


### 여러 페이지를 한번에 크롤링

for page_num in range(10):
    if page_num == 0:
        res = requests.get("https://davelee-fun.github.io/")
    else:
        res = requests.get("https://davelee-fun.github.io/page" + str(page_num + 1))
    soup = BeautifulSoup(res.content, "html.parser")

    data = soup.select("h4.card-text")
    for item in data:
        print(item.get_text().strip())
