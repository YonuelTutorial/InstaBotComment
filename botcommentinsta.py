#Creado totamente por hobbie
#Github https://github.com/YonuelTutorial


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


tc = 4 #tiempo entre comentarios / time between comments
bi = 1 #para bucle infinito / loop infinite
randomcomments = ['@ever @Kim','Hola','Hello World',] #replace with your words, separate comments between , and ''



#Inicio de Session/ Login
driver = webdriver.Chrome() #Abrir/Open Pag
driver.get("https://www.instagram.com")#Ingresar/Get into Link
sleep(3)
driver.find_element(by=By.NAME, value='username').send_keys('AAA') #Entre las '' agregar tu usuario en send_keys
driver.find_element(by=By.NAME, value='password').send_keys('123456')  #Entre las '' agregar tu contraseña en send_keys
sleep(1)
driver.find_element(By.XPATH,'//button[@type="submit"]').click() 
sleep(9)



with open("linkpublic.txt") as f: #Abrir/Open File
    for url in f:
        driver.get(url)  
        
driver.implicitly_wait(6)

##Primer/First Comment
driver.find_element(By.XPATH,'//*[@class ="_aaof"]//textarea').click() #Click al texto de el comentario.
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aaof"]//textarea').send_keys(random.choice(randomcomments)) #Escribir / Write random
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aaof"]//button[@type="submit"]').click()#Click de commentar/ Click to comment
sleep(tc)

#Inicio/Start Loop Infinite
while (bi >= 1):
    
    driver.find_element(By.XPATH,'//*[@class ="_aaof"]//textarea').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@class ="_aaof"]//textarea').send_keys(random.choice(randomcomments))
    sleep(1)
    driver.find_element(By.XPATH,'//*[@class ="_aaof"]//button[@type="submit"]').click()

    sleep(tc)
    
    bi += 1