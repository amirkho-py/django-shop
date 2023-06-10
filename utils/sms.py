from sms_ir import SmsIr
from random import randint
sms_ir = SmsIr(
    api_key="",
    linenumber="+9830004757",
)




sms_ir.send_verify_code(
    number="9379364715",
    template_id="830439",
    parameters=[
        {
            "name" : "CODE",
            "value": str(randint(1000,9999)),
        },
    ],
)
