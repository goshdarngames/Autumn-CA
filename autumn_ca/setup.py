from distutils.core import setup
from Cython.Build import cythonize

import numpy

setup (
    ext_modules = cythonize("lib/neighbourhood.pyx"),
    include_dirs=[numpy.get_include()],
    extra_compile_args = ["-ffast-math"]
)
