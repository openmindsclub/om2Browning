cat intro.md > README.md
echo "" >> README.md
echo "" >> README.md

echo "##Sommaire" >> README.md
echo "" >> README.md
cat SUMMARY.md >> README.md
echo "" >> README.md

################ INIT CHAP1 ####################

echo "##Chapitre 1: Début d'année:" > chap1/README.md

echo "" >> chap1/README.md
cat chap1/inscriptions.md >> chap1/README.md
echo "" >> chap1/README.md

echo "" >> chap1/README.md
echo "" >> chap1/README.md
echo "" >> chap1/README.md
cat chap1/welcomeday.md >> chap1/README.md
echo "" >> chap1/README.md


################ COPY CHAP1 ####################

echo "______________" >> README.md

echo "" >> README.md
cat chap1/README.md >> README.md

#################################################

cp -r . /mnt/0/mdreader
