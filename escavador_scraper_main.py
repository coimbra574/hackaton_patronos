from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Emulate stroke of keys such as "shift"
from selenium.webdriver.chrome.options import Options 
from escavador_scraper import f_get_link_professor
from escavador_scraper import f_get_info_from_professor 


# path do do seu chrome driver
driver = webdriver.Chrome(f'C:/Users/taina/OneDrive/Desktop/Scrapper_Escavador/chromedriver.exe')

driver.get("https://www.escavador.com/")

link = f_get_link_professor(driver, "Akebo Yamakami")
info_dict = f_get_info_from_professor(driver, link)

# Imprimir orientadores e seus respectivos trabalhos
for item in info_dict["formacao"]:
    print('\n')
    print(str(item.text))
    
for item in info_dict["area_atuacao"]:
    print('\n')
    print(str(item.text))
    
for item in info_dict["endereco_profissional"]:
    print('\n')
    print(str(item.text))
    
print("Terminou operação")
driver.close()
    

