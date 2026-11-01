# 🏥 MediCare — Hospital Management & Doctor Appointment Booking Web App

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Framework-Django%204.2%2B-092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-7952B3.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Live Demo](https://img.shields.io/badge/Live_Demo-PythonAnywhere-22c55e.svg?style=for-the-badge&logo=pythonanywhere&logoColor=white)](https://akhilbinu.pythonanywhere.com/)

<p align="center">
  <b>A comprehensive, production-modeled healthcare management and patient appointment scheduling web application engineered with Django's Model-View-Template (MVT) architecture.</b>
</p>

</div>

---

## 📌 Overview

**MediCare** provides a streamlined healthcare experience for both patients and medical administrators. Patients can explore medical departments, review specialist doctor credentials, schedule consultation dates, and receive automated booking confirmations. The medical staff and hospital administration manage appointments, doctor rosters, and patient records through a secure, permissioned Django administration portal.

---

## ✨ Features

- 👨‍⚕️ **Doctor Directory & Profiles**: Detailed specialist profiles showcasing medical qualifications, specialties, biographies, and headshot photography.
- 🏢 **Department Listings**: Medical discipline breakdown (Cardiology, Neurology, Pediatrics, Orthopedics, General Medicine).
- 📅 **Patient Appointment Booking**:
  - Interactive appointment booking form with real-time field validation.
  - Dynamic doctor selection filtered by department.
  - Date and time picker integration with conflict avoidance.
- 📄 **Booking Confirmation Receipt**: Instant digital confirmation invoice displaying booking reference numbers and visit instructions.
- 🛡️ **Administrative Control Center**: Full CRUD controls via the Django Admin suite for doctor availability, departments, and booking schedule queues.
- 📱 **Fully Responsive UI**: Mobile-first design crafted with modern Bootstrap 5 and Crispy Forms.

---

## 🏗️ Architecture & Database Models

MediCare strictly adheres to Django's **MVT (Model-View-Template)** pattern:

- **Department Model (`Departments`)**: Stores department name, description, and status.
- **Doctor Model (`Doctors`)**: Relates doctors to their specific department, storing contact details, biography, and image uploads.
- **Booking Model (`Booking`)**: Stores patient name, phone number, email address, selected doctor (`ForeignKey`), booking date, and creation timestamps.

---

## 🛠️ Quickstart & Local Installation

### 1. Clone & Set Up Virtual Environment

```bash
# Clone the repository
git clone https://github.com/Akhil-Binu/Python_Django_App.git
cd Python_Django_App

# Create a clean virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
cd mysite
pip install -r requirement.txt
```

### 3. Database Migration & Superuser Setup
```bash
# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create administrator account
python manage.py createsuperuser
```

### 4. Launch the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
- **Public Portal**: `http://127.0.0.1:8000/`
- **Admin Dashboard**: `http://127.0.0.1:8000/admin/`

---

## 📁 Repository Structure

```
Python_Django_App/
├── mysite/                   # Core Django project root
│   ├── manage.py             # Django CLI management script
│   ├── requirement.txt       # Python package dependencies
│   ├── mysite/               # Project configuration (settings, routing, wsgi)
│   ├── home/                 # Main healthcare application
│   │   ├── models.py         # Department, Doctors, and Booking database schemas
│   │   ├── views.py          # Request handlers and business logic
│   │   ├── forms.py          # Patient booking forms
│   │   └── urls.py           # App endpoint routing
│   ├── templates/            # HTML5 Jinja templates
│   │   ├── base.html         # Global layout and navbar/footer
│   │   ├── index.html        # Landing page
│   │   ├── doctors.html      # Specialist directory
│   │   ├── booking.html      # Appointment booking form
│   │   └── confirmation.html # Success confirmation receipt
│   └── static/               # CSS styles, JavaScript, and branding imagery
└── notes.md                  # Developer reference notes & quick setup guide
```

---

## 📄 License

Distributed under the [MIT License](LICENSE). Developed with ❤️ by [Akhil Binu](https://akhilbinu.in/).
