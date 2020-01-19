set circuit [lindex $argv 0]
#puts "this is $circuit"
set tb [lindex $argv 1]
proc command {circuit tb} {
    set cmd1 [exec python3.7 write.py $tb]
    set cmd2 [exec verilator -Wall --cc $circuit --exe sim_main.cpp]
    set cmd3 [exec make -j -C obj_dir -f Vour.mk Vour]
    set cmd4 [exec obj_dir/Vour]
    puts $cmd1
    puts $cmd2
    puts $cmd3
    puts $cmd4
}
command $circuit $tb
