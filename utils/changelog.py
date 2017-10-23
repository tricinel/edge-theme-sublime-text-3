# -*- coding: utf-8 -*-

"""
Edge Theme Changelog
"""

import sublime
import sublime_plugin
import webbrowser

STYLES = '''
.mdpopups {
  {{'.background'|css}}
}

.edge-config-changes ul li, .edge-config-changes p {
  {{'.foreground'|css}}
}

.edge-config-changes a {
  text-decoration: none;
  color: #6D88FF;
}

.edge-config-changes h1,
.edge-config-changes h2,
.edge-config-changes h3,
.edge-config-changes h4,
.edge-config-changes h5,
.edge-config-changes h6 {
  {{'.string'|css('color')}}
}

.edge-config-changes h1,
.edge-config-changes h2 {
  margin-top: 50px;
}

.edge-config-changes h3,
.edge-config-changes h4 {
  margin-top: 30px;
}
'''


class EdgeChangesCommand(sublime_plugin.WindowCommand):
  def on_navigate(self, href):
    webbrowser.open_new_tab(href)

  def run(self):
      import mdpopups
      text = sublime.load_resource('Packages/Edge Theme/CHANGELOG.md')
      view = self.window.new_file()
      view.set_name('Edge Theme Changelog')
      view.settings().set('gutter', False)
      html = '<div class="edge-config-changes">%s</div>' % mdpopups.md2html(view, text)
      mdpopups.add_phantom(view, 'changelog', sublime.Region(0), html, sublime.LAYOUT_INLINE, css=STYLES, on_navigate=self.on_navigate)
      view.set_read_only(True)
      view.set_scratch(True)

  def is_enabled(self):
      try:
          import mdpopups
      except Exception:
          return False

      return (mdpopups.version() >= (1, 9, 0)) and (int(sublime.version()) >= 3119)

  is_visible = is_enabled
