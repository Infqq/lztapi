import requests


class lztapi:
        def __init__(self, token) -> str:
                self._token = token

        def users_find(self, username='Lanskoy'):
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                r = requests.get(f"https://lolz.guru/api/index.php?users/find&username={username}&oauth_token={self._token}", headers=headers)
                return r.text
