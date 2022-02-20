all: slides

slides:
	jupyter-nbconvert **/L*.ipynb  --to slides  --SlidesExporter.reveal_theme=solarized --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=fade

html:
	jupyter-nbconvert **/**.ipynb  --to html

zip:
	git archive --output=python-slides.zip HEAD

sync:
	git checkout-index -a -f --prefix=${HOME}/nextcloud/feng.li/python/
	rsync -av python-slides.zip ${HOME}/nextcloud/feng.li/python/
