# 네이버 Papago NMT API 예제
import urllib.request
import Using_class_for_papago as UCFP


client_id = "??"
client_secret = "??"

User = UCFP.UserInfo(client_id, client_secret)

encText = urllib.parse.quote("진짜 이거 되는거야?")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", User.getId)
request.add_header("X-Naver-Client-Secret", User.getPasswd)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)