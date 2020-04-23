import requests


def buscar_avatar(usuario):
    """
    Busca el avatar de un usuario en Github
    :param usuario: str con el nombre de usuario en Github
    :return: str con el link del avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
