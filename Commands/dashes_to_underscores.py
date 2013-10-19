# -*- coding: utf-8 -*-
import sublime, sublime_plugin


class DashesToUnderscoresCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		for region in self.view.sel():
			content = self.view.substr(region)

			content = content.replace(u'-', '_')

			self.view.replace(edit, region, content)
