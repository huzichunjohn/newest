from django.core.management.base import BaseCommand, CommandError
from subprocess import Popen, STDOUT, PIPE
import shlex, os

class Command(BaseCommand):
    def handle(self, *args, **options):
	os.system("rm `find . -type f -name '*.pyc'`")
	
	cmd = "find . -type f -name '*.pyc'"
	args = shlex.split(cmd)
	files = Popen(args, stderr=STDOUT, stdout=PIPE).communicate()[0].split("\n")
        print files
	if len(files) < 2:
	    self.stdout.write("all *.pyc files were successfully cleaned up!\n")
	else:
	    self.stdout.write("whoops! something went wrong!\n")



