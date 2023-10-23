import feedparser
import os

test_env = os.environ.get("TEST_ENV", "✏️ Latest Blog Post")

print(f"test_env = {test_env}")

mukjjangBlogUrlRss = "https://mukjjang.tistory.com/rss"
rss_feed = feedparser.parse(mukjjangBlogUrlRss)

MAX_POST_NUM = 5

latest_blog_post_list = ""

MAX_POST_NUM = 5

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=250&section=header&text=I'm%20녜정&fontSize=85)

## 🚀 About Me

- 안녕하세요! 백엔드 개발자 윤혜정 입니다.
- [블로그](https://mukjjang.tistory.com/), [깃허브](https://github.com/yoonheyjung) 등 보다 나은 소통을 위해 기록을 시작했습니다.
- 쉽고 간단한 코드가 유지보수하기 좋고 누구든지 이해할 수 있는, 좋은 코드라고 생각합니다.

</br>

## 🚧 TECH STACK 🚧

<div style="display:flex; flex-direction:column; align-items:flex-start;">

### 💡 Used as the main

<div>
  <img src='https://img.shields.io/badge/node-518d7d?style=flat&logo=Node.js&logoColor=white'>
  <img src='https://img.shields.io/badge/Express-f8ca8f?style=flat&logo=express&logoColor=white'>
  <img src='https://img.shields.io/badge/JavaScript-ffcc00?style=flat&logo=javascript&logoColor=white'>
  <img src='https://img.shields.io/badge/php-04558A?style=flat&logo=php&logoColor=white'>
  <img src="https://img.shields.io/badge/MySql-586fab?style=flat&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/redis-d65353?style=flat&logo=redis&logoColor=white"/>
</div>

### 💡 Used as least once

<div>
  <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat&logo=amazon aws&logoColor=white"> 
  <img src="https://img.shields.io/badge/Docker-4465c0?style=flat&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/MongoDB-21aca9?style=flat&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vue-01B257?style=flat&logo=vue.js&logoColor=white"/>
  <img src="https://img.shields.io/badge/html-fe8d6f?style=flat&logo=html5&logoColor=white"/>
</div>
</br>
</br>

</div>
<!-- [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=yoonheyjung&theme=tokyonight&repo=badwords-ko)](https://github.com/yoonheyjung/badwords-ko) -->

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=yoonheyjung&theme=onedark&layout=compact)](https://github.com/yoonheyjung/badwords-ko)

![Heyjung's GitHub stats](https://github-readme-stats.vercel.app/api?username=yoonheyjung&show_icons=true&theme=noctis_minimus)

## ✏️ Latest Blog Post

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)