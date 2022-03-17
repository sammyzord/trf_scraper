import requests

cookies = {
    "TRF1style": "default",
    "PHPSESSID": "ioq92aq55enu0mai3ofcicr3t6",
    "Qr1B4j3mrGeNWFYCqhmqt3LQGa1No9UGQ-77i7OniCmqfjjjIN6GvGu4swo_": "v1vtE+JQSDwNZ",
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": (
        "https://processual.trf1.jus.br/consultaProcessual/nomeParte.php?secao=TRF1"
    ),
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://processual.trf1.jus.br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

params = (("secao", "TRF1"),)

data = {
    "nome": "Pedro Paulo Silva",
    "secao": "TRF1",
    "pg": "2",
    "enviar": "Pesquisar",
    "g-recaptcha-response": "",
    "nmToken": "nomeParte",
}

response = requests.post(
    "https://processual.trf1.jus.br/consultaProcessual/parte/listar.php",
    headers=headers,
    params=params,
    cookies=cookies,
    data=data,
)

filename = "test.txt"
chunk_size = 100
with open(filename, "wb") as fd:
    for chunk in response.iter_content(chunk_size):
        fd.write(chunk)
