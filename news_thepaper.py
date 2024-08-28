import requests

OUTPUT_TEMPLATE_1 = '''请阅读下面链接'''
OUTPUT_TEMPLATE_2 = '''。并对这篇新闻进行摘要，字数要求不超过200字。把数字改成中文数字。不要添加任何其他信息。'''

def get_prompt():
    url = "https://cache.thepaper.cn/contentapi/wwwIndex/rightSidebar"

    response = requests.get(url)

    if response.status_code == 200:
        thepaper_data = response.json()
        for index, hot_news in enumerate(thepaper_data['data']['hotNews']):
            content_id = hot_news['contId']
            hot_news_url = f" https://www.thepaper.cn/newsDetail_forward_{content_id} "
            prompt = f"{OUTPUT_TEMPLATE_1}{hot_news_url}{OUTPUT_TEMPLATE_2}"
            yield prompt
    else:
        print('Failed to retrieve s webpage')

def main():
    for prompt in get_prompt():
        print(prompt)

if __name__ == "__main__":
    main()
