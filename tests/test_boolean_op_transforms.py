"""Tests for `boolean_op_transforms` module."""

import pytest


def test_single_bit_and_operation() -> None:
    """Test the `and_transform` function."""
    input_module = """
        module and_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x & y;
        endmodule
    """

    # Conservative Source: (Ardeshiricham et al. 2017), Figure 3, Part a
    # Precise Source: (Ardeshiricham et al. 2017), Figure 3, Part b
    # Precise Source: (Hu et al. 2011), Equation 1
    expected_output = """
        module and_gate (
            input wire x,
            input wire x_tag_conservative_prop0_ABCD,
            input wire x_tag_precise_prop0_ABCD,
            input wire y,
            input wire y_tag_conservative_prop0_ABCD,
            input wire y_tag_precise_prop0_ABCD,
            output wire z,
            output wire z_tag_conservative_prop0_ABCD,
            output wire z_tag_precise_prop0_ABCD
        );
            assign z = x & y;
            assign z_tag_conservative_prop0_ABCD = (
                x_tag_conservative_prop0_ABCD | y_tag_conservative_prop0_ABCD
            );
            assign z_tag_precise_prop0_ABCD = (
                (x_tag_precise_prop0_ABCD & y_tag_precise_prop0_ABCD) |
                (x & y_tag_precise_prop0_ABCD) |
                (y & x_tag_precise_prop0_ABCD)
            );
        endmodule
    """

    raise NotImplementedError


def test_single_bit_or_operation() -> None:
    """Test the `or_transform` function."""
    input_module = """
        module or_gate (
            input wire g,
            input wire h,
            output wire f
        );
            assign f = g | h;
        endmodule
    """

    # Precise Source: (Hu et al. 2011), Equation 7
    expected_output = """
        module or_gate (
            input wire g,
            input wire g_tag_conservative_prop0_ABCD,
            input wire g_tag_precise_prop0_ABCD,
            input wire h,
            input wire h_tag_conservative_prop0_ABCD,
            input wire h_tag_precise_prop0_ABCD,
            output wire f,
            output wire f_tag_conservative_prop0_ABCD,
            output wire f_tag_precise_prop0_ABCD
        );
            assign f = g & h;
            assign f_tag_conservative_prop0_ABCD = (
                g_tag_conservative_prop0_ABCD | h_tag_conservative_prop0_ABCD
            );
            assign f_tag_precise_prop0_ABCD = (
                (g_tag_precise_prop0_ABCD & h_tag_precise_prop0_ABCD) |
                ((~g) & h_tag_precise_prop0_ABCD) |
                ((~h) & g_tag_precise_prop0_ABCD)
            );
        endmodule
    """

    raise NotImplementedError


def test_single_bit_xor_operation() -> None:
    """Test the `xor_transform` function."""
    input_module = """
        module xor_gate (
            input wire g,
            input wire h,
            output wire f
        );
            assign f = g ^ h;
        endmodule
    """

    # Precise Source: (Hu et al. 2011), Equation 10

    # Interesting property: Conservative and precise tags are the same calculation.
    expected_output = """
        module xor_gate (
            input wire g,
            input wire g_tag_conservative_prop0_ABCD,
            input wire g_tag_precise_prop0_ABCD,
            input wire h,
            input wire h_tag_conservative_prop0_ABCD,
            input wire h_tag_precise_prop0_ABCD,
            output wire f,
            output wire f_tag_conservative_prop0_ABCD,
            output wire f_tag_precise_prop0_ABCD
        );
            assign f = g ^ h;
            assign f_tag_conservative_prop0_ABCD = (
                g_tag_conservative_prop0_ABCD | h_tag_conservative_prop0_ABCD
            );
            assign f_tag_precise_prop0_ABCD = (
                g_tag_conservative_prop0_ABCD | h_tag_conservative_prop0_ABCD
            );
        endmodule
    """

    raise NotImplementedError


