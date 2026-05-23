//! {{ cookiecutter.description }}

/// Placeholder entry point.
pub fn hello() -> &'static str {
    "hello from {{ cookiecutter.project_snake }}"
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn hello_returns_greeting() {
        assert!(hello().contains("{{ cookiecutter.project_snake }}"));
    }
}
