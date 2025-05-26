"""Transformations for boolean operations."""

import pyslang


def transform_boolean_op(verilog: str) -> str:
    """Transform the boolean operations in the given Verilog code."""

    ast = pyslang.SyntaxTree.fromText(verilog)

    def visit_all(
        node: pyslang.SyntaxNode,
        *,
        idx_chain: list[int],
    ) -> None:
        """Visit all the nodes in the given syntax tree.

        Performs a depth-first search.
        """
        idx_chain_str = "".join(f"[{idx}]" for idx in idx_chain)

        print(
            f"{idx_chain_str} -> "
            f"Node: '{str(node).strip()}', Kind: {node.kind}, Type: {type(node)}"
        )

        if isinstance(node, pyslang.Token):
            return

        for idx, sub_node in enumerate(node):
            visit_all(
                sub_node,
                idx_chain=[*idx_chain, idx].copy(),
            )

    visit_all(ast.root, idx_chain=[])

    # Try renaming 'x' to something else.
    # [1][3][1][0][2][0] -> Node: 'x', Kind: TokenKind.Identifier, Type: <class 'pyslang.Token'>

    ast.root[1][3][1][0][2][0] = pyslang.Token(
        alloc=pyslang.BumpAllocator,
        kind=pyslang.TokenKind.Identifier,
        rawText="x_new_name",
        location=pyslang.SourceLocation(),
    )

    return str(ast.root)

    # for node in ast.root:
    #     print(f"Node: {node}")
    #     for sub_node in node:
    #         print(f"Sub-node: {sub_node}")

    #     breakpoint()

    ast = pyslang.SyntaxTree.fromText(verilog)
    module = ast.root

    if module.kind != pyslang.SyntaxKind.ModuleDeclaration:
        msg = "The given code is not a Verilog `module`."
        raise ValueError(msg)

    new_ports: list[str] = []
    tag_signals: list[str] = []
    assignments: list[str] = []

    ast_out = pyslang.SyntaxTree()

    for port in module:
        name = port.name.value
        direction = port.direction.value
        data_type = port.type.syntax_string

        tag_name = f"{name}_tag_conservative_prop0_ABCD"
        new_ports.append(f"{direction} {data_type} {name}")
        new_ports.append(f"{direction} {data_type} {tag_name}")

        if direction == "input":
            tag_signals.append(tag_name)
        elif direction == "output":
            assignments.append(tag_name)

    z_tag = assignments[0] if assignments else "z_tag_conservative_prop0_ABCD"
    tag_assignment = f"assign {z_tag} = (" + " | ".join(tag_signals) + ");"

    module_body = input_str.split(";", 1)[1].strip()

    transformed_module = f"""
        module {module.name.value} (
            {",\n            ".join(new_ports)}
        );
            {module_body}
            {tag_assignment}
        endmodule
    """
    return transformed_module.strip()


if __name__ == "__main__":
    input_str = """
        module and_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x & y;
        endmodule
    """

    print(transform_boolean_op(input_str))
