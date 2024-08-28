import os

import news_thepaper
import news_tongyi

MAX_NEWS_NUMER_PER_AUDIO = 8
def main():
    news_file_name = "news.txt"
    if os.path.exists(news_file_name):
        os.remove(news_file_name)
    for index, prompt in enumerate(news_thepaper.get_prompt()):
        if index > MAX_NEWS_NUMER_PER_AUDIO:
            break;
        print(prompt)
        news_tongyi.generate_news(prompt,news_file_name)


if __name__ == "__main__":
    main()
