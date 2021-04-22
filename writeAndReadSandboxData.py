import cloudshell.api.cloudshell_api as api

session = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')

res_id = '7c76bd66-be05-45d3-8ff5-3736611170ac'

data1 = api.SandboxDataKeyValue('optimus', 'prime')
data2 = api.SandboxDataKeyValue('star', 'scream')

all_data = [data1, data2]

session.SetSandboxData(res_id, all_data)


data = session.GetSandboxData(res_id)

for keyValue in data.SandboxDataKeyValues:
    print (keyValue.Key + " :: " + keyValue.Value)