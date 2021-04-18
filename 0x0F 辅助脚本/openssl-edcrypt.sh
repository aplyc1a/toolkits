#!/bin/bash
echo "=============================================="
echo "Encrypt files in the current directory.\n (1) to encrypt....\n (2) to decrypt...."
read -r x
echo "=============================================="
if [ $x -eq 1 ]; then
	echo "[Encrypt mode]"
	file_key=`head -1 /dev/urandom| md5sum | awk '{print $1}'`
	echo -ne "KEY: \033[40;31m"${file_key}"\033[0m\n"
	
	echo -ne "> [step1] Specify name for archive package: \033[40;32m"
	read -a archive_name
	echo -ne "\033[0m\n\033[40;33m"
	tar -zcvf - * | openssl aes-256-cfb -salt -k ${file_key} | dd of=${archive_name}.endata
	echo -ne "\033[0m\n"
	echo ${file_key} > ${archive_name}.key
	
	echo -ne "> [step2] Encrypt the key of \`${archive_name}.endata\`.\n\033[40;32m"
	zip -re ${archive_name}-enckey.zip ${archive_name}.key
	echo -ne "\033[0m\n"
	
	echo "> [step3] Done!"
	
elif [ $x -eq 2 ];then
	echo "[Decrypt mode]"
	echo -ne "> [step1] Give the name of the archive package.\`\$filename\$\`.endata:\033[40;32m"
	read -a archive_name
	echo -ne "\033[0m"
	if [ ! -e ${archive_name}".endata" ]; then
		echo ${archive_name}".endata not exist!"
		exit
	fi
	
	echo -ne "> [step2] Get the key of \`${archive_name}.endata\`.\n\033[40;32m"
	unzip ${archive_name}-enckey.zip
	echo -ne "\033[0m\n"
	
	echo "> [step3] Decrypt \`${archive_name}.endata\`."
	dd if=${archive_name}.endata | openssl aes-256-cfb -d -kfile ${archive_name}.key | tar zxf -
	
	echo "> [step4] Done!"
else
	echo "Run again please!"
fi

rm ${archive_name}.key
exit
