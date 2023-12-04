from buildbot.plugins import util
#from twisted.python import log

from zorg.buildbot.util.workerowner import WorkerOwnerAuthz
from zorg.buildbot.util.workerowner import WorkerEndpointMatcher
from zorg.buildbot.util.workerowner import RolesFromWorkerOwner

import config

from buildbot import www

def getAuth():
 return www.auth.NoAuth()

def getAuthz():
    authz = WorkerOwnerAuthz(
        allowRules=[],
        roleMatchers=[
            util.RolesFromGroups(groupPrefix="llvm/"),
            # role owner is granted when property owner matches the email of the user
            util.RolesFromOwner(role="owner"),
            RolesFromWorkerOwner(role="worker-owner"),
        ],
    )

    return authz
