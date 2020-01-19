module HW2(I, clk, reset, stop);
output [3:0] I;
input clk;
input reset;
input stop;

reg [3:0] I;
wire d0, d1, d2, d3;

TFF tff0(I[0], stop, clk, reset);
nand(d0, ~stop, I[0]);//(out, in, in)
TFF tff1(I[1], d0, clk, reset);
nand(d1, ~d0, I[1]);
TFF tff2(I[2], d1, clk, reset);
nand(d2, ~d1, I[2]);
TFF tff3(d3, d2, clk, reset);
endmodule

module TFF(in, clk, reset, out);
output out;
input in, clk, reset;
wire dd, d;

xor(dd, in, out);
not(d, dd);
DFF dff0(out, d, clk, reset);
endmodule

module DFF(q, d, clk, reset);
output q;
input d, clk, reset;
reg q;
always @(posedge clk or posedge reset) begin
    if (reset) begin
        // reset
        q = 1'b0;
    end
    else begin
        q = d;
    end
end
endmodule