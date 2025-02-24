use sv_parser::{unwrap_node, RefNode, SyntaxTree};

use crate::ast_transforms::get_identifier;

pub fn print_tree(syntax_tree: SyntaxTree) -> () {
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
