from setuptools import setup

version = '0.1.dev0'


setup(name='tools',
      version=version,
      description="Tools and scripts for Reinout",
      long_description='',
      classifiers=[],
      keywords='',
      author='Reinout van Rees',
      author_email='reinout@vanrees.org',
      url='http://reinout.vanrees.org',
      license='GPL',
      packages=['tools'],
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'checkoutmanager',
          'createcoverage',
          'docutils',
          'dotfiles',
          'eazysvn',
          'eolfixer',
          'nensskel',
          'pep8',
          'pyflakes',
          'zc.rst2',
          'zest.releaser',
          ],
      entry_points={
          'console_scripts': [
              # 'copytoblog = blog:copytoblog',
              # 'makedocs = blog:makedocs',
              # 'fixthunderbird = thunderbird:fix_thunderbird',
              # 'latestentries = blog:list_todays_entries',
              # 'sommen = sommen:main',
              # 'jslint = jslint:main',
              # 'jshint = jshint:main',
              # 'L = engineerlog:main',
              # 'bl = booklog:main',
              ],
          },
      )
