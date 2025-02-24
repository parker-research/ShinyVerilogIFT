use std::{collections::HashMap, path::PathBuf};

use sv_parser::{parse_sv, parse_sv_str, unwrap_node, Define, Locate, RefNode, SyntaxTree};

pub fn parse_sv_str_simple(
    verilog_code: &str,
) -> Result<
    (
        SyntaxTree,
        HashMap<std::string::String, std::option::Option<Define>>,
    ),
    sv_parser::Error,
> {
    let fake_path = PathBuf::from("test.sv");
    // The list of defined macros
    let defines = HashMap::new();
    // The list of include paths
    let includes: Vec<PathBuf> = Vec::new();
    let parsed_out = parse_sv_str(verilog_code, fake_path, &defines, &includes, true, true);
    parsed_out
}

pub fn parse_sv_file_simple(
    file_path: PathBuf,
) -> Result<
    (
        SyntaxTree,
        HashMap<std::string::String, std::option::Option<Define>>,
    ),
    sv_parser::Error,
> {
    let defines = HashMap::new();
    let includes: Vec<PathBuf> = Vec::new();
    let parsed_out = parse_sv(file_path, &defines, &includes, true, true);
    parsed_out
}

/// Source: sv-parser README
pub fn get_identifier(node: RefNode) -> Option<Locate> {
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
