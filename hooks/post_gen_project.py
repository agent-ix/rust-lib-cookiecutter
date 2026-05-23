#!/usr/bin/env python
"""Post-generation hook for rust-lib-cookiecutter.

Initializes the generated project: makes scripts executable, runs `cargo fmt`
so the initial commit is already format-clean, and (if cargo is available)
runs `cargo check` as a quick sanity test.

Skips initialization if cargo is not on PATH.
"""
import os
import shutil
import stat
import subprocess
import sys


def make_executable(path: str) -> None:
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)


def main() -> None:
    script = os.path.join("scripts", "check_unsafe_comments.sh")
    if os.path.exists(script):
        make_executable(script)

    if shutil.which("cargo") is None:
        print("\ncargo not found on PATH; skipping fmt + check.")
        print("Install Rust (https://rustup.rs) then run:")
        print("  make fmt && make lint && make test")
        return

    print("\nRunning cargo fmt...")
    subprocess.run(["cargo", "fmt"], check=False)

    print("Running cargo check...")
    result = subprocess.run(["cargo", "check"], check=False)
    if result.returncode != 0:
        print("\ncargo check failed. Project generated, but needs manual fix.")
        sys.exit(1)

    print("\nProject is ready. Try: make fmt-check && make lint && make test")


if __name__ == "__main__":
    main()
