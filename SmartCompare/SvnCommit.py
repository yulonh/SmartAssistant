import sublime, sublime_plugin, logging, subprocess
logging.basicConfig(level = logging.INFO)

class SvnCommitCommand(sublime_plugin.TextCommand):
    settings = sublime.load_settings("SmartCompare.sublime-settings")

    def run(self, edit):
        window = self.view.window()
        #window.show_input_panel("Please input svn commit message :"," ",self.onInputDone,None,None)
        self.svnCommit(self.view.file_name(), "-sublime commit")

    def onInputDone(self, message):
        self.svnCommit(view.file_name(), message)

    def svnCommit(self, path, message):
        svnPath = self.settings.get('SVNPath')
        logging.info(path)
        logging.info(svnPath)
        subprocess.Popen([self.settings.get('SVNPath'), path, message])
