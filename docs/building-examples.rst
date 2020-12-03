Building example designs
========================

Before building any example, set the installation directory to match what you
set it to earlier, for example:

.. code-block:: bash
   :name: export-install-dir

   export INSTALL_DIR=~/opt/symbiflow

Select your fpga family:

.. tabs::

   .. group-tab:: Artix-7

      .. code-block:: bash
         :name: fpga-fam-xc7

         FPGA_FAM="xc7"

   .. group-tab:: EOS S3

      .. code-block:: bash
         :name: fpga-fam-eos-s3

         FPGA_FAM="eos-s3"

Next, prepare the enviroment:

.. code-block:: bash
   :name: conda-prep-env

   export PATH="$INSTALL_DIR/$FPGA_FAM/install/bin:$PATH";
   source "$INSTALL_DIR/$FPGA_FAM/conda/etc/profile.d/conda.sh"

Finally, enter your working Conda enviroment:

.. code-block:: bash
   :name: conda-act-env

   conda activate $FPGA_FAM

.. note::

   If you don't know how to upload any of the following examples onto your
   development board, please refer to the Running examples section.


Xilinx 7-Series
---------------

Enter the directory that contains examples for Xilinx 7-Series FPGAs:

.. code-block:: bash
   :name: enter-dir-xc7

   cd xc7

Counter test
~~~~~~~~~~~~

This example design features a simple 4-bit countrer driving LEDs. To build the
counter example, run the following command:

.. jinja:: xc7

   .. tabs::

   {% for k, v in counter_test.items() %}
   {% if v['is_build'] %}

      .. group-tab:: {{v['name']}}

         .. code-block:: bash

            {% for line in v['code'] %}
               {{ line }}
            {% endfor %}

   {% endif %}
   {% endfor %}

Now you can upload the design with:

.. jinja:: xc7

   .. code-block:: bash

      {% for line in counter_test['upload']['code'] %}
         {{ line }}
      {% endfor %}


The result should be as follows:

.. image:: images/counter-example-arty.gif
   :align: center

PicoSoC demo
~~~~~~~~~~~~

This example features a picorv32 soft CPU and a SoC based on it. To build the
picosoc example, run the following commands:

.. jinja:: xc7

   .. tabs::

   {% for k, v in picosoc_demo.items() %}
   {% if v['is_build'] %}

      .. group-tab:: {{v['name']}}

         .. code-block:: bash

            {% for line in v['code'] %}
               {{ line }}
            {% endfor %}

   {% endif %}
   {% endfor %}

Now you can upload the design with:

.. jinja:: xc7

   .. code-block:: bash

      {% for line in picosoc_demo['upload']['code'] %}
         {{ line }}
      {% endfor %}


You should observe the following line in the OpenOCD output:

.. jinja:: xc7

   .. code-block::

      {% for line in picosoc_demo['jtag']['code'] %}
         {{ line }}
      {% endfor %}


The UART output should look as follows:

.. jinja:: xc7

   .. code-block::

      {% for line in picosoc_demo['output']['code'] %}
         {{ line }}
      {% endfor %}

.. note::

   PicoSoC uses baud rate of ``460800`` by default.

The board's LED should blink at a regular rate from left to the right

.. image:: images/picosoc-example-basys3.gif
   :width: 49%
   :align: center

Linux LiteX demo
~~~~~~~~~~~~~~~~

This example design features a Linix-capable SoC based around VexRiscv soft
CPU. It also includes DDR and Ethernet controllers. To build the litex example,
run the following commands:

.. code-block:: bash
   :name: example-litex-deps

   wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py;
   chmod +x litex_setup.py;
   ./litex_setup.py init;
   ./litex_setup.py install;
   wget https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.1.0-2019.01.0-x86_64-linux-ubuntu14.tar.gz;
   tar -xf riscv64-unknown-elf-gcc-8.1.0-2019.01.0-x86_64-linux-ubuntu14.tar.gz;
   export PATH=$PATH:$PWD/riscv64-unknown-elf-gcc-8.1.0-2019.01.0-x86_64-linux-ubuntu14/bin/
   #pushd litex/litex/boards/targets && ./arty.py --toolchain symbiflow --cpu-type vexriscv --build && popd

To build the linux-litex-demo example, run the following commands:

.. tabs::

   .. group-tab:: Arty 35T

      .. code-block:: bash
         :name: example-litex-a35t

         TARGET="arty_35" make -C linux_litex_demo

   .. group-tab:: Arty 100T

      .. code-block:: bash
         :name: example-litex-a100t

         TARGET="arty_100" make -C linux_litex_demo

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

.. image:: images/linux-example-console.gif
   :align: center
   :width: 80%

Additionally, two LED's on the board should be turned on

.. image:: images/linux-example-arty.jpg
   :width: 49%
   :align: center

QuickLogic EOS S3
-----------------

Enter the directory that contains examples for QuickLogic EOS S3:

.. code-block:: bash
   :name: enter-dir-eos-s3

   cd eos-s3

Button counter
~~~~~~~~~~~~~~

This example design features a simple 4-bit countrer driving LEDs. To build the
counter example, run the following command:

.. code-block:: bash
   :name: eos-s3-counter

   make -C btn_counter
