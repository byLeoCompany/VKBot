import requests as req
group_key = '0aaa91bab6259cac94db217ce93b9beb11265fcf741d45564a1e6d894f246a429a9fb0a7abd64ebb5c6ed'
group_id = 184350568
v = 5.101

while True:
    params = {'access_token': group_key, 'v': v, 'group_id': group_id}
    r = req.get('https://api.vk.com/method/groups.getLongPollServer', params=params).json()
    key = r['response']['key']
    server = r['response']['server']
    ts = r['response']['ts']
    params = {'access_token': group_key, 'v': v}
    r = req.get(f'{server}?act=a_check&key={key}&ts={ts}&wait=25', params=params).json()
    if r['updates']:
        peer_id = r['updates'][0]['object']['peer_id']
        message = r['updates'][0]['object']['text']
        if message.lower() == 'привет':
            params['peer_id'] = peer_id
            params['message'] = 'Hello user <:'
            params['random_id'] = 0
            r = req.get('https://api.vk.com/method/messages.send', params=params).json()
        elif message.lower() == 'помощь':
            params['peer_id'] = peer_id
            params['message'] = 'помощи нет('
            params['random_id'] = 0
            r = req.get('https://api.vk.com/method/messages.send', params=params).json()
