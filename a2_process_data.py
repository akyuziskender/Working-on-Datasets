#######################################################
### You can ignore the following lines of code.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do NOT need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

print("""
<!DOCTYPE html>
<html lang="en-US">
	<head>
		<title>Marriages and Divorces in 21st century</title>
		<meta charset="UTF-8">
		<style>
			h1 {
				color: purple;
				font-family: Courier New;
				text-align: center;
				background-color: white;
			}
			td {
				background: #6fc49c;
				color: black;
				border-style: groove;
				text-align: center;
				padding: 10px;
				font-family: Book Antiqua, Comic Sans MS, sans-serif;
			}
			tr {
				background: #f2f2f2
				border-style: groove;
			}
			table {
				float: left;
				border: 3px solid black;
				border-collapse: collapse;
				margin-left: 25px;
			}
			p {
				font-famiy: Book Antiqua, Comic Sans MS, sans-serif;
				text-indent: 25px;
				font-size: 20px;
			}
			ul {
				display: inline-block;
				list-style-type: circle;
				list-style-position: inside;
				font-family: Book Antiqua, Comic Sans MS, sans-serif;
		</style>
	</head>
	<body style="background-color: #2ECCFA">
		<h1>Marriages and Divorces in 21st century</h1>
		<br>
	""")
### This is where I displayed my datas in a table.
print("		<table>")
for x in range (0,16):
	print("			<tr>")
	print('				<td>' + contents[x][0] + "</td>")
	print('				<td>' + contents[x][1] + "</td>")
	print('				<td>' + contents[x][2] + "</td>")
	print('				<td>' + contents[x][3] + "</td>")
	print('				<td>' + contents[x][4] + "</td>")
	print("			</tr>")
print("		</table>")
print("""
		<p style="color: RGB(128,0,0)"><strong>There are some knowledge and calculations related to the table below.</strong></p>""")

### Some specific datas in the table.
print("""		<p>The information about divorces and marriages in 2010: </p>
		<ul>""")
for y in range(0,5):
	print("			<li>" + contents[0][y] + ": " + contents[10][y] + "</li>")
print("""		</ul>""")

### It is the data in D16, which shows the number of divorces in 2015.
print("		<p>The number of divorces in 2015: " + str(contents[15][3]) + "</p>")

### The sum of the marriages in 21st century.
total_marriages = 0
celll = 1
while celll < 16:
	total_marriages = total_marriages + int(contents[celll][1])
	celll += 1
print("		<p>The total number of marriages: " + str(total_marriages) + "</p>")

### The average number of the divorces
total_divorces = 0
for cell in range (1,16):
	total_divorces = total_divorces + int(contents[cell][3])
average_of_divorces = float(total_divorces / 15)
print("		<p>The average number of the divorces: " + str(average_of_divorces) + "</p>")

### The sum of the divorces which are above average.
total_divorces_above_average = 0
for cell in range (1,16):
	if int(contents[cell][3]) > average_of_divorces:
		total_divorces_above_average = total_divorces_above_average + int(contents[cell][3])
print("		<p>The sum of the divorces which are above average: " + str(total_divorces_above_average) + "</p>")

### The number of years when the divorce number is lower than the average
the_numbers_lower_than_average = []
for cell in range (1,16):
	if int(contents[cell][3]) < average_of_divorces:
		the_numbers_lower_than_average.append(int(contents[cell][3]))
print("		<p>The number of the years when the divorce number is lower than the average: " + str(len(the_numbers_lower_than_average)) + "</p>")
print("	</body>")
print("</html>")

### The type of the cell, A12, and the row 2
#print("The type of the cell, A12 is: " + str(type(contents[11][0])))
#print("The type of the second row is: " + str(type(contents[1])))

##### Error Section #####
## print(contents["batman"])
# TypeError: list indices must be integers, not str
## print(2 + "ali")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

## When I try to multiply a number with a string.
#print("because i am batman" * 5)
# Its output "because i am batmanbecause i am batmanbecause i am batmanbecause i am batmanbecause i am batman"