"""Copy of the elaboration example in Pyslang."""

import sys

from pyslang import CommandLineOptions, Driver


def demo_elaboration() -> None:
    """Elaborates a design, logging any diagnostics (errors, mostly) to the console.

    Source: https://github.com/MikePopoloski/slang/blob/master/pyslang/examples/driver.py
    """
    # Create a slang driver with default command line arguments
    driver = Driver()
    driver.addStandardArgs()

    # Parse command line arguments
    args = " ".join(sys.argv)
    if not driver.parseCommandLine(args, CommandLineOptions()):
        return

    # Process options and parse all provided sources
    if not driver.processOptions() or not driver.parseAllSources():
        return

    # Perform elaboration and report all diagnostics
    compilation = driver.createCompilation()
    driver.reportCompilation(compilation, quiet=False)


if __name__ == "__main__":
    demo_elaboration()
