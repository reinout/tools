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
          # 'media-manager',
          # ^^^ Only on osx at the moment,included in the buildout

          # 'eolfixer',
          # 'nensbuild',
          # 'nenslint',
          # 'z3c.dependencychecker',
          'createcoverage',
          'checkoutmanager',
          'docutils',
          'dotfiles',
          'fabric',
          'ipython',
          'legit',
          'nensskel',
          'oplop',
          'pep8',
          'pyflakes',
          'readline',
          'sphinx',
          'zest.releaser',
          ],
      entry_points={
        'console_scripts': [
            'L = tools.engineerlog:main',
            'add_time = tools.add_time:main',
            'copytoblog = tools.blog:copytoblog',
            'new_sermon = tools.blog:new_sermon',
            'fixthunderbird = tools.thunderbird:fix_thunderbird',
            'gh = tools.github:main',
            'jsonformatter = tools.jsonformatter:main',
            'latestentries = tools.blog:list_todays_entries',
            'makedocs = tools.blog:makedocs',
            'naw = tools.naw:main',
            'sommen = tools.sommen:main',
            'vc = tools.vagrant:main',
            'tl = tools.timelog:add_timelog_entry',
            'pt = tools.timelog:main',
            'gac = tools.git:main',
            'mkinit = tools.mkinit:main',
            ],
        },
      )
