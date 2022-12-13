class Program {
  static void Main(string[] args) {
    Cat cat1 = new Cat("Tane");
    cat1.Meow();
    Cat cat2 = new Cat("Papu");
    cat2.Meow();
    Cat cat3 = cat1;
    cat3.Meow();
    cat2 = cat1;
    cat2.Meow();
  }
}

class Cat {
  private string name;

  public Cat(string name) {
    this.name = name;
  }

  public void Meow() {
    Console.WriteLine(name + " says meow!");
  }
}


