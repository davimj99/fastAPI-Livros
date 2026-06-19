import csv

import requests
import json

API_URL="http://127.0.0.1:8000"

def tratar_resposta(resp: requests.Response):
    """Imprimir de forma amigável responta da API, trantando erros."""
    try:
        data = resp.json()
    except ValueError:
        print(f"\nStatus: {resp.status_code}")
        print("⚠️ Resposta sem JSON.")
        print(resp.text)
        return
    
    if resp.status_code >= 400:
        print(f"\n❌ Erro ({resp.status_code})")
    print(json.dumps(data, indent=4, ensure_ascii=False))

def listar_livros():
    print("\n📚 Listar Livros:")

    pagina=1
    livros = []

    resp = requests.get(f"{API_URL}/livros/?page={pagina}")
    print("-" *10 + " Página 1" + "-"*10)
    tratar_resposta(resp)

    if resp.status_code != 200:
        return
    dados = resp.json()
    livros.extend(dados)

    total_pages = int(resp.headers.get("X-Total-Pages", 1))

    for pagina in range(2, total_pages + 1):
        resp = requests.get(f"{API_URL}/livros/?page={pagina}")
        print( f"\nPágina {pagina}:")
        tratar_resposta(resp)
        if resp.status_code != 200:
            continue

        dados = resp.json()
        livros.extend(dados)
        
    print(f"\nTotal de livros listados: {len(livros)}")

def obter_livro():
    livro_uuid = input("UUID do livro: ").strip()
    resp = requests.get(f"{API_URL}/livros/{livro_uuid}")
    print("\n📘 Detalhes do Livro:")
    tratar_resposta(resp)

def adicionar_livro():
    print("\nDigite os dados do novo livro:")
    autor = input("Autor: ")
    titulo = input("Título: ")
    editora = input("Editora: ")
    ano = int(input("Ano de publicação: "))

    payload = {
        "autor": autor,
        "titulo": titulo,
        "editora": editora,
        "ano": ano,
    }

    resp = requests.post(f"{API_URL}/livros/", json=payload)
    print("\n Livro Adicionado:")
    tratar_resposta(resp)

def atualizar_livro():
    livro_uuid = input("UUID do livro a atualizar (PUT): ").strip() #strip tira espaços digitados sem querer
    
    print("\nDigite os NOVOS dados completos do livro:")
    autor = input("Autor: ")
    titulo = input("Título: ")
    editora = input("Editora: ")
    ano = int(input("Ano de publicação: "))

    payload = {
        "autor": autor,
        "titulo": titulo,
        "editora": editora,
        "ano": ano,
    }

    resp = requests.put(f"{API_URL}/livros/{livro_uuid}", json=payload)
    print("\n Livro Atualizado (PUT):")
    tratar_resposta(resp)

def atualizar_parcial():
    livro_uuid = input("UUID do livro a atualizar parcialmente (PATCH): ").strip()
    
    print("\nDigite APENAS os campos que deseja atualizar (deixe em branco para ignorar):")
    autor = input("Autor: ")
    titulo = input("Título: ")
    editora = input("Editora: ")
    ano = input("Ano de publicação: ")

    payload = {}

    if autor:
        payload['autor'] = autor
    if editora:
        payload['editora'] = editora
    if titulo:
        payload['titulo'] = titulo
    if ano:
        payload['ano'] = int(ano)

    resp = requests.patch(f"{API_URL}/livros/{livro_uuid}", json=payload)
    print("\n Livro Atualizado parcialmente (PATCH):")
    tratar_resposta(resp)

def deletar_livro():
    livro_uuid = input("UUID do livro a deletar (DELETE): ").strip()
    resp = requests.delete(f"{API_URL}/livros/{livro_uuid}")
    
    print("\n Resultado da exclusão (DELETE):")
    tratar_resposta(resp)

def importar_csv():
    caminho = input("Caminho do arquivo CSV:(ex: livros.csv) ").strip()

    try:
        with open(caminho, encoding='utf-8') as f:
            leitor = csv.DictReader(f, delimiter=';')
            print("\nImportando livros do CSV:")
            total = 0
            for linha in leitor:
                payload = {
                    "autor": linha['autor'],
                    "titulo": linha['titulo'],
                    "editora": linha['editora'],
                    "ano": int(linha['ano']),
                }
                resp = requests.post(f"{API_URL}/livros/", json=payload)
                if resp.status_code == 200 or resp.status_code == 201:
                   total += 1
                else:
                    print(f"Erro ao importar livro:")
                    tratar_resposta(resp)

            print(f"\nImportação concluída. Total de livros importados:{total}")
    except FileNotFoundError:
        print("Arquivo CSV não encontrado. Verifique o caminho e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro durante a importação: {e}")
                        

def menu():
    while True:
        print("\n=== CLIENTE API DE LIVROS ===")
        print("1. Listar Livros")
        print("2. Obter livro por UUID")
        print("3. Adicionar livro (POST)")
        print("4. Atualizar livro inteiro (PUT)")
        print("5. Atualizar parcialmente (PATCH)")
        print("6. Deletar livro (DELETE)")
        print("7. IMPORTAR livros de CSV")
        print("0. Sair")

        opcao = input("Escolha a opção: ").strip()

        if opcao == "1":
            listar_livros()

        elif opcao == "2":
            obter_livro()

        elif opcao == "3":
            adicionar_livro()

        elif opcao == "4":
            atualizar_livro()

        elif opcao == "5":
            atualizar_parcial()

        elif opcao == "6":
            deletar_livro()
            
        elif opcao == "7":
            importar_csv()
            
        elif opcao == "0":
            print("Encerrando cliente ...")
            break
        else:
            print("\n❌ Opção inválida!")
        
if __name__=="__main__":
    menu()
        