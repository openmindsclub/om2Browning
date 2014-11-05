echo "#O2MB General Headlines" > README.md

cat intro.md >> README.md
echo "" >> README.md
echo "" >> README.md

echo "##Sommaire" >> README.md
echo "" >> README.md
cat SUMMARY.md >> README.md
echo "" >> README.md

################ INIT CHAP0 ####################

echo "##Chapitre 0: Vote du nouveau bureau:" > chap0/README.md

echo "" >> chap0/README.md
cat chap0/preVote.md >> chap0/README.md
echo "" >> chap0/README.md

echo "" >> chap0/README.md
cat chap0/postVote.md >> chap0/README.md
echo "" >> chap0/README.md

echo "______________" >> README.md

echo "" >> README.md
cat chap0/README.md >> README.md

################ INIT CHAP1 ####################

echo "##Chapitre 1: Début d'année:" > chap1/README.md

echo "" >> chap1/README.md
cat chap1/inscriptions.md >> chap1/README.md
echo "" >> chap1/README.md

echo "" >> chap1/README.md
cat chap1/welcomeday.md >> chap1/README.md
echo "" >> chap1/README.md

echo "______________" >> README.md

echo "" >> README.md
cat chap1/README.md >> README.md

################ INIT CHAP2 ####################

echo "##Chapitre 2: Formations :" > chap2/README.md

echo "" >> chap2/README.md
cat chap2/formateurs.md >> chap2/README.md
echo "" >> chap2/README.md

echo "" >> chap2/README.md
cat chap2/inscrits.md >> chap2/README.md
echo "" >> chap2/README.md

echo "______________" >> README.md

echo "" >> README.md
cat chap2/README.md >> README.md

################ INIT CHAP3 ####################

echo "##Chapitre 3: COM Externe" > chap3/README.md

echo "______________" >> README.md

echo "" >> README.md
cat chap3/README.md >> README.md

################ CHAP4 ##################

echo "##Chapitre 4: COM interne" > chap4/README.md

echo "______________" >> README.md

echo "" >> README.md
cat chap4/README.md >> README.md


################ INIT CHAP5 ####################

echo "##Chapitre 5: Evenements" > chap3/README.md

echo "______________" >> README.md

echo "" >> README.md
cat chap3/README.md >> README.md

################ INIT CHAP6 ####################

echo "##Chapitre 6: Projets" > chap4/README.md

echo "______________" >> README.md

echo "" >> README.md
cat chap4/README.md >> README.md


#################################################

cp -r . /mnt/0/mdreader
