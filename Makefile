
INPUT = resume.yaml templates/* configs/*
OUTPUT_DIR = output
UPLOAD_FILES = resume-ehrat.pdf resume-ehrat.txt resume-ehrat.json
WIKI_FILE = resume-ehrat.wiki
WIKI_ACTION_URL=https://ehrat.io/w/index.php?title=R%C3%A9sum%C3%A9\&action=
TEMPLATE_OUTPUT_FILES = resume-ehrat.tex resume-ehrat.txt resume-ehrat.json resume-ehrat.wiki

TEX_PATH = /usr/local/texlive/2012/bin/x86_64-darwin/

SHELL := /bin/bash
PATH := $(TEX_PATH):$(PATH)
UPLOAD_OUTPUT := $(addprefix $(OUTPUT_DIR)/, $(UPLOAD_FILES))
TEMPLATE_OUTPUT = $(addprefix $(OUTPUT_DIR)/, $(TEMPLATE_OUTPUT_FILES))

all: $(UPLOAD_OUTPUT) $(TEMPLATE_OUTPUT)

$(TEMPLATE_OUTPUT): $(INPUT)
	python render-templates.py

output/resume-ehrat.pdf: output/resume-ehrat.tex
	cd output; pdflatex resume-ehrat.tex; cd ..

upload: $(UPLOAD_OUTPUT)
	rsync --verbose --update $(OUTPUT) braden@origin.behrat.net:/ebs/www/bradenehrat.com/html/

post:
	diff <(curl $(WIKI_ACTION_URL)raw) output/resume-ehrat.wiki
	python post-wiki.py

publish: upload post
