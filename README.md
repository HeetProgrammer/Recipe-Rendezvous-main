

Recipe Rendezvous

A Flask web application that allows users to register, log in, and log out, while also providing personalized recipe recommendations based on dietary preferences (e.g., vegetarian, non-vegetarian) and cuisine choices.

#Features:

**User Authentication**

  * User registration with secure password hashing
  * Login & Logout functionality with session management
  * Flask-Login integration

**Recipe Recommendations**

  * Filter recipes based on dietary preferences (Vegetarian, Vegan, etc.)
  * Choose from different cuisines
  * Recipes fetched dynamically from an external API

**User-Friendly Interface**

  * Clean and responsive templates with Jinja2
  * Flash messages for better user experience


#Getting Started:
1. Clone the Repository

```Bash
git clone https://github.com/your-username/recipe-rendezvous.git
cd recipe-rendezvous
```

2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Set Environment Variables

Create a `.env` file in the project root with the following:

```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
API_KEY="41c2f8ab2111424583f16604c80809f8"
```

5. Initialize Database

```bash
python
>>> from directory import db, app
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

### 6. Run the Application

```bash
flask run
```

Visit `http://127.0.0.1:5000/` in your browser.










Heet, do you want me to also include **example screenshots and usage steps** (like registering and searching for a vegetarian Italian dish) in the README, or should I keep it simple and clean?
