"""Tests of the pyslang library, especially involving string conversions."""

import pyslang


def test_full_circle_string() -> None:
    """Test that converting a string to a SyntaxTree and back gives the same string."""
    input_str = """
        module and_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x & y;
        endmodule
    """

    ast = pyslang.SyntaxTree.fromText(input_str)
    output_str = str(ast.root)

    assert input_str.strip() == output_str.strip()
    assert input_str.rstrip() == output_str.rstrip()
