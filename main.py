import pymongo



cluster = pymongo.MongoClient(SEU AUTENTICADOR DO MONGODB PARA SUA DATABASE)
db = cluster.get_database(NOME DA DATABASE)
collection = db.get_collection(NOME DA COLECAO QUE SERA ACESSADA)



def registrar(usuario:str, senha:str):
    dados = {
        'name' :  f'{usuario}',
        'senha' : f'{senha}'

    }

    collection.insert_one(dados)


def authenticar(usuario:str, senha:str):

    validação = collection.find_one({})

    if validação['name'] == usuario and validação['senha'] == senha:
        print("Bem vindo.")
    else:
        print("Usuario ou senha incorretos")


print('Escolha\n[ 1 ] - Para se REGISTRAR\n[ 2 ] - Para se CADASTRAR\nSua escolha: ')
escolha = input(" ")

if escolha == '1':
    usuario = input("Usuario: ").lower()
    senha = input("Senha: ").lower()

    registrar(usuario, senha)
   


elif escolha == '2':
    print("Digite seu usuario e senha abaixo:\n ")

    usuario = input("Usuario:").lower()
    senha = input("Senha: ")
    authenticar(usuario, senha)

else: 
    print("Opcao invalida")
