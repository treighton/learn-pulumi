from datetime import datetime
import json
import azure.functions as func

app = func.FunctionApp()

def main(req: func.HttpRequest, msg: func.Out[str]) -> func.HttpResponse:

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
    }

    if req.method == "OPTIONS":
        return func.HttpResponse("", headers=headers, status_code=204)

    now = datetime.now()
    now_in_ms = int(now.timestamp()) * 1000

    headers["Content-Type"] = "application/json"

    output_data = {
        "now": now_in_ms,
        "msg": "im in a queue!" 
    }

    json_output_data = json.dumps(output_data)

    msg.set(json_output_data)

    return func.HttpResponse(
        json_output_data, headers=headers, status_code=200
    )
