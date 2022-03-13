from fastapi import APIRouter, Depends, HTTPException

#Init router class, holds all sub functions
router = APIRouter(
    prefix="/relations",
    tags=["relations_control", "extension"]
    )


@router.get("/")
async def get_overview():
    print("Values are: ")
    # TODO: Get values of NPCs, Relationship structure, And Player relations + recent history (last 3 actions)

@router.get("/{relation_tag}")
async def get_relation_connection(person1: str = "bill", person2: str = "ben"):
    x, y = person1, person2
    print(f"Showing relations between: {x} and {y}")
