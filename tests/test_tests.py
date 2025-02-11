"""Basic tests for the tests module."""

import pyslang


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

    st1 = pyslang.SyntaxTree.fromText(input_1)
    st1_again = pyslang.SyntaxTree.fromText(input_1)
    st1_stripped = pyslang.SyntaxTree.fromText(input_1.strip())

    assert st1.root.isEquivalentTo(st1_again.root)
    assert st1.root.isEquivalentTo(st1_stripped.root)
    assert st1_again.root.isEquivalentTo(st1_stripped.root)

    st2 = pyslang.SyntaxTree.fromText(input_2)
    st2_stripped = pyslang.SyntaxTree.fromText(input_2.strip())

    assert st1_stripped.root.isEquivalentTo(st2.root)
    assert st1.root.isEquivalentTo(st2.root)
    assert st1.root.isEquivalentTo(st2_stripped.root)
