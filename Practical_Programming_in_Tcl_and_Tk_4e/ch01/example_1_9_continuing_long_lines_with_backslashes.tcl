#!/usr/bin/tclsh

set one Hello
set two World
set totalLength [expr [string length $one] + \
    [string length $two]]
puts $totalLength
