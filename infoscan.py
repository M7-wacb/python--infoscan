from mitmproxy.http import flow
from mitmproxy import ctx
import mitmproxy
import re
import threading
import aiohttp
import asyncio
from colorama import init,Fore
init()
def response(flow):
    if flow.response.status_code == 200:
        url_s = flow.request.url
        info_s =flow.response.text
        handle(info_s=info_s,url_s=url_s)
def handle(info_s,url_s):
    threading.Thread(target=go,args=(info_s,url_s,)).start()
def go(info_s,url_s):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url_s)
    url = re.sub(r"[\[\]']", "", str(url))
    chunk_size = max(1, len(info_s) // 4)
    chunks = [info_s[i:i + chunk_size] for i in range(0, len(info_s), chunk_size)]
    threads = []
    for i in chunks:
        pattern = r'[\'"](?:\/|\.\.\/|\.\/)([^\/\>\< \)\(\{\}\,\'\"\\]([^\>\< \)\(\{\}\,\'\"\\])*?|[^\/\>\< \)\(\{\}\,\'\"\\][\w\/]*?\/[\w\/]*?)[\'"]'
        thread = threading.Thread(target=lambda: echo(re.findall(pattern, i),url))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def echo(res,url):
    path = []
    for i in res:
        end = i[0].split('.')[-1]
        blacklist = ['gif','jpg','png','html','htmls','css','htm','svg'] #黑名单
        # if end == 'gif' or end == 'jpg' or end == 'png' or end == 'htm':
        if end in blacklist:
            continue
        urls = (str(url+'/')+str(i[0]))
        asyncio.run(main(url=urls))

async def main(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                if res.status == 200:
                    print(Fore.GREEN+'[{0}]'.format(res.status)+Fore.RESET+url)
                    # print(f"[{res.status}]{url}")
                else:
                    print(Fore.RED+f"[{res.status}]"+Fore.RESET+url)
                    # print(f"[{res.status}]{url}")
    except:
        print(Fore.RED+'MAIN ERROR!')