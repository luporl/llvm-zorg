from buildbot.process.properties import Interpolate
from buildbot.plugins import reporters

import config
from zorg.buildbot.util.InformativeMailNotifier import LLVMInformativeMailNotifier

from twisted.python import log

# Returns a list of Status Targets. The results of each build will be
# pushed to these targets. buildbot.plugins reporters has a variety
# to choose from, including email senders, and IRC bots.
def getReporters():
    return []
