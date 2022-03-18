# TRF Scraper

Simple spider made with scrapy used to scrape the contents of the [TRF1](https://processual.trf1.jus.br/consultaProcessual/nomeParte.php?secao=TRF1) website into `.csv` files

## Instructions

The project needs poetry to be installed in your machine, installation instructions [here](https://python-poetry.org/docs/)

After having installed poetry you can install the dependecies with the following command:

```
poetry install
```

After installing all dependencies you can run the project with the following command:

```
poetry run scrapy runspider trf_spider.py
```

## Output

The spider will create 4 `.csv` files for each scraped item, each in its own location on the following folders:

```
./output/distribuicao
./output/movimentacao
./output/peticao
./output/processo
```

The files will be named according to the folder name and process number as following:
`{folder_name}_{process_number}.csv`

If the contents parsed are empty the `.csv` file will be empty as well. This is intended behaviour that probably should be tweaked
but it works well enough 🙃
