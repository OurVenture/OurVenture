package OurVentureClass

import (
	"math"
)

type Relation struct {
	RelationsList []string
}

type RelationType struct {
	RelationTypeName  string
	RelationTypeValue float64
}

func (rel *RelationType) CalculateRelationship() {
	possibleTypes := []string{"Atrocious", "Terrible", "Bad", "Worsening",
		"Neutral", "Positive", "Good",
		"Favorable", "Exceptional"}
	relNum := math.Round(rel.RelationTypeValue*10) / 10
	if relNum >= -4.5 && relNum <= -6.0{
		rel.RelationTypeName = possibleTypes[0]
	} else if relNum >= -3.5 && relNum <= -4.4 {
		rel.RelationTypeName = possibleTypes[1]
	} else if relNum >= -2.0 && relNum <= -3.4 {
		rel.RelationTypeName = possibleTypes[2]
	} else if relNum >= -0.5 && relNum <= -1.9 {
		rel.RelationTypeName = possibleTypes[3]
	} else if relNum >= -0.4 && relNum <= 0.4 {
		rel.RelationTypeName = possibleTypes[4]
	}
 }