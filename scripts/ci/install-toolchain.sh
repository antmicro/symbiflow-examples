#!/bin/bash
set -e

fpga_fam=$1

# create conda env
eval $(tuttest docs/getting-symbiflow.rst wget-conda)
eval $(tuttest docs/getting-symbiflow.rst conda-install-dir)
eval $(tuttest docs/getting-symbiflow.rst fpga-fam-$fpga_fam)
eval $(tuttest docs/getting-symbiflow.rst conda-setup)
eval $(tuttest docs/getting-symbiflow.rst download-arch-def-$fpga_fam)

