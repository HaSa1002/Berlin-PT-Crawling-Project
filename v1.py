import urllib.request
import datetime
import bs4
#Define the base scrapping parts
sbahn = "http://www.s-bahn-berlin.de/bauinformationen/betriebslage.htm";
sbahnPlanned = "http://www.s-bahn-berlin.de/bauinformationen/uebersicht";
bvg = "http://www.bvg.de/de/Fahrinfo/Verkehrsmeldungen";

#Define the base tags
b_sbahn = "http://www.s-bahn-berlin.de/"
b_bvg = "http://www.bvg.de/"

def crawl(url, b_url, file_name):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(url), "lxml");
    #Make the tags production ready
    tag = soup.new_tag("base", href=b_url);

    soup.head.link.insert_before(tag);
    with open("data/"+file_name, 'wb') as file:
        file.write(soup.prettify("ISO 8859-1"));

    
run = 1;
time = datetime.datetime.now();
interval = datetime.timedelta(0,20);
while (run):
    if (time + interval < datetime.datetime.now()):
        crawl(sbahn, b_sbahn, datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d.%H-%M-%S.%z")+"sbahn.html");
        crawl(sbahnPlanned, b_sbahn, datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d.%H-%M-%S.%z")+"sbahnGeplant.html");
        crawl(bvg, b_bvg, datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d.%H-%M-%S.%z")+"bvg.html");
        time = datetime.datetime.now();
        print (str(time)+": Pages crawlt");
    #Do some input checks to cancel the loop
