# -*- coding: utf-8 -*-
#------------------------------------------------------------
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.grouptherapyradio'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# Entry point
def run():
# Get params
	params = plugintools.get_params()

	if params.get("action") is None:
		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("grouptherapyradio.main_list "+repr(params))

plugintools.add_item( 
    #action="", 
    title="Group Therapy",
    url="plugin://plugin.video.youtube/playlist/PL6RLee9oArCArCAjnOtZ17dlVZQxaHG8G/",
    thumbnail="https://yt3.ggpht.com/-drh3xWldPhs/AAAAAAAAAAI/AAAAAAAAAAA/XpIkyAjpczA/s288-c-k-no-mo-rj-c0xffffff/photo.jpg",
    folder=True )

run()