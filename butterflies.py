
#-- OBJECTIVE 1: Scrape butterfly species --#


#-- Import everything --#

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from itertools import zip_longest
import requests
import time
import csv


#-- Make an empty list for all the species --#

butterflies = []


#-- GET A THROUGH E --#

url1 = 'https://en.wikipedia.org/wiki/Category:Butterflies_of_North_America'

#-- Make ~the soup~ --#
webpage1 = requests.get(url1)
soup1 = BeautifulSoup(webpage1.text, 'html.parser')

page_div1 = soup1.find('div', id='content')

body_div1 = page_div1.find('div', id='bodyContent')

content_div1 = body_div1.find('div', id='mw-content-text')

pages_div1 = content_div1.find('div', id='mw-pages')

content_ltr1 = pages_div1.find('div', class_='mw-content-ltr')

category_div1 = content_ltr1.find('div', class_='mw-category')

category_groups1 = category_div1.find_all('div', class_='mw-category-group')

#------------------------------------------#

a_div = category_groups1[1]

a_list = a_div.find('ul')

a_list_li = a_list.find_all('li')

for a in a_list_li:
    a_species = a.get_text()
    butterflies.append(a_species)

#------------------------------------------#

b_div = category_groups1[2]

b_list = b_div.find('ul')

b_list_li = b_list.find_all('li')

for b in b_list_li:
    b_species = b.get_text()
    butterflies.append(b_species)

#------------------------------------------#

c_div = category_groups1[3]

c_list = c_div.find('ul')

c_list_li = c_list.find_all('li')

for c in c_list_li:
    c_species = c.get_text()
    butterflies.append(c_species)

#------------------------------------------#

d_div = category_groups1[4]

d_list = d_div.find('ul')

d_list_li = d_list.find_all('li')

for d in d_list_li:
    d_species = d.get_text()
    butterflies.append(d_species)

#------------------------------------------#

e_div = category_groups1[5]

e_list = e_div.find('ul')

e_list_li = e_list.find_all('li')

for e in e_list_li:
    e_species = e.get_text()
    butterflies.append(e_species)


#-- GET E THROUGH S --#


url2 = 'https://en.wikipedia.org/w/index.php?title=Category:Butterflies_of_North_America&pagefrom=Eurema+nicippe#mw-pages'

#-- Make ~the soup~
webpage2 = requests.get(url2)
soup2 = BeautifulSoup(webpage2.text, 'html.parser')

page_div2 = soup2.find('div', id='content')

body_div2 = page_div2.find('div', id='bodyContent')

content_div2 = body_div2.find('div', id='mw-content-text')

pages_div2 = content_div2.find('div', id='mw-pages')

content_ltr2 = pages_div2.find('div', class_='mw-content-ltr')

category_div2 = content_ltr2.find('div', class_='mw-category')

category_groups2 = category_div2.find_all('div', class_='mw-category-group')

#------------------------------------------#

e_cont_div = category_groups2[0]

e_cont_list = e_cont_div.find('ul')

e_cont_list_li = e_cont_list.find_all('li')

for e_cont in e_cont_list_li:
    e_cont_species = e_cont.get_text()
    butterflies.append(e_cont_species)

#------------------------------------------#

f_div = category_groups2[1]

f_list = f_div.find('ul')

f_list_li = f_list.find_all('li')

for f in f_list_li:
    f_species = f.get_text()
    butterflies.append(f_species)

#------------------------------------------#

g_div = category_groups2[2]

g_list = g_div.find('ul')

g_list_li = g_list.find_all('li')

for g in g_list_li:
    g_species = g.get_text()
    butterflies.append(g_species)

#------------------------------------------#

h_div = category_groups2[3]

h_list = h_div.find('ul')

h_list_li = h_list.find_all('li')

for h in h_list_li:
    h_species = h.get_text()
    butterflies.append(h_species)

#------------------------------------------#

i_div = category_groups2[4]

i_list = i_div.find('ul')

i_list_li = i_list.find_all('li')

for i in i_list_li:
    i_species = i.get_text()
    butterflies.append(i_species)

#------------------------------------------#

j_div = category_groups2[5]

j_list = j_div.find('ul')

j_list_li = j_list.find_all('li')

for j in j_list_li:
    j_species = j.get_text()
    butterflies.append(j_species)

#------------------------------------------#

k_div = category_groups2[6]

k_list = k_div.find('ul')

k_list_li = k_list.find_all('li')

for k in k_list_li:
    k_species = k.get_text()
    butterflies.append(k_species)

#------------------------------------------#

l_div = category_groups2[7]

l_list = l_div.find('ul')

l_list_li = l_list.find_all('li')

