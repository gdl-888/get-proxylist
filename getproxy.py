import re
import requests

reqTypes = ['http', 'https', 'socks4', 'socks5'];

rawList = "";

for reqType in reqTypes:
    rawList += requests.get("https://www.proxy-list.download/api/v1/get?type=" + reqType).text;
    print(reqType.upper() + " proxies added.");
    rawList += "\r\n";

rawList = re.sub("\r", "", rawList);
ProxyList = re.sub("[:]\d{1,6}$", "", rawList, flags=re.MULTILINE);

RevList = "";

for ip in ProxyList.split('\n'):
    RevList = ip + "\n" + RevList;

f = open("prxylist.txt", "w+");
f.write("Total " + str(len(ProxyList.split("\n"))) + " Proxies \r\n \r\n" + ProxyList);
f.close();

f = open("rpxylist.txt", "w+");
f.write("Total " + str(len(RevList.split("\n"))) + " Proxies in reversed order \r\n \r\n" + RevList);
f.close();
