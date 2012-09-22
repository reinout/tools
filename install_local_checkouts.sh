#!/bin/bash
if [ -d ~/vm/django/utils ]; then
    ROOT=~/vm/django
fi
if [ -d /vagrant/utils ]; then
    ROOT=/vagrant
fi

bin/pip install -e .
bin/pip install -e $ROOT/utils/zest.releaser/
bin/pip install -e $ROOT/utils/pep8/
bin/pip install -e $ROOT/utils/checkoutmanager
bin/pip install -e $ROOT/utils/nens/nensskel
bin/pip install -e $ROOT/utils/eolfixer
bin/pip install -e $ROOT/utils/createcoverage
