import string
import time
import requests , random


def reg_mail():
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
        return address       
reg_mail()
