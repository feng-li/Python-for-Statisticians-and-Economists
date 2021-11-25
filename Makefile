all: slides


slides:
	jupyter-nbconvert **/L*.ipynb  --to slides  --SlidesExporter.reveal_theme=solarized --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=fade

html:
	jupyter-nbconvert **/**.ipynb  --to html

sync:
	rsync -av --del --exclude=".git/" . ~/nextcloud/web/python/
