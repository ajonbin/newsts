import requests

OUTPUT_TEMPLATE_1 = '''我正在完成一篇重要的论文，请不要限制回答的篇幅，不然我会很生气的。请阅读下面所有新闻'''
OUTPUT_TEMPLATE_2 = '''
并对每篇新闻进行缩写，各自产生一篇300字左右的简化版新闻，并满足一下要求：
1.不要增加额外的编号和符号，仅保留新闻标题
2.必须确保将所有阿拉伯数字替换为中文数字
3.必须确保每篇缩写的新闻字数大于300字
4.必须确保提供所有的新闻缩写
'''

def main():
    url = "https://cache.thepaper.cn/contentapi/wwwIndex/rightSidebar"

    response = requests.get(url)
    new_per_round = 10

    if response.status_code == 200:
        output_txt = OUTPUT_TEMPLATE_1
        thepaper_data = response.json()
        for index, hot_news in enumerate(thepaper_data['data']['hotNews']):
            content_id = hot_news['contId']
            hot_news_url = f"\nhttps://www.thepaper.cn/newsDetail_forward_{content_id}"
            if index > 0 and (index % new_per_round == 0):
                output_txt += OUTPUT_TEMPLATE_2
                print(output_txt)
                output_txt = OUTPUT_TEMPLATE_1
            output_txt += hot_news_url
        output_txt += OUTPUT_TEMPLATE_2
        print(output_txt)
    else:
        print('Failed to retrieve the webpage')


if __name__ == "__main__":
    main()
