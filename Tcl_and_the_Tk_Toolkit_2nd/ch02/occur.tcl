#!/usr/bin/tclsh

proc occur {value list} {
    set count 0
    foreach el $list {
        if $el==$value {
            incr count
        }
    }
    return $count
}

puts [occur 18 {1 18 -7 18 5}]
