import http.client
from threading import Timer, Thread
import json

def alive():
    #sends GET request to /alive and decodes HTTPresponse to UTF-8
    conn = http.client.HTTPConnection('192.168.42.1', 5000)
    conn.request('GET', '/alive')
    r = conn.getresponse()
    decoder = r.read().decode('utf-8')
    response = json.loads(decoder)
    t = Timer(2.0, alive)
    t.start()

    return print(response)

alive_thread = Thread(target=alive)

def establish():
    #sends GET request to /establish and decodes HTTPresponse to UTF-8
    conn = http.client.HTTPConnection('192.168.42.1', 5000)
    conn.request('GET', '/establish')
    r = conn.getresponse()
    decoder = r.read().decode('utf-8')
    response = json.loads(decoder)
    alive_thread.start()
    return print(response)

def water():
    # sends GET request to /water and decodes HTTPresponse to UTF-8
    conn = http.client.HTTPConnection('192.168.42.1', 5000)
    conn.request('GET', '/water')
    r = conn.getresponse()
    decoder = r.read().decode('utf-8')
    response = json.loads(decoder)

    return print(response)

def dbfetch():
    #Fetches API weather dB data from server
    conn = http.client.HTTPConnection('192.168.42.1', 5000)
    conn.request('GET', '/dbfetch')
    r = conn.getresponse()
    decoder = r.read().decode('utf-8')
    return print(decoder)

def storm(status):
    lib = {'status': status}
    json_encode = json.dumps(lib)
    headers = {'Content-type': 'application/json'}

    conn = http.client.HTTPConnection('192.168.42.1', 5000)
    conn.request('POST', '/storm', json_encode, headers)

    r = conn.getresponse()
    decoder = r.read().decode('utf-8')
    return print(decoder)

if __name__ == '__main__':
    establish()