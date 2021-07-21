# Alan Baines

import http.server
import socketserver
import os


# aliases
exists = os.path.exists
abspath = os.path.abspath
join = os.path.join


# settings
ServerPort = 8000


# code
cwd = os.getcwd()

doc = abspath("../docs/")

# expected files
indexHtml = join(doc,"index.html")
scriptJs = join(doc,"script.js")
wordsOut = join(doc,"words.out")

print(indexHtml,exists(indexHtml))
print(scriptJs,exists(scriptJs))
print(wordsOut,exists(wordsOut))


# http request handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):
   def __init__(self,*args,**kwargs):
      super().__init__(*args, directory=doc,**kwargs)
      

# verify files before starting server
if exists(indexHtml) and exists(scriptJs) and exists(wordsOut):

   server_address = ("",ServerPort)
   
   print("Happy Setup. Starting Server.",server_address,doc)

   # start http server
   with socketserver.TCPServer(server_address, RequestHandler) as httpServer:
      print("Http server",server_address)
      httpServer.serve_forever()
      print("The End")

else:
   print("Missing critical file. Please fix before starting.")

