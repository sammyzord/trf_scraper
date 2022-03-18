import re
import csv
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
        proc_number = response.css(
            "div#aba-processo > table > tbody > tr > td::text"
        ).get()

        proc_number = re.sub("[^0-9]", "", proc_number)

        self.parse_processo(response, proc_number)
        self.parse_distribuicao(response, proc_number)
        self.parse_movimentacao(response, proc_number)
        self.parse_peticao(response, proc_number)

    def parse_processo(self, response, proc_number):
        file = open(f"output/processo/processo_{proc_number}.csv", "w")
        writer = csv.writer(file)

        for item in response.css("div#aba-processo > table > tbody > tr"):
            title = item.css("th::text").get()

            if title is not None:
                title = title.strip()

            content = item.css("td::text").get()

            if content is not None:
                content = content.strip()

            writer.writerow([title, content])

        file.close()

    def parse_distribuicao(self, response, proc_number):
        file = open(f"output/distribuicao/distribuicao_{proc_number}.csv", "w")
        writer = csv.writer(file)

        for table in response.css("div#aba-distribuicao > table"):
            headers = []
            for header in table.css("thead > tr > th::text"):
                headers.append(header.get())

            writer.writerow(headers)

            content = []
            for item in table.css("tbody > tr > td"):
                x = item.css("::text").get()
                if x:
                    content.append(x)
                else:
                    content.append("Não encontrado")

            rows = [
                content[x : x + len(headers)]
                for x in range(0, len(content), len(headers))
            ]

            writer.writerows(rows)

        file.close()

    def parse_movimentacao(self, response, proc_number):
        file = open(f"output/movimentacao/movimentacao_{proc_number}.csv", "w")
        writer = csv.writer(file)

        for table in response.css("div#aba-movimentacao > table"):
            headers = []
            for header in table.css("thead > tr > th::text"):
                headers.append(header.get())

            writer.writerow(headers)

            content = []
            for item in table.css("tbody > tr > td"):
                x = item.css("::text").get()
                if x:
                    content.append(x)
                else:
                    content.append("Não encontrado")

            rows = [
                content[x : x + len(headers)]
                for x in range(0, len(content), len(headers))
            ]

            writer.writerows(rows)

        file.close()

    def parse_peticao(self, response, proc_number):
        file = open(f"output/peticao/peticao_{proc_number}.csv", "w")
        writer = csv.writer(file)

        for table in response.css("div#aba-peticoes > table"):
            headers = []
            for header in table.css("thead > tr > th::text"):
                headers.append(header.get())

            writer.writerow(headers)

            content = []
            for item in table.css("tbody > tr > td"):
                x = item.css("::text").get()
                if x:
                    content.append(x)
                else:
                    content.append("Não encontrado")

            rows = [
                content[x : x + len(headers)]
                for x in range(0, len(content), len(headers))
            ]

            writer.writerows(rows)

        file.close()
