binwalk -e Milk_Best_Friend/oreo.jpg
strings Milk_Best_Friend/_oreo.jpg.extracted/b.jpg | grep flag{
rm -r Milk_Best_Friend/_oreo.jpg.extracted