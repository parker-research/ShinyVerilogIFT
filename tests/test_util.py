"""Tests for the `util.py` module."""

from shiny_verilog_ift.util import is_verilog_equal


def test_is_verilog_equal_when_equal() -> None:
    """Assert `is_verilog_equal` when the two Verilog modules are equal."""
    input_1 = """
        module and_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x & y;
        endmodule
    """

    input_2 = """
        module and_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x & y;
            // Comment here
        endmodule
    """

    assert is_verilog_equal(input_1, input_2) is True


def test_is_verilog_equal_when_not_equal() -> None:
    """Assert `is_verilog_equal` when the two Verilog modules are not equal."""
    input_1 = """
        module and_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x & y;
        endmodule
    """

    input_2 = """
        module or_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x | y;
        endmodule
    """

    assert is_verilog_equal(input_1, input_2) is False
