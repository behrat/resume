# resume

This is the source code to generate my resume. I wanted to maintain many formats of it, which would be tedius, so I've automated the processes.

The source information is stored in resume.yaml. Reading that file, the render-templates.py script uses [Jinja2](http://jinja.pocoo.org/) templates to render the resume in LaTeX source, MediaWiki markup, and plain text. Additionally, a JSON version is output, which I originally meant to follow the [JSON Resume](https://jsonresume.org/) spec, but I unfortunately found it too limiting, and my output isn't exactly to spec.

A Makefile completes the process. The LaTeX source is rendered to PDF by `pdflatex`. If `make publish` is run, it further `rsync`s the PDF, TXT, and JSON files to my webserver. The post-wiki.py script is called to publish to MediaWIki, using the [wikitools](https://github.com/alexz-enwp/wikitools) package.
