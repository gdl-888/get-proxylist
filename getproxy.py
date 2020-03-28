import re
import requests

rawList = requests.get("https://www.proxy-list.download/api/v1/get?type=http").text;

rawList = re.sub("\r", "", rawList);
ProxyList = re.sub("[:]\d{1,6}$", "", rawList, flags=re.MULTILINE);

print(ProxyList);

f = open("prxylist.txt", "w+");
f.write("Total " + str(len(ProxyList.split("\n"))) + " Proxies \r\n \r\n" + ProxyList);
f.close();
