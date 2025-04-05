import json

json_data = """
{
    "lastBuildDate": "Tue, 01 Apr 2025 00:22:13 +0900",
    "total": 14554,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "<b>펩트론</b>, 플랫폼 사업 다각화···ADC 카드 만지작",
            "originallink": "https://www.sisajournal-e.com/news/articleView.html?idxno=410645",
            "link": "https://www.sisajournal-e.com/news/articleView.html?idxno=410645",
            "description": "<b>펩트론</b>이 플랫폼 기술 사업 분야를 넓혀 수익 구조를 다각화하겠다는 목표를 세웠다. 그중 차세대 항암... 31일 업계에 따르면 <b>펩트론</b>이 ADC 효능을 극대화할 수 있는 차세대 펩타이드 플랫폼 기술 'IEP' 개발을... ",
            "pubDate": "Mon, 31 Mar 2025 16:18:00 +0900"
        },
        {
            "title": "<b>펩트론</b> &quot;ADC 치료 한계 극복할 IEP 플랫폼, 美 AACR서 성과 발표&quot;",
            "originallink": "https://www.job-post.co.kr/news/articleView.html?idxno=138632",
            "link": "https://www.job-post.co.kr/news/articleView.html?idxno=138632",
            "description": "이미지출처 =<b>펩트론</b> 바이오 기업 <b>펩트론</b>이 내달 25일부터 미국 시카고에서 개최되는 '2025 미국암연구학회(AACR)'에서 차세대 펩타이드 플랫폼 기술 'IEP' 연구 성과를 발표한다고 지난 28일 밝혔다. IEP(Intracellular... ",
            "pubDate": "Mon, 31 Mar 2025 18:28:00 +0900"
        },
        {
            "title": "<b>펩트론</b>, AACR서 차세대 ADC 플랫폼 'IEP' 연구 성과 발표",
            "originallink": "https://www.topstarnews.net/news/articleView.html?idxno=15625647",
            "link": "https://www.topstarnews.net/news/articleView.html?idxno=15625647",
            "description": "바이오 기업 <b>펩트론</b>은 오는 4월 25일부터 미국 시카고에서 열리는 미국암연구학회(AACR)에서 항체-약물... <b>펩트론</b>은 이러한 한계를 극복하기 위해 IEP를 ADC에 적용해 암 조직 접근성과 세포 내 약물 유입을 동시에... ",
            "pubDate": "Sun, 30 Mar 2025 08:40:00 +0900"
        },
        {
            "title": "<b>펩트론</b> &quot;미국 암학회서 차세대 ADC 효능증강 기술 소개&quot;",
            "originallink": "https://www.newsis.com/view/NISX20250328_0003117099",
            "link": "https://n.news.naver.com/mnews/article/003/0013148411?sid=102",
            "description": "바이오 기업 <b>펩트론</b>은 내달 25일부터 미국 시카고에서 열리는 미국암연구학회(AACR)에서 항체-약물 접합체... 이를 극복하기 위해 <b>펩트론</b>은 ADC에 IEP를 접목해 암 조직으로 접근성을 높이고 약물의 세포 내 유입을... ",
            "pubDate": "Fri, 28 Mar 2025 10:11:00 +0900"
        },
        {
            "title": "항암 치료 새 시대 열리나?... <b>펩트론</b>, 약효 10배 높인 ADC 기술 공개",
            "originallink": "https://www.pinpointnews.co.kr/news/articleView.html?idxno=332400",
            "link": "https://www.pinpointnews.co.kr/news/articleView.html?idxno=332400",
            "description": "<b>펩트론</b> 주가가 들썩이고 있다. 30일 한국거래소에 따르면 전 거래일 4.68% 올라 9만 1800원에 거래를... 하지만 <b>펩트론</b>의 신기술은 암세포에 대한 선택성을 높여 부작용을 최소화하고 치료 효과를 극대화했다.... ",
            "pubDate": "Sun, 30 Mar 2025 16:48:00 +0900"
        },
        {
            "title": "<b>펩트론</b>, 美 암학회서 펩타이드 기반 ADC 효능 증강 기술 발표",
            "originallink": "https://mdtoday.co.kr/news/view/1065579908697187",
            "link": "https://mdtoday.co.kr/news/view/1065579908697187",
            "description": "▲ <b>펩트론</b> 기업 로고(사진= <b>펩트론</b> 제공) [메디컬투데이=이호빈 기자] <b>펩트론</b>은 오는 4월 미국 시카고에서 열리는 미국암연구학회(AACR) 연례 학회에서 항체-약물 접합체(ADC)의 효능을 극대화할 수 있는 차세대... ",
            "pubDate": "Fri, 28 Mar 2025 18:36:00 +0900"
        },
        {
            "title": "<b>펩트론</b>, 美 암학회서 'IEP' 연구 성과 발표",
            "originallink": "https://www.medipana.com/article/view.php?news_idx=339411&sch_cate=D",
            "link": "https://www.medipana.com/article/view.php?news_idx=339411&sch_cate=D",
            "description": "<b>펩트론</b>(대표이사 최호일)은 다음달 25일부터 미국 시카고에서 열리는 미국암연구학회(American Association... 지난 8년간 <b>펩트론</b>이 독자적으로 개발한 IEP 기술은 MEP(Micro Exon Peptide) 기반의 세포 내재화 촉진... ",
            "pubDate": "Fri, 28 Mar 2025 08:42:00 +0900"
        },
        {
            "title": "<b>펩트론</b>, 차세대 펩타이드 기반 ADC 효능 증강 기술 발표",
            "originallink": "https://weekly.hankooki.com/news/articleView.html?idxno=7107911",
            "link": "https://weekly.hankooki.com/news/articleView.html?idxno=7107911",
            "description": "사진 = <b>펩트론</b> 제공  <b>펩트론</b>은 다음 달 25일부터 미국 시카고에서 열리는 미국암연구학회 연례 학회에서 항체-약물 접합체의 효능을 극대화할 수 있는 차세대 펩타이드 플랫폼 기술인 'IEP'(Internalization-Enhancing Peptide)... ",
            "pubDate": "Fri, 28 Mar 2025 17:10:00 +0900"
        },
        {
            "title": "“암세포 저격 정확도 높인다”…<b>펩트론</b>, 美 암학회서 ADC 신기술 공개",
            "originallink": "https://kormedi.com/?p=2708478",
            "link": "https://n.news.naver.com/mnews/article/296/0000088058?sid=101",
            "description": "바이오 기업 <b>펩트론</b>(대표 최호일)이 항체-약물 접합체(ADC)의 효능을 획기적으로 높일 수 있는 차세대 펩타이드 플랫폼 'IEP(Internalization-Enhancing Peptide)' 기술을 발표한다. <b>펩트론</b>은 내달 25일부터 미국 시카고에서... ",
            "pubDate": "Fri, 28 Mar 2025 10:00:00 +0900"
        },
        {
            "title": "<b>펩트론</b>, 美암연구학회서 ADC효능 증강 펩타이드 기술 발표",
            "originallink": "https://www.e-science.co.kr/news/articleView.html?idxno=103625",
            "link": "https://www.e-science.co.kr/news/articleView.html?idxno=103625",
            "description": "| 이코노미사이언스 신지원 기자 | <b>펩트론</b>은 오는 4월 25일부터 미국 시카고에서 열리는 미국암연구학회... <b>펩트론</b>은 이러한 문제를 극복하기 위해 ADC에 IEP를 접목하여 암 조직으로 접근성을 높이고 약물의 세포... ",
            "pubDate": "Fri, 28 Mar 2025 13:06:00 +0900"
        }
    ]
}
"""

json_data = json.loads(json_data)
print(json_data["items"][0]["title"])
print(json_data["lastBuildDate"])
