package OurVentureClass

type Player struct {
	FirstName string
}

func (pc Player) ShowPlayerName() {
	pc.FirstName = "Johnny"
	print(pc.FirstName)

}
