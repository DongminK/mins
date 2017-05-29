import urllib2
from OpenSSL import SSL

url = 'https:\/\/www.googleapis.com/customsearch/v1?'
apiKey = 'key=AIzaSyDnsiSk70gNNHsZqiu4OCz_K_tb1K3i3b4'
engineId = 'cx=004703749585167965054%3Apix_u24kxva'

if __name__ == "__main__":
    searchContext = input("search : ")
    print(searchContext)

#    data = urllib2.urlopen(url + "q=" + searchContext + "&" + apiKey + "&" + engineId)
    #print(data)
