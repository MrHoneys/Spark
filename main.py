# ------------------------------ BIBLIOTECA INSTALADAS ------------------------------ #
import os
from googlesearch import search
import requests
import socket
from termcolor import colored  # Módulo para colorir o texto no terminal

# ------------------------------ ONDE SERÁ REALIZADO O SERVIÇO  ------------------------------ #

def pesquisar_google(query):
    try:
        resultados = search(query, num=30, stop=10, pause=2)  # Pesquisa por até 10 resultados
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

def consultar_whois_cnpj(cnpj):
    try:
        response = requests.get(f'https://publica.cnpj.ws/cnpj/{cnpj}')
        
        if response.status_code == 200:
            data = response.json()
            print("\033[1;34mInformações sobre o CNPJ:\033[0m")
            print("\033[1;37mCNPJ Raiz:\033[0m", f"\033[1;31m{data['cnpj_raiz']}\033[0m")
            print("\033[1;37mRazão Social:\033[0m", f"\033[1;31m{data['razao_social']}\033[0m")
            print("\033[1;37mCapital Social:\033[0m", f"\033[1;31m{data['capital_social']}\033[0m")
            print("\033[1;37mResponsavel Federativo:\033[0m", f"\033[1;31m{data['responsavel_federativo']}\033[0m")   
            print("\033[1;37mAtualizado Em:\033[0m", f"\033[1;31m{data['atualizado_em']}\033[0m")  
            print("\033[1;37mNatureza Juridica\033[0m", f"\033[1;31m{data['natureza_juridica']}\033[0m")                               
            # Etc... adicione as outras informações conforme necessário
            print("\033[1;34mSócios:\033[0m")
            for idx, socio in enumerate(data['socios'], start=1):
                print(f"\033[1;37mSócio {idx}:\033[0m")
                print("\033[1;37mNome do Sócio:\033[0m", f"\033[1;31m{socio['nome']}\033[0m")
                print("\033[1;37mCPF do Sócio:\033[0m", f"\033[1;31m{socio['cpf_cnpj_socio']}\033[0m")
                print("\033[1;37mTipo:\033[0m", f"\033[1;31m{socio['tipo']}\033[0m")
                print("\033[1;37mData de Entrada:\033[0m", f"\033[1;31m{socio['data_entrada']}\033[0m")
                print("\033[1;37mFaixa Etária:\033[0m", f"\033[1;31m{socio['faixa_etaria']}\033[0m")
                print("\033[1;37mAtualizado em:\033[0m", f"\033[1;31m{socio['atualizado_em']}\033[0m")
                print("\033[1;37mPais ID:\033[0m", f"\033[1;31m{socio['pais_id']}\033[0m")
                print("\033[1;37mQualificação do Sócio:\033[0m", f"\033[1;31m{socio['qualificacao_socio']['descricao']}\033[0m")
                print("-------------------------------------------------")

            # E assim por diante para os outros dados
        else:
            print("\033[1;31mErro ao obter informações do CNPJ.\033[0m")
    except Exception as e:
        print(f"Ocorreu um erro ao obter informações do CNPJ: {e}")


def port_scan(host, port):
    # Dicionário para mapear portas aos serviços correspondentes
    services = {
        21: "FTP",
        23: "Telnet",
        25: "SMTP",
        80: "HTTP",
        443: "HTTPS",
        139: "NetBIOS",
        445: "SMB",
        3389: "RDP",
        5900: "VNC",
        5901: "VNC alternativo",
        5902: "VNC alternativo",
        22: "SSH",
        8080: "HTTP alternativo",
        1433: "Microsoft SQL Server",
        1723: "PPTP",
        3306: "MySQL",
        5432: "PostgreSQL",
        6667: "IRC",
        110: "POP3",
        143: "IMAP",
        53: "DNS",
        4433: "HTTPS alternativo"
    }

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((host, port))
        service_name = services.get(port, "Desconhecido")
        
        if result == 0:
            status = colored("ABERTA", "green")
        else:
            status = colored("FECHADA", "red")
        sock.close()

        return f"Porta {port} ({service_name}): {status}"
    except socket.error as e:
        return f"Erro: {e}"

def portscan(ip):
    try:
        print(f"Iniciando varredura de portas para o IP: {ip}")

        categorias = {
            "Gerenciamento Remoto": [5900, 5901, 5902, 22, 3389, 8080],
            "Serviços Vulneráveis": [1433, 1723, 3306, 5432, 6667],
            "Serviços Essenciais": [25, 80, 443, 110, 143, 53, 4433]
        }

        for categoria, portas in categorias.items():
            print(f"\n{categoria}:")
            for porta in portas:
                resultado = port_scan(ip, porta)
                print(f"- {resultado}")
    except KeyboardInterrupt:
        print("Varredura interrompida")
    except Exception as e:
        print(f"Erro durante a varredura: {e}")


