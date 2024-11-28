use std::{collections::HashMap, path::PathBuf};

use sv_parser::{parse_sv_str, unwrap_node, Locate, RefNode, SyntaxTree};


fn main() {
    let verilog_code = r#"
        module and_gate (
            input wire x,
            input wire y,
            output wire z
        );
            assign z = x & y;
        endmodule
    "#;

    let fake_path = PathBuf::from("test.sv");
    // The list of defined macros
    let defines = HashMap::new();
    // The list of include paths
    let includes: Vec<PathBuf> = Vec::new();
    let syntax_tree = parse_sv_str(
        verilog_code, fake_path, &defines, &includes, true, true
    );

    if let Ok((tree, _)) = syntax_tree {
        print_tree(tree);
    }
    else {
        println!("Failed to parse the code");
    }
}

fn print_tree(syntax_tree: SyntaxTree) {
    let mut total_element_count = 0;
    let mut interesting_element_count = 0;

    // &SyntaxTree is iterable
    for node in &syntax_tree {
        total_element_count += 1;
        // The type of each node is RefNode
        match node {
            RefNode::ModuleDeclarationNonansi(x) => {
                // unwrap_node! gets the nearest ModuleIdentifier from x
                let id = unwrap_node!(x, ModuleIdentifier).unwrap();

                let id = get_identifier(id).unwrap();

                // Original string can be got by SyntaxTree::get_str(self, locate: &Locate)
                let id = syntax_tree.get_str(&id).unwrap();
                println!("module: {}", id);
                
                interesting_element_count += 1;
            }
            RefNode::ModuleDeclarationAnsi(x) => {
                let id = unwrap_node!(x, ModuleIdentifier).unwrap();
                let id = get_identifier(id).unwrap();
                let id = syntax_tree.get_str(&id).unwrap();
                println!("module: {}", id);

                interesting_element_count += 1;
            }
            // Create a list of the non-interesting ones.
            RefNode::WhiteSpace(_) | RefNode::Locate(_) => {}
            x => {
                println!("{:?}", x);

                interesting_element_count += 1;
            }
        }
    }

    println!(
        "Total elements: {}, Interesting elements: {}",
        total_element_count, interesting_element_count
    );
}

/// Source: sv-parser README
fn get_identifier(node: RefNode) -> Option<Locate> {
    // unwrap_node! can take multiple types
    match unwrap_node!(node, SimpleIdentifier, EscapedIdentifier) {
        Some(RefNode::SimpleIdentifier(x)) => {
            return Some(x.nodes.0);
        }
        Some(RefNode::EscapedIdentifier(x)) => {
            return Some(x.nodes.0);
        }
        _ => None,
    }
}
