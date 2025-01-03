## 📖 Overview
This is a Django web application that simulates a campaign website for a mock political candidate.

---

## How to Set Up and Run the Project Locally

### ✅ Prerequisites
Make sure you have the following installed on your system:
- Python 3.x
- Django 4.x or later

---

### 📥 Installation Steps

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anelenzimande/L3TO10.git
   cd candidate
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**:
   The project requires a set of dependencies to run. These are listed in the `requirements.txt` file. If the `requirements.txt` file is missing or empty, you need to generate it or manually add the required libraries.

   - If the `requirements.txt` is present and contains the necessary dependencies, install them with the following command:
     ```bash
     pip install -r requirements.txt
     ```

   - If the `requirements.txt` is empty or missing, you need to create it. Here's how:

     - **To create the `requirements.txt` file**:
       After installing the required libraries for your project (for example, Django), you can create a `requirements.txt` file by running:
       ```bash
       pip freeze > requirements.txt
       ```
       This will generate a `requirements.txt` file with the libraries currently installed in your environment.

5. **Run migrations** to set up the database:
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   After setting up the project and dependencies, run the following command to start the local development server:
   ```bash
   python manage.py runserver
   ```

---

## 📄 Requirements

- Python 3.x
- Django 4.x or later

If you need to add dependencies to your project, make sure to update the `requirements.txt` by running:
```bash
pip freeze > requirements.txt
```

---

## 📧 Contact

For questions or feedback, feel free to contact the project maintainer:
- Name: Anele Nzimande
- Email: anelenzimande@gmail.com
