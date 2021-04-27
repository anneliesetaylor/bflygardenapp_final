
#-- Import everything --#

from bs4 import BeautifulSoup
from itertools import zip_longest
import requests
import csv


#-- Make empty lists for data collection --#

plant_common_name = []

plant_family = []

plant_habitats = []

plant_range = []

plant_physical_characteristics = []

plant_cultivation = []

plant_propagation = []

#------------------------------------------#



#-- OBJECTIVE 1: Get plant species latin names from CSV file --#

with open('plant_species.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


latin_name = []

for eachname in data:
    latin_name.append(eachname[1])

latin_name.remove('latin_name') #-- Removing column heading --#

#-- species with no data and no alternate species name --#
latin_name.remove('Zinnia')
latin_name.remove('Senna hebacarpa')
latin_name.remove('Symphyotrichum oblongifolium')



#-- OBJECTIVE 2: Use latin names to make partial links for web scraping --#

plant_partial_links = []

for eachspecies in latin_name:
    species_partials = eachspecies.replace('Cornus racemosa', 'Cornus amomum').replace(u'\xa0', u' ').replace(' ', '+')
    plant_partial_links.append(species_partials)



#-- OBJECTIVE 3: Scrape plant data from Plants for a Future online database --#

for eachpartial in plant_partial_links:

    if eachpartial == 'Lavendula':
        eachpartial = 'Lavandula+stoechas'

    url = ('https://pfaf.org/user/Plant.aspx?LatinName=' + eachpartial)
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.text, 'html.parser')


    try:

        table_div = soup.find('div', class_='col-xs-1 col-md-7 col-lg-5')

        table = table_div.find('table', class_='table table-hover table-striped')

        common_name_cell = soup.find('span', id='ContentPlaceHolder1_lblCommanName').get_text()
        plant_common_name.append(common_name_cell)


        family_cell = soup.find('span', id='ContentPlaceHolder1_lblFamily').get_text()
        plant_family.append(family_cell)


        habitats_cell = soup.find('span', id='ContentPlaceHolder1_txtHabitats').get_text()
        plant_habitats.append(habitats_cell)


        range_cell = soup.find('span', id='ContentPlaceHolder1_lblRange').get_text()
        plant_range.append(range_cell)


        phys_char = soup.find('span', id='ContentPlaceHolder1_lblPhystatment').get_text()
        plant_physical_characteristics.append(phys_char)


        cult_details = soup.find('span', id='ContentPlaceHolder1_txtCultivationDetails').get_text()
        plant_cultivation.append(cult_details)


        propagation = soup.find('span', id='ContentPlaceHolder1_txtPropagation').get_text()
        plant_propagation.append(propagation)

    except:

        plant_common_name.append('ERROR')

        plant_family.append('ERROR')

        plant_habitats.append('ERROR')

        plant_range.append('ERROR')

        plant_physical_characteristics.append('ERROR')

        plant_cultivation.append('ERROR')




#-- OBJECTIVE 4: Write to CSV --#


def write_csv():

    #-- Create and open a new file
    output_file = open('plant_data.csv', 'w')

    #-- Python CSV writer object
    csv_writer = csv.writer(output_file)

    #-- Determine order of columns
    lists = [latin_name, plant_common_name, plant_family, plant_habitats, plant_range, plant_physical_characteristics, plant_cultivation, plant_propagation]

    export_data = zip_longest(*lists, fillvalue = '')

    #-- Column headings
    csv_writer.writerow(['latin_name', 'plant_common_name', 'plant_family', 'plant_habitats', 'plant_range', 'plant_physical_characteristics', 'plant_cultivation', 'plant_propagation'])

    #-- Write data to CSV
    csv_writer.writerows(export_data)

    output_file.close()


write_csv()

print('done :)')
