package OurVentureClass

import (
	"fmt"
)

type Player struct {
	FirstName string
	Name string
	Class string
	Alignment string
	Diplomatic bool
	Relations Relation
}

func NewPlayer(FirstName string, Name string, Class string, Alignment string, Diplomatic bool, Relations Relation) Player {
	print("Making new player!")
	// TODO: implement player class creation method 
	// Player class takes args similar to dict, and creates new instance of player
	return Player{FirstName: FirstName, Name: Name, Class: Class, Alignment: Alignment, Diplomatic: Diplomatic,
	// Create function to initiate relations
	Relations: Relations}
}

func (pc Player) ShowPlayerDetails() {
	fmt.Printf("%+v\n", pc)
}