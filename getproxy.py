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

f = open("prxylist.txt", "w+");
f.write("Total " + str(len(ProxyList.split("\n"))) + " Proxies \r\n \r\n" + ProxyList);
f.close();
