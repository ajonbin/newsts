from openai import OpenAI

MOONSHOT_API_KEY = "sk-0KvkBSIz8k0kp60aRNQ4hmKMPJwpeS5ajRUjWrSlninoPkjd"

KIMI_SYSTEM_CONTENT = "你是个新闻收集者，主要收集当下网络中热度最高的新闻，并整理新闻摘要。"
KIMI_USER_GET_NEWS = "请获取2024巴黎奥运会的五条最新动态，按照新闻热度排序，并形成摘要，每条新闻的摘要要求不少于500字。"
KIMI_USER_MODIFY_NUMBER = "请将上述摘要中的阿拉伯数字用中文字表示，数字 0 用中文 零 表示。"

client = OpenAI(
    api_key = f"{MOONSHOT_API_KEY}",
    base_url = "https://api.moonshot.cn/v1",
)

history = [
    {"role": "system", "content": f"{KIMI_SYSTEM_CONTENT}"}]

def chat(query, history):
    history.append({
        "role": "user",
        "content": query
    })
    completion = client.chat.completions.create(
        model="moonshot-v1-32k",
        messages=history,
        temperature=0.3,
    )
    result = completion.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": result
    })
    return result

print(chat(f"{KIMI_USER_GET_NEWS}", history))
print(chat(f"{KIMI_USER_MODIFY_NUMBER}", history))
