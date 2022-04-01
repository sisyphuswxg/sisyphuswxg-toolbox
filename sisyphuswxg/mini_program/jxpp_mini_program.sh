
BRANCH="feature_pg_couponcenter_v1.1.0"

cd /Users/wangxg/code_jd/mini_program/jxapp

echo -e "Git operation"
echo -e "---------------------"
git restore .
git pull

git checkout $BRANCH
git pull

echo -e "\nSwitch node version to 12"
echo -e "---------------------"
. ~/.nvm/nvm.sh   # or nvm: command not found
nvm use 12
node -v

echo -e "\nStart build"
echo -e "---------------------"
npm run build

cd ./jxpp
npm run build:weapp