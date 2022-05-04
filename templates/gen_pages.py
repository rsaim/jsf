from jinja2 import Template, StrictUndefined, BaseLoader, Environment, FileSystemLoader
import os
import json

J2_ENV = Environment(loader=FileSystemLoader([".", "./components"]))

def generate_page(templ_file, out_file, context, data):
    redndered_data = J2_ENV.get_template(templ_file).render(
        data=data,
        title="Jeevanstambh Foundation",
        context=context
    )
    with open(out_file, 'w') as outfile:
        outfile.write(redndered_data)
    outfile_path = os.path.abspath(out_file)
    print(f"Rendered to {outfile_path}")

# A Jinja template with the name + ".html" should exist in the CWD.
# The template will be rendered as a HTML file in the parent dir
TEMPL_TO_PAGE = [
    "index",
    "about",
    "work",
    "donate",
    "blog",
    "gallery",
    "contact",
    # Events
    "covid_lockdown"
]

DATADIR = "../data"

for pagename in TEMPL_TO_PAGE:
    data_file = os.path.join(DATADIR, f"{pagename}.json")
    data = {}
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)
    else:
        print(f"{data_file} doesn't exist", end=" ---> ")
    context = {
        "index": False,
        "about": False,
        "work": False,
        "donate": False,
        "blog": False,
        "gallery": False,
        "contact": False
    }
    context[pagename] = True
    generate_page(templ_file=f"{pagename}.html",
                  out_file=f"../{pagename}.html",
                  context=context,
                  data=data)