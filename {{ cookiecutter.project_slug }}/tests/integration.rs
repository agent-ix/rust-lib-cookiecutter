use {{ cookiecutter.project_snake }}::hello;

#[test]
fn hello_is_non_empty() {
    assert!(!hello().is_empty());
}
