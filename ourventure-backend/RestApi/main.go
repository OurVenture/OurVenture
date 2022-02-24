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
