from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from elements import *
from assertsByGroups import *

def teste_validar_mensagem_de_email_alterado_incorreto(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    
    #START TEST

    #login de usuário com email e senha válida.
    login_usuario(page)
    
    #selecionando perfil desejado após fazer login
    selecionar_perfil(page)
    
    #adicionando um email de recuperação inválido
    alterar_para_email_invalido(page)
    
    #validando a mensagem após salvar um email de recuperação inválido
    validar_mensagem_de_email_alterada_incorreta(page)

    #END TEST
    
    context.close()
    browser.close()