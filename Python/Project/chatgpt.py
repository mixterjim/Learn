import requests

api_key = "API_KEY"

proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080'
}

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
url = f"https://api.openai.com/v1/chat/completions"

model_engine="gpt-3.5-turbo"
messages_list=[
    {"role": "system", "content": "You are a cute kitten."},
    # {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who are you？"},
    {"role": "assistant", "content": "I am a cute kitten."},
]

cost_total = 0

while True:
    content = input("请输入内容: ")
    if content == "clear":
        messages_list.clear()
        print("清空历史记录")
        continue
    elif content == "exit":
        break
    messages_list.append({"role": "user", "content": content})
    data = {
        "model": model_engine,
        "messages" : messages_list,
        "temperature": 1.0,
        "max_tokens": 50,
    }

    try:
        response = requests.post(url, json=data, headers=headers,timeout=10,proxies=proxies)
        result = response.json()
        messages_list.append(result["choices"][0]["message"])                                    
        print(result["choices"][0]["message"]["content"])
        print("Cost: $" + str(result["usage"]["total_tokens"]/1000*0.002))
        cost_total += result["usage"]["total_tokens"]/1000*0.002
        print("Cost Total: $" + str(cost_total))
        print("Finish: ", result["choices"][0]["finish_reason"])                                                       
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.RequestException as e:
        print(e)
