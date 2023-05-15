# UPS Power Module Server

This module will install a server on your Raspberry Pi, that will in turn display current, voltage, power consumption,
remaining battery capacity, cpu temp, battery temp and usage of cpu, gpu, memory and disk, in the
onboard display of the Waveshare UPS HAT.

NOTE: THIS UPS HAT WAS MADE FOR JETSON NANO BUT IS BEING REPURPOSED FOR RASPBERRY PI

If you find an issue, please [let us know](../..//issues/new)!

## Setup

Follow the steps below to download UPS-Power-Module directly or create it from scratch.

On the Raspberry Pi, run the ups-display installation script

    git clone https://github.com/anvishinc/ups_display_server.git
    cd UPS-Power-Module
    sudo ./install.sh

