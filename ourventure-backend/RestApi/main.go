package main

import (
	"fmt"
	"OurVenture/RestApi/OurVentureClass"
)

func main() {
	fmt.Println("Hello, world.")
	pc := OurVentureClass.Player{
		FirstName: "Johnny",
		Name: "X",
		Class: "Y",
		Alignment: "Z",
		Diplomatic: false,
	}
	
	pc.ShowPlayerDetails()
}
