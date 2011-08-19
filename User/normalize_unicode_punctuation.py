# -*- coding: utf-8 -*-
import sublime, sublime_plugin


class NormalizeUnicodePunctuationCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		for region in self.view.sel():
			content = self.view.substr(region)

			content = content.replace(u'“', '"')
			content = content.replace(u'”', '"')
			content = content.replace(u'“', '"')
			content = content.replace(u'‹', '"')
			content = content.replace(u'›', '"')
			content = content.replace(u'«', '"')
			content = content.replace(u'»', '"')
			content = content.replace(u'»', '"')
			content = content.replace(u'‘', "'")
			content = content.replace(u'’', "'")
			content = content.replace(u'–', '-')
			content = content.replace(u'…', '...')

			self.view.replace(edit, region, content)
