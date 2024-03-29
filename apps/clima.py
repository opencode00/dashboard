import requests
from datetime import datetime
import urllib.parse as parse
import pprint

# url = 'https://www.el-tiempo.net/provincias/38/municipios/38038'
# https://www.el-tiempo.net/api/json/v2/provincias/38/municipios/38038
# https://www.el-tiempo.net/api/json/v2/provincias/38/municipios/38023

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

def getMoonPhases(size = 150):
    now = datetime.now()
    configMoon = {
        'LDZ': datetime(now.year, now.month, 1).timestamp(),
        'lang'  	:'es', 
        'month' 	: now.month,
        'year'  	: now.year,
        'size'		: size, 
        'lightColor': 'rgb(255,255,210)', 
        'shadeColor': 'black', 
        'texturize'	: 'true', 
    }          
    url = "https://www.icalendar37.net/lunar/api/?" + parse.urlencode(configMoon)
    s = requests.get(url, headers=headers)
    return s.json()

# # POr alguna razon el índice del día lo trae desordenado....
# def calculateIndex(d):
#     ti = d+22
#     if (ti>31):
#         ti = ti-31
#     return ti

def getTodayMoon():
    d = datetime.now()
    moon = getMoonPhases(75)
    html = ''
    weekday= d.weekday()
    day = d.day
    html = f'<b>{moon["nameDay"][weekday]}, {day} de {moon["monthName"]}</b><br/>'
    html += f'<div style="margin-top: 1em">{moon["phase"][str(day)]["svg"]}</div>'
    html += f'<div>{moon["phase"][str(day)]["phaseName"]}' 
    if moon['phase'][str(day)]['isPhaseLimit'] is not False:
        html+=''
    else:
        html+= "(" + str(round(moon['phase'][str(day)]['lighting'])) + ")%"
    html += "</div>"
    return html

def getMonthMoons():
    moons = getMoonPhases(75)
    html = ''
    for index, moon in moons['phase'].items():
        if(moon['isPhaseLimit'] is not False):
            html += '<div style="float:left; margin-left:10px; width: 90px; text-align: center ">'
            html += f'<div>{index}</div>' 
            html += f'<div>{moon["svg"]}</div>' 
            html += f'<div>{moon["phaseName"]}</div>' 
            html += '</div>'    
        
    return html

def getCalendarMoons():
    moons = getMoonPhases(75)
    html = ''
    for index, moon in moons['phase'].items():
        if ((int(index)-1)%7 == 0):
            html+='<br>'
        html += '<div style="display: inline-block; width: 90px; margin: 10px 10px;; vertical-align: middle">'
        html += f'<div>{index}</div>' 
        html += f'<div>{moon["svg"]}</div>' 
        html += f'<div>{moon["phaseName"]}</div>' 
        html += '</div>'    
    
    return html


if __name__ == '__main__':
    pprint.pprint(getCalendarMoons())
    # print(getMonthMoons())