module ift_and_precise (
    input wire a,
    input wire a_tag,
    input wire b,
    input wire b_tag,
    output wire o_tag
);
    assign o_tag = (
        (a_tag & b_tag) |
        (a & b_tag) |
        (b & a_tag)
    );
endmodule
