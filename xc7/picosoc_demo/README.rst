PicoSoC example for Xilinx 7 Series
===================================

.. code-block:: bash
   :name: example-basys3-picosoc_demo-xc7

   TARGET="basys3" make -C picosoc_demo

.. code-block:: bash
   :name: example-upload-picosoc_demo-xc7

   openocd -f ${INSTALL_DIR}/conda/share/openocd/scripts/board/digilent_arty.cfg -c "init; pld load 0 top.bit; exit"

.. code-block::
   :name: example-jtag-picosoc_demo-xc7

   Info : JTAG tap: xc7.tap tap/device found: 0x0362d093 (mfg: 0x049 (Xilinx), part: 0x362d, ver: 0x0)

.. code-block::
   :name: example-output-picosoc_demo-xc7

   Terminal ready
   Press ENTER to continue..
   Press ENTER to continue..
   Press ENTER to continue..
   Press ENTER to continue..

    ____  _          ____         ____
   |  _ \(_) ___ ___/ ___|  ___  / ___|
   | |_) | |/ __/ _ \___ \ / _ \| |
   |  __/| | (_| (_) |__) | (_) | |___
   |_|   |_|\___\___/____/ \___/ \____|


   [9] Run simplistic benchmark

   Command>
