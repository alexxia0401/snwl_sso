#!/usr/bin/tclsh

if {![info exists foobar]} {
    set foobar 0
} else {
    incr foobar
}
