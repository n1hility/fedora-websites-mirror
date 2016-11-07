include ../Makefile.in

$(LANGUAGES): % : | static rss-cache po/%.mo data/templates/translations.html
	$(PYTHON) $(BUILDDIR)/build.py -o out -i data/content -l $@ -p po -b $(BASEPATH)

json-releases:
	$(PYTHON) build/releases-json.py > out/new-release-file.json
	# And if that completes successfully, ...
	mv out/new-release-file.json out/releases.json
