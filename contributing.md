# Contributing

## Você precisa

- docker
- gcloud

## Tech Stack

- python
- docker
- Flask
- [Peewee](http://docs.peewee-orm.com/en/latest/index.html) (ORM)

## Executando localmente

1. 'sh cli.sh build-image'

2. 'sh cli.sh run-container'

## Deploy

1. Logar no GCP com gcloud 'gcloud auth login'

2. Configure o projeto GCP 'gcloud config set project o-que-le-agora'

3. Rode 'gcloud app deploy'

## Referências

https://realpython.com/python-testing/