# # import socket
# # # create an INET, STREAMing socket 81.192.163.59
# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # print("What website's ip would you like to find?")
# # print((socket.gethostbyname('extranet.marocmeteo.ma'), 80))
# import socket #module for gethostbyname
# website = 'extranet.marocmeteo.ma'# you can put any websitewww.google.com142.250.200.196
# ip = socket.gethostbyname(website)
# print(ip)