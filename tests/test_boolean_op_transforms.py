"""Tests for `boolean_op_transforms` module."""

import pytest


def test_single_bit_and_operation():
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
                x_tag_conservative_prop0_ABCD & y_tag_conservative_prop0_ABCD
            );
            assign z_tag_precise_prop0_ABCD = (
                (x_tag_precise_prop0_ABCD & y_tag_precise_prop0_ABCD) |
                (x & y_tag_precise_prop0_ABCD) |
                (y & x_tag_precise_prop0_ABCD)
            );
        endmodule
    """

    assert input_module == expected_output
