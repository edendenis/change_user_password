#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar a `alterar a senha o usuário` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar a `alterar a senha o usuário` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `alterar a senha o usuário` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `Senha do usuário`
# 
# A senha do usuário é uma sequência de caracteres utilizada como mecanismo de autenticação para acessar sistemas, aplicativos ou dispositivos eletrônicos protegidos. Ela serve para verificar a identidade do usuário, garantindo que apenas indivíduos autorizados possam realizar login e acessar informações confidenciais ou realizar operações específicas. Uma senha segura geralmente combina letras maiúsculas e minúsculas, números e caracteres especiais, garantindo assim maior segurança contra tentativas de acesso não autorizado.
# 

# ## 1. Como configurar/instalar/usar a `senha do usuário` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar a `senha do usuário` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. **Alterar a senha**: No terminal, digite o seguinte comando e pressione `Enter`: `sudo passwd nome_do_usuário`
# 
#     Substitua `nome_do_usuário` pelo nome do usuário para o qual você deseja alterar a senha.
# 
# 4. **Seguir as instruções**:
# 
# - Você será solicitado a digitar a senha do superusuário (`root`). Após digitar e pressionar `Enter`, você será solicitado a inserir a nova senha para o usuário especificado.
# 
# - Digite a nova senha quando solicitado e pressione `Enter` novamente. Você será solicitado a confirmar a senha digitando-a novamente.
# 
# 5. **Confirmação**:
# 
# - Após confirmar a nova senha, o `Terminal Emulator` deve exibir uma mensagem informando que a senha foi atualizada com sucesso.
# 
# Este procedimento permite que você altere a senha de qualquer usuário no sistema, desde que você tenha privilégios de superusuário (`root`), garantindo a segurança do acesso ao sistema.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `alterar a senha de usuário` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÂO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Alterar Senha Usuário Linux.*** Disponível em: <https://chatgpt.com/c/a7aeeffc-d47f-4195-b4d2-e2d564719945> (texto adaptado). StackExchange. Acessado em: 22/12/2023 11:35.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 22/12/2023 11:36.
# 
