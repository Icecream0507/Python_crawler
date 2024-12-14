import re
import requests
import pandas as pd
import os

path = "./曲谱合集"




url = "https://mp.weixin.qq.com/s/xLBtQCLyoYQ3HwaU8p87hQ"

head = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers = head)
 

originhtml = resp.text


obj1 = re.compile(r'<a target="_blank" href=(?P<urls>.*?) '
                  r'textvalue="(?P<names>.*?)" linktype="text" imgurl="" .*?</a>', re.S)

obj2 = re.compile(r'data-ratio="1.\d+" data-s="300,640" data-src="(?P<photo_url>.*?)" data-type="(?P<types>.*?)" data-w="\d\d\d\d" style=""  /></p>', re.S)


#<p style="text-align: center;"><img class="rich_pages js_insertlocalimg" data-ratio="1.4146772767462423" data-s="300,640" data-src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/sL5v5AmZWvf9SSVCxKZ9k5FTqBR2O3opZ0X3yaTsTmlOQxicyHPEmQb2QLceChS0PGyQPXiaFoyxicfXtvibv0asUQ/640?wx_fmt=jpeg" data-type="jpeg" data-w="1131" style=""  /></p>

name_obj = re.compile(r'<meta property="twitter:title" content=".*?《(?P<name>.*?)》.*?"')

type_obj = re.compile(r'wx_fmt=(?P<type>.*?)&')


lst = obj1.finditer(originhtml)



mycookies = {
    "cookie": "RK=cVM8wlfD6i; ptcz=b778709bac7279ef72aad6253b3887a1fee3e7a96c1ddc10689b6bf40528e05c; _qimei_uuid42=188010c1e121008e5c5fb9e4163e8b91080d5c30f5; pac_uid=0_aXEkZmp3MD8dG; suid=user_0_aXEkZmp3MD8dG; _qimei_q36=; _qimei_h38=19c544dc5c5fb9e4163e8b9102000008718801; eas_sid=h1s7Y283s2g7y9O8S6N0a5D6G1; _uetvid=ab13920056f511efa279a13386491bfb; pgv_pvid=5210999240; mm_lang=zh_CN; _qimei_fingerprint=8d5754faa58fd468c58cd6bdb1896be4; rewardsn=; wxtokenkey=777; poc_sid=HGM-XWejczn-0qlEQ31_xwGZNNd8REyndHd08n2I"
}


n = 0


e_num = 0

for _ in range(400):
        next(lst, None)

for i in lst:
    # //sorted_i = {i.groupdict()[k] for k in fieldnames}

    

    sonurl = i.group('urls').strip("\"")

    sonresp = requests.get(sonurl, headers = head, cookies= mycookies)

    sonhtml = sonresp.text

    photoiter = obj2.finditer(sonhtml)

    with open('test.html', 'w', encoding='utf-8') as t:
        t.write(sonhtml)

    # print(sonhtml)

    searchres = name_obj.search(sonhtml)

    if(searchres == None):
        continue

    subpath = name_obj.search(sonhtml).group('name')

    print("name:", "《", subpath, "》")

    finalpath = path + '/' + subpath

    index = 1

    if os.path.exists(finalpath) == 0 :
        try:
            os.makedirs(finalpath)
        except OSError:
            subpath = subpath.strip(subpath[-1])
            finalpath = path + '/' + subpath
            os.makedirs(finalpath)

    for j in photoiter:

        purl = j.group('photo_url')

        presp = requests.get(purl, headers = head, cookies= mycookies)

        print(purl)

        ptype = j.group('types')

        filename = finalpath + '/' + f'{subpath}_{index}.{ptype}'

        print(presp.status_code)


        try:
            with open(filename, 'wb') as f:
                f.write(presp.content)
        except FileNotFoundError:
            continue

        print("grasping...", f"index = {index}")

        index += 1

        

    n += 1

    print("completed:", n/6.29, "%...")

print(n)


# df = pd.read_csv('guitar.csv')

# df.to_excel('exguitar.xlsx', index=False)