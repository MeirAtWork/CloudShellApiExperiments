from cloudshell.api.cloudshell_api import CloudShellAPISession


############### user tests ####################

'''
session = CloudShellAPISession(host='localhost',
                               username='user',
                               password='user',
                               domain='Global')

# reserve API
r = session.CreateImmediateTopologyReservation(reservationName='myReservation',
                                               durationInMinutes=100,
                                               topologyFullPath='CloudShell Sandbox Template',
                                               owner='user')

t = session.RestoreSavedSandbox('whatever',
                                savedSandboxId='450bb681-e442-4cf2-2552-3cd70fb1d608',
                                durationInMinutes=10,
                                owner='user')

'''

############### admin tests ####################

session = CloudShellAPISession(host='localhost',
                               username='admin',
                               password='admin',
                               domain='Global')


# restore API
t = session.RestoreSavedSandbox('whatever',
                                savedSandboxId='450bb681-e442-4cf2-2552-3cd70fb1d608',
                                durationInMinutes=10,
                                owner='admin')

print t
