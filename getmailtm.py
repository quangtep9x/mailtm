    
def reg_mail(self):
    letters = string.ascii_lowercase
    address = ''.join(random.choice(letters) for i in range(7)) + str(random.randint(12321, 982736)) + '@bugfoo.com'
    password = '123456'

    headers = {
            'authority': 'api.mail.tm',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/json',
            'origin': 'https://mail.tm',
            'referer': 'https://mail.tm/',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    json_data = {
            'address': address,
            'password': password,
    }
    while True:
            response = requests.post('https://api.mail.tm/accounts',
                                    headers=headers, json=json_data)

            # print(response.json())
            g = response.json()
            if g['@context'] == '/contexts/Account':
                    print(f'Tạo mail: {address} - thành công!')
                    break
            else:
                    print('Mail đã sử  dụng')
                    time.sleep(5)

    return address, password


def gettoken(self,account):
    headers = {
            'authority': 'api.mail.tm',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/json',
            'origin': 'https://mail.tm',
            'referer': 'https://mail.tm/',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    json_data = {
            'address': account[0],
            'password': account[1],
    }

    response = requests.post('https://api.mail.tm/token',
                            headers=headers, json=json_data)

    token = response.json()['token']
    return token


def getcode(self,token):
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
