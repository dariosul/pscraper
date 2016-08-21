from lxml import html
import requests
import csv

page = requests.get('http://state.1keydata.com/state-electoral-votes.php')
tree = html.fromstring(page.content)

state = tree.xpath("//table[@class ='content1']/tr/td/a/text()")
state_pages =tree.xpath("//table[@class = 'content1']/tr/td/a/@href") #tree.xpath('//a/@href')
state_names =tree.xpath("//table[@class = 'content1']/tr/td/a/text()")
state_names = [str(name) for name in state_names]

BASE_URL = 'http://state.1keydata.com/'
list_of_state_urls = [BASE_URL+link for link in state_pages[:50]]

def get_page_content_tree(page_url):
    page = requests.get(page_url)
    return html.fromstring(page.content)

def get_state_population(state_tree):
    res = state_tree.xpath("//table[@class='content']/tr/td/b/a[starts-with(.,'State Population (')]/../../../td/text()")#[@text() = 'State Population']/../td/text()")
    return  int(res[0].replace(',', ''))  if res else -1

def get_state_electoralvotes(state_tree):
    res = state_tree.xpath("//table[@class='content']/tr/td/b/a[starts-with(.,'Electoral Vote')]/../../../td/text()")#[@text() = 'State Population']/../td/text()")
    return int(res[0]) if res else -1

population_per_state = []
electoralvotes_per_state = []

for state_url in list_of_state_urls:
    current_state_tree = get_page_content_tree(state_url)
    population_per_state.append(get_state_population(current_state_tree))
    electoralvotes_per_state.append(get_state_electoralvotes(current_state_tree))

with open('state_data.csv', 'wb') as csvfile:
    state_writer = csv.writer(csvfile, delimiter = ',')
    for name,votes, population in zip(state_names, electoralvotes_per_state, population_per_state):
        state_writer.writerow( [name, population, votes])
