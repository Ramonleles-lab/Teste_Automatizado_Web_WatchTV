from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from elements import *
from assertsByGroups import *

def teste_validar_conteudo_na_lista_de_favoritos(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    
    #START TEST

    #login de usuário com email e senha válida
    login_usuario(page)
    
    #selecionando perfil desejado após fazer login
    selecionar_perfil(page)
    
    #pesquisando um filme na icone da lupa
    pesquisar_conteudo(page)
    
    #validar conteudo já na lista de favorito com resposta "Remover da lista"
    validar_conteudo_na_lista_de_favoritos(page)
   
    #END TEST
    
    context.close()
    browser.close()