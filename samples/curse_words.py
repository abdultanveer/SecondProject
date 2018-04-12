from urllib.request import urlopen
from urllib.parse import urlencode


def read_file():
   contents = open("C:\\Users\\Ansari\\Desktop\\cursewords\\movie_quotes.txt")
   quotes = contents.read()
   #print(quotes)
   check_badwords(quotes)

def check_badwords(word_tocheck):
    abc = "http://www.wdylike.appspot.com/?q="+word_tocheck
    #abc.encode('utf-8')
    abc = abc.encode('ascii', 'ignore').decode('ascii')

    connection =   urlopen(abc)

    output = connection.read()
    print(output)

    '''data = urllib.parse.urlencode(d).encode("utf-8")
    req = urllib.request.Request("http://www.wdylike.appspot.com")
    with urllib.request.urlopen(req, q=word_tocheck) as f:
        resp = f.read()
        print(resp)'''

read_file()
