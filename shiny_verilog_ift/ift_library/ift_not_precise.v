module ift_not_precise (
    input wire a,
    input wire a_tag,
    output wire o_tag
);
    assign o_tag = a_tag;
endmodule
