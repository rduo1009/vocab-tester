# Code taken from https://github.com/himbeles/ctypes-example
# additional info at https://stackoverflow.com/questions/4529555/building-a-ctypes-based-c-library-with-distutils

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig


class CTypesExtension(Extension):
    pass


class build_ext(build_ext_orig):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypesExtension)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return "lib" + ext_name + ".so"
        return super().get_ext_filename(ext_name)


ext_modules = [
    CTypesExtension(
        name="python_src.lego.key",
        sources=["python_src/lego/key.cpp"],
        include_dirs=["python_src/_vendor/Obfuscate"],
    )
]


def build(setup_kwargs):
    setup_kwargs.update({
        "ext_modules": ext_modules,
        "cmdclass": {"build_clib": build_ext},
    })
