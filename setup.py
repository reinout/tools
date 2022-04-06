from setuptools import setup

version = "0.1.dev0"


setup(
    name="tools",
    version=version,
    description="Tools and scripts for Reinout",
    long_description="",
    classifiers=[],
    keywords="",
    author="Reinout van Rees",
    author_email="reinout@vanrees.org",
    url="https://reinout.vanrees.org",
    license="GPL",
    packages=["tools"],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # 'media-manager',
        # ^^^ Only on osx at the moment,included in the buildout
        # 'createcoverage',
        # 'eolfixer',
        # 'nensbuild',
        # 'nenslint',
        "coverage",
        "future",
        "nose",
        "pyserial",
        # 'readline',
        "six",  # Trying to make it explicit
    ],
    entry_points={
        "console_scripts": [
            "log = tools.engineerlog:main",
            "add_time = tools.add_time:main",
            "copytoblog = tools.blog:copytoblog",
            "new_sermon = tools.blog:new_sermon",
            "fixthunderbird = tools.thunderbird:fix_thunderbird",
            "gh = tools.github:main",
            "latestentries = tools.blog:list_todays_entries",
            "makedocs = tools.blog:makedocs",
            "sommen = tools.sommen:main",
            "gac = tools.git:main",
            "mkinit = tools.mkinit:main",
            "python_coding_cleanup = tools.python_coding_cleanup:main",
        ]
    },
)
