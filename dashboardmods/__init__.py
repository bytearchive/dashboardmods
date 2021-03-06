__version_info__ = {
    'major': 0,
    'minor': 2,
    'micro': 2,
    'releaselevel': 'final',
    'serial': 1
}

def get_version():
    vers = ["%(major)i.%(minor)i" % __version_info__, ]

    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()

try:
    from modules import get_memcache_dash_modules, get_rss_dash_modules, get_varnish_dash_modules
except ImportError:
    pass
