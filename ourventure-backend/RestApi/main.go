package main

import (
	"OurVenture/RestApi/OurVentureClass"
	"fmt"
)

func main() {
	var number int
	fmt.Println("Starting service, Please write the number of players: ")
	numInput, _ := fmt.Scanf("%d", &number)
	
	fmt.Println("Number of players is ", numInput)
	
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
}
