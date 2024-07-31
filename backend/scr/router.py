from fastapi import APIRouter
from scr.init import cmc_client

router = APIRouter(
    prefix="/currencies"
)

@router.get("")
async def get_currencies():
    return await cmc_client.get_listings()


@router.get("/{specific_id}")
async def get_currencies(specific_id: int):
    return await cmc_client.get_specific(specific_id)