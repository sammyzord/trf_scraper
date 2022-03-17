from scrapy import Spider, FormRequest, Request

# from scrapy.shell import inspect_response


class TRFSpider(Spider):
    custom_settings = {
        "ROBOTSTXT_ENABLED": False,
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

        yield FormRequest.from_response(
            response, formnumber=1, formdata=data, callback=self.parse_list
        )

    def parse_list(self, response):
        for href in response.css("td > a.listar-processo::attr(href)"):
            url = response.urljoin(href.get())
            yield Request(url, callback=self.parse_inside_list)

    def parse_inside_list(self, response):
        for href in response.css("td > a::attr(href)"):
            url = response.urljoin(href.get())
            yield Request(url, callback=self.parse_results)

    def parse_results(self, response):
        # self.parse_processo(response)
        self.parse_distribuicao(response)

    def parse_processo(self, response):
        for item in response.css("div#aba-processo > table > tbody > tr"):
            title = item.css("th::text").get()

            if title is not None:
                title = title.strip()

            content = item.css("td::text").get()

            if content is not None:
                content = content.strip()

            print(title, content)

    def parse_distribuicao(self, response):
        for table in response.css("div#aba-distribuicao > table"):
            print("\n\nHeader")
            for header in table.css("thead > tr > th::text"):
                print(header.get())

            print("\nContent")
            for item in table.css("tbody > tr > td::text"):
                print(item.get())

    def parse_partes(self, response):
        pass

    def parse_movimentacao(self, response):
        pass

    def parse_peticoes(self, response):
        pass