for l in l_list_li:
    l_species = l.get_text()
    butterflies.append(l_species)

#------------------------------------------#

m_div = category_groups2[8]

m_list = m_div.find('ul')

m_list_li = m_list.find_all('li')

for m in m_list_li:
    m_species = m.get_text()
    butterflies.append(m_species)

#------------------------------------------#

n_div = category_groups2[9]

n_list = n_div.find('ul')

n_list_li = n_list.find_all('li')

for n in n_list_li:
    n_species = n.get_text()
    butterflies.append(n_species)

#------------------------------------------#

o_div = category_groups2[10]

o_list = o_div.find('ul')

o_list_li = o_list.find_all('li')

for o in o_list_li:
    o_species = o.get_text()
    butterflies.append(o_species)

#------------------------------------------#

p_div = category_groups2[11]

p_list = p_div.find('ul')

p_list_li = p_list.find_all('li')

for p in p_list_li:
    p_species = p.get_text()
    butterflies.append(p_species)

#------------------------------------------#

q_div = category_groups2[12]

q_list = q_div.find('ul')

q_list_li = q_list.find_all('li')

for q in q_list_li:
    q_species = q.get_text()
    butterflies.append(q_species)

#------------------------------------------#

r_div = category_groups2[13]

r_list = r_div.find('ul')

r_list_li = r_list.find_all('li')

for r in r_list_li:
    r_species = r.get_text()
    butterflies.append(r_species)

#------------------------------------------#

s_div = category_groups2[14]

s_list = s_div.find('ul')

s_list_li = s_list.find_all('li')

for s in s_list_li:
    s_species = s.get_text()
    butterflies.append(s_species)


#-- GET S THROUGH Z --#



url3 = 'https://en.wikipedia.org/w/index.php?title=Category:Butterflies_of_North_America&pagefrom=Speyeria+coronis#mw-pages'

#-- Make ~the soup~
webpage3 = requests.get(url3)
soup3 = BeautifulSoup(webpage3.text, 'html.parser')

page_div3 = soup3.find('div', id='content')

body_div3 = page_div3.find('div', id='bodyContent')

content_div3 = body_div3.find('div', id='mw-content-text')

pages_div3 = content_div3.find('div', id='mw-pages')

content_ltr3 = pages_div3.find('div', class_='mw-content-ltr')

category_div3 = content_ltr3.find('div', class_='mw-category')

category_groups3 = category_div3.find_all('div', class_='mw-category-group')

#------------------------------------------#

s_cont_div = category_groups3[0]

s_cont_list = s_cont_div.find('ul')

s_cont_list_li = s_cont_list.find_all('li')

for s_cont in s_cont_list_li:
    s_cont_species = s_cont.get_text()
    butterflies.append(s_cont_species)

#------------------------------------------#

t_div = category_groups3[1]

t_list = t_div.find('ul')

t_list_li = t_list.find_all('li')

for t in t_list_li:
    t_species = t.get_text()
    butterflies.append(t_species)

#------------------------------------------#

u_div = category_groups3[2]

u_list = u_div.find('ul')

u_list_li = u_list.find_all('li')

for u in u_list_li:
    u_species = u.get_text()
    butterflies.append(u_species)

#------------------------------------------#

v_div = category_groups3[3]

v_list = v_div.find('ul')

v_list_li = v_list.find_all('li')

for v in v_list_li:
    v_species = v.get_text()
    butterflies.append(v_species)

#------------------------------------------#

w_div = category_groups3[4]

w_list = w_div.find('ul')

w_list_li = w_list.find_all('li')

for w in w_list_li:
    w_species = w.get_text()
    butterflies.append(w_species)

#------------------------------------------#

z_div = category_groups3[5]

z_list = z_div.find('ul')

z_list_li = z_list.find_all('li')

for z in z_list_li:
    z_species = z.get_text()
    butterflies.append(z_species)

#------------------------------------------#










#-- OBJECTIVE 2: Remove species that don't have data --#



#-- Make an empty list for each species's partial link --#

bfly_partial_links = []

for eachspecies in butterflies:
    species_partials = eachspecies.replace(' ', '-')
    bfly_partial_links.append(species_partials)


#-- Make an empty list for species with no results --#

no_results = []


for eachpartial in bfly_partial_links:

    driver = webdriver.Chrome('/.../chromedriver')
    driver.get('https://www.butterfliesandmoths.org/species/' + eachpartial)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    time.sleep(2)

    try:

        soup.find('div', class_='moscone-column-content-region moscone-sidebar panel-panel')

    except:

        if soup.find('div', class_='moscone-column-content-region moscone-sidebar panel-panel') == None:
            no_results.append(eachpartial)
            continue



