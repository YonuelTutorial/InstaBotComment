<br>

<p align="center">
  <h1 align="center">InstaBotComment</h1>
  <p align="center">Este es un algoritmo que comenta una publicación específica automáticamente en b>Instagram</b>.</p>
  <p align="center">This is an algorithm that comments on a specific post automatically on <b>Instagram</b>.</p>
</p>

</br>

--------

## Requisito / Requirements
- [Python](https://www.python.org/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) **Version close to the browser Obligatory**
- [Selenium 4.20](https://pypi.org/project/selenium/4.2.0/) **Version obligatory**

<br>

## **Como instalar / How to install**

#### Instalar Selenium
Abrir **PowerShell** y poner / Open **PowerShell** and put:

```elm
pip uninstall selenium

pip install selenium==4.2.0
```

#### Intalar ChromeDriver
Mover a la carpeta del script de InstaBotComment / Move to InstaBotComment script folder
```elm
chromedriver.exe
```
>Se veria algo asi:
>```elm
>chromedriver.exe
>botcommentinsta.py
>linkpublic.txt
>```
#### Configurar su Usuario / Config User

-Dirijase a (by=By.NAME, value='username') y en **send_Keys('YouUser')** y sustituyes por el tuyo.
-Para la contraseña en (by=By.NAME, value='password').**send_keys('YouPass')** y sustituyes por tu contraseña

Ejemplo se veria asi:

```python
driver.find_element(by=By.NAME, value='username').send_keys('Alejandro_uwu')
driver.find_element(by=By.NAME, value='password').send_keys('123456')
```
#### Configurar Comentarios / Config Comments:
Para los comentarios solo vas a variable randomcomments el cual cojera aleatoriamente de entre las ,

Para configurar solo separe entre `''` y `,`

Ejemplo:

randomcomments = ['@ever @Kim','Hola','Hello World',]

Si se aleatoriamente se elije la primera `,`

>```elm
>@ever @Kim
>```

#### Configurar Link / Config Link:
Ve a la carpeta de instalacion abre el archivo `linkpublic.txt` y pones el link de la publicacion:

Ejemplo:

>```elm
>linkpublic.txt
>https://www.instagram.com/p/CekUfsfegga0/
>
>
>
>
>
>```

#### *Start Script:*

Abrir **PowerShell** y poner / Open **PowerShell** and put:


>```python
>python .\botcommentinsta.py
>```

Ya en ese paso se pondra ** comentarios infinitamente.🚀**

## Warning

*Para que funcione se necesita no tener A2F

*La version del chromedriver tiene que ser una cercana a su navegador

*Tener Selenio 4.20

*For it to work you need to not have A2F

*The chromedriver version has to be the one close to your browser

*Have Selenium 4.20

--------

## License

