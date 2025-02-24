use clap::{Parser, Subcommand};
use std::path::PathBuf;

use crate::ast_transforms;
use crate::debugging;

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Decode a Verilog file
    Decode {
        /// Path to the Verilog file
        path: PathBuf,
    },
    /// Perform IFT on a Verilog file
    Ift {
        /// Path to the Verilog file
        path: PathBuf,
    },
}

fn cli_action_decode(path: PathBuf) {
    println!("Decoding Verilog file: {:?}", path);

    let (ast, _defines) = ast_transforms::parse_sv_file_simple(path).unwrap();

    debugging::print_tree(ast);
}

fn cli_action_ift(path: PathBuf) {
    println!("Performing IFT on Verilog file: {:?}", path);

    let (ast, _defines) = ast_transforms::parse_sv_file_simple(path).unwrap();

    // FIXME: Make this do something cool instead.
    debugging::print_tree(ast);
}

pub fn main() {
    let cli = Cli::parse();

    match cli.command {
        Commands::Decode { path } => cli_action_decode(path),
        Commands::Ift { path } => cli_action_ift(path),
    }
}
