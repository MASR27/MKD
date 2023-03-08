import yaml

# Define the pages of your site
pages = [
    {'Home': 'index.md'},
    {'About': 'about.md'},
    {'Contact': 'contact.md'}
]

# Create a dictionary for the navigation bar
nav = {'nav': pages}

# Write the dictionary to a YAML file
with open('mkdocs.yml', 'a') as f:
    f.write(yaml.dump(nav))
