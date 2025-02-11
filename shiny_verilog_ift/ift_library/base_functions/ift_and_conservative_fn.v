function automatic logic ift_and_conservative_fn(
    input logic a_tag, 
    input logic b_tag
);
    return a_tag | b_tag;
endfunction
