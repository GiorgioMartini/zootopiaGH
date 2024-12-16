import json
from data_fetcher import data_fetcher

name = input('Give a name: ')
data = data_fetcher(name)

# Generate the output HTML content
def serialize_animal(animal_obj):
    output = ''
    name = animal_obj.get("name", "Unknown")
    taxonomy = animal_obj.get("taxonomy", {})
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})
    
    output += f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <ul class="card__text">
            <li><strong>Diet:</strong> {characteristics.get("diet", "Unknown")}</li>
            <li><strong>Location:</strong> {", ".join(locations) if locations else "Unknown"}</li>
    """
    if 'type' in characteristics:
        output += f'            <li><strong>Type:</strong> {characteristics["type"]}</li>'
    output += """
        </ul>
    </li>
    """
    return output

# Aggregate all serialized animals into a single string
output = ""
if data == False:
  output = '<li>Sorry no animal with that name.</li>'
else:
  for animal in data:
      output += serialize_animal(animal)

# Load the template HTML file
with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Replace the placeholder in the template with the generated output
html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

# Save the final HTML content to a new file
with open('animals.html', 'w', encoding="utf-8") as file:
    file.write(html_content)

# Print the HTML content
print(html_content)
