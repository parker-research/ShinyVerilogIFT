"""Basic tests for the tests module."""

# TODO: Try import pyslang
import pyverilog


def test_always_passes() -> None:
    """Test that always passes."""
    assert True


def test_verilog_equality() -> None:
    """Test that two Verilog modules with minor differences are evaluated as equal."""

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
            input wire y, // Comment here
            output wire z
        );
            // Comment here
            assign z = x & y;
            /* Another comment here */
        endmodule
    """

    # st1 = pyslang.SyntaxTree.fromText(input_1)
    # st1_again = pyslang.SyntaxTree.fromText(input_1)
    # st1_stripped = pyslang.SyntaxTree.fromText(input_1.strip())

    # assert st1 == st1_again
    # assert st1 == st1_stripped

    # st2 = pyslang.SyntaxTree.fromText(input_2)

    pyverilog_input_1 = pyverilog.utils.verilog.read_verilog(input_1)
