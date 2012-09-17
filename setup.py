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
          'eolfixer',
          'nensskel',
          'pep8',
          'pyflakes',
          'zest.releaser',
          ],
      entry_points={
        'console_scripts': [
            'L = tools.engineerlog:main',
            'add_time = tools.add_time:main',
            'copytoblog = tools.blog:copytoblog',
            'fixthunderbird = tools.thunderbird:fix_thunderbird',
            'gh = tools.github:main',
            'jshint = tools.jshint:main',
            'jsonformatter = tools.jsonformatter:main',
            'latestentries = tools.blog:list_todays_entries',
            'makedocs = tools.blog:makedocs',
            'sommen = tools.sommen:main',
            'vc = tools.vagrant:main',
            ],
        },
      )
