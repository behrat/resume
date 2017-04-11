import os
import sys
import errno
import yaml
import json
import jinja2

with open('resume.yaml', 'r') as f:
    resume_data = f.read()

template = "default"

with open('configs/default.yaml', 'r') as f:
    default_config = f.read()

resume_yaml = resume_data + default_config

config = None
if len(sys.argv) > 1:
    config = sys.argv[1]
    with open('configs/%s.yaml' % config, 'r') as f:
        resume_yaml += f.read()

#print resume_yaml

resume = yaml.load(resume_yaml)

output_dir = "output"
if config:
    output_dir += "/" + config
try:
    os.makedirs(output_dir)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

with open(output_dir + "/resume-ehrat.json", "wb") as fh:
    fh.write(json.dumps(resume, indent=4))

with open(output_dir + "/resume-ehrat.yaml", "wb") as fh:
    fh.write(yaml.dump(resume, default_flow_style=False))

JINJA_TEMPLATES_FOLDER = 'templates'
jinja_loader = jinja2.FileSystemLoader(JINJA_TEMPLATES_FOLDER)

txt_jinja_env = jinja2.Environment(
        loader = jinja_loader,
        trim_blocks = True,    
        lstrip_blocks = True,
)

txt_template = txt_jinja_env.get_template('template.txt')
resume_txt = txt_template.render(resume=resume)

with open(output_dir + "/resume-ehrat.txt", "wb") as fh:
    fh.write(resume_txt.encode('utf-8'))

latex_jinja_env = jinja2.Environment(
        loader = jinja_loader,
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        trim_blocks = True,
        lstrip_blocks = True,
)

latex_template = latex_jinja_env.get_template('template.tex')
resume_tex = latex_template.render(resume=resume)

with open(output_dir + "/resume-ehrat.tex", "wb") as fh:
    fh.write(resume_tex.encode('utf-8'))

wiki_jinja_env = jinja2.Environment(
        loader = jinja_loader,
        block_start_string='<block>',
        block_end_string='</block>',
        variable_start_string='<var>',
        variable_end_string='</var>',
#        comment_start_string='<#',
#        comment_end_string='<#',
        trim_blocks = True,
        lstrip_blocks = True,
)

wiki_template = wiki_jinja_env.get_template('template.wiki')
wiki_resume = wiki_template.render(resume=resume)

with open(output_dir + "/resume-ehrat.wiki", "wb") as fh:
    fh.write(wiki_resume.encode('utf-8'))
