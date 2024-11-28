# Flow Rules

The following flow rules are considered in this project:

1. Combination AND: `C = A & B`
    * [RTLIFT, Fig 5]
    * Conservative: `C_tag = A_tag | B_tag`
    * Precise: `C_tag = (A & B_tag) | (B & A_tag)`
    * Precise, according to RTLIFT: `C_tag = (A & B_tag) | (B & A_tag) | (A & B)`



* Conditional Assignment in `if` Statement
    * [RTLIFT, Fig 5]
    * Imprecise (conservative?):
        ```verilog
        if (condition) begin
            C = A;
            C_tag = A_tag | condition_tag;
        end
        else begin
            C = B;
            C_tag = B_tag | condition_tag;
        end
        ```
    
    * Precise:
        ```verilog
        if (condition) begin
            C = A;
            C_tag = A_tag | (condition_tag & ((A_tag & B_tag) | (A_tag ^ B_tag)));
        end
        else begin
            C = B;
            C_tag = B_tag | (condition_tag & ((A_tag & B_tag) | (A_tag ^ B_tag)));
        end
        ```
