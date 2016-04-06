
INPUT = resume.yaml templates/* configs/*
OUTPUT = output/resume-ehrat.pdf output/resume-ehrat.txt output/resume-ehrat.json
TEMPLATE_OUTPUT = output/resume-ehrat.tex output/resume-ehrat.txt output/resume-ehrat.json output/resume-ehrat.wiki
TEX = output/resume-ehrat.tex

SHELL := /bin/bash
TEX_PATH = /usr/local/texlive/2012/bin/x86_64-darwin/
PATH := $(TEX_PATH):$(PATH)

all: $(OUTPUT)

$(TEMPLATE_OUTPUT): $(INPUT)
	python render-templates.py

output/resume-ehrat.pdf: output/resume-ehrat.tex
	cd output; pdflatex resume-ehrat.tex; cd ..

publish: $(OUTPUT)
	rsync --verbose --update $(OUTPUT) braden@origin.behrat.net:/ebs/www/bradenehrat.com/html/
