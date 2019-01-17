import multiprocessing
import sys
import os
import re
import logging
import requests
import time


def crawlComments(movieCode):
    headers = {
        'accept': "application/vnd.frograms+json;version=20",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        'cookie': "_ga=GA1.2.904402677.1546843109; _gid=GA1.2.375865238.1547228674; _s_guit=f0f0bb245308866908b0f66047b27c354434885950e43bafe8501a2bce56; fbm_126765124079533=base_domain=.watcha.com; _gat=1; _guinness_session=bGVvQk5CeWdmbWJNSURNc25mRXY2R3ZaUElKYmJPcFViZ0dRelFHK0ZYSWFmSXZYT1UyUWYvL1JJWXVVK0JRUThuamlld2ZxbHBUWXAyZnphR21GN1hna05oam40ZlN1RDVRSUs1ejFHRHM9LS1FZHdva3ZJaG95c1pqd0xHRnV1NUp3PT0%3D--6f705ce8a14af3fccdc6b070a71a3cacb9285100; fbsr_126765124079533=pxskb9g2p48hPyp5WsX2FvRe4YToqJMRA0SsCqcdaOQ.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURNMkgzZlduODBWR1BsSHFfMnp2d1ppaVFXdTJreTQtT1pseFg4dzlIblpjSFFvVTY5Z2JEYVZ4ejloaWl3QlRpeTUtejJtUURha21lczNHcjdCcDZ2RG5lVVVrVXNaZEtvSUFYVmcwT0FkMUUzV2diUWVoSkNnQVF3MXhMbm9FRTdueUdzeTNTeWkyME5ITzd0RG9jYnVadEJVMklDZGk4b0RCcndfZml3TkZ6TDdPNVNTUkhpS1VLX1pzR2RwOEtaX0xmNXo1eUxmdXMySklTWWdRSE9VZ0ZYZjROOGNOSV83ak5HY2dSMDZuWm8xY3o5NHUySzZnQWdBXzM5VENkRkdENzBaWFNNUnpvS0dxMDRrX1dEbW5aTktTM2FuUHNYUi03eUhoakl6SUozcmp1WW4wYW1yN0w1eS1XNmk0OFo3d0Q1X0JKX2FlUHlsVkxnQUpkdjRJQUt6clVpbmFJNVp0cG50NnF6ZnciLCJpc3N1ZWRfYXQiOjE1NDcyNzA4OTcsInVzZXJfaWQiOiIyMjU1MTM2ODQ0NzA5MDcyIn0",
        'dnt': "1",
        'origin': "https://watcha.com",
        'referer': "https://watcha.com/ko-KR/contents/mP5m3GO/comments",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.53.4 Safari/537.36",
        'x-watcha-client': "Watcha-WebApp",
        'x-watcha-client-language': "ko",
        'x-watcha-client-region': "KR",
        'x-watcha-client-version': "1.0.0",
        'cache-control': "no-cache",
        'Postman-Token': "1978cee3-436b-4ea4-a333-93104d50e92b"
    }
    session = requests.Session()

    next_uri = "https://api.watcha.com/api/contents/{}/comments?filter=all&order=popular&page=1&size=100".format(movieCode)

    while next_uri:
        try:
            content = session.get(next_uri, headers=headers, timeout=5).json()
        except requests.exceptions.RequestException as re:
            logging.warning("{} --> {}".format(next_uri, re))
            break

        localLines = list()
        for c in list(filter(lambda c: c['user_content_action']['rating'], content['result']['result'])):
            for s in list(filter(lambda f: len(f.strip()), c['text'].splitlines())):
                localLines.append("__label__{} {}".format(c['user_content_action']['rating'], s.strip()))
        next_uri = 'https://api.watcha.com{}'.format(content['result']['next_uri']) if content['result']['next_uri'] else None

    taskQueue.put(localLines)

    return


def writer():
    with open('result.txt', 'w') as result:
        while True:
            try:
                lines = taskQueue.get(timeout=10)
            except:
                logging.warning('queue empty')
                break
            result.writelines('{}\n'.format(re.sub('\s\s+', ' ', l)) for l in lines)


def initializer(q):
    global taskQueue
    taskQueue = q


if __name__ == "__main__":
    logging.basicConfig(filename='event.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info('start logging')

    movieCodeSet = list()

    with open('movieCodeRandom.txt') as movieCode:
        for l in movieCode.readlines():
            movieCodeSet.append(l.rstrip('\n'))

    # print(str(int(process.memory_info().rss / 1024 / 1024)) + ' MB')
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count, initializer=initializer, initargs=(multiprocessing.Queue(), ))
    print('pool size : ' + str(cpu_count))
    pool.apply_async(writer)
    pool.map_async(crawlComments, list(set(movieCodeSet)))
    pool.close()
    pool.join()

    print('all done')
