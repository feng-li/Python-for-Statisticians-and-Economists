all: slides


slides:
	jupyter-nbconvert **/**.ipynb  --to slides

html:
	jupyter-nbconvert **/**.ipynb  --to html

sync:
	rsync -av --exclude=".git/" . ~/nextcloud/web/python/
