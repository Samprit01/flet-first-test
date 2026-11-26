# First Flet Deployment

A beginner-friendly cross-platform Python application built with **Flet 1.x**. Using a single Python script (`test1.py`), this project demonstrates how to render the same user interface natively on a Windows desktop, in a web browser, and live on an Android smartphone.

## Prerequisites

* **Python 3** installed on Windows
* **Windows Command Prompt (`cmd`)**
* **Web Browser** (Chrome, Edge, or Firefox) for browser mode
* **Flet App** installed from the **Google Play Store** (for Android live preview)
* **Shared Wi-Fi / Internet Connection** connecting both your computer and your Android phone (required for Android live preview)

## Project Structure

```text
mb_flet/
├── codes/
│   └── test1.py          # Main Flet application script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Installation & Setup

1. Create and navigate to your project directory in Command Prompt:

   ```cmd
   mkdir D:\mb_flet
   cd /d D:\mb_flet
   ```

2. Create and activate a Python virtual environment:

   ```cmd
   python -m venv .
   Scripts\activate
   ```

3. Install the required packages from `requirements.txt`:

   ```cmd
   pip install -r requirements.txt
   ```

## Running the Application

Navigate to the folder containing `test1.py` (for example, `cd codes`) with your virtual environment active.

### 1. Native Desktop App (Windows)

In `test1.py`, ensure the launch line at the bottom is set to:

```python
ft.run(main)
```

Then run:

```cmd
python test1.py
```

*(Note: Flet 1.0+ uses `ft.run(main)`. The older `ft.app(target=main)` syntax from Flet 0.x is no longer supported.)*

### 2. Web Browser Mode

To launch the app in your default web browser instead of a desktop window, update the bottom of `test1.py` to:

```python
# ft.run(main)
ft.run(main, view=ft.AppView.WEB_BROWSER)
```

Save the file and run:

```cmd
python test1.py
```

Flet will start a local web server (e.g., `http://127.0.0.1:62930`) and open your app in a new browser tab.

### 3. Live Preview on Android

> **Important:** Make sure both your computer and your Android phone are connected to the **same internet connection or Wi-Fi network** before starting.

1. Download and install the official **Flet** app from the **Google Play Store** on your Android phone.
2. In Command Prompt, start the Android live-preview server:

   ```cmd
   flet run --android test1.py
   ```

3. Scan the QR code displayed in Command Prompt using your phone's Camera app (or a QR scanner) and open the link in the **Flet** app.
4. Any saved edits to `test1.py` will automatically reload on your phone. To exit the app and return to the Flet mobile home screen, shake your phone or long-press anywhere with three fingers.

## Troubleshooting

### Windows SSL Certificate Error (`CERTIFICATE_VERIFY_FAILED`)

If Flet fails during its first-time desktop client download with `ssl.SSLCertVerificationError`, configure Python to use `certifi`'s certificate bundle for your current Command Prompt session (temporary—will not modify your permanent Windows environment variables):

```cmd
for /f "delims=" %i in ('python -c "import certifi; print(certifi.where())"') do set SSL_CERT_FILE=%i
python test1.py
```

## Quick Command Reference

| Command | Description |
| :--- | :--- |
| `python -m venv .` | Create a virtual environment in the current folder |
| `Scripts\activate` | Activate the virtual environment (Windows CMD) |
| `pip install -r requirements.txt` | Install all project dependencies |
| `python test1.py` | Run the app in Desktop or Web Browser mode |
| `flet run --android test1.py` | Start the live-preview server and QR code for Android |