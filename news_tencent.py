import requests

OUTPUT_TEMPLATE_1 = '''请阅读下面链接'''
OUTPUT_TEMPLATE_2 = '''并对这篇新闻进行摘要，字数要求不超过200字。注意，请把其中的数字改成中文数字，包括日期时间和百分比。不要添加任何其他信息。'''

def get_prompt():
    url = "https://r.inews.qq.com/gw/event/hot_ranking_list?page_size=50"

    response = requests.get(url)

    if response.status_code == 200:
        tencent_data = response.json()
        for index, hot_news in enumerate(tencent_data['idlist'][0]['newslist']):
            if hot_news['articletype'] == "0": # Text Type
                hot_news_url = f" {hot_news['url']} "
                prompt = f"{OUTPUT_TEMPLATE_1}{hot_news_url}{OUTPUT_TEMPLATE_2}"
                yield prompt
    else:
        print('Failed to retrieve s webpage')

def main():
    for prompt in get_prompt():
        print(prompt)

if __name__ == "__main__":
    main()
