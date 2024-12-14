import requests

url = "https://fanyi.baidu.com/sug"

s = input("Input:")

kw = {
    "kw": s
}

resp = requests.post(url, data = kw)

with open("translate.json", mode='w', encoding='utf-8') as f:
    f.write(resp.text)

print(resp.json())#将服务器内容按json处理 => dict

resp.close()
