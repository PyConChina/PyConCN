#!/bin/bash    
cd /usr/web
rm -f enversion*
rm -rf pyhunterpig*
wget https://github.com/pyhunterpig/PyConCN/zipball/enversion
unzip enversion
NEWFLODER=`ls | grep 'pyhunterpig'`
cp -rf $NEWFLODER/* pycon/
cd pycon
rm -rf static
uliweb exportstatic static
chown www:www * -R

HOST="v2.ftp.upyun.com"
USER="datong/pycon"
PASS="pycon2011zh"
LCD="/usr/web/pycon/static/"
RCD="/"
lftp -c "set ftp:list-options -a;
open ftp://$HOST; 
user $USER $PASS;
lcd $LCD;
cd $RCD;
mirror --reverse \
       --delete \
       --verbose \
       --dereference"

cd ..
rm -f enversion*
rm -rf pyhunterpig*
