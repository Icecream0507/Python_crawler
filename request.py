
import requests

url = 'https://www.sogou.com/web?query=周杰伦'



dics = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=dics)#小小反爬虫


print(resp)


print(resp.text) #页面源代码


with open("baidu_jay.html", mode='w', encoding='utf-8') as f:
    f.write(resp.text)

print('Ez')

resp.close()

