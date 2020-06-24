#!/bin/bash

function print_header()
{
cat <<"EOF"
  __ _           _                        
 / _| | __ _ ___| | __   __ _ _ __  _ __  
| |_| |/ _` / __| |/ /  / _` | '_ \| '_ \ 
|  _| | (_| \__ \   <  | (_| | |_) | |_) |
|_| |_|\__,_|___/_|\_\  \__,_| .__/| .__/ 
                             |_|   |_|    

EOF
}

echo "=== Running ecosystem-home-api dev server ==="
print_header

FLASK_APP=ecosystem-home-api.py flask run -p 5001 --reload
