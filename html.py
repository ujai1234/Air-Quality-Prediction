import os
import time
import requests
import sys


def retrieve_html():
    for year in range(2013, 2019):
        for month in range(1, 13):
            if month < 10:
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            texts = requests.get(url)

            if texts.status_code == 20:
                text_utf = texts.text.encode('utf=8')
                print("Data HTML berhasil diambil untuk {}/{}".format(month, year))

                if not os.path.exists("Data/Html_Data/{}".format(year)):
                    os.makedirs("Data/Html_Data/{}".format(year))
                    print("Folder berhasil dibuat.")
                    
                with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                    output.write(text_utf)
            
            else:
                print("Gagal mengambil data HTML untuk {}/{}. Kode status: {}".format(month, year, texts.status_code))

        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    time_taken = stop_time - start_time
    print("time taken: {}".format(time_taken))