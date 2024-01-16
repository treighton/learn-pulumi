from datetime import datetime
import json
import logging
import azure.functions as func

app = func.FunctionApp()

def main(msg: func.QueueMessage, msg_out: func.Out[str]) -> func.QueueMessage:
    logging.info("Python Queue trigger function processed a %s", msg)

    now = datetime.now()
    now_in_ms = int(now.timestamp()) * 1000

    output_data = json.dumps({
            "now": now_in_ms,
            "msg": msg
        })

    logging.info(
        output_data
    )

    return msg_out.set(output_data)
    
