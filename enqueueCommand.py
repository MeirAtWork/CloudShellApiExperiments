import cloudshell.api.cloudshell_api as api

session = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')

res_id = '330d98ae-caf8-46f3-b064-eae4bb1a4ef2'

for x in range(10000):
    session.EnqueueCommand(res_id, "my service model", "Service", "cmd_run_cleanup_command", [], True)

print("done!!!")
