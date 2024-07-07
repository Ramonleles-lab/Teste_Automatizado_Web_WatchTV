from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright
from elements import *
from assertsByGroups import *

def teste_login_usuario(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    
    #START TEST

    #login de usuário com email e senha válida.
    login_usuario(page)
    
    #selecionando perfil desejado após fazer login
    selecionar_perfil(page)
   
    #END TEST
    
    context.close()
    browser.close()