Linux LiteX example for Xilinx 7 Series
=======================================

.. code-block:: bash
   :name: example-prereq-linux_litex_demo-xc7

   wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py;
   chmod +x litex_setup.py;
   ./litex_setup.py init;
   ./litex_setup.py install;
   wget https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.1.0-2019.01.0-x86_64-linux-ubuntu14.tar.gz;
   tar -xf riscv64-unknown-elf-gcc-8.1.0-2019.01.0-x86_64-linux-ubuntu14.tar.gz;
   export PATH=$PATH:$PWD/riscv64-unknown-elf-gcc-8.1.0-2019.01.0-x86_64-linux-ubuntu14/bin/;
   pushd litex/litex/boards/targets && ./arty.py --toolchain symbiflow --cpu-type vexriscv --build && popd

.. code-block:: bash
   :name: example-a35t-linux_litex_demo-xc7

   TARGET="arty_35" make -C linux_litex_demo

.. code-block:: bash
   :name: example-a100t-linux_litex_demo-xc7

   TARGET="arty_100" make -C linux_litex_demo

.. code-block:: bash
   :name: example-upload-linux_litex_demo-xc7

   openocd -f ${INSTALL_DIR}/conda/share/openocd/scripts/board/digilent_arty.cfg -c "init; pld load 0 top.bit; exit"
