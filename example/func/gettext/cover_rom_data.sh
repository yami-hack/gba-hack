#!/bin/bash
arm-none-eabi-objcopy --set-section-flags .rom="r,c,a" fe8us.elf
