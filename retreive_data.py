from lxml import html
import requests

page = requests.get('http://state.1keydata.com/state-electoral-votes.php')
tree = html.fromstring(page.content)

state = tree.xpath("//table[@class ='content1']/tr/td/a/text()")
state_pages =tree.xpath("//table[@class = 'content1']/tr/td/a/@href") #tree.xpath('//a/@href')

BASE_URL = 'http://state.1keydata.com/'
list_of_state_urls = [BASE_URL+link for link in state_pages[:50]]

def get_page_content_tree(page_url):
    page = requests.get(page_url)
    return html.fromstring(page.content)

def get_state_population(state_tree):
    return state_tree.xpath("//table[@class='content']/tr/td/b/a[starts-with(.,'State Population (')]/../../../td/text()")#[@text() = 'State Population']/../td/text()")

def get_state_electoralvotes(state_tree):
    return state_tree.xpath("//table[@class='content']/tr/td/b/a[starts-with(.,'Electoral Votes')]/../../../td/text()")#[@text() = 'State Population']/../td/text()")

print get_state_population(get_page_content_tree(list_of_state_urls[0]))

for state_url in list_of_state_urls:
    print state_url
