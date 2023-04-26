import json , time, random,string , requests



def gettoken(account):
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

u = gettoken(account_mail)
