main_title: Python PIP cheatsheet
lang: bash

#------------------------------------------------------------------------------
title: Install from requirements.txt
pip install -r  requirements.txt
#------------------------------------------------------------------------------
title: Upgrade a package
sudo pip install [package_name] --upgrade
Example: pip install --upgrade PyPDF2
#------------------------------------------------------------------------------
title: Upgrade all packages (using pip-review)
pip install pip-review
pip-review --interactive # interactive upgrade
pip-review  --auto       # automatic upgrade
#------------------------------------------------------------------------------


