package OurVentureClass


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
	if rel.RelationTypeValue >= -4.5 && rel.RelationTypeValue <= -6.0{
		rel.RelationTypeName = possibleTypes[0]
	}
}