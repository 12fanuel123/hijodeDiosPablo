from selenium import webdriver
import time
from random import randrange

resfrescar=10
lista=[]

navegador_1=webdriver.Chrome("C:\DriverPithon\chromedriver.exe")
navegador_2=webdriver.Chrome("C:\DriverPithon\chromedriver.exe")
navegador_3=webdriver.Chrome("C:\DriverPithon\chromedriver.exe")


lista.append(navegador_1)
lista.append(navegador_2)
lista.append(navegador_3)

for browser in lista:
    browser.get("https://youtu.be/5vggvqCwfsI")

while(True):
    nave=randrange(0,len(lista))
    lista[nave].refresh()
    print("browser numer ",nave,"Bot hecho por el hijo de Dios")    
    time.sleep(resfrescar)
