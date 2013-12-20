import sublime, sublime_plugin, subprocess, logging, re
logging.basicConfig(level = logging.INFO)
    
class SmartCompareCommand(sublime_plugin.TextCommand):

    def __init__(self , view):
        sublime_plugin.TextCommand.__init__(self, view)
        self.settings = sublime.load_settings("SmartCompare.sublime-settings")

    def compare(self, l, r):
        subprocess.Popen([self.settings.get('BeyondComparePath'), l, r])


    def smartMacth(self , path):
        matchStr = self.settings.get('match','.*')
        logging.info("Setting macth : " + matchStr)
        logging.info("File path : " + path)
        pattern = re.compile(matchStr)
        comparePath = path;
        if pattern.search(path):
            rules = self.settings.get('rules',[])
            for rule in rules:
                logging.info(" rule :" + rule + "=>" +rules[rule])
                comparePath = comparePath.replace(rule,rules[rule])
            logging.info("compare path :" + comparePath)
            return comparePath


    def run(self, edit):
        path = self.view.file_name()
        comparePath = self.smartMacth(path)
        if comparePath:
            self.compare(path , comparePath)
        logging.info(self.settings.get('rules'));
