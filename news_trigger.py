import os
import time
import news_thepaper
import news_tencent
import news_tongyi
import news_kimi
from news_util import get_output_name, get_news_dir

MAX_NEWS_NUMER_PER_AUDIO = 20
def main():
    news_file_name = f"{get_news_dir()}/{get_output_name()}.txt"
    if os.path.exists(news_file_name):
        os.remove(news_file_name)
    for index, prompt in enumerate(news_tencent.get_prompt()):
        if index > MAX_NEWS_NUMER_PER_AUDIO:
            break;
        print(prompt)
        news_kimi.generate_news(prompt,news_file_name)
        time.sleep(60)


if __name__ == "__main__":
    main()
