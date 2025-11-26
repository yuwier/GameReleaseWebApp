from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Optional
from service import sort_filter_table, get_all_unique_values
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/games/", response_class=HTMLResponse)
def get_games(
	request: Request,
	column_sort: Optional[List[str]] = Query(None),
	column_filter: Optional[str] = None,
	value_filter: Optional[str] = None,
	ascending: bool = True,
	page: int = 1,
	limit: int = 10,
):
	result = sort_filter_table(
		column_sort=column_sort,
		column_filter=column_filter,
		value_filter=value_filter,
		ascending=ascending,
		page=page,
		limit=limit,
	)
	
	unique_values = get_all_unique_values()

	return templates.TemplateResponse(
		"index.html", {"request": request, "items": result, 'unique_values': unique_values, "total_pages": 9, "page": page, 'limit': limit}
	)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run("app:app", reload=True)
