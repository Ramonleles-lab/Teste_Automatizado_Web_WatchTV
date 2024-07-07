from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from elements import *
from assertsByGroups import *

def teste_novo_usuario(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    
    #START TEST

    #login de usuário com email e senha válida.
    login_usuario(page)
    
    #selecionando perfil desejado após fazer login.
    selecionar_perfil(page)
    
    #adicionar novo usuário para a conta.
    adicionar_novo_usuario(page)
    
    #mensagem de novo perfil de usuario criado com sucesso logo após salvar.
    validar_mensagem_usuario_criado_com_sucesso(page)
    
    #END TEST
    
    context.close()
    browser.close()