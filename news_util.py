import datetime

def get_output_name()-> str:
      """Gets the current time as a string in the format 'xxxx year xx month xx day AM or PM'."""
      now = datetime.datetime.now()
      #am_pm = "晨间新闻" if now.hour < 12 else "晚间新闻"
      #return f"{now.year}年{now.month}月{now.day}日{am_pm}"
      return f"{now.year}年{now.month}月{now.day}日热点新闻"

def get_voice_pickle_name(idx) -> str:
    now = datetime.datetime.now()
    return f"./voices/{now.year}年{now.month}月{now.day}_{idx}.pkl"

def get_news_dir() -> str:
    return "news"
