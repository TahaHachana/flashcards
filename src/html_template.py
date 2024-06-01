# main.py
from jinja2 import Environment, PackageLoader, select_autoescape

# Set up the environment and loader
env = Environment(
    loader=PackageLoader('html_template', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Load the template
index_template = env.get_template('index.html')
carousel_template = env.get_template('carousel.html')

# # Define the data to be passed to the template
# context = {
#     'title': 'My Title',
# }

# # Render the template with the context data
# html_output = template.render(context)

