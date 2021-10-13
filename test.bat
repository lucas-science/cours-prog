@echo off

if %1 NEQ "" (
    git pull
    git add .
    git commit -m %1
    git push -o orgin
) else (
    ECHO "il faut donner une chaine de charactère en paramètre pour nommer le commit."
)
