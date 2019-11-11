# Evolución de las reservas hídricas de los embalses de España

El objetivo del algoritmo es la creación de un dataset a partir de los datos contenidos en la web de Embalses.net mediante la técnica de web scraping. El dataset contendrá información sobre las reservas hídricas de los embalses (>5Hm3) con periodicidad semanal, almacenándolo de forma tabular en un archivo csv 

El scrip se ha codificado en python 3 utilizando las siguientes librerías:
- request
- pandas
- BeautifulSoup
- re

el archivo csv contiene los siguiente campos:

-	**Cuenca**: Demarcación hidrográfica en el que se encuentra el embalse.
-	**Pantano**: nombre del embalse (> 5 hm3 de capacidad).
-	**Capacidad**: capacidad del embalse en Hm3.
-	**Embalsada**: volumen de agua en el embalse en Hm3.
-	**Variación**: Variación de agua embalsada en porcentaje respecto a la semana pasada.
-	**Fecha**: Fecha a la que hace referencia el agua embalsada y la variación respecto a la semana pasada.
