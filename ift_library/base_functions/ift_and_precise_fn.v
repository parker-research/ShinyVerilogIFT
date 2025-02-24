function automatic logic ift_and_precise_fn(
    input logic a, 
    input logic a_tag, 
    input logic b, 
    input logic b_tag
);
    return (a_tag & b_tag) | (a & b_tag) | (b & a_tag);
endfunction
