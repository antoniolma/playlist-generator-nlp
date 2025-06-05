# Projeto - Gerador de Playlists

Insper 2025.1

**Eletiva**: Natural Language Processing (NLP).

**Grupo**:
- Antonio Lucas Michelon de Almeida
- Pedro Nery Affonso dos Santos
- Rafael Gordon Paves

## Descrição do Projeto

São geradas 3 playlists de músicas a partir de um pedido do usuário, cada uma com 10 músicas e geradas de uma maneira diferente. Queríamos saber qual seria a melhor estratégia considerando os dados utilizados (veja ![tratamento dos dados](db.ipynb)) e o tempo gasto.

Métodos utilizados:
- Requisição simples: uma requisição única para o Gemini
- Agentes: um agente especialista em construção de playlists e um especialista em opinar conversando
- Modelo BERT

Após isso, foi feito uma validação de qual seria o melhor modelo pedindo para várias pessoas escolherem qual playlist elas mais gostaram. Veja os resultados em ![pontuação](pontuacao.md)

## Como rodar

Para utilizar o código deste repositório, siga as instruções a seguir:

Crie um ambiente virtual do Python:

``` shell
python3 -m venv env
```

Ative o ambiente virtual:

``` shell
# No Windows
env\Scripts\activate

# No Linux/MacOS
source venv/bin/activate
```

Instale as dependências com:

``` shell
python3 -m pip install -r requirements.txt --upgrade
```

`db.ipynb`:
- Baixar o Dataset original do Kaggle (link: [kaggle.com](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information/data?select=song_lyrics.csv))
- Rodar os códigos necessários para poder ter acesso ao banco de dados filtrado de acordo com a necessidade do projeto.

\
``main.ipynb:``
- Passo 1
- Passo 2

## Referências

[Referência 1](https://github.com/alexdjulin/spotify-playlist-generator)

[Referência 2](https://github.com/daytonaio/sample-python-ai-playlist-generator)
