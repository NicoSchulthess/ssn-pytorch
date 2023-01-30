from setuptools import setup, Extension
from torch.utils import cpp_extension

setup(name='pair_wise_distance',
      ext_modules=[cpp_extension.CppExtension(
          'pair_wise_distance', ['lib/ssn/pair_wise_distance.cu'])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})
