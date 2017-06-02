import wikitools
from pprint import pprint

with open("output/resume-ehrat.wiki", "r") as f:
    wikitext = f.read()

site = wikitools.wiki.Wiki("https://ehrat.io/w/api.php")
site.login("braden",
           remember=True, # Save to braden.cookies
           verify=False, # Still asks for password with cookie file for some reason
        )
page = wikitools.page.Page(site, title="Resume")
result = page.edit(text=wikitext,
          summary="Publish",
          bot=True)

print("Wiki POST result:")
pprint(result)
