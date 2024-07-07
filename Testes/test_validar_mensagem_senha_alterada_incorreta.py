from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from elements import *
from assertsByGroups import *

def teste_validar_senha_alterada_incorreta(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    
    #START TEST

    #login de usuário com email e senha válida.
    login_usuario(page)
    
    #selecionando perfil desejado após fazer login
    selecionar_perfil(page)
    
    #atelrando senha para uma nova senha com padrão inválido
    alterar_para_senha_invalida(page)
    
    #validando mensagem que a senha está fora do padrão
    validar_mensagem_de_senha_alterada_incorreta(page)

    #END TEST
    
    context.close()
    browser.close()