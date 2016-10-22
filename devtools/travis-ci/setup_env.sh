#!/bin/sh

if [ "$TRAVIS_OS_NAME" = "osx" ]; then
    wget http://repo.continuum.io/miniconda/Miniconda-3.7.0-MacOSX-x86_64.sh -O miniconda.sh;
else
    wget http://repo.continuum.io/miniconda/Miniconda-3.7.0-Linux-x86_64.sh -O miniconda.sh;
fi

bash miniconda.sh -b

export PATH=$HOME/miniconda/bin:$PATH
# install stable version
pip install conda

conda update -n root conda-build --yes
conda install --yes conda-build jinja2 anaconda-client pip

# create myenv
conda create -y -n myenv python=$PYTHON_VERSION nose pytest numpy coverage pytest-cov cython netcdf4

source activate myenv

# ParmEd
# pip install https://github.com/ParmEd/ParmEd/archive/2.5.1.tar.gz
conda install parmed -c ambermd --yes

# ambermini
conda install ambermini -c omnia --yes

# sander
conda install sander -c ambermd --yes

# pytraj
pip install pytraj