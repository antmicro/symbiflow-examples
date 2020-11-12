# SymbiFlow examples
[![Build Status](https://travis-ci.com/antmicro/symbiflow-examples.svg?branch=master)](https://travis-ci.com/antmicro/symbiflow-examples)

This repository provides example FPGA designs that can be built using the
SymbiFlow open source toolchain. These examples target the Xilinx Artix-7 and
the QuickLogic EOS S3 devices.

The repository includes:
* [examples](./examples) - Example FPGA designs including:
  * Verilog code
  * Pin constraints files
  * Timing constraints files
  * Makefiles for running the SymbiFlow toolchain
* [docs](./docs) - Guide on how to get started with SymbiFlow and build
                   provided examples
* [.travis.yml](.travis.yml) - Travis CI configuration file

Please refer to the documentation in [docs](./docs) for a proper guide on how
to run these examples. The examples provided by this repository are
automatically built by extracting necessary code snippets with
[tuttest](https://github.com/antmicro/tuttest). Note that SymbiFlow
architecture definitons for 7-Series FPGAs require ca. 21 GiBs of storage
space, so currently only Travis CI can support testing this repository (GH
Actions provide only 12 GiBs).
