let i=0
while read f1
do 
	#i=$((i+1))
	#if [ $i -eq 30 ] ; then
	#	exit 0
	#fi

	
	f1=$(echo $f1 | tr -d "\r\n")
	echo $f1
	curl -XPOST 'http://localhost:9200/pfc_diy_sdata/sdata?pipeline=parse_pfc_sdata_log' -H 'Content-Type:application/json' -d "{ \"sdata\": \"$f1\" }"
done < pfc_log_data.log
