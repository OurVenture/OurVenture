package main

import (
	"OurVenture/RestApi/OurVentureClass"
	"github.com/gin-gonic/gin"
	"fmt"
)

func main() {
	var numInput int
	fmt.Println("Starting service, Please write the number of players: ")
	_, err := fmt.Scanf("%d", &numInput)
	
	fmt.Println("Number of players is ", numInput, err)
	
	for i := 1; i <= numInput; i++ {
		fmt.Println(i)
		fmt.Println("Please add information about your players!")
		playerName, charName, chosenClass, chosenAlignment, isDiplomatic := GetPlayerArguments()
		fmt.Println(playerName, charName, chosenAlignment, chosenClass, isDiplomatic)
	}
	pc := OurVentureClass.Player{
		FirstName: "Johnny",
		Name: "X",
		Class: "Y",
		Alignment: "Z",
		Diplomatic: false,
		Relation: OurVentureClass.Relation{
			RelationsList: []OurVentureClass.RelationType{
				{
					RelationTypeName: OurVentureClass.GetRelationshipValue(0.0),
					RelationTypeValue: 0.0,
				},
				{
					RelationTypeName: OurVentureClass.GetRelationshipValue(0.0),
					RelationTypeValue: 0.3,
				},
				{
					RelationTypeValue: 0.7,
					RelationTypeName: OurVentureClass.GetRelationshipValue(0.7),
				},

			},
		},
	}
	
	pc.ShowPlayerDetails()
	// print(pc.Relation.RelationsList[2])
	// Putting this here to suppress go errors
	r := gin.Default()
	print("We like ", r)
}
