#!/bin/bash 
set -eu
# python ライブラリのインストール
pip install -r requirements.txt
# フォルダを作成して移動させる
echo "Create "$HOME"/.aws-sw"
mkdir $HOME"/.aws-sw"
cp *.py $HOME"/.aws-sw"
cp *.txt $HOME"/.aws-sw"
cp sw $HOME"/.aws-sw"
chmod 755 $HOME"/.aws-sw"
chmod 755 $HOME"/.aws-sw/sw"
# profileに追加する
set +eu
st=`echo ${SHELL}  | cut -d '/' -f 3`
echo 'export PATH="$HOME/.aws-sw:$PATH"' >>  $HOME"/."$st"rc"
source $HOME"/."$st"rc"
echo 'Run the following command : source "'$HOME'/.'$st'rc"'