def remove_missing_species():

    for eachresult in no_results:
        missing_species = eachresult.replace('-', ' ')
        butterflies.remove(missing_species)

    return butterflies


final_species = remove_missing_species()


final_partial_links = []


for eachfinal in final_species:
    final_partials = eachfinal.replace(' ', '-')
    final_partial_links.append(final_partials)




#-- OBJECTIVE 3: Acquire data on each butterfly species --#


#-- Make empty lists --#

family = []

subfamily = []

identification = []

wingspan = []

caterpillarhost = []

adultfood = []

habitat = []

flight = []

range = []

#----------------------#



for eachfinalspeciespartial in final_partial_links:

    driver = webdriver.Chrome('/.../chromedriver')
    driver.get('https://www.butterfliesandmoths.org/species/' + eachfinalspeciespartial)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    try:
        content_column = soup.find('div', class_='moscone-column-content-region moscone-sidebar panel-panel')

    #----------------------------------------------------------------------------------------#

        family_div = content_column.find('div', class_='views-field views-field-field-family')

        family_span = family_div.find('span', class_='field-content')

        butterfly_family = family_span.find('a').get_text()

        family.append(butterfly_family)

    #----------------------------------------------------------------------------------------#

        subfamily_div = content_column.find('div', class_='views-field views-field-field-subfamily')

        subfamily_span = subfamily_div.find('span', class_='field-content')

        butterfly_subfamily = subfamily_span.get_text()

        subfamily.append(butterfly_subfamily)

    #----------------------------------------------------------------------------------------#

        identification_div = content_column.find('div', class_='views-field views-field-field-identification')

        identification_span = identification_div.find('span', class_='field-content')

        butterfly_identification = identification_span.get_text()

        identification.append(butterfly_identification)

    #----------------------------------------------------------------------------------------#

        wingspan_div = content_column.find('div', class_='views-field views-field-field-wingspan')

        wingspan_span = wingspan_div.find('span', class_='field-content')

        butterfly_wingspan = wingspan_span.get_text()

        wingspan.append(butterfly_wingspan)

    #----------------------------------------------------------------------------------------#

        cathost_div = content_column.find('div', class_='views-field views-field-field-caterpillarhosts')

        cathost_span = cathost_div.find('span', class_='field-content')

        butterfly_caterpillarhost = cathost_span.get_text()

        caterpillarhost.append(butterfly_caterpillarhost)

    #----------------------------------------------------------------------------------------#

        adultfood_div = content_column.find('div', class_='views-field views-field-field-adultfood')

        adultfood_span = adultfood_div.find('span', class_='field-content')

        butterfly_adultfood = adultfood_span.get_text()

        adultfood.append(butterfly_adultfood)

    #----------------------------------------------------------------------------------------#

        habitat_div = content_column.find('div', class_='views-field views-field-field-habitat')

        habitat_span = habitat_div.find('span', class_='field-content')

        butterfly_habitat = habitat_span.get_text()

        habitat.append(butterfly_habitat)

    #----------------------------------------------------------------------------------------#

        flight_div = content_column.find('div', class_='views-field views-field-field-flight')

        flight_span = flight_div.find('span', class_='field-content')

        butterfly_flight = flight_span.get_text()

        flight.append(butterfly_flight)

    #----------------------------------------------------------------------------------------#

        range_div = content_column.find('div', class_='views-field views-field-field-range')

        range_span = range_div.find('span', class_='field-content')

        butterfly_range = range_span.get_text()

        range.append(butterfly_range)

    except:

        family.append('ERROR')

        subfamily.append('ERROR')

        identification.append('ERROR')

        wingspan.append('ERROR')

        caterpillarhost.append('ERROR')

        adultfood.append('ERROR')

        habitat.append('ERROR')

        flight.append('ERROR')

        range.append('ERROR')




#---------------------------------------------#

#-- QUIT DRIVER FOR WHOLE CODE
driver.quit()

#---------------------------------------------#



#-- OBJECTIVE 4: Write to CSV --#


def write_csv():

    #-- Create and open a new file
    output_file = open('butterfly_data.csv', 'w')

    #-- Python CSV writer object
    csv_writer = csv.writer(output_file)

    #-- Determine order of columns
    lists = [final_species, family, subfamily, identification, wingspan, caterpillarhost, adultfood, habitat, flight, range]

    export_data = zip_longest(*lists, fillvalue = '')

    #-- Column headings
    csv_writer.writerow(['species', 'family', 'subfamily', 'identification', 'wingspan', 'caterpillarhost', 'adultfood', 'habitat', 'flight', 'range'])

    #-- Write data to CSV
    csv_writer.writerows(export_data)

    output_file.close()


write_csv()

print('done :)')
