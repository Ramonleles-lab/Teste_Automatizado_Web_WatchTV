from environments import *
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect

class values():
        # login_user
        login_username_input_value = 'ramon_leles@hotmail.com'
        login_password_input_value = 'Leles1990'

        #login_user_invalid
        login_username_input_value_invalid = 'ramon@hotmail.com'
        login_password_input_value_invalid = 'Leles1990'
        
        #mensagem_error
        mensagem_error_user = 'A senha ou e-mail estão incorretos, tente novamente ou clique em "Esqueci a minha senha" para redefinir a sua senha.'
        
        #titulo_pesquisado
        conteudo_pesquisar = "gladiador"
        
        #texto_do_titulo_do_conteudo_selecionado
        texto_do_conteudo = "Gladiador"
        
        #validar reposta ao passar o mouse no icone da lista
        icone_da_lista_valor = "Remover da lista"
        
        #validar titulo do conteudo dentro do reprodutor de vídeo
        titulo_do_conteudo_player_valor = "Gladiador"
        
        #nome de novo usuario
        inserir_nome_usuario_1_valor = "fulano"
        
        #mensagem de que usuario foi criado com sucesso
        mensagem_criado_com_sucesso_valor = "Perfil criado com sucesso"
        
        #validando texto de usuário excluido com sucesso
        texto_de_cofirmacao_exclusao_valor = "Seu perfil foi excluído com sucesso"
        
        ##validar mensagem quando altera para uma senha invalida 
        campo_senha_atual_valor = "Leles1990"
        campo_nova_senha_invalida_valor = "123"
        campo_nova_senha_invalida_confirmar_valor = "123"
        mensagem_de_erro_de_senha_valor = "A senha deve ter pelo menos 6 caracteres"
        
        #validar mensagem quando altera para uma email invalido
        campo_novo_email_valor = "ramongmail.com"
        mensagem_de_erro_de_email_valor = "O email deve ser um endereço de email válido"
        
        #alterar telefone do usuario para um número inválido
        campo_telefone_valor = "3"
        
class elements():

        # login_usuario
        login_username = '#email'
        login_password = '#password'
        sign_button = "button[type='submit']"
        message_error = "div[id='error'] p"

        # validar_mensagem_usuário_incorreto
        validar_usuario_invalido = 'A senha ou e-mail estão incorretos, tente novamente ou clique em "Esqueci a minha senha" para redefinir a sua senha.'
        
        selecionar_usuario = "div[class='sc-f7504c4f-0 efKNZY'] div:nth-child(1) div:nth-child(1) div:nth-child(1) img:nth-child(1)"
        
        #minha_area
        botão_minha_área = "img[alt='Ícone da aba Minha área']"
        
        #pesquisa
        botão_pesquisar = "img[alt='Icone de busca']"
        caixa_pesquisar_conteudo = "input[placeholder='O que você está procurando?']"
        botão_assistir = "button[class='sc-8ee56eea-0 fYqpnb primary-button watch']"
        
        #validando_conteudo_pesquisado
        selecionar_conteudo = "div[class='sc-d3ba6ae7-1 boubMs'] div[class='sc-e1ef3774-3 dWYKcc']"
        titulo_do_conteudo = "(//h1[normalize-space()='Gladiador'])[1]"
        
        #icone de adiconar ou remover da lista
        icone_lista = "button[aria-label='Remover da lista'] img[alt='Ícone de adicionar na lista']"
        
        #validar titulo do conteudo dentro do reprodutor de vídeo
        titulo_do_conteudo_player = "div[class='left-info'] div h2"
        
        #perfis do usuario
        botao_perfil = ".sc-b9c41dc-0.gLEbTu"
        botao_novo_usuario = ".sc-9c32bced-6.jqUPLT"
        inserir_nome_usuario_1 = "#name"
        botao_salvar_novo_usuario = "button[class='sc-8ee56eea-0 fYqpnb undefined watch']"
        
        #validar usuario cadastrado com sucesso
        mensagem_criado_com_sucesso = ".text"
        
        #para tornar um perfil infantil
        botão_ativar_faixa_etaria = "div[class='sc-a3295a3e-8 hcapAF'] div[class='sc-83c8599-0 hilXmT'] div[class='sc-83c8599-1 lkBGDX'] div span[class='slider round']"
        caixa_de_selecao_faixa_etaria = ".sc-d96e42b-1.gTBJeI"
        selecionar_faixa_etaria = "//div[contains(@class,'sc-8fc84cb9-1 jVkfxe active selected')]//div[contains(@class,'sc-8fc84cb9-2 iLZvzX dot')]"
        botao_salvar_alteracao = "div[class='sc-ed8341e0-9 jGYfDj'] button[type='button']"
        botao_salvar_novo_usuario = "button[class='sc-8ee56eea-0 fYqpnb undefined watch']"
        
        #para excluir um usuario
        selecionar_gerenciar_perfis = "//a[normalize-space()='Gerenciar perfis']"
        botao_editar_perfil = "//button[normalize-space()='Editar perfil']"
        selecionando_perfil = "//div[@class='sc-4cf032f0-0 iPfFcU']"
        botao_excluir_perfil = "//button[normalize-space()='Excluir perfil']"
        botao_confirmar_sim = "//button[normalize-space()='Sim']"
        
        #validando texto de usuário excluido com sucesso
        texto_de_cofirmacao_exclusao = "//span[@class='text']"
        
        #valdando texto de desfazer exclusão de usuario
        texto_desfazer_exclusao = "//button[normalize-space()='Desfazer']"
        
        #validar mensagem quando altera para uma senha invalida 
        botao_selecionar_conta = "//a[normalize-space()='Conta']"
        botao_alterar_senha = "//button[normalize-space()='Alterar senha']"
        campo_senha_atual = "#currentPassword"
        campo_nova_senha_invalida = "#password"
        campo_nova_senha_invalida_confirmar = "#confirmPassword"
        botao_salvar_nova_senha = "//button[normalize-space()='Salvar']"
        mensagem_de_erro_de_senha = "//div[@id='error-password']"
        
        #validar mensagem quando altera para uma email invalido
        botao_adiconar_email = "//button[normalize-space()='Adicionar um endereço de email']"
        campo_novo_email = "//input[@id='email']"
        botao_salvar_novo_email = "//div[@class='sc-e54b94c7-1 kgGDvE']//button[@type='submit'][normalize-space()='Salvar']"
        mensagem_de_erro_email = "//div[@id='error-email']"
        
        #alterar telefone do usuario para um número inválido
        botao_editar_dados = "//button[normalize-space()='Editar dados']"
        campo_telefone = "//input[@id='phone']"
        botao_salvar_dados_usuario = "//div[@class='sc-26e9f2de-1 MSjRu class-align']//button[@type='submit'][normalize-space()='Salvar']"