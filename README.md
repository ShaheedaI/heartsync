\ 🫀 HeartSync – Heart Disease Prediction Web App



HeartSync is a Django-based web application that uses a Naive Bayes machine learning model to predict the likelihood of heart disease based on patient health inputs. It integrates with MongoDB for database storage and features a clean, user-friendly interface.



---



\ 🚀 Live Preview



> Run locally on: \[http://127.0.0.1:8000](http://127.0.0.1:8000)



---



\ 📷 Screenshots



\ 🧾 Form Page

!\[Form Screenshot](screenshots/form.png)



\ 📊 Result Page

!\[Result Screenshot](screenshots/result.png)



---



\ ⚙️ Features



\- 🎯 Heart disease prediction using trained Naive Bayes model

\- 📦 Data stored in MongoDB

\- 🎨 Modern and responsive UI (with images and styled form)

\- 📁 CSV-based dataset loading

\- 🔐 Custom Django views and model integration



---



\ 🧪 Sample Input (Try this!)



```text

Age: 52

Blood Pressure: 130

Cholesterol: 250

Max Heart Rate: 140

Target: 1



🛠️ How to Run This Project

🔹 Step 1: Clone the Repo

bash

Copy

Edit

git clone https://github.com/yourusername/heartsync.git

cd heartsync

Replace yourusername with your actual GitHub username.



🔹 Step 2: Install Requirements

bash

Copy

Edit

pip install django djongo pymongo pandas scikit-learn

🔹 Step 3: Start MongoDB

Make sure MongoDB is installed and running:



bash

Copy

Edit

mongod

🔹 Step 4: Run the ML Training Script

bash

Copy

Edit

python predictor/ml\_model.py

This will generate model.pkl.



🔹 Step 5: Apply Migrations and Start Server

bash

Copy

Edit

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Now visit: http://127.0.0.1:8000



🗂 Folder Structure

css

Copy

Edit

heartsync/

├── heart\_disease.csv

├── model.pkl

├── manage.py

├── README.md

├── screenshots/

│   ├── form.png

│   └── result.png

├── predictor/

│   ├── forms.py

│   ├── ml\_model.py

│   ├── models.py

│   ├── templates/

│   │   └── predictor/

│   │       ├── index.html

│   │       └── result.html

│   └── ...

🧠 Tech Stack

Python + Django



scikit-learn



MongoDB + Djongo



HTML5, CSS



Naive Bayes Classifier



🌐 Future Ideas

Add user login \& patient history tracking



Analytics dashboard with graphs



Deploy online (PythonAnywhere, Render, etc.)



👩‍💻 Author

Shahida I.

Machine Learning Enthusiast | Software Developer

GitHub: @yourusername



⭐ Support

If you like this project, star it 🌟 on GitHub!



yaml

Copy

Edit



---



\### 🖼 Step 3: Add Screenshots (Optional but Highly Recommended)



1\. Take a screenshot of:

&nbsp;  - The \*\*form page\*\* (before prediction)

&nbsp;  - The \*\*result page\*\* (after prediction)



2\. Create a folder in the root project called:  

screenshots



yaml

Copy

Edit



3\. Save your images as:

\- `form.png`

\- `result.png`



> They will automatically show up in the `README.md` due to the paths used above.



---



\### 💾 Step 4: Save and Push to GitHub



```bash

git add README.md screenshots/

git commit -m "Added README with screenshots"

git push



