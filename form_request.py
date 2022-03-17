import requests

headers = {"Cache-Control": "no-cache"}

params = (("secao", "TRF1"),)

data = {
    "nome": "Pedro Paulo Silva",
    "secao": "TRF1",
    "pg": "2",
    "enviar": "Pesquisar",
}

response = requests.post(
    "https://processual.trf1.jus.br/consultaProcessual/parte/listar.php",
    headers=headers,
    params=params,
    data=data,
)

filename = "test.txt"
chunk_size = 100

with open(filename, "wb") as fd:
    for chunk in response.iter_content(chunk_size):
        fd.write(chunk)
