import cloudshell.api.cloudshell_api as api

session = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')

res_id = 'f597a65d-18b5-424b-b3cb-cdefd11c7321'

data = session.GetReservationInputs(res_id)

inputs = data.GlobalInputs
name = inputs[2].ParamName
password = inputs[2].Value

decryptedPassword = session.DecryptPassword(password).Value

print(name + ": " + password + " which is " + decryptedPassword)

