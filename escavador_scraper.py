from tkinter import NONE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Emulate stroke of keys such as "shift"
from selenium.webdriver.common.by import By
import time

########### Função que encontra o link do escavador dado o nome da pessoa ###########

def f_get_link_professor(driver=None, name_person=None):

    try:
        url = "https://www.escavador.com/busca?q={}&qo=p&f[pt][0]=curriculo".format(name_person)
        driver.get(url)
        
        element = None
        
        try:
            element = driver.find_element(By.XPATH, "//div[@class='link-adrress-box']//*[@class='link-address']")
            print(element.text)
            #time.sleep(10)      
        except Exception as e:
            pass
        
        if element != None:
            return element.text
            
    except:
        print("\nescavador_profile.f_get_link: Erro.\n")
        
   
   
        
############ Função que retira informações das páginas: formação, área de formação, etc ##############

def f_get_info_from_professor(driver=None, link=None):
    
    info_dict = {'endereco_profissional' : None,
                 'area_atuacao': None,
                 'formacao' : None,
                 'foi_orientado_por' : None}
    
    xpath_dict = {'endereco_profissional' : "//div[@id='endereco-profissional']",
                 'area_atuacao': "//div[@id='areas_atuacao']",
                 'formacao' : "//div[@id='formacao']",
                 'foi_orientado_por' : None}
    
    try:
        #try to open page
        driver.get(str(link))
        time.sleep(1)
        
        tried = 0
        
        while tried != 5:
            try:
                element = driver.find_elements(By.XPATH, "//section[@id='academico']")
                if len(element) == 0:
                    print("entrou element is none")
                    tried += 1
                    driver.close()
                    driver = webdriver.Chrome(f'C:/Users/taina/OneDrive/Desktop/Scrapper_Escavador/chromedriver.exe')
                    driver.get(str(link))
                else:
                    tried = 5
            except Exception as e:
                print("deu except")
                tried += 1
                # Tentou entrar na pagina mas nao conseguiu de jeito nenhum, então ignora aquele nome e info = None
                pass
                
        # Get info from dicts   
        for info, xpath in zip(info_dict, xpath_dict):
            element = None
            try:
                element = driver.find_elements(By.XPATH, xpath_dict[xpath])
                if element != None:
                    info_dict[info] = element
            except Exception as e:
                pass
            
        return info_dict
    
    # If can't open escavador, stop and throw error       
    except:
        print("\nescavador_profile.f_get_link: Erro.\n")
        
