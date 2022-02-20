package OurVentureClass

import (
	"math"
)

type Relation struct {
	RelationsList []RelationType 
}

type RelationType struct {
	RelationTypeName  string `example:"Neutral"`
	RelationTypeValue float64 `example:"0.0"`
}

func NewRelation(RelationsList []RelationType) Relation {
	print("Making new relation!")
	return Relation{RelationsList: RelationsList}
}

func NewRelationType (RelationTypeName string, RelationTypeValue float64) RelationType {
	return RelationType{RelationTypeName: GetRelationshipValue(0.0), RelationTypeValue: 0.0}
}
func GetRelationshipValue(rel float64) string {
	// Details array of possible Relationship types, these could be objects themselves but a simple text reperesentation will suffice for now ...
	possibleTypes := []string{"Atrocious", "Terrible", "Bad", "Worsening",
		"Neutral", "Positive", "Good",
		"Favorable", "Exceptional"}
	// Rounds the number to an integer, no preference given	
	relNum := math.Round(rel)
	// Checks which value to return
	if BetweenRange(-6.0, -4.5, relNum){
		return possibleTypes[0]
	} else if BetweenRange(-4.4, -3.4, relNum) {
		return possibleTypes[1]
	} else if BetweenRange(-3.3, -2.0, relNum) {
		return possibleTypes[2]
	} else if BetweenRange(-1.9, -0.5, relNum) {
		return possibleTypes[3]
	} else if BetweenRange(-0.4, 0.4, relNum) {
		return possibleTypes[4]
	} else if BetweenRange(0.5, 1.4, relNum) {
		return possibleTypes[5]
	} else if BetweenRange(1.5, 2.9, relNum) {
		return possibleTypes[6]
	} else if BetweenRange(3.0, 4.4, relNum) {
		return possibleTypes[7]
	} else if BetweenRange(4.5, 6.0, relNum) {
		return possibleTypes[8]
	} else if relNum > 6.0 || relNum < -6.0 {
		return "error"
	}
	return possibleTypes[4]
 }

func BetweenRange (argMin float64, argMax float64, comparisonArg float64) bool {
	if (comparisonArg >= argMin && comparisonArg <= argMax) {
		return true
	} else {
		return false
	}

}