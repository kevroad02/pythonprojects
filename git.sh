#!/data/data/com.termux/files/usr/bin/bash
cd /storage/emulated/0/Documents/Termux/
git add .
git config --global user.name "Kevin Roadarmel" 
git config --global user.email "goldenrobloxian@gmail.com"
echo Enter a concise summary of what you edited
read varname
git commit -m $varname
echo Pushed to GitHub with update name $varname
git remote add origin https://github.com/kevroad02/pythonprojects.git
git push -u origin master

