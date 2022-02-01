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
		<li class="green bold">JavaScript</li>
		<li class="green" id="python-li">Python</li>
	</ol>

</body>
</html>

"""

parsed_html = BeautifulSoup(html_string, 'html.parser')

html_elem = parsed_html.select("li")[3]
html_elem_list = parsed_html.select("li")  # Gel list from "li" data

html_elem.get_text()  # Get text from element

for elem in html_elem_list:
    print(elem.attrs)
    # print(elem.get_text())
    # print(elem.name)

print(html_elem.attrs['class'])
print(html_elem['id'])
