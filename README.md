
# 1. Mettre à jour pip
pip install --upgrade pip

# 2. Installer les librairies nécessaires pour le TP
pip install numpy <br>
pip install matplotlib <br>
pip install scikit-learn <br>
pip install seaborn <br>
pip install Pillow <br>
pip install scikit-image <br>

# 3. Installation en une seule commande (alternative)
pip install numpy matplotlib scikit-learn seaborn Pillow scikit-image


# 4. Installer depuis requirements.txt (alternative)
pip install -r requirements.txt

# 5. Vérifier les installations
python -c "import numpy; print(f'NumPy: {numpy.__version__}')" <br>
python -c "import sklearn; print(f'Scikit-learn: {sklearn.__version__}')" <br>
python -c "import matplotlib; print(f'Matplotlib: {matplotlib.__version__}')" <br>
python -c "import seaborn; print(f'Seaborn: {seaborn.__version__}')" <br>
python -c "import PIL; print(f'Pillow: {PIL.__version__}')" <br>
python -c "import skimage; print(f'Scikit-image: {skimage.__version__}')" <br>

