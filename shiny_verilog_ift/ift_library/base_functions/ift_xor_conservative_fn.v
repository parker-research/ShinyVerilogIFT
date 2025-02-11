function automatic logic ift_xor_conservative_fn (
    input wire a_tag,
    input wire b_tag
);
    return a_tag | b_tag;
endfunction
