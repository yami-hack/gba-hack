#!/bin/bash
arm-none-eabi-ld fe8us.rom.o sub_800A240.o -Tromhack.ld -o fe8us.elf -Tlink.ld
#注意：-Tromhack.ld必须再-Tlink.ld前面
