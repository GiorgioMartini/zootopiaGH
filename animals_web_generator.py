from data_fetcher import data_fetcher

def serialize_animal(animal_obj):
    """
    Converts an animal object into HTML markup for display.
    
    Args:
        animal_obj (dict): Dictionary containing animal data with keys:
            - name: Animal name
            - taxonomy: Dictionary of taxonomic information
            - locations: List of locations where animal is found
            - characteristics: Dictionary containing diet, type and other traits
    
    Returns:
        str: HTML markup for displaying the animal as a card
    """
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

def main():
    name = input('Give a name: ')
    data = data_fetcher(name)

    # Aggregate all serialized animals into a single string
    output = ""
    if not data:
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


if __name__ == "__main__":
    main()
