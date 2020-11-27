#!/bin/bash
set -e

fpga_fam=$1
shift

# select particular example for xc7
examples="$@"
if [ "$fpga_fam" == "xc7" -a -z "$examples" ] ; then
    examples="counter picosoc litex"
fi;

# activate conda and enter example dir
eval $(tuttest docs/building-examples.rst export-install-dir)
eval $(tuttest docs/building-examples.rst fpga-fam-$fpga_fam)
eval $(tuttest docs/building-examples.rst conda-prep-env)
eval $(tuttest docs/building-examples.rst conda-act-env)
eval $(tuttest docs/building-examples.rst enter-dir-$fpga_fam)

if [ "$fpga_fam" = "xc7" ]; then
    for example in $examples; do
        case $example in
            "counter")
                # counter example
                eval $(tuttest ../docs/building-examples.rst example-counter-a35t)
                make -C counter_test clean
                eval $(tuttest ../docs/building-examples.rst example-counter-a100t)
                make -C counter_test clean
                eval $(tuttest ../docs/building-examples.rst example-counter-basys3)
                make -C counter_test clean
                ;;
            "picosoc")
                # PicoSoC example
                eval $(tuttest ../docs/building-examples.rst example-picosoc-basys3) 
                ;;
            "litex")
                # LiteX example
                eval $(tuttest ../docs/building-examples.rst example-litex-deps)
                eval $(tuttest ../docs/building-examples.rst example-litex-a35t)
                ;;
        esac
    done
else
    # counter example
    eval $(tuttest ../docs/building-examples.rst eos-s3-counter)
fi;
