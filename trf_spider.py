from scrapy import Spider, FormRequest
from scrapy.shell import inspect_response


class TRFSpider(Spider):
    custom_settings = {
        "COOKIES_DEBUG": True,
        "ROBOTSTXT_ENABLED": False,
        "HTTPERROR_ALLOW_ALL": True,
        "RETRY_ENABLED": False,
    }

    name = "trf-spider"
    trf_url = (
        "https://processual.trf1.jus.br/consultaProcessual/nomeParte.php?secao=TRF1"
    )
    start_urls = [trf_url]

    def parse(self, response):

        data = {
            "nome": "Pedro Paulo Silva",
            "secao": "TRF1",
            "pg": "2",
            "enviar": "Pesquisar",
            "g-recaptcha-response": "",
            "nmToken": "nomeParte",
        }

        yield FormRequest(
            url=self.trf_url,
            formdata=data,
            method="POST",
            callback=self.parse_results,
        )

    def parse_results(self, response):
        inspect_response(response, self)
