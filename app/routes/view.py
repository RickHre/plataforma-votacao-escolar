from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse

router = APIRouter(tags=["view"])

@router.get("/", include_in_schema=False)
def index():
    return RedirectResponse(url="/simple")

@router.get("/simple", include_in_schema=False)
def index():
    return FileResponse("./app/views/simple.html")

@router.get("/complete", include_in_schema=False)
def index():
    return FileResponse("./app/views/complete.html")

@router.get("/admin", include_in_schema=False)
def index():
    return FileResponse("./app/views/admin.html")
