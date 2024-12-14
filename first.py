from urllib.request import urlopen
import chardet



url = "http://www.baidu.com"
resp = urlopen(url)

content = resp.read()

encoding = chardet.detect(content)["encoding"]

decoded_data = content.decode(encoding)

print()

with open("mybaidu.html", mode = "w", encoding='utf-8') as f:
    f.write(decoded_data)

print("ez")

resp.close()

