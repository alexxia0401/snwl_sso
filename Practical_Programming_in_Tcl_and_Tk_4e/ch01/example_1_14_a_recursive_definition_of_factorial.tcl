#!/usr/bin/tclsh

proc Factorial {x} {
    if {$x <= 1} {
        return 1
    } else {
        return [expr {$x * [Factorial [expr {$x -1}]]}]
    }
}

puts [Factorial 10]
