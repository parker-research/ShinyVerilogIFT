function automatic logic ift_or_conservative_fn (
    input wire a_tag,
    input wire b_tag
);
    return a_tag | b_tag;
endfunction
