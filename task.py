import matplotlib.pyplot as plt

# ~ import mpld3
# ~ mpld3.enable_notebook()
# ~ plt.rcParams['figure.figsize'] = [9.5,6]


import csv
import urllib.request
import codecs

def get_csv_map(url):
    array = []
    url = "https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment2/best.mway"
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    for line in csvfile:
        integers = []
        for value in line:
            integer_value = int(value)
            integers.append(integer_value)
        array.append(integers)
    return array
        
transport = get_csv_map('https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment2/best.mway')
geology = get_csv_map('https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment2/best.geology')
population = get_csv_map('https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/assessment2/best.pop')

# make a display that combines/merges the maps,  
# with weighting on each map determined by one of three scrollbars
# and displays them combined

transport_weight = 100
geology_weight = 100
population_weight = 100

cumulative = []

print(len(transport[0]))

for i in range(len(transport)):
    cumulative_line = []
    for j in range(len(transport[0])):
        
        cumulative_line.append(transport[i][j] * transport_weight + geology[i][j] * geology_weight + population[i][j] * population_weight / 300)
    cumulative.append(cumulative_line)

plt.imshow(cumulative)
