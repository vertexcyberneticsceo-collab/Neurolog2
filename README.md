# Neurolog2
git clone https://github.com/vertexcyberneticsceo-collab/Neurolog2.git
cd Neurolog2

mkdir -p backend/alembic/versions backend/tests mobile/lib nginx

touch \
  backend/main.py \
  backend/database.py \
  backend/models.py \
  backend/schemas.py \
  backend/detector.py \
  backend/requirements.txt \
  backend/Dockerfile \
  docker-compose.yml \
  .gitignore

git add .
git commit -m "Add Neurolog backend scaffold"
git push