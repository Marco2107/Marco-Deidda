# **Monefy Test Automation**

## **Introduction**
This project contains a test automation framework for the **Monefy Android** application, written in **Python** using **Behave** and **Appium**. It focuses on automating user flows identified during exploratory testing.

---

## **Prerequisites**
Before starting, ensure the following tools are installed and configured:

### **1. Required Tools**
- **Python 3.10 or higher**: [Download here](https://www.python.org/downloads/).
- **Node.js**: [Download here](https://nodejs.org/).
- **Poetry**: Dependency manager for Python: [Install Poetry](https://python-poetry.org/docs/#installation).
- **Appium**: Install the Appium server globally:
```
npm install -g appium
```
-**Appium Doctor**: Verify your setup with Appium Doctor:
```
npm install -g appium-doctor
```
### **2. Android SDK**
1. Download and install Android Studio: https://developer.android.com/studio.
2. Configure environment variables:
    - ANDROID_HOME: Path to the Android SDK:
        - Default on Windows: C:\Users\<your_username>\AppData\Local\Android\Sdk.
        - Default on macOS/Linux: ~/Library/Android/sdk.
    - Add the following paths to PATH:
       ```
        $ANDROID_HOME/platform-tools
        $ANDROID_HOME/emulator
       ```
3. Ensure ADB is properly configured:
    adb devices
    If an emulator or device is detected, you'll see output like this:
    ```
    List of devices attached
    emulator-5554   device
    ```
### **3. Java JDK**
1. Install Java Development Kit (JDK) version 8 or higher: https://openjdk.org/.
2. Configure the JAVA_HOME environment variable:
    - On Windows: Path to C:\Program Files\Java\<version>
    - On macOS/Linux: Path to /usr/libexec/java_home
3. Verify the installation:
    ```
    java -version
    ```
## **Setup**
1. Clone the Project

Clone this repository to your local machine:

    git clone git@github.com:Marco2107/Marco-Deidda.git
    cd monefy-test-automation
4. Install Dependencies
Install dependencies using Poetry:
    ```
    poetry install
    ```
6. Configure the config.json File
The config.json file contains the Desired Capabilities required to run the tests. Ensure the file is structured like this:
```json
{
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "app": "./apps/monefy.apk",
    "appWaitActivity": "com.monefy.activities.onboarding.OnboardingActivity_",
    "newCommandTimeout": 300,
    "platformVersion": "15.0",
    "noReset": false,
    "fullReset": false
}
```
Notes:
- deviceName: If using a physical device, use the unique ID returned by adb devices.
- platformVersion: Specify the Android version of the device or emulator.

## **Running the Tests**
Running the Tests
1. Prepare the Environment
    - Start an Android emulator or connect a physical device via USB.
    - Start the Appium server in a new terminal window:
    ```
    appium
    ```
2. Execute the Tests
- To run all tests:
    ```
    behave
    ```
- To run a specific test:
    ```
    behave features/transaction.feature
    ```
## **Troubleshooting**
- ADB not working: Ensure adb is installed and added to your PATH:
    ```
    adb --version
    ```
- Appium Doctor errors: Run the following to diagnose configuration issues:
    ```
    appium-doctor --android
    ```
- Emulator not detected: Ensure the emulator is running and Android platform tools are properly configured.

## **Approach and Tech Stack**
**Approach:**

The framework is built with a focus on simplicity, reusability, and scalability. I adopted the Behavior-Driven Development (BDD) methodology using Gherkin syntax to align testing with user behavior and improve collaboration. The Page Object Model (POM) was implemented to separate UI interactions from test logic, ensuring clean and maintainable test scripts.

**Tech Stack:**

**Python:** Chosen for its simplicity, readability, and approachable learning curve. It enables fast onboarding for non-technical team members, helping them gain proficiency quickly.

**Behave:** Allows reusable test steps, documents application behavior, and promotes a user-centric mindset when designing tests.

**Appium:** Ideal for mobile automation, supporting black-box testing without app source code. It works seamlessly across Android and iOS, ensuring scalability.

**Poetry:** Facilitates clean dependency management and ensures consistent environments.

**Page Object Model (POM):** Improves maintainability and test reliability by encapsulating UI interactions in dedicated classes.

**Allure:** Simplifies the monitoring of automated tests by providing a clear overview of results, facilitates failure investigations with detailed insights, and enhances collaboration through interactive and accessible reports.

These tools were chosen not only for their technical strengths but also for their popularity, strong community support, and availability of solid resources. This ensures efficient, scalable, and maintainable end-to-end testing for the Monefy Android application.

## **Test report**
1. **JUnit Test Report**

A JUnit-compatible test report is available at the following location:
```
reports/junit-results/TESTS-transaction.xml
```

2. **Generating an Allure Report**

1-Install Allure Command-line Tool Ensure that Allure is installed on your system. Use the following commands:
```
brew install allure   # For macOS with Homebrew
```

2-Run Tests with Allure Data Collection Execute the tests with the --alluredir option to generate Allure results:
```
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
```

3-Serve the Allure Report Generate and serve the Allure report locally:
```
allure serve reports/allure-results
```

This will open a detailed interactive report in your default browser.

As show below:

<img width="1413" alt="allure-1" src="https://github.com/user-attachments/assets/d5428313-a0e4-4eb0-91db-2191c8408341">

<img width="1420" alt="allure-21" src="https://github.com/user-attachments/assets/828f8654-cb2d-4c48-a4a5-25743b38d5e5">

<img width="1430" alt="allure-2" src="https://github.com/user-attachments/assets/02b254c6-883c-4f0b-b802-473d4a73d601">

<img width="1426" alt="allure-4" src="https://github.com/user-attachments/assets/05643a00-ec60-4d8f-bdc5-ce3a0b716bab">









