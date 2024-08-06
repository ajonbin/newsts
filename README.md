# Prompt #

请获取2024巴黎奥运会的五条最新动态，按照新闻热度排序，并形成摘要，每条新闻的摘要要求不少于500字。

请将上述摘要中的阿拉伯数字用中文字表示

----

请阅读下面所有新闻
https://www.thepaper.cn/newsDetail_forward_28304996
https://www.thepaper.cn/newsDetail_forward_28307332
https://www.thepaper.cn/newsDetail_forward_28311328
并对每篇新闻进行缩写，各自产生一篇500字左右的简化版新闻，并满足一下要求：
不要增加额外的编号，仅保留新闻标题
将所有阿拉伯数字替换为中文数字

# Usage #

~~~
$ python newsts.py --help
usage: newsts.py [-h] [-f NEWS_FILE]

News To Speech

options:
  -h, --help            show this help message and exit
  -f NEWS_FILE, --news-file NEWS_FILE
                        Text file include news lines
~~~
