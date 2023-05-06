import requests

cookies = {
    'PHPSESSID': '',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=xxxxxxxxxxxxxx',
    'Origin': 'http://3wifi.stascorp.com',
    'Pragma': 'no-cache',
    'Referer': 'http://3wifi.stascorp.com/find?p=4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'a': 'find',
}

data = {
    'bssid': '',
    'essid': '◯',
    'key': '◯',
    'wps': '◯',
    'page': '1',
}

response = requests.post(
    'http://3wifi.stascorp.com/3wifi.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
