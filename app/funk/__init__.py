from datetime import datetime
import json
import logging
import azure.functions as func

app = func.FunctionApp()

def main(msg: func.QueueMessage) -> None:
    logging.info("Python Queue trigger function processed a %s", msg)

    now = datetime.now()
    now_in_ms = int(now.timestamp()) * 1000

    logging.info(
        json.dumps({
            "now": now_in_ms,
            "msg": msg
        })
    )
    
