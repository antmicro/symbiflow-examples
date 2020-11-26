SymbiFlow examples
==================

.. image:: https://travis-ci.com/SymbiFlow/symbiflow-examples.svg?branch=master
   :target: https://travis-ci.com/SymbiFlow/symbiflow-examples

This repository provides example FPGA designs that can be built using the
SymbiFlow open source toolchain. These examples target the Xilinx Artix-7 and
the QuickLogic EOS S3 devices.

The repository includes:

* `examples/ <./examples>`_ - Example FPGA designs including:

  * Verilog code
  * Pin constraints files
  * Timing constraints files
  * Makefiles for running the SymbiFlow toolchain
* `docs/ <./docs>`_ - Guide on how to get started with SymbiFlow and build provided examples
* `scripts/ci/ <./scripts/ci>`_ - extra CI scripts
* `.travis.yml <.travis.yml>`_ - Travis CI configuration file

Please refer to the documentation in `docs <./docs>`_ for a proper guide on how
to run these examples. The examples provided by this repository are
automatically built by extracting necessary code snippets with `tuttest <https://github.com/antmicro/tuttest>`_.
Note that SymbiFlow architecture definitons for 7-Series FPGAs require ca. 21
GiBs of storage space, so currently only Travis CI can support testing this
repository (GH Actions provide only 12 GiBs).

Building those docs
-------------------

To build Sphinx documentation, you need at least Python 3.6. You will also need
to install Sphinx v3.3.0 and additional dependencies, which you can get with
``pip``::

   pip install -r docs/requirements.txt

Next, just run::

   make -C docs html

The output will be found in the ``docs/_build/html`` directory.

Running "CI" locally
--------------------

The CI uses a bunch of scripts in the `scripts/ci/ <./scripts/ci>`_ directory to execute the needed tests.
You can use the same scripts locally to test without having to wait for the online CIs to pass if you want to quickly test stuff.

For this, you will need `tuttest <https://github.com/antmicro/tuttest/>`_,
which you can install with::

    pip install git+https://github.com/antmicro/tuttest

``<fpga-fam>`` is one of ``{eos-s3,xc7}`` (the two currently covered platforms - EOS S3 and Xilinx series 7).

To install the toolchain (just the first time), run::

   scripts/install-toolchain.sh <fpga-fam>

To build all the examples locally, just run::

   scripts/ci/build.sh <fpga-fam>
