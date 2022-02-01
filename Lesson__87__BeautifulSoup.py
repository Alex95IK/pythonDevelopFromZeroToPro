from bs4 import BeautifulSoup
html_string = """
<!DOCTYPE html>
<html>
<head>
	<title>Web Development Page</title>
	<style type="text/css">
		
		h1{
			color: white;
			background: red;
		}

		li{
			color: red;
		}

		#css-li{
			color: blue;
		}

		.green{
			color: green;
		}

	</style>
</head>
<body>
	<h1>Web Development</h1>
	<h1 class="green">Web</h1>
	<h3>Programming Languages</h3>

	<ol>
		<li>HTML</li>
		<li id="css-li">CSS</li>
		<li class="green">JavaScript</li>
		<li class="green">Python</li>
	</ol>

</body>
</html>

"""

parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html)
# print(type(parsed_html))

# print(parsed_html.body.li)  # parsed_html
# print(parsed_html.find('li'))  # find
# print(parsed_html.find_all('li'))  # find_all
# print(parsed_html.find(id="css-li"))  # find id
# print(parsed_html.find_all(class_="green"))  # find_all id
# print(parsed_html.select('#css-li'))  # select
print(parsed_html.select('.green')[1])  # select with key list
print(parsed_html.select('li'))  # select
