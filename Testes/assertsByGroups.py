from environments import *
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from elements import *
from time import sleep

def login_usuario(page):
    page.locator(elements.login_username).fill(values.login_username_input_value)
    page.locator(elements.login_password).fill(values.login_password_input_value) 
    page.click(elements.sign_button)
    
def login_usuario_invalido(page):
    page.locator(elements.login_username).fill(values.login_username_input_value_invalid)
    page.locator(elements.login_password).fill(values.login_password_input_value_invalid) 
    page.click(elements.sign_button)

def validar_mensagem_error(page):
    element = page.locator(elements.message_error)
    expect(element).to_have_text(elements.validar_usuario_invalido)
    
def selecionar_perfil(page):
    page.click(elements.selecionar_usuario)

def acessar_minha_area(page):
    page.click(elements.botão_minha_área)

def pesquisar_conteudo(page):
    page.click(elements.botão_pesquisar)
    sleep(5)
    page.locator(elements.caixa_pesquisar_conteudo).fill(values.conteudo_pesquisar)
    page.keyboard.press("Enter")
    
def validar_conteudo_selecionado(page):
    page.click(elements.selecionar_conteudo,force=True)
    #page.click(elements.botão_assistir)
    element = page.locator(elements.titulo_do_conteudo)
    expect(element).to_have_text(values.texto_do_conteudo)
    
def validar_conteudo_na_lista_de_favoritos(page):
    page.click(elements.selecionar_conteudo, force=True)
    elemento = page.locator(elements.icone_lista)
    elemento.hover()
    page.wait_for_timeout(1000)
    values.icone_da_lista_valor = elemento.inner_text()

def validar_conteudo_selecionado_pra_assitir(page):
    page.click(elements.selecionar_conteudo, force=True)
    page.click(elements.botão_assistir)
    element = page.locator(elements.titulo_do_conteudo_player)
    expect(element).to_have_text(values.titulo_do_conteudo_player_valor)

def adicionar_novo_usuario(page):
    page.click(elements.botao_perfil)
    page.click(elements.botao_novo_usuario)
    page.locator(elements.inserir_nome_usuario_1).fill(values.inserir_nome_usuario_1_valor)
    page.click(elements.botao_salvar_novo_usuario)

def validar_mensagem_usuario_criado_com_sucesso(page):
    element = page.locator(elements.mensagem_criado_com_sucesso)
    expect(element).to_have_text(values.mensagem_criado_com_sucesso_valor)

def adicionar_faixa_etaria(page):
    page.click(elements.botao_perfil)
    page.click(elements.botao_novo_usuario)
    page.locator(elements.inserir_nome_usuario_1).fill(values.inserir_nome_usuario_1_valor)
    page.click(elements.botão_ativar_faixa_etaria)
    page.click(elements.caixa_de_selecao_faixa_etaria)
    page.click(elements.selecionar_faixa_etaria)
    page.click(elements.botao_salvar_alteracao)
    page.click(elements.botao_salvar_novo_usuario)

def excluir_perfil_selecionado(page):
    page.click(elements.botao_perfil)
    page.click(elements.selecionar_gerenciar_perfis)
    page.click(elements.botao_editar_perfil)
    page.click(elements.selecionando_perfil)
    page.click(elements.botao_excluir_perfil)
    page.click(elements.botao_confirmar_sim)

def validar_mensagem_usuario_excluido_com_sucesso(page):
    element = page.locator(elements.texto_de_cofirmacao_exclusao)
    expect(element).to_have_text(values.texto_de_cofirmacao_exclusao_valor)

def validar_mensagem_de_desfazer_exclusao(page):
    page.click(elements.texto_desfazer_exclusao)

def alterar_para_senha_invalida(page):
    page.click(elements.botao_perfil)
    page.click(elements.botao_selecionar_conta)
    page.click(elements.botao_alterar_senha)
    page.locator(elements.campo_senha_atual).fill(values.campo_senha_atual_valor)
    page.locator(elements.campo_nova_senha_invalida).fill(values.campo_nova_senha_invalida_valor)
    page.locator(elements.campo_nova_senha_invalida_confirmar).fill(values.campo_nova_senha_invalida_confirmar_valor)
    page.click(elements.botao_salvar_nova_senha)

def validar_mensagem_de_senha_alterada_incorreta(page):
    element = page.locator(elements.mensagem_de_erro_de_senha)
    expect(element).to_have_text(values.mensagem_de_erro_de_senha_valor)

def alterar_para_email_invalido(page):
    page.click(elements.botao_perfil)
    page.click(elements.botao_selecionar_conta)
    page.click(elements.botao_adiconar_email)
    page.locator(elements.campo_novo_email).fill(values.campo_novo_email_valor)
    page.click(elements.botao_salvar_novo_email)

def validar_mensagem_de_email_alterada_incorreta(page):
    element = page.locator(elements.mensagem_de_erro_email)
    expect(element).to_have_text(values.mensagem_de_erro_de_email_valor)   

def alterar_dados_do_usuario(page):
    page.click(elements.botao_perfil)
    page.click(elements.botao_selecionar_conta)
    page.click(elements.botao_editar_dados)
    page.locator(elements.campo_telefone).fill(values.campo_telefone_valor)
    page.locator(elements.botao_salvar_dados_usuario)