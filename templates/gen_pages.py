from jinja2 import Template, StrictUndefined, BaseLoader, Environment, FileSystemLoader
import os
import json

J2_ENV = Environment(loader=FileSystemLoader([".", "./components"]))


def generate_page(templ_file, out_file, context, data, relief_area):
    redndered_data = J2_ENV.get_template(templ_file).render(
        data=data,
        title="Jeevan Stambh Foundation",
        context=context,
        relief_area=relief_area
    )
    with open(out_file, 'w') as outfile:
        outfile.write(redndered_data)
    outfile_path = os.path.abspath(out_file)
    print(f"Rendered to {outfile_path}")


# A Jinja template with the name + ".html" should exist in the CWD.
# The template will be rendered as a HTML file in the parent dir
TEMPLATE_MAPPING = [
    # Template               Output File                    Data filename
    ("index.html",           "index.html",                  ""),
    ("about.html",           "about.html",                  ""),
    ("work.html",            "work.html",                   "work.json"),
    ("donate.html",          "donate.html",                 ""),
    # ("blog.html",          "blog.html",                   ""),
    ("gallery_tmpl.html",    "gallery.html",                "gallery.json"),
    ("contact.html",         "contact.html",                ""),
    # Events
    ("relief_templ.html",    "covid_relief.html",           "covid_relief.json"),
    ("relief_templ.html",    "fire_relief.html",            "fire_relief.json"),
    ("relief_templ.html",    "flood_relief.html",           "flood_relief.json"),
    ("relief_templ.html",    "rehab_relief.html",           "rehab_relief.json"),
    ("relief_templ.html",    "medical_relief.html",         "medical_relief.json"),
    ("relief_templ.html",    "rescue_relief.html",          "rescue_relief.json"),
    ("relief_templ.html",    "demolition_relief.html",      "demolition_relief.json"),
    ("relief_templ.html",    "events.html",                 "events.json"),
    ("partners_and_donors.html",
     "partners_and_donors.html",
     "partners_and_donors.json"),
    ("work.html",           "press.html",                   "press.json"),
]

DATADIR = "../data"

for templ_fname, outfile, datafname in TEMPLATE_MAPPING:
    relief_area = ""
    data = {}
    if datafname:
        data_file = os.path.join(DATADIR, datafname)
        if os.path.exists(data_file):
            with open(data_file, 'r') as f:
                data = json.load(f)
            if isinstance(data, list) and len(data) == 2 and "relief_area" in data[0]:
                relief_area = data[0]["relief_area"]
                data = data[1]
        else:
            print(f"{data_file} doesn't exist", end=" ---> ")
    context = {outfile: True}
    generate_page(templ_file=f"{templ_fname}",
                  out_file=f"../{outfile}",
                  context=context,
                  data=data,
                  relief_area=relief_area)
