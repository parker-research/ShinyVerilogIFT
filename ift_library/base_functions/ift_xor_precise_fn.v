function automatic logic ift_xor_precise_fn (
    input wire a,
    input wire a_tag,
    input wire b,
    input wire b_tag
);
    return (
        a_tag | b_tag
    );
endfunction
