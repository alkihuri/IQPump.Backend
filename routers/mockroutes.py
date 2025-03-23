


# mock routes for testing purposes only

from fastapi import APIRouter, HTTPException

router = APIRouter()
 

# mock touyters for mock duels for queez games between two players

@router.get("/mockduel/{player1}/{player2}")
async def mockduel(player1: str, player2: str):
    return {"player1": player1, "player2": player2, "winner": player1}

@router.get("/mockduel/{player1}/{player2}/{winner}")
async def mockduel(player1: str, player2: str, winner: str):
    return {"player1": player1, "player2": player2, "winner": winner}

@router.get("/mockduel/{player1}/{player2}/{winner}/{loser}")
async def mockduel(player1: str, player2: str, winner: str, loser: str):
    return {"player1": player1, "player2": player2, "winner": winner, "loser": loser}

@router.get("/mockduel/{player1}/{player2}/{winner}/{loser}/{score}")
async def mockduel(player1: str, player2: str, winner: str, loser: str, score: int):
    return {"player1": player1, "player2": player2, "winner": winner, "loser": loser, "score": score}