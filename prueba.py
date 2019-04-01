from bs4 import BeautifulSoup
import requests, re

urlLogin = "https://zeusr.sii.cl/AUT2000/InicioAutenticacion/IngresoRutClave.html?https://www1.sii.cl/cgi-bin/Portal001/mipeSelEmpresa.cgi?DESDE_DONDE_URL=OPCION%3D2"
with requests.Session() as s:
    s.get(urlLogin)

    loginData = dict(rutcntr='6.490.249-0',
                     clave='180297PA')
    print(s.headers)
    r = s.post(urlLogin, data=loginData)

    print(r.status_code)
    soupR = BeautifulSoup(r.content, 'html.parser')
    print(soupR.prettify)