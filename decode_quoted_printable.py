
import sublime, sublime_plugin, quopri


class DecodeQuotedPrintableCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		for region in self.view.sel():
			content = unicode(quopri.decodestring(self.view.substr(region)), errors='ignore')
			self.view.replace(edit, region, content)
