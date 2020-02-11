# encoding: utf-8

###########################################################################################################
#
#
#	Palette Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Palette
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class MasterSwitcher (PalettePlugin):
	
	dialog = objc.IBOutlet()
	previousSwitch = objc.IBOutlet()
	nextSwitch = objc.IBOutlet()
	italicSwitch = objc.IBOutlet()
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': u'Master Switcher',
			'de': u'Master-Switcher',
			'es': u'Control de Másteres',
			'fr': u'Changeur de Masters',
		})
		
		# Load .nib dialog (without .extension)
		self.loadNib('IBdialog', __file__)
	
	# @objc.python_method
	# def start(self):
	# 	# Adding a callback for the 'GSUpdateInterface' event
	# 	Glyphs.addCallback(self.update, UPDATEINTERFACE)
	#
	# @objc.python_method
	# def __del__(self):
	# 	Glyphs.removeCallback(self.update)
	
	# Action triggered by UI
	@objc.IBAction
	def switchMaster_( self, sender=None ):
		font = Glyphs.font
		if font:
			# default: next master
			step = 1
			
			# determine which button:
			if sender is self.previousSwitch:
				step = -1
			elif sender is self.italicSwitch:
				step = int(len(font.masters)/2)
			
			# step to master:
			font.masterIndex = (font.masterIndex+step) % len(font.masters)
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	
	# Temporary Fix
	# Sort ID for compatibility with v919:
	_sortID = 0
	@objc.python_method
	def setSortID_(self, id):
		try:
			self._sortID = id
		except Exception as e:
			self.logToConsole( "setSortID_: %s" % str(e) )
	
	@objc.python_method
	def sortID(self):
		return self._sortID
	