from spack import *

class Atop(Package):
    """Atop is an ASCII full-screen performance monitor for Linux"""
    homepage = "http://www.atoptool.nl/index.php"
    url      = "http://www.atoptool.nl/download/atop-2.2-3.tar.gz"

    version('2.2-3', '034dc1544f2ec4e4d2c739d320dc326d')

    def install(self, spec, prefix):
        make()
        mkdirp(prefix.bin)
        install("atop", join_path(prefix.bin, "atop"))
        mkdirp(join_path(prefix.man, "man1"))
	install(join_path("man", "atop.1"),
            join_path(prefix.man, "man1", "atop.1"))
