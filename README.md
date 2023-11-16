# Resumo
Buscar informações da rede modbus para depois tratar os dados com um Power BI.

- buscar as informações via chamada API
- as chamadas devem acontecer de uma em uma hora
- os dados devem ser armazenados em um arquivo csv

# Configurando o ambiente

## Windows Store
O Windows Store já configura tudo o que é necessário, é mais fácil e seguro do que fazer o download do instalador nos sites oficiais dos produtos. Instalar:  
- python 12
- vscode

Utilizar o *vscode* para abrir o projeto.

Confirmar a instalação do python
```sh
C:\Users\...\modbus> python --version
Python 3.12.0
```
## Virtual environment
O python possui pacotes built-in como o *csv, time, json* que não precisam ser instalados separadamente. Para pacotes específicos como o *requests* se cria o arquivo *requirements.txt* que armazena o nome do pacote e a versão. Antes de instalar os pacotes, uma boa prática criar a *virtual envinronment*.

A *Virtual Environment* serve para isolar os pacotes python específicos do projeto ao invés de instalar no sistema operacional. Isso trás mais segurança e controle sobre o ambiente de trabalho.

** É necessário ativar a *venv* toda vez que for rodar o projeto.

```sh
# Criar a virtual environment
C:\Users\...\modbus> python -m venv venv
# Ativar a virtual environment
C:\Users\...\modbus> venv\Scripts\activate
# Instalar os requirements
C:\Users\...\modbus> pip install -r requirements.txt
# Rodar o script python
C:\Users\...\modbus> python main.py
```

## Rodando o script python
```sh
venv\Scripts\activate
python main.py
```
