from sms_ir import SmsIr
from random import randint
sms_ir = SmsIr(
    api_key="8Ca4PBnyrDH6t9mQapjjB8eFsU8z6iBxEg0ExI33uaJl6hnlfyvePAKzSwd7XDkt",
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