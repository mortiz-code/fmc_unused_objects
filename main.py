#usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = "Matias Ortiz"
__email__ = "matias.ortiz@bvstv.com"
__webpage__ = "https://github.com/mortiz-code"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022, all rights reserved."
__license__ = "BSD 3-Clause License."

from dotenv import load_dotenv
from os import getenv
from fireREST import FMC
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

def login():
    """
    login Funcion de login

    Returns:
        _type_: Lista con el objeto de conexion y el hostmame.
    """
    
    load_dotenv(dotenv_path='.env')
    HOST = getenv('HOST')
    USER = getenv('USR')
    PWD = getenv('PASS')
    host=HOST
    user=USER
    pwd=PWD
    fmc = FMC(hostname=host, username=user, password=pwd, domain='Global')
    return [fmc, host]

def objectos(fmc):
    """
    objectos Objetos

    Args:
        fmc (_type_): _description_

    Returns:
        _type_: Listado de objetos a ser buscandos.
    """
    net_objects = fmc.object.network.get()
    host_objects = fmc.object.host.get()
    port_objects = fmc.object.port.get()
    url_objects = fmc.object.url.get()
    networkgroup_objects = fmc.object.networkgroup.get()
    portobjectgroup_objects = fmc.object.portobjectgroup.get()
    urlgroup_objects = fmc.object.urlgroup.get()

    return [net_objects, host_objects, port_objects, url_objects, networkgroup_objects, portobjectgroup_objects, urlgroup_objects]

def header(fmc):
    """
    header _summary_

    Args:
        fmc (_type_): _description_

    Returns:
        _type_: Headers para requests.
    """
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["X-auth-access-token"] = fmc.conn.headers['X-auth-access-token']
    return headers

def usages(data, host, headers):
    """
    usages Busqueda de objetos sin uso. Se utiliza UUID y tipo de objeto en el busqueda. El primer loop es una lista y el segundo un diccionario.

    Args:
        data (_type_): _description_
        host (_type_): _description_
        headers (_type_): _description_
    """
    print(f' Busqueda de objetos sin uso en {host} '.center(100, '-'))
    n = 0
    q = 0
    for i in data:
        for _ in i:
            q += 1
            name = _['name']
            uuid= _['id']
            t = _['type']
            url = f"https://{host}/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/operational/usage?filter=uuid:{uuid};type:{t}"
            resp = requests.get(url, headers=headers, verify = False)
            try:
                if resp.json()['paging']['count'] == 0:
                    n += 1
                    print(t + ' : ' +  name + ' ->  No se usa')
            except KeyError as e:
                print(resp.status_code)
                
    print(f" Cantidad de objetos sin uso: {n} de {q} ".center(100, '-'))

def main():
    start = datetime.now()
    fmc = login()
    data = objectos(fmc[0])
    headers = header(fmc[0])
    usages(data, fmc[1], headers)
    total_time = datetime.now() - start
    print(f" Tiempo de ejecucion: {total_time} ".center(100, '-'))

if __name__ == '__main__':
    main()
