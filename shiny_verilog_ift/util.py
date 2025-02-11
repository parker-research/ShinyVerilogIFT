"""Utilities for this project."""

import pyslang


def is_verilog_equal(verilog_left: str, verilog_right: str) -> bool:
    """Check if two Verilog modules are equivalent."""
    ast_left = pyslang.SyntaxTree.fromText(verilog_left)
    ast_right = pyslang.SyntaxTree.fromText(verilog_right)
    return (ast_left.root).isEquivalentTo(ast_right.root)
