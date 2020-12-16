Linux LiteX demo
~~~~~~~~~~~~~~~~

This example design features a LiteX SoC based around VexRiscv soft
CPU. To build the litex example, run the following commands:

.. code-block:: bash
   :name: example-litex-deps

   wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py;
   chmod +x litex_setup.py;
   ./litex_setup.py init;
   ./litex_setup.py install;
   python3 litex-boards/litex_boards/targets/zyboz7.py

Now you can upload the design with:

.. code-block:: bash

   openocd -f ${INSTALL_DIR}/conda/share/openocd/scripts/board/digilent_arty.cfg -c "init; pld load 0 top.bit; exit"

.. note::

   LiteX on Linux demo excepts you to use IPv4 address of ``192.168.100.100/24``
   on your network interface.

You should observe the following line in the OpenOCD output

.. code-block:: bash

   Info : JTAG tap: xc7.tap tap/device found: 0x0362d093 (mfg: 0x049 (Xilinx), part: 0x362d, ver: 0x0)

In the ``picocom`` terminal, you should observe the following output:

.. image:: ../../docs/images/linux-example-console.gif
   :align: center
   :width: 80%

Additionally, two LED's on the board should be turned on

.. image:: ../../docs/images/linux-example-arty.jpg
   :width: 49%
   :align: center
