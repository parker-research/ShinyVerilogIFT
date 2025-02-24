use std::{collections::HashMap, path::PathBuf};

use sv_parser::{parse_sv_str, unwrap_node, Locate, RefNode, SyntaxTree};

use crate::ast_transforms::get_identifier;

pub fn add_tracking_signals(st: SyntaxTree) -> SyntaxTree {
    let mut new_st = st.clone();

    for node in &mut new_st {
        match node {
            RefNode::ModuleDeclarationNonansi(x) => {
                let id = unwrap_node!(x, ModuleIdentifier).unwrap();
                let id = get_identifier(id).unwrap();
                let id = new_st.get_str(&id).unwrap();
                println!("module: {}", id);
            }
            RefNode::ModuleDeclarationAnsi(x) => {
                let id = unwrap_node!(x, ModuleIdentifier).unwrap();
                let id = get_identifier(id).unwrap();
                let id = new_st.get_str(&id).unwrap();
                println!("module: {}", id);
            }
            _ => {}
        }
    }

    new_st
}
