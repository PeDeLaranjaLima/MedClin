# MedClin

Para criar o projeto basta baixar o repositório com  clone, ativar o .venv com o ```venv\Scripts\Activate```.
Pode ser necessário instalar o django ```pip install django```. É importante rodar o servidor ``` python manage.py runserver ```.

A estrutura do projeto é:

```
meu_projeto/
│
├── manage.py
├── requirements.txt
│
├── config/                  # Configuração do projeto (core)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/                    # Camada de negócio
│   ├── acesso/
│   ├── cadastros/
│   ├── atendimento/
│   ├── prontuario/
│   ├── farmacia/
│   └── financeiro/
│
├── core/                    # Código compartilhado (regras comuns)
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── validators/
│
├── templates/               # Camada de apresentação (HTML global)
│   └── base.html
│
├── static/                  # CSS, JS, imagens
│   ├── css/
│   ├── js/
│   └── img/
│
├── media/                   # Uploads (arquivos do usuário)
│
└── db.sql                   # Banco
```

Dentro da pasta de prontuário:
```
apps/
└── prontuario/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py              # Camada de dados
    ├── views.py               # Camada de apresentação
    ├── urls.py
    │
    ├── services/              # Regras de negócio: O que está no diagrama de classes
    │   ├── __init__.py
    │   └── prontuario_service.py
    │
    ├── dtos/                  # entrada/saída de dados
    │   └── prontuario_dto.py
    │
    ├── selectors/             # consultas complexas
    │   └── prontuario_selector.py
    │
    ├── templates/
    │   └── prontuario/
    │
    └── tests/
```
Desse modo, o fluxo ideal seria: View → Service → Model → Banco.
