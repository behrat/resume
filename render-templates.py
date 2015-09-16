import os
import errno
import yaml
import jinja2

with open('resume.yaml', 'r') as f:
    resume_data = f.read()

with open('configs/default.yaml', 'r') as f:
    resume_config = f.read()

resume = yaml.load(resume_data + resume_config)
#resume_stream = file('resume.yaml', 'r')
#resume = yaml.load(resume_stream)

JINJA_TEMPLATES_FOLDER = 'templates'

jinja_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(JINJA_TEMPLATES_FOLDER),
        trim_blocks = True,    
        lstrip_blocks = True,
)

latex_jinja_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(JINJA_TEMPLATES_FOLDER),
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
#        line_statement_prefix = '%-',
        line_statement_prefix = None,
        line_comment_prefix = '%#',
        trim_blocks = True,
        lstrip_blocks = True,
        autoescape = False,
)

latex_template = latex_jinja_env.get_template('template.tex')
resume_tex = latex_template.render(resume=resume)

txt_template = jinja_env.get_template('template.txt')
resume_txt = txt_template.render(resume=resume)

try:
    os.makedirs("output")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

with open("output/resume-ehrat.txt", "wb") as fh:
    fh.write(resume_txt.encode('utf-8'))

with open("output/resume-ehrat.tex", "wb") as fh:
    fh.write(resume_tex.encode('utf-8'))
