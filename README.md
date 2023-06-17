## Plan Travel with OpenAI

Planeje suas viagens com ajuda do ChatGPT informando apenas o período e o destino da sua viagem.

### Como rodar o projeto:
- clone o repositório:
```console
git clone git@github.com:matheusfs99/plan-travel-openai.git
```

- acesse o repositório do projeto:
```console
cd plan-travel-openai
```

- instale as dependências do projeto:
```console
pip install -r requirements.txt
```

- crie um arquivo **.env** e adicione a variável de ambiente **OPENAI_API_KEY** com a sua APIkey do OpenAI

- setar o arquivo do app flask:
```console
export FLASK_APP=index.py
```

- execute o projeto:
```console
flask run
```

- fazer requisição:
```console
curl --request POST \
  --url http://127.0.0.1:5000/plan \
  --data '{
	"start_date": "<data_inicial>",
	"end_date": "<data_final>",
	"destination": "<destino>"
}'
```