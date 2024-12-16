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
            assign f = g & h;
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
