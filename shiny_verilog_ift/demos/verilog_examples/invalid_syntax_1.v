module ift_or_conservative (
    input wire a_tag,
    input wire b_tag,
    output wire o_tag
);
    assign o_tag = a_tag | b_tag
endmodule
