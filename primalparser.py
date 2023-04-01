import requests
import xml.etree.ElementTree as ET
import gzip
import io

# Example list of sitemap URLs to download
sitemap_urls = [
"https://www.arjeplog.se/sitemap1.xml.gz",
"https://www.arvika.se/sitemap1.xml.gz",
"https://www.bjurholm.se/sitemap1.xml.gz",
"https://www.bollnas.se/sitemap1.xml.gz",
"https://www.borlange.se/sitemap1.xml.gz",
"https://www.boras.se/sitemap1.xml.gz",
"https://www.botkyrka.se/sitemap1.xml.gz",
"https://www.ekero.se/sitemap1.xml.gz",
"https://www.emmaboda.se/sitemap1.xml.gz",
"https://www.enkoping.se/sitemap1.xml.gz",
"https://www.eskilstuna.se/sitemap1.xml.gz",
"https://www.essunga.se/sitemap1.xml.gz",
"https://www.falkoping.se/sitemap1.xml.gz",
"https://www.falun.se/sitemap1.xml.gz",
"https://www.gislaved.se/sitemap1.xml.gz",
"https://www.gnesta.se/sitemap1.xml.gz",
"https://www.gnosjo.se/sitemap1.xml.gz",
"https://www.gullspang.se/sitemap1.xml.gz",
"https://www.hagfors.se/sitemap1.xml.gz",
"https://www.hallsberg.se/sitemap1.xml.gz",
"https://www.hallstahammar.se/sitemap1.xml.gz",
"https://www.halmstad.se/sitemap1.xml.gz",
"https://www.haparanda.se/sitemap1.xml.gz",
"https://www.heby.se/sitemap1.xml.gz",
"https://www.herrljunga.se/sitemap1.xml.gz",
"https://www.hudiksvall.se/sitemap1.xml.gz",
"https://www.harnosand.se/sitemap1.xml.gz",
"https://www.hassleholm.se/sitemap1.xml.gz",
"https://www.jarfalla.se/sitemap1.xml.gz",
"https://www.jonkoping.se/sitemap1.xml.gz",
"https://www.kalmar.se/sitemap1.xml.gz",
"https://www.karlskoga.se/sitemap1.xml.gz",
"https://www.katrineholm.se/sitemap1.xml.gz",
"https://www.kinda.se/sitemap1.xml.gz",
"https://www.kiruna.se/sitemap1.xml.gz",
"https://www.knivsta.se/sitemap1.xml.gz",
"https://www.kramfors.se/sitemap1.xml.gz",
"https://www.krokom.se/sitemap1.xml.gz",
"https://www.kumla.se/sitemap1.xml.gz",
"https://www.kungsbacka.se/sitemap1.xml.gz",
"https://www.kungsor.se/sitemap1.xml.gz",
"https://www.kavlinge.se/sitemap1.xml.gz",
"https://www.laxa.se/sitemap1.xml.gz",
"https://www.lerum.se/sitemap1.xml.gz",
"https://www.lidingo.se/sitemap1.xml.gz",
"https://www.lidkoping.se/sitemap1.xml.gz",
"https://www.lindesberg.se/sitemap1.xml.gz",
"https://www.ljusdal.se/sitemap1.xml.gz",
"https://www.lomma.se/sitemap1.xml.gz",
"https://www.ludvika.se/sitemap1.xml.gz",
"https://www.lund.se/sitemap1.xml.gz",
"https://www.lysekil.se/sitemap1.xml.gz",
"https://www.malmo.se/sitemap1.xml.gz",
"https://www.malung-salen.se/sitemap1.xml.gz",
"https://www.mariestad.se/sitemap1.xml.gz",
"https://www.markaryd.se/sitemap1.xml.gz",
"https://www.mjolby.se/sitemap1.xml.gz",
"https://www.mullsjo.se/sitemap1.xml.gz",
"https://www.molndal.se/sitemap1.xml.gz",
"https://www.nordanstig.se/sitemap1.xml.gz",
"https://www.nordmaling.se/sitemap1.xml.gz",
"https://www.norrkoping.se/sitemap1.xml.gz",
"https://www.nykvarn.se/sitemap1.xml.gz",
"https://www.ockelbo.se/sitemap1.xml.gz",
"https://www.olofstrom.se/sitemap1.xml.gz",
"https://www.orsa.se/sitemap1.xml.gz",
"https://www.orust.se/sitemap1.xml.gz",
"https://www.oxelosund.se/sitemap1.xml.gz",
"https://www.ragunda.se/sitemap1.xml.gz",
"https://www.ronneby.se/sitemap1.xml.gz",
"https://www.rattvik.se/sitemap1.xml.gz",
"https://www.sandviken.se/sitemap1.xml.gz",
"https://www.sigtuna.se/sitemap1.xml.gz",
"https://www.skelleftea.se/sitemap1.xml.gz",
"https://www.solleftea.se/sitemap1.xml.gz",
"https://www.strangnas.se/sitemap1.xml.gz",
"https://www.stromsund.se/sitemap1.xml.gz",
"https://www.sundsvall.se/sitemap1.xml.gz",
"https://www.svalov.se/sitemap1.xml.gz",
"https://www.svenljunga.se/sitemap1.xml.gz",
"https://www.soderhamn.se/sitemap1.xml.gz",
"https://www.solvesborg.se/sitemap1.xml.gz",
"https://www.tanum.se/sitemap1.xml.gz",
"https://www.tidaholm.se/sitemap1.xml.gz",
"https://www.tierp.se/sitemap1.xml.gz",
"https://www.tjorn.se/sitemap1.xml.gz",
"https://www.tyreso.se/sitemap1.xml.gz",
"https://www.toreboda.se/sitemap1.xml.gz",
"https://www.uddevalla.se/sitemap1.xml.gz",
"https://www.umea.se/sitemap1.xml.gz",
"https://www.upplands-bro.se/sitemap1.xml.gz",
"https://www.upplandsvasby.se/sitemap1.xml.gz",
"https://www.vansbro.se/sitemap1.xml.gz",
"https://www.varberg.se/sitemap1.xml.gz",
"https://www.vaxholm.se/sitemap1.xml.gz",
"https://www.vimmerby.se/sitemap1.xml.gz",
"https://www.vindeln.se/sitemap1.xml.gz",
"https://www.vargarda.se/sitemap1.xml.gz",
"https://www.vanersborg.se/sitemap1.xml.gz",
"https://www.vannas.se/sitemap1.xml.gz",
"https://www.varmdo.se/sitemap1.xml.gz",
"https://www.varnamo.se/sitemap1.xml.gz",
"https://www.vaxjo.se/sitemap1.xml.gz",
"https://www.ange.se/sitemap1.xml.gz",
"https://www.astorp.se/sitemap1.xml.gz",
"https://www.almhult.se/sitemap1.xml.gz",
"https://www.alvdalen.se/sitemap1.xml.gz",
"https://www.alvkarleby.se/sitemap1.xml.gz",
"https://www.ockero.se/sitemap1.xml.gz",
"https://www.orebro.se/sitemap1.xml.gz",
"https://www.orkelljunga.se/sitemap1.xml.gz",
"https://www.ornskoldsvik.se/sitemap1.xml.gz",
"https://www.ostersund.se/sitemap1.xml.gz",
]

