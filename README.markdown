# E-commerce Selenium Test Automation

This project automates end-to-end testing for the [Sauce Demo](https://www.saucedemo.com/) e-commerce website using Selenium WebDriver with Python. It simulates a user flow: logging in, adding a product to the cart, proceeding to checkout, and verifying the checkout page. The project uses the Page Object Model (POM) for maintainability and includes logging and Chrome options to handle browser prompts.

## Features
- Automates login with predefined credentials (`standard_user`, `secret_sauce`).
- Adds a product (Sauce Labs Backpack) to the cart.
- Navigates to the cart and proceeds to checkout.
- Verifies the checkout page is displayed.
- Includes delays and robust waits to handle dynamic page loads.
- Suppresses Google password prompts and browser notifications.

## Prerequisites
- **Python**: Version 3.8 or higher (tested with Python 3.12).
- **Google Chrome**: Latest stable version.
- **ChromeDriver**: Matching your Chrome version, downloadable from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
- **Git**: For cloning and pushing to the repository.
- **pip**: Python package manager.
- **Virtualenv** (optional but recommended): For isolated Python environments.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ecommerceselenium
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv myenv
   .\myenv\Scripts\activate  # Windows
   # or
   source myenv/bin/activate  # macOS/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` includes:
   ```
   selenium==4.9.0
   ```

4. **Set Up ChromeDriver**:
   - Check your Chrome version (`chrome://settings/help`).
   - Download the matching ChromeDriver from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
   - Place `chromedriver.exe` in `drivers/chromedriver.exe` (e.g., `D:\Pythonproject\ecommerceselenium\drivers\chromedriver.exe`).
   - Update `config.py` with the correct `DRIVER_PATH`:
     ```python
     DRIVER_PATH = "D:\\Pythonproject\\ecommerceselenium\\drivers\\chromedriver.exe"
     ```

## Running the Tests
1. **Activate the Virtual Environment** (if not already active):
   ```bash
   .\myenv\Scripts\activate  # Windows
   ```

2. **Run the Tests**:
   ```bash
   python -m unittest tests/test_ecommerce.py
   ```

3. **Expected Output**:
   - The test navigates to https://www.saucedemo.com/, logs in, adds a product to the cart, proceeds to checkout, and verifies the checkout page.
   - Logs (`INFO` and `ERROR`) are printed to the console for debugging.
   - A successful run shows:
     ```
     Ran 1 test in X.XXXs
     OK
     ```

## Project Structure
```
ecommerceselenium/
├── drivers/                   # Store chromedriver.exe
├── myenv/                     # Virtual environment
├── pages/                     # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py          # Base class with common methods
│   ├── login_page.py         # Login page interactions
│   ├── inventory_page.py     # Inventory page interactions
│   ├── cart_page.py          # Cart page interactions
│   └── checkout_page.py      # Checkout page interactions
├── tests/                     # Test cases
│   ├── __init__.py
│   └── test_ecommerce.py     # Main test script
├── config.py                 # Configuration (URL, credentials, driver path)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Troubleshooting
- **Selenium Manager Error** (`The chromedriver version cannot be discovered`):
  - Ensure internet access for Selenium Manager or use the manual ChromeDriver setup (see Setup Instructions).
  - Verify `config.py` has the correct `DRIVER_PATH`.
- **TimeoutException** (e.g., checkout button not found):
  - Check logs for the current URL and page source.
  - Manually verify the checkout button (`id="checkout"`) at https://www.saucedemo.com/cart.html.
  - Increase delays in `login_page.py`, `inventory_page.py`, or `cart_page.py` (e.g., `time.sleep(2)`).
- **Google Password Prompt**:
  - The test uses Chrome options to disable password manager and pop-ups. If prompts persist:
    - Disable “Offer to save passwords” in `chrome://settings/passwords`.
    - Set Safe Browsing to “No protection” in `chrome://settings/security` (re-enable after testing).
    - Check logs for alert