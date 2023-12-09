import os
from googlesearch import search
import requests

def pesquisar_google(query):
    try:
        resultados = search(query, num=10, stop=10, pause=2)  # Pesquisa por até 10 resultados
        for i, resultado in enumerate(resultados, 1):
            print(f"\033[1;34mResultado {i}:\033[0m")
            print(resultado)
            print("----------------------")
        print("\033[1;32mPesquisa concluída\033[0m")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def obter_informacoes_ip(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
            print("\033[1;34mInformações sobre o endereço IP:\033[0m")
            print("\033[1;37mIP:\033[0m", f"\033[1;31m{data['ip']}\033[0m")
            print("\033[1;37mLocalização:\033[0m", f"\033[1;31m{data['city']}, {data['region']}, {data['country']}\033[0m")
            print("\033[1;37mProvedor de Internet:\033[0m", f"\033[1;31m{data['org']}\033[0m")
            print("\033[1;37mLatitude, Longitude:\033[0m", f"\033[1;31m{data['loc']}\033[0m")
            print("\033[1;37mCódigo Postal:\033[0m", f"\033[1;31m{data['postal']}\033[0m")
        else:
            print("\033[1;31mErro ao obter informações do IP.\033[0m")
    except Exception as e:
        print(f"Ocorreu um erro ao obter informações do IP: {e}")



def main():
    def limpar_tela():
        if os.name == "posix":  # Limpar tela no Unix/Linux/Mac
            os.system("clear")
        elif os.name == "nt":  # Limpar tela no Windows
            os.system("cls")
    
    limpar_tela()
       
    print("\033[1;35m")
    print("""
   ▄████████    ▄███████▄    ▄████████    ▄████████    ▄█   ▄█▄ 
  ███    ███   ███    ███   ███    ███   ███    ███   ███ ▄███▀ 
  ███    █▀    ███    ███   ███    ███   ███    ███   ███▐██▀   
  ███          ███    ███   ███    ███  ▄███▄▄▄▄██▀  ▄█████▀    
▀███████████ ▀█████████▀  ▀███████████ ▀▀███▀▀▀▀▀   ▀▀█████▄    
         ███   ███          ███    ███ ▀███████████   ███▐██▄   
   ▄█    ███   ███          ███    ███   ███    ███   ███ ▀███▄ 
 ▄████████▀   ▄████▀        ███    █▀    ███    ███   ███   ▀█▀ 
                                         ███    ███   ▀         
    """)

    print("\033[1;36mMenu:\033[0m")
    print("\033[1;36m1. Google Hacking Spark\033[0m")
    print("\033[1;36m2. Pesquisar WHOIS de um IP\033[0m")
    print("\033[1;36m0. Sair\033[0m")

    opcao = input("\033[1;36mEscolha uma opção: \033[0m")

    if opcao == "1":
        limpar_tela()  # Limpar a tela antes de exibir a nova arte ASCII
        print("\033[1;35m")
        print("""
   ▄██████▄   ▄██████▄   ▄██████▄     ▄██████▄   ▄█          ▄████████ 
  ███    ███ ███    ███ ███    ███   ███    ███ ███         ███    ███ 
  ███    █▀  ███    ███ ███    ███   ███    █▀  ███         ███    █▀  
 ▄███        ███    ███ ███    ███  ▄███        ███        ▄███▄▄▄     
▀▀███ ████▄  ███    ███ ███    ███ ▀▀███ ████▄  ███       ▀▀███▀▀▀     
  ███    ███ ███    ███ ███    ███   ███    ███ ███         ███    █▄  
  ███    ███ ███    ███ ███    ███   ███    ███ ███▌    ▄   ███    ███ 
  ████████▀   ▀██████▀   ▀██████▀    ████████▀  █████▄▄██   ██████████
        """)
        query = input("\033[1;32mDigite o termo de pesquisa: \033[0m")
        pesquisar_google(query)
    elif opcao == "2":
        limpar_tela()
        ip = input("\033[1;32mDigite o IP para pesquisa WHOIS: \033[0m")
        obter_informacoes_ip(ip)
    elif opcao == "0":
        print("\033[1;31mSaindo do programa.\033[0m")
    else:
        print("\033[1;31mOpção inválida.\033[0m")

if __name__ == "__main__":
    main()