# ------------------------------ LIMPEZA DE TELA ANTES DE COMEÇAR  ------------------------------ #

def main():
    def limpar_tela():
        if os.name == "posix":  # Limpar tela no Unix/Linux/Mac
            os.system("clear")
        elif os.name == "nt":  # Limpar tela no Windows
            os.system("cls")
    
    limpar_tela()

# ------------------------------ TELA INICIAL PARA A LOGO  ------------------------------ #
      
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
    print("\033[1;36m2. Whois IP\033[0m")
    print("\033[1;36m3. Whois CNPJ\033[0m")
    print("\033[1;36m4. PortScan\033[0m")
    print("\033[1;36m0. Sair\033[0m")

    opcao = input("\033[1;36mEscolha uma opção: \033[0m")

# ------------------------------ OPÇÕES PARA IR ATE O SERVIÇOS  ------------------------------ #

    # -- ------------ SERVIÇO 1 -- ------------  # 
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

    # -- -- ------------  SERVIÇO 2 -- ------------  # 
    elif opcao == "2":
        limpar_tela()
        print("\033[1;35m")
        print("""
 ▄█     █▄     ▄█    █▄     ▄██████▄   ▄█     ▄████████       ▄█     ▄███████▄ 
███     ███   ███    ███   ███    ███ ███    ███    ███      ███    ███    ███ 
███     ███   ███    ███   ███    ███ ███▌   ███    █▀       ███▌   ███    ███ 
███     ███  ▄███▄▄▄▄███▄▄ ███    ███ ███▌   ███             ███▌   ███    ███ 
███     ███ ▀▀███▀▀▀▀███▀  ███    ███ ███▌ ▀███████████      ███▌ ▀█████████▀  
███     ███   ███    ███   ███    ███ ███           ███      ███    ███        
███ ▄█▄ ███   ███    ███   ███    ███ ███     ▄█    ███      ███    ███        
 ▀███▀███▀    ███    █▀     ▀██████▀  █▀    ▄████████▀       █▀    ▄████▀  
        """)
        ip = input("\033[1;32mDigite o IP para pesquisa WHOIS: \033[0m")
        obter_informacoes_ip(ip)

    # -- -- ------------  SERVIÇO 3 -- ------------  # 
    elif opcao == "3":
        limpar_tela()
        print("\033[1;35m]")
        print("""
               ▄█     █▄     ▄█    █▄     ▄██████▄   ▄█     ▄████████       ▄████████ ███▄▄▄▄      ▄███████▄▄█ 
███     ███   ███    ███   ███    ███ ███    ███    ███      ███    ███ ███▀▀▀██▄   ███    ███     ███ 
███     ███   ███    ███   ███    ███ ███▌   ███    █▀       ███    █▀  ███   ███   ███    ███     ███ 
███     ███  ▄███▄▄▄▄███▄▄ ███    ███ ███▌   ███             ███        ███   ███   ███    ███     ███ 
███     ███ ▀▀███▀▀▀▀███▀  ███    ███ ███▌ ▀███████████      ███        ███   ███ ▀█████████▀      ███ 
███     ███   ███    ███   ███    ███ ███           ███      ███    █▄  ███   ███   ███            ███ 
███ ▄█▄ ███   ███    ███   ███    ███ ███     ▄█    ███      ███    ███ ███   ███   ███            ███ 
 ▀███▀███▀    ███    █▀     ▀██████▀  █▀    ▄████████▀       ████████▀   ▀█   █▀   ▄████▀      █▄ ▄███ 
                                                                                               ▀▀▀▀▀▀
              
              """)
        cnpj = input("\033[1;32mDigite o CNPJ para consulta WHOIS: \033[0m")
        consultar_whois_cnpj(cnpj)

    # -- -- ------------  SERVIÇO 4 -- ------------  # 
    elif opcao == "4":
        limpar_tela()
        print("\033[1;35m]")
        print("""
              
       
                                                                                           
              """)
        ip = input("\033[1;32mDigite o IP para consulta PortScan: \033[0m")
        portscan(ip)  # Substitua "127.0.0.1" pelo IP que você deseja verificar

    # -- SERVIÇO DE SÁIDA  # 
    elif opcao == "0":
        print("\033[1;31mSaindo do programa.\033[0m")
    else:
        print("\033[1;31mOpção inválida.\033[0m")

if __name__ == "__main__":
    main()
