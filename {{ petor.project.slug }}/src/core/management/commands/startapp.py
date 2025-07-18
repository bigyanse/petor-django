import os
import shutil
from django.core.management.commands.startapp import Command as StartAppCommand
from django.core.management.base import CommandError

class Command(StartAppCommand):
    help = "Overridden startapp: creates app and moves it into src/"

    def handle(self, *args, **options):
        app_name = options.get('name')
        cwd = os.getcwd()
        temp_path = os.path.join(cwd, app_name)
        target_base = os.path.join(cwd, 'src')
        target_path = os.path.join(target_base, app_name)

        # Run the original startapp in the current directory
        super().handle(*args, **options)

        # Check and move to src/
        if not os.path.exists(temp_path):
            raise CommandError(f"App {app_name} was not created.")

        os.makedirs(target_base, exist_ok=True)

        if os.path.exists(target_path):
            raise CommandError(f"Target path {target_path} already exists.")

        shutil.move(temp_path, target_path)
