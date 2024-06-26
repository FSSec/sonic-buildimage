#!/bin/bash

set_pca_mux_idle_disconnect()
{
    echo -2 | tee /sys/bus/i2c/drivers/pca932d/*-00*/idle_state >& /dev/null
    if [ $? -ne 0 ]; then
        echo Fail to set pca932d mux idle disconnect
        exit 2
    fi
}

set_pca_mux_idle_disconnect
