from sucupira_scraper import get_professors_from_page
from sucupira_scraper import get_students_from_page
from sucupira_scraper import concatenate_excel_out
import os

path = os.chdir('./Outputs') 

area_list = ['ENGENHARIA QUÍMICA (33003017034P8)',
             'ENGENHARIA CIVIL (33003017041P4)',
             'ENGENHARIA DE ALIMENTOS (33003017029P4)',
             'ENGENHARIA AGRÍCOLA (33003017026P5)'
            ]

# Exportar info professores
for area in area_list:
    info_df = get_professors_from_page(area)
    print(info_df.head())
    info_df.to_excel(f"{area}_output.xlsx")
    print(f"Terminou exportação de {area}")
 
# Exportar info alunos   
for area in area_list:
    info_df = get_students_from_page(area)
    print(info_df.head())
    info_df.to_excel(f"{area}_alunos_output.xlsx")
    print(f"Terminou exportação de alunos {area}")

# Concatenar tudo em um arquivo só
concatenate_excel_out()
 
    


