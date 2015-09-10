import os
import json
import jinja2

resume_stream = file('resume.json', 'r')
resume = json.load(resume_stream)

jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        trim_blocks=True,    
        lstrip_blocks=True,
)

txt_template = jinja_env.get_template('template.txt')
resume_txt = txt_template.render(resume=resume)

try:
    os.makedirs("output")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

with open("output/resume-ehrat.txt", "wb") as fh:
    fh.write(resume_txt.encode('utf-8'))
