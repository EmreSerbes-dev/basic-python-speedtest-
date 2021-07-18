import speedtest
import os

os.system("pip install speedtest-cli")
test = speedtest.Speedtest()

print("Serverlar yükleniyor...")
test.get_servers() # getting servers
print("En iyi server bulunuyor...")
best = test.get_best_server() # getting best server
print("En iyi server bulundu")
print("Download test ediliyor...")
downT = test.download()
print("Upload test ediliyor...")
upT = test.upload()
print("Ping test ediliyor...")
ping = test.results.ping

print(f"Download hızı: " + str(downT / 1024 / 1024))
print(f"Upload hızı: " + str(upT/ 1024 / 1024))
print(f"Ping: " + str(ping))









