import os
import errno
import yaml
import jinja2

with open('resume.yaml', 'r') as f:
    resume_data = f.read()

with open('configs/default.yaml', 'r') as f:
    resume_config = f.read()

resume = yaml.load(resume_data + resume_config)

try:
    os.makedirs("output")
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

JINJA_TEMPLATES_FOLDER = 'templates'
jinja_loader = jinja2.FileSystemLoader(JINJA_TEMPLATES_FOLDER)

txt_jinja_env = jinja2.Environment(
        loader = jinja_loader,
        trim_blocks = True,    
        lstrip_blocks = True,
)

txt_template = txt_jinja_env.get_template('template.txt')
resume_txt = txt_template.render(resume=resume)

with open("output/resume-ehrat.txt", "wb") as fh:
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

with open("output/resume-ehrat.tex", "wb") as fh:
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

with open("output/resume-ehrat.wiki", "wb") as fh:
    fh.write(wiki_resume.encode('utf-8'))
