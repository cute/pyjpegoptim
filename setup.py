from distutils.core import setup, Extension

include_dirs = ['/usr/include', '/usr/local/include']
library_dirs = ['/usr/lib', '/usr/local/lib']
libraries = ['jpeg']
runtime_library_dirs = []
extra_objects = []
define_macros = []

setup(name = "jpegoptim",
      version = "0.1.1",
      author = "Guangming Li",
      author_email = "leeful@gmail.com",
      license = "GPL",
      url = "http://liguangming.com/jpegoptim",
      packages = ["jpegoptim"],
      ext_package = "jpegoptim",
      ext_modules = [Extension( name = "jpegoptim",
                                sources = ["src/jpegoptim.c"],
                                include_dirs = include_dirs,
                                library_dirs = library_dirs,
                                runtime_library_dirs = runtime_library_dirs,
                                libraries = libraries,
                                extra_objects = extra_objects,
                                define_macros = define_macros
                              )],
      )

