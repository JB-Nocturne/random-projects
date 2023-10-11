import csv

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def generate_html_sorted(data):
    # Sort the data alphabetically
    sorted_data = sorted(data)

    html = """<!DOCTYPE html>
<html>
<head>
    <title>CSV to HTML</title>
</head>
<body>
    <ul>\n"""

    for item in sorted_data:
        # Assuming each item is a string, remove square brackets if present
        item_str = str(item[0]) if isinstance(item, list) else str(item)

        # Define your inline CSS styles directly in the li element
        # For example: style="font-family: 'Lato'; color: red;"
        li_style = 'style=\'font-family: \"Trebuchet MS\";\''  # Add more CSS properties as needed

        html += f'        <li {li_style}>{item_str}</li>\n'

    html += """    </ul>
</body>
</html>
"""

    with open('output_sorted.html', 'w') as htmlfile:
        htmlfile.write(html)

# Read CSV data
csv_data = read_csv('test.csv')

# Generate HTML in alphabetical order
generate_html_sorted(csv_data)


