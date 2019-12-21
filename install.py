# $Id: install.py 1373 2015-10-14 13:50:32Z mwall $
# installer for simple
# Copyright 2014 Matthew Wall

from setup import ExtensionInstaller

def loader():
    return SimpleInstaller()

class SimpleInstaller(ExtensionInstaller):
    def __init__(self):
        super(SimpleInstaller, self).__init__(
            version="0.5",
            name='simple',
            description='A minimalist layout.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            config={
                'StdReport': {
                    'simple': {
                        'skin':'simple',
                        'HTML_ROOT':'simple'}}},
            files=[('skins/simple',
                    ['skins/simple/index.html.tmpl',
                     'skins/simple/skin.conf'])
                   ]
            )
