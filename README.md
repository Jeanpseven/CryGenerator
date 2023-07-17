# CryGenerator
gerador de ransomware

O script fornecido é um gerador de ransomware de demonstração. Ele é projetado para fins educacionais e de aprendizado e não deve ser usado de forma maliciosa ou ilegal.

O funcionamento do script é o seguinte:

Geração de Chaves:
O script gera uma chave simétrica aleatória para criptografar os arquivos e um par de chaves assimétricas (pública e privada) para criptografar a chave simétrica.

Criptografia dos Arquivos:
O script varre o diretório atual em busca de arquivos e, em seguida, criptografa o conteúdo de cada arquivo usando a chave simétrica gerada. Os arquivos originais são substituídos pelos arquivos criptografados.

Geração do Ransomware:
O script gera um arquivo chamado "CryBaby.py" que contém a chave pública criptografada e uma mensagem personalizada a ser exibida após a descriptografia. O arquivo "CryBaby.py" pode ser considerado como o ransomware gerado.

Descriptografia (Opcional)
Após a criptografia dos arquivos, o usuário pode optar por descriptografá-los digitando "s" no prompt. Se essa opção for selecionada, o usuário precisará inserir a chave privada para descriptografar os arquivos.
É importante ressaltar que o ransomware é uma forma de malware que criptografa arquivos em um sistema sem a permissão do usuário e, em seguida, exige um resgate para fornecer a chave de descriptografia. O uso de ransomware é ilegal e altamente prejudicial para os usuários afetados.
Este script foi fornecido apenas para fins educacionais e de aprendizado, para mostrar como a criptografia assimétrica e simétrica podem ser usadas para proteger e desproteger dados. A utilização deste script ou qualquer forma de ransomware de maneira maliciosa é estritamente proibida e pode resultar em sérias consequências legais.
Reforço que o uso responsável e ético da tecnologia é fundamental para garantir a segurança e privacidade de todos os usuários. Se você encontrar algum ransomware ou atividade suspeita em seus sistemas, é importante procurar ajuda de um profissional de segurança cibernética ou denunciar às autoridades competentes.


# a chave criptografada dentro do crybaby pode ser usada diretamente para descriptografar?

Não, a chave criptografada dentro do "CryBaby" não pode ser usada diretamente para descriptografar os arquivos. A chave criptografada dentro do "CryBaby" é a chave simétrica usada para criptografar os arquivos no processo de geração do ransomware.
Essa chave simétrica é criptografada com a chave pública do par de chaves assimétricas geradas anteriormente. O objetivo dessa etapa é proteger a chave simétrica e garantir que apenas quem possui a chave privada correspondente possa descriptografá-la e, assim, descriptografar os arquivos.
No processo de descriptografia, quando o usuário insere a chave privada no "CryBaby", a chave simétrica criptografada é descriptografada usando a chave privada, revelando a chave simétrica original. Com a chave simétrica em mãos, o "CryBaby" pode descriptografar os arquivos.
Essa abordagem é chamada de criptografia híbrida e é comum em sistemas de segurança para garantir a confidencialidade dos dados. A criptografia simétrica é usada para proteger os dados em si (arquivos neste caso), e a criptografia assimétrica é usada para proteger a chave simétrica usada para criptografar os dados.
