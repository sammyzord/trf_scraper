import requests

cookies = {
    "PHPSESSID": "65pn76ohrvpsdt12c1km6dr6v5",
    "Qr1B4j3mrGeNWFYCqhmqt3LQGa1No9UGQ-77i7OniCmqfjjjIN6GvGu4swo_": "v1XNM+JQSDwQw",
    "TRF1style": "default",
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
    ),
    "Accept": "text/html, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": (
        "https://processual.trf1.jus.br/consultaProcessual/processo.php?"
        "proc=229089119974010000&secao=TRF1"
        "&nome=PEDRO%20PAULO%20SILVA&mostrarBaixados=N"
    ),
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

params = (
    ("proc", "229089119974010000"),
    ("secao", "TRF1"),
    ("origem", "juris"),
)

response = requests.get(
    "https://processual.trf1.jus.br/consultaProcessual/arquivo/partes.php",
    headers=headers,
    params=params,
    cookies=cookies,
)
