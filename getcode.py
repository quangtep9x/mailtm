import json , time, random,string , requests



def getcode(token):
      while True:
              auth_headers = {
                      "accept": "application/ld+json",
                      "Content-Type": "application/json",
                      "Authorization": "Bearer {}".format(token)
              }

              r = requests.get("https://api.mail.tm/messages?page=1",headers=auth_headers)


              getms = r.json()
              if getms['hydra:member'] == []:
                      print('Chưa về mã')
                      time.sleep(2)
                      # print(getms)
              else:
                      print('Đã có mã!')
                      break

      message = []

      for message_data in getms['hydra:member']:
              auth_headers = {
              "accept": "application/ld+json",
              "Content-Type": "application/json",
              "Authorization": "Bearer {}".format(token)
              }

              r = requests.get(f"https://api.mail.tm/messages/{message_data['id']}", headers=auth_headers)
              full_message_json = r.json()
              text = full_message_json["text"]
              html = full_message_json["html"]
              #print('html', html)
              # print(html[0])
              try:
                      code = html[0].split('solid #ccc;">FB-')[1].split('</td>')[0]
                      print('code: ', code)
                      return code
                      break
              except:
                      pass
getcode(tokenma)
