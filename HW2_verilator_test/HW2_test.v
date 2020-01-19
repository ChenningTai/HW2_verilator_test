`timescale 1ns/100ps
module HW2_test();
reg stop, clk, reset;
wire [3:0] I;

HW2 uut (
    .I(I),
    .stop(stop),
    .clk(clk),
    .reset(reset)//?需要括號?
    );

initial clk = 1'b0;
always #10 clk = ~clk;

initial begin
    // $sdf_annotate("HW2.sdf",my_alu);
    // $fsdbDumpfile("HW2.fsdb"); 
    // $fsdbDumpvars; 
    $dumpfile("HW2.vcd");
    $dumpvars;
    stop = 1'b0;
    reset = 1'b1;
    #180 stop = 1'b1;
end
endmodule