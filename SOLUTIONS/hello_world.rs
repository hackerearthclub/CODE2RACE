fn main() {
    let mut name = String::new();
    std::io::stdin()
        .read_line(&mut name)
        .expect("Pleas add a valid string for your Name");
    println!("hello World! from {}", name);
}