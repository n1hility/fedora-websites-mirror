include ../Makefile.in

$(LANGUAGES): % : | static rss-cache po/%.mo data/templates/translations.html
	$(PYTHON) $(BUILDDIR)/build.py -o out -i data/content -l $@ -p po -b $(BASEPATH)

json-releases:
# FIXME: This is being provided statically for F25 GA,
# but must be fixed by F26 Alpha
# q.v.:
#   https://pagure.io/fedora-websites/issue/54
#   https://pagure.io/fedora-qa/fedfind/issue/2
	mv out/static/releases.json out/releases.json
