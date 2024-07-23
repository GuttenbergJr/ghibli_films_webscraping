# Melhores filmes do Estúdio Ghibli classificados pelo Rotten Tomatoes

<p>Aplicativo de web scraping desenvolvido para extrair informações diretamente da página do <a href='https://editorial.rottentomatoes.com/guide/all-studio-ghibli-movies-ranked-by-tomatometer/'>Rotten Tomatoes</a>. Utilizando técnicas de scraping, o aplicativo coleta dados relevantes sobre os filmes do Studio Ghibli, como ranking, títulos e ano de lançamento.</p>

## Como utilizar
1. Clone o Repositório <br>
Clone o repositório utilizando o seguinte comando:
git clone https://github.com/GuttenbergJr/ghibli_films_webscraping.git 

2. Instale as Dependências <br>
Certifique-se de ter o Python e o Scrapy instalados. Caso o Scrapy não esteja instalado basta utilizar o pip: ```pip install scrapy```

3. Execute o Spider <br>
Para coletar os dados dos filmes do Studio Ghibli, execute o spider usando o Scrapy: ```scrapy crawl films -O filmes_ghibli.csv ``` <br>
Isso iniciará o spider ghibli_spider, que vai extrair os dados dos filmes do Studio Ghibli e salvá-los no arquivo filmes_ghibli.csv no diretório atual.

4. Explore os Dados Coletados <br>
Após a execução bem-sucedida do spider, você pode explorar os dados coletados no arquivo filmes_ghibli.csv Você pode usar esses dados para análise, visualização ou qualquer outro propósito desejado.


Sinta-se à vontade para abrir issues e pull requests para melhorias e correções!

## Tecnologias Utilizadas
<ul>
    <li> Python </li>
    <li> Scrapy (framework) </li>
<ul>