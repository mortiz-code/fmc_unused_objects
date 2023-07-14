#usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = "Matias Ortiz"
__email__ = "matias.ortiz@bvstv.com"
__webpage__ = "https://github.com/mortiz-code"
__version__ = "0.2.0"
__copyright__ = "Copyright (c) 2023, all rights reserved."
__license__ = "BSD 3-Clause License."

from dotenv import load_dotenv
from os import getenv
from fireREST import FMC
from fireREST.exceptions import AuthError
import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime

load_dotenv(dotenv_path='.env')
_HOST = getenv('HOST')
_USER = getenv('USR')
_PWD = getenv('PASS')

def objectos(fmc):
    networkaddress_objects = fmc.object.networkaddress.get()
    host_objects = fmc.object.host.get()
    network_objects = fmc.object.network.get()
    range_objects = fmc.object.range.get()
    fqdn_objects = fmc.object.fqdn.get()
    networkgroup_objects = fmc.object.networkgroup.get()
    port_objects = fmc.object.port.get()
    protocolportobject_objects = fmc.object.protocolportobject.get()
    portobjectgroup_objects = fmc.object.portobjectgroup.get()
    icmpv4object_objects = fmc.object.icmpv4object.get()
    icmpv6object_objects = fmc.object.icmpv6object.get()
    anyprotocolportobject_objects = fmc.object.anyprotocolportobject.get()
    url_objects = fmc.object.url.get()
    urlgroup_objects = fmc.object.urlgroup.get()
    vlantag_objects = fmc.object.vlantag.get()
    vlangrouptag = fmc.object.vlangrouptag.get()


    return [networkaddress_objects,host_objects,network_objects,range_objects,fqdn_objects,networkgroup_objects,port_objects,protocolportobject_objects,portobjectgroup_objects,icmpv4object_objects,icmpv6object_objects,anyprotocolportobject_objects,url_objects,urlgroup_objects,vlantag_objects,vlangrouptag] 

def header(fmc):
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["X-auth-access-token"] = fmc.conn.headers['X-auth-access-token']
    return headers

def usages(data, fmc, headers):
    domain = fmc.system.info.domain.get()[0]['uuid']
    print(f' Searching for unused objects in {_HOST} '.center(100, '-'))
    n = 0
    q = 0
    try:
        for i in data:
            for _ in i:
                q += 1
                name = _['name']
                uuid= _['id']
                obj = _['type']
                url = f"https://{_HOST}/api/fmc_config/v1/domain/{domain}/object/operational/usage?filter=uuid:{uuid};type:{obj}"
                resp = requests.get(url, headers=headers, verify = False, timeout=10)
                try:
                    if resp.json()['paging']['count'] == 0:
                        n += 1
                        print(f'Type {obj} : {name} ->  Not used.')
                except KeyError:
                    pass
                except requests.exceptions.ReadTimeout:
                    print(f'HTTP Error: {resp.status_code}')
    except KeyboardInterrupt:
        exit()
    print(f" Number of unused objects {n} of {q} / {round(100 * n / q)}% ".center(100, '-'))

def main():
    start = datetime.now()
    try:
        fmc = FMC(hostname=_HOST, username=_USER, password=_PWD, domain='Global')
        headers = header(fmc)
        data = objectos(fmc)
        usages(data, fmc, headers)
        total_time = datetime.now() - start
        print(f" Execution time: {total_time} ".center(100, '-'))
    except (AuthError, requests.exceptions.ConnectionError):
        print(' Check your .env file '.center(80, '-'))

if __name__ == '__main__':
    main()
