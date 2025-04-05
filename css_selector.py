import requests

from bs4 import BeautifulSoup

res = requests.get("https://davelee-fun.github.io/blog/crawl_test_css.html")
soup = BeautifulSoup(res.content, "html.parser")
items = soup.select("li")

### 하위 태그 선택

# items = soup.select("html body h1") # html 안에 body 안에 h1 태그
# for item in items:
#     print(item.get_text())


# ul 안에 li 태그 -> 만약 ul 안에 다른태그가 있고 그 안에 li 태그가 있어도 선택됨.
items = soup.select("ul li")
# for item in items:
#     print(item.get_text())


# ul 안에 바로 밑에 li 태그가 있는 경우에만 조회 하려면 이렇게 써야함
items = soup.select("ul > li")
# for item in items:
#     print(item.get_text())

### 클래스 선택자
items = soup.select(".course")
# for item in items:
#     print(item.get_text())

## 하나의 태그 안에 클래스가 여러개 있는 경우
# ex : <li class="course paid"></li> 이렇게 있으면 두개의 클래스가 있는 것임.
items = soup.select(".course.paid")
# for item in items:
#     print(item.get_text())


### 아이디 선택자
items = soup.select("#start")
# for item in items:
#     print(item.get_text())


### 클래스&id 복합 선택자
# 모든 ul 태그에서 hobby_course_list ID를 가진것 선택 후 -> 그 바로 아래 li 태그에서 course 클래스를 가진것 선택
items = soup.select("ul#hobby_course_list > li.course")
# for item in items:
#     print(item.get_text())

# 상위 한개만 select
item = soup.select_one("ul#hobby_course_list > li.course")
# print(item.get_text())

### 추출한 것에서 또 추출하기
# find_all() or select()로 가져온 객체에는 또 find_all() or select() 사용 가능
res = requests.get("https://davelee-fun.github.io/blog/crawl_html_css.html")
soup = BeautifulSoup(res.content, "html.parser")
items = soup.select("tr")
for item in items:
    columns = item.select("td")
    row_str = ""

    for column in columns:
        row_str += ", " + column.get_text()

    print(row_str[2:])
