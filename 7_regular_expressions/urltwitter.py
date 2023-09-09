import re

url = input('URL: ').strip()

'''
# Método de string replace, primer argumento qupe quieres reemplazar, segundo con qupe lo quieres reemplazar
username = url.replace('https://twitter.com/', '')
'''
'''
# función re,sub que es más específica que la built in .replace()
# con ésta función, no podemos usar el formato condicional
username = re.sub(r'^(https?://)?(www\.)?twitter\.com/', "", url):
print(f'Username: {username}')
'''

if matches := re.search(r'^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$', url, re.IGNORECASE):
    # escribimos group(3), ya que el username es el tercer grupo encerrado por paréntesis en nuestro pattern
    print(f'Username: {matches.group(1)}')