
from flask import Flask, render_template
import csv


def convert_to_dict(filename):

    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts

#------------------------------------------#

app = Flask(__name__)
application = app

#------------------------------------------#

plant_list = convert_to_dict('plant_data.csv')

butterfly_list = convert_to_dict('butterfly_data2.csv')

plant_pairs = []

butterfly_pairs = []

for p in plant_list:
    plant_pairs.append( (p['id'], p['latin_name']) )

for b in butterfly_list:
    butterfly_pairs.append( (b['id'], b['species']) )

#------------------------------------------#



#-- INDEX.HTML: First app route --#
@app.route('/')
def index():
    return render_template('index.html', the_title="Blooming for Butterflies: A Guide to Butterfly Gardening")


@app.route('/butterflygardening')
def bflygardening():
    return render_template('butterflygardening.html', the_title="Blooming for Butterflies: How to Butterfly Garden")


#--Plant Directory --#
@app.route('/plantdirectory')
def pdirectory():
    return render_template('plantdirect.html', plantpairs=plant_pairs, the_title="Blooming for Butterflies: Plant Species")


#--Butterfly Directory --#
@app.route('/bflydirectory')
def bdirectory():
    return render_template('bflydirect.html', bflypairs=butterfly_pairs, the_title="Blooming for Butterflies: Butterfly Species")



#--Specific plant pages --#
@app.route('/plantspecies/<num>')
def plantfunc(num):
    try:
        plant_dict = plant_list[int(num) - 1]
    except:
        return f"<h1>Invalid Page Number: {num}</h1>"

    return render_template('plantpage.html', pspecies=plant_dict, the_title=('Blooming for Butterflies: ' + plant_dict['latin_name']))


#--Specific butterfly pages --#
@app.route('/bflyspecies/<num>')
def bflyfunc(num):
    try:
        bfly_dict = butterfly_list[int(num) - 1]
    except:
        return f"<h1>Invalid Page Number: {num}</h1>"

    return render_template('bflypage.html', bflyspecies=bfly_dict, the_title=('Blooming for Butterflies: ' + bfly_dict['species']))





#------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)