# Function to download sitemap and parse XML
def parse_sitemap(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        try:
            if url.endswith('.gz'):
                # Handle gzip-compressed sitemap
                content = gzip.decompress(response.content)
                root = ET.fromstring(content)
            else:
                # Handle uncompressed sitemap
                root = ET.fromstring(response.content)
            return root
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"Error: Failed to download sitemap from {url}")

# Function to extract PDF links and <lastmod> date from sitemap XML
def extract_pdf_links_and_dates(root):
    pdf_links_and_dates = []
    for elem in root.iter():
        if elem.tag.endswith('url'):
            url = ''
            lastmod = ''
            for child_elem in elem.iter():
                if child_elem.tag.endswith('loc'):
                    url = child_elem.text
                if child_elem.tag.endswith('lastmod'):
                    lastmod = child_elem.text
            if url.endswith('.pdf'):
                pdf_links_and_dates.append((url, lastmod))
    return pdf_links_and_dates

# Loop over sitemap URLs, extract PDF links and <lastmod> dates, and store in list
pdf_links_and_dates = []
for sitemap_url in sitemap_urls:
    root = parse_sitemap(sitemap_url)
    if root is not None:
        pdf_links_and_dates += extract_pdf_links_and_dates(root)

# Sort list by <lastmod> date (if available)
pdf_links_and_dates.sort(key=lambda x: x[1], reverse=True)

# Write sorted list of PDF links and <lastmod> dates to a text file
with open('docs.txt', 'w') as file:
    count = 0
    for pdf_link, lastmod in pdf_links_and_dates:
        count += 1
        file.write(f"{pdf_link} ({lastmod})\n")
    
print(f"{count} PDF links and <lastmod> dates written to docs.txt")
