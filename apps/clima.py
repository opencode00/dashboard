# from requests_html import HTMLSession
import requests
import pprint

# url = 'https://www.el-tiempo.net/provincias/38/municipios/38038'
# https://www.el-tiempo.net/api/json/v2/provincias/38/municipios/38038
# https://www.el-tiempo.net/api/json/v2/provincias/38/municipios/38023
# 0:= 0-24 ; 1: 0-12 ; 2: 12-24 ; 3: 0-6 ; 4: 6-12 ; 5: 12-18; 6: 18-24

# http://www.wdisseny.com/lluna/?lang=es
# https://tidesandcurrents.noaa.gov/astronomical.html
# http://jivebay.com/calculating-the-moon-phase/
# https://www.spaceweatherlive.com/es/calendario-de-fases-lunares.html


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
    'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;'
    'q=0.9,image/webp,*/*;q=0.8'}

def tiempo(mun = 'sc'):
    url = 'https://www.el-tiempo.net/api/json/v2/provincias/38/municipios/38038'
    if mun != 'sc':
        url = 'https://www.el-tiempo.net/api/json/v2/provincias/38/municipios/38023'
    
    response = requests.get(url, headers=headers).json()
    proximos = []

    fecha = response['fecha']
    icon = response['stateSky']['id']
    desc = response['stateSky']['description']
    tmax = response['temperaturas']['max']
    tmin = response['temperaturas']['min']
    hum = response['humedad']   
    viento = response['viento']   
    plluvia = response['lluvia'] 
    clluvia = response['precipitacion']

    proximos.append({'fecha': fecha, 'plluvia':plluvia, 'cielo':icon, 'viento': viento, 'sens_termica': tmax+"-"+tmin, 'desc':desc, 'humedad': hum, 'cant_lluvia': clluvia})
    for dia in response['proximos_dias']:
        fecha = dia['@attributes']['fecha']
        plluvia = max([int(x) for x in dia['prob_precipitacion']])
        if (len(dia['estado_cielo']) > 2 ):
            cielo = dia['estado_cielo'][1] + "/" + dia['estado_cielo'][2] # 12-24
        else:
            cielo = dia['estado_cielo'][0]

        if (len(dia['viento']) > 2):
            viento = dia['viento'][0]['velocidad'] + "" + dia['viento'][0]['direccion']
        else:
            viento = dia['viento']['velocidad'] + " " + dia['viento']['direccion']

        tsens = dia['sens_termica']['maxima'] + "-" + dia['sens_termica']['minima']

        proximos.append({'fecha': fecha, 'plluvia':plluvia, 'cielo':cielo, 'viento': viento, 'sens_termica': tsens, 'desc':'', 'humedad':'', 'cant_lluvia': ''})

    return proximos


if __name__ == '__main__':
    pprint.pprint(sc())
    # sc()