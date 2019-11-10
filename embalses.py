#!/usr/bin/env python
# coding: utf-8

# In[81]:


print(soup.body.section.prettify())


# In[76]:


# WEB SCRAPPING DEL SITIO WEB EMBALSES.NET

# Se importan las librerías que se van a utilizar
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

# 1. Obtención de los links a los datos de los embalses para cada cuenca

ca = soup.body.find_all(class_='index_bodysecLisT2_list')

# 1.a Se extrae todos los links de la sección que hemos extraido
link = []
for k in soup('a'):
    link.append(k.get('href'))

# 1.b Se filtran los links que nos interesan (el de las cuencas) y se almacenan en una lista
link1=[]
for i in link:
    if re.search('www.embalses.net/cuenca-', i):
        link1.append(i)

# 2. Extracción de los datos de cada embalse para todas las cuencas

# 2.a Se crea un dataframe vacío en el que se van a ir almacenando los datos
df2 = pd.DataFrame()

# 2.b Se crea un bucle que extrae los datos de los embalses ubicados en cada link (cuenca) y los almacena en un dataframe
for i in link1:
    # 
    page = requests.get(i)
    soup = BeautifulSoup(page.content)
    
    a = soup.body.section.div.find_all(class_='SeccionCentral_Caja')[0]

    # Se obtiene el nombre de la cuenca y se almacena en una variable
    cuenca = soup.find(class_='SeccionCentral_TituloTexto').text
    cuenca = cuenca.replace('Cuenca: ', '')
    
    #Se obtiene la fecha del agua embalsada
    a = soup.body.section.div.find_all(class_='SeccionCentral_Caja')[0]
    fecha = a.find(class_='Campo').text
    fecha = fecha.replace('Agua embalsada (','')
    fecha = fecha.replace('):', '')
    
    # Se extraen los nombres de los campos y se almacenan en una lista
    b = soup.body.section.div.find_all(class_='SeccionCentral_Caja')[1]
    tupa = []
    for i in b.tr.find_all('td'):
        tupa.append(i.get_text())


    # Se extraen los valores de los embalses (pantano, capacidad, embalsada y variación) y se almacenan en una lista
    tupa1 = []
    for i in b.find_all(class_='ResultadoCampo'):
        for j in i.find_all('td'):
            tupa1.append(j.get_text())

    # Quitar espacio en blanco y "\n"
    tupa1 = [words.replace('\n', '') for words in tupa1]
    tupa1 = [words.strip() for words in tupa1]

    
    # la lista tupa1 se transforma en una lista de listas
    recorrer = len(tupa)
    tupa2 = [tupa1[i:i+recorrer] for i in range(0, len(tupa1), recorrer)]
    

    # Se transforma la lista de listas con los valores de los embalses en un dataframe
    df = pd.DataFrame(tupa2,columns = tupa)
    # se añade un nuevo campo al dataframe con el nombre de la cuenca
    df['Cuenca'] = cuenca
    df['fecha'] = fecha
    df2 = pd.concat([df2, df], axis=0)
    

# 2.c Se genera un archivo csv a partir del dataframe

df2.to_csv(r'D:\estado_embalses.csv', index= False)
print(df2)    


# In[52]:


# Extracción de gráficos

import requests
def load_requests(source_url):
    r = requests.get(source_url, stream = True)
    if r.status_code == 200:
        aSplit = source_url.split('?a=')
        aSplit1 = aSplit[0].split('/')
        ruta = "D:/Graficos/"+aSplit[len(aSplit)-1] + "_" + aSplit1[len(aSplit1)-1]
        print(ruta)
        output = open(ruta,"wb")
        for chunk in r:
            output.write(chunk)
        output.close()

load_requests(images)


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id17
# 
# https://recursospython.com/guias-y-manuales/listas-y-tuplas/
# 
#  https://www.tutorialspoint.com/python3/python_lists.htm  
#  
#  https://python-para-impacientes.blogspot.com/2014/02/expresiones-regulares.html
#  
