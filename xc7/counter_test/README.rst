Counter example for Xilinx 7 Series
===================================

.. code-block:: bash
   :name: example-a35t-counter_test-xc7

   TARGET="arty_35" make -C counter_test

.. code-block:: bash
   :name: example-a100t-counter_test-xc7

   TARGET="arty_100" make -C counter_test

.. code-block:: bash
   :name: example-basys3-counter_test-xc7

   TARGET="basys3" make -C counter_test

.. code-block:: bash
   :name: example-upload-counter_test-xc7
   
   openocd -f ${INSTALL_DIR}/conda/share/openocd/scripts/board/digilent_arty.cfg -c "init; pld load 0 top.bit; exit"

