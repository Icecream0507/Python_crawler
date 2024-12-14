import requests

url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": "1",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

head = {

    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

}

resp = requests.get(url, params= param, headers=head)



print(resp.request.headers)

# with open("douban.html", mode = "w", encoding='utf-8') as f:
#     f.write()

print(resp.text)

resp.close()


