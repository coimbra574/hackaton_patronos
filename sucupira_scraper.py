from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys # Emulate stroke of keys such as "shift"
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import os


############## GET PROFESSORES DATA FROM SUCUPIRA WEB PAGE ###################
def get_professors_from_page(area):
    
    # Localização do seu chromedriver
    driver = webdriver.Chrome(f'C:/Users/taina/OneDrive/Desktop/Scrapper_Escavador/chromedriver.exe')

    driver.get("https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/docente/listaDocente.jsf;jsessionid=NJ+CP6RYoM9ufkpDTQQSDE-e.sucupira-213/")


    # Instituicao de ensino
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'form:j_idt30:inst:input'))).send_keys("unicamp")
    time.sleep(10)
    driver.find_element(By.XPATH, "//select[@name='form:j_idt30:inst:listbox']/option[text()='33003017 UNIVERSIDADE ESTADUAL DE CAMPINAS (UNICAMP)']").click()

    # Programa
    time.sleep(10)
    driver.find_element(By.XPATH, f"//select[@name='form:j_idt30:j_idt110']/option[text()='{area}']").click()

    # Botao aceito termos
    time.sleep(10)
    button = driver.find_element(By.XPATH, "//button[@class ='br-button primary small']").click()

    # Botao consulta
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Get data from table (lê só até a primeira página)
    time.sleep(10)
    table_names = driver.find_elements(By.XPATH, "//*[@class='table table-striped table-bordered']/tbody/tr/td[1]")
    table_categoria = driver.find_elements(By.XPATH, "//*[@class='table table-striped table-bordered']/tbody/tr/td[2]")
    
    name_list = []
    categoria_list = []

    for name in table_names:
        name_list.append(name.text)

    for cat in table_categoria:
        categoria_list.append(cat.text)
    
    info_df = pd.DataFrame(name_list) 
    info_df['area_atuacao'] = area
    info_df['categoria'] = pd.Series(categoria_list)
    info_df['nivel_academico'] = 'Professor'
    
    return info_df

    
    
############## GET STUDENTS DATA FROM SUCUPIRA WEB PAGE ###################
def get_students_from_page(area):
    
    # Localização do seu chromedriver
    driver = webdriver.Chrome(f'C:/Users/taina/OneDrive/Desktop/Scrapper_Escavador/chromedriver.exe')

    driver.get("https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/discente/listaDiscente.jsf;jsessionid=AtDK4lTmG2jv89CXOzcDf7OG.sucupira-203/")


    # Instituicao de ensino
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'form:j_idt30:inst:input'))).send_keys("unicamp")
    time.sleep(5)
    driver.find_element(By.XPATH, "//select[@name='form:j_idt30:inst:listbox']/option[text()='33003017 UNIVERSIDADE ESTADUAL DE CAMPINAS (UNICAMP)']").click()

    # Programa
    time.sleep(5)
    driver.find_element(By.XPATH, f"//select[@name='form:j_idt30:j_idt118']/option[text()='{area}']").click()
    time.sleep(5)

    # Botao aceito termos
    time.sleep(5)
    button = driver.find_element(By.XPATH, "//button[@class ='br-button primary small']").click()

    # Botao consulta
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Get data from table (lê só até a primeira página)
    time.sleep(5)
    table_names = driver.find_elements(By.XPATH, "//*[@class='table table-striped table-bordered']/tbody/tr/td[1]")
    table_nivel_academico = driver.find_elements(By.XPATH, "//*[@class='table table-striped table-bordered']/tbody/tr/td[2]")
    table_categoria = driver.find_elements(By.XPATH, "//*[@class='table table-striped table-bordered']/tbody/tr/td[3]")
    
    name_list = []
    categoria_list = []
    nivel_list = []

    for name in table_names:
        name_list.append(name.text)

    for cat in table_categoria:
        categoria_list.append(cat.text)
        
    for cat in table_nivel_academico:
        nivel_list.append(cat.text)
    
    info_df = pd.DataFrame(name_list) 
    info_df['area_atuacao'] = area
    info_df['categoria'] = pd.Series(categoria_list)
    info_df['nivel_academico'] = pd.Series(nivel_list)
    
    return info_df



############## CONCATENATE EXCEL SHEETS ###################
def concatenate_excel_out():
    path = os.getcwd()
    files = os.listdir(path)  
    print(files)
    df = pd.DataFrame()
    for file in files:
        if file.endswith('.xlsx'):
            df = df.append(pd.read_excel(file), ignore_index=True) 
    df.head() 
    df.to_excel('final_output.xlsx')
    
    
    
    



    