def test_single_bit_not_operation() -> None:
    """Test the `not_transform` function."""
    input_module = """
        module not_gate (
            input wire g,
            output wire f
        );
            assign f = ~g;
        endmodule
    """

    # Precise Source: (Hu et al. 2011), Equation 10

    # Interesting property: Conservative and precise tags are the same calculation.
    expected_output = """
        module not_gate (
            input wire g,
            input wire g_tag_conservative_prop0_ABCD,
            input wire g_tag_precise_prop0_ABCD,
            output wire f,
            output wire f_tag_conservative_prop0_ABCD,
            output wire f_tag_precise_prop0_ABCD
        );
            assign f = g & h;
            assign f_tag_conservative_prop0_ABCD = (
                g_tag_conservative_prop0_ABCD
            );
            assign f_tag_precise_prop0_ABCD = (
                g_tag_conservative_prop0_ABCD
            );
        endmodule
    """

    raise NotImplementedError


def test_single_bit_2mux_composition_operation() -> None:
    """Test tagging on a sample 2-bit mux design."""
    # Source: (Hu et al. 2011), Figure 3, Part a.
    input_module = """
        module basic_2mux (
            input wire S,
            input wire A,
            input wire B,
            output wire O
        );
            assign C = S & A;
            assign D = ~S & B;
            assign O = C | D;
        endmodule
    """

    # TODO: Figure out what the correct tag outputs are.
    expected_output = """
        module basic_2mux (
            input wire S,
            input wire S_tag_conservative_prop0_ABCD,
            input wire S_tag_precise_prop0_ABCD,
            input wire A,
            input wire A_tag_conservative_prop0_ABCD,
            input wire A_tag_precise_prop0_ABCD,
            input wire B,
            input wire B_tag_conservative_prop0_ABCD,
            input wire B_tag_precise_prop0_ABCD,
            output wire O,
            output wire O_tag_conservative_prop0_ABCD,
            output wire O_tag_precise_prop0_ABCD
        );
            assign C = S & A;
            assign C_tag_conservative_prop0_ABCD = (
                S_tag_conservative_prop0_ABCD | A_tag_conservative_prop0_ABCD
            );
            assign C_tag_precise_prop0_ABCD = (
                (S_tag_precise_prop0_ABCD & A_tag_precise_prop0_ABCD)
                | (S & A_tag_precise_prop0_ABCD)
                | (A & S_tag_precise_prop0_ABCD)
            );

            assign D = ~S & B;
            assign D_tag_conservative_prop0_ABCD = (
                S_tag_conservative_prop0_ABCD | B_tag_conservative_prop0_ABCD
            );
            assign D_tag_precise_prop0_ABCD = (
                (S_tag_precise_prop0_ABCD & B_tag_precise_prop0_ABCD)
                | ((~S) & B_tag_precise_prop0_ABCD)
                | (B & S_tag_precise_prop0_ABCD)
            );

            assign O = C | D;
            assign O_tag_conservative_prop0_ABCD = (
                C_tag_conservative_prop0_ABCD | D_tag_conservative_prop0_ABCD
            );
            assign O_tag_precise_prop0_ABCD = (
                (C_tag_precise_prop0_ABCD & D_tag_precise_prop0_ABCD)
                | ((~C) & D_tag_precise_prop0_ABCD)
                | ((~D) & C_tag_precise_prop0_ABCD)
            );
        endmodule
    """

    raise NotImplementedError


def test_single_bit_composition_operation() -> None:
    """Test tagging on composition of many operations."""
    input_module = """
        module and_gate (
            input wire w,
            input wire x,
            input wire y,
            output wire z
        );
            assign z = (x & y) | (~w);
        endmodule
    """

    # TODO: Figure out what the correct tag outputs are.
    expected_output = """
        module and_gate (
            input wire w,
            input wire w_tag_conservative_prop0_ABCD,
            input wire w_tag_precise_prop0_ABCD,
            input wire x,
            input wire x_tag_conservative_prop0_ABCD,
            input wire x_tag_precise_prop0_ABCD,
            input wire y,
            input wire y_tag_conservative_prop0_ABCD,
            input wire y_tag_precise_prop0_ABCD,
            output wire z,
            output wire z_tag_conservative_prop0_ABCD,
            output wire z_tag_precise_prop0_ABCD
        );
            assign z = (x & y) | (~w);
            assign z_tag_conservative_prop0_ABCD = (
                ...
            );
            assign z_tag_precise_prop0_ABCD = (
                ...
            );
        endmodule
    """

    raise NotImplementedError
