import time
import cloudshell.api.cloudshell_api as api

session = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')

res_id = '69b58834-2f2e-40ac-8ce6-a09e809f37a3'

for x in range(1000):
    print("sending 1000 requests")
    for y in range(1000):
        cmdInput1 = api.InputNameValue("batch", str(x))
        cmdInput2 = api.InputNameValue("number", str(y))
        session.EnqueueCommand(res_id, "my service model", "Service", "cmd_run_cleanup_command", [cmdInput1, cmdInput2], True)
    print("1000 requests sent. waiting 1 minute")
    time.sleep(60)


print("done!!!")
