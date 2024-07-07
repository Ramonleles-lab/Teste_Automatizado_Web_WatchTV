from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from elements import *
from assertsByGroups import *

def teste_alterar_dados_invalido_do_usuario(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    
    #START TEST

    #login de usuário com email e senha válida.
    login_usuario(page)
    
    #selecionando perfil desejado após fazer login
    selecionar_perfil(page)
    
    #alterando telefone do usuário para um número fora do padrão (obs:se o teste passar significa que o sistema aceita qualuer valor digitado como telefone)
    alterar_dados_do_usuario(page)

    #END TEST
    
    context.close()
    browser.close()