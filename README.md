<h1 align="center">
<img src= "./src/image.png"/>
<p>OPORTUNIDADE</p>
</h1>

## 📘 Sobre

O projeto é um **CRUDS**, dessa forma permite utilizar: Create, Read, Update, Delete, Search. Onde conseguimos criar, ler, atualizar, deletar ou buscar um contato existente.

## 💡 Tecnologias

- [Flask](https://flask.palletsprojects.com/en/2.3.x/) 

- [MySQL](https://dev.mysql.com/doc)

- [Flask-MySQL](https://flask-mysql.readthedocs.io/en/stable/)


##  💻 Como configurar o ambiente

**Instalação da venv**:

Crie uma Virtual Environment:
Abra o terminal (ou prompt de comando) na pasta do seu projeto e execute o seguinte comando para criar uma venv:

No **Windows**:
```bash
python -m venv venv
```
No **macOS e Linux**:
```bash
python3 -m venv venv
```
Isso criará uma pasta chamada "venv" no diretório do seu projeto com uma cópia isolada do Python e suas bibliotecas.

Ative a Virtual Environment:
No **Windows**, execute:
```bash
venv\Scripts\activate
```
No **macOS e Linux**, execute:
```bash
source venv/bin/activate
```
Ao ativar a venv, você verá o prompt de comando mudar para mostrar o nome da venv.

**Instale as dependências:**

Com a venv ativada, você pode instalar as dependências usando o pip.

Em seguida, execute o seguinte comando para instalar as dependências listadas no arquivo requirements.txt:
```bash
pip install -r requirements.txt
```
##  🚀 Como utilizar
No ínicio do código faça a configuração necessária do seu banco de dados MySQL.

Utilizando o Postman ou outra plataforma semelhante para testar APIs faça uma requisição *POST* para a seguinte rota: localhost:5000/tabela_contatos, onde irá gerar sua tabela com todos os campos necessários.

**CRIAR CONTATO**

Utilize a rota: localhost:5000/contato, selecione o method como *POST*, em seguida passe um json neste formato:

{
    "Nome": "TesteNome",
    "Sobrenome": "TesteSobrenome",
    "Email": "testeEmail@gmail.com",
    "Telefone": "(41) 99999-4444"
}

**LER CONTATO**

Utilize a rota: localhost:5000/contato/ID, selecione o method como *GET*, em seguida substitua o ID pelo número do ID do contato que deseja ler.

**ATUALIZAR CONTATO**

Utilize a rota: localhost:5000/contato/ID, selecione o method como *PUT*, em seguida substitua o ID pelo número do ID do contato que deseja atualizar. Depois passe um json neste formato: 

{
    "Nome": "TesteNome",
    "Sobrenome": "TesteSobrenome",
    "Email": "testeEmail@gmail.com",
    "Telefone": "(41) 99999-4444"
}

**DELETAR CONTATO**

Utilize a rota: localhost:5000/contato/ID, selecione o method como *DELETE*, em seguida substitua o ID pelo número do ID do contato que deseja deletar.

**BUSCAR CONTATOS**

Utilize a rota: localhost:5000/contato?nome=Teste, selecione o method como *GET*, em seguida substitua o Teste pelo nome dos contatos que deseja buscar.

## 🙋‍♂️ Créditos
Feito por Felipe Vidal Gevaerd.

