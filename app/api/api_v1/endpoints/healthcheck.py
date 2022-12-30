from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def healthcheck() -> Any:
    """
    ### API healthcheck
    """
    return {"ok": True, "status": "healthy "}
