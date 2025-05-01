# Diceus Automation Challenge

This project covers the full automation task described in the Diceus QA challenge. It includes UI tests, API tests, and test analysis tasks. The repository is structured using Page Object Model and supports running tests in Chrome and Firefox.

## 1. Pencil Testing Task

When testing a pencil with an eraser on one end, you can check it in different ways depending on the type of testing.

**Functional** — does the pencil write, does the eraser work, and how well?  
**Usability** — is it comfortable to hold, does it slip, is it easy to write for a long time, is the eraser easy to use?  
**Performance** — how much can you write before the pencil gets too short, how long does the eraser last, how many times can it erase?  
**Load / Stress** — what happens if you press hard or drop it on the floor, does it break or crack?  
**Security** — is it safe for kids: no sharp edges, no small parts, no harmful materials?  
**Edge cases** — these are unusual situations that don’t happen often, but are still good to test. For example:
- writing with a wet pencil  
- leaving it in direct sunlight  
- sharpening it too often

## 2. Product Recommendations on Hepsiburada

On the hepsiburada.com website, product recommendations appear in several places:

- **Main page** – usually popular or promotional items.
- **Product pages** – related or complementary products (e.g., a case for a phone).
- **Cart page** – items that are often bought together.

These suggestions are not random. They’re based on what the user has viewed, searched for, or bought before. This information is remembered using **cookies** and sometimes **session/local storage** in the browser.

This helps build a simple user profile and show more relevant items.

In some cases, sellers may also pay to promote certain products in these blocks, so part of the list may be ads.

Overall, the goal is to increase chances of purchase by showing what the user might want next — either based on their behavior, or through sponsored content.

## 3. UI Test Scenario — useinsider.com

UI automation scenario (Python + Selenium):
1. Open https://useinsider.com and verify the homepage loads.
2. Navigate to “Company” → “Careers” and ensure the Careers page is loaded. Validate that the “Locations”, “Teams”, and “Life at Insider” blocks are visible.
3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”.
4. Filter jobs by:
   - **Location**: Istanbul, Turkey
   - **Department**: Quality Assurance
5. Ensure at least one job is listed and each job contains:
   - “Quality Assurance” in the Position and Department fields
   - “Istanbul, Turkey” in the Location field
6. Click on the “View Role” button and check the redirection to the Lever Application page.

- Test code uses **Page Object Model (POM)** structure.
- Test supports **Chrome** and **Firefox** via CLI parameters.
- Takes screenshots on failure.

## 4. API Tests — Swagger Petstore

CRUD tests using https://petstore.swagger.io/v2/pet endpoints.

Tests include:
- Create a new pet (positive)
- Get a pet by ID (positive and invalid)
- Update a pet (positive)
- Delete a pet (positive and non-existent ID)
- Create with invalid body (negative)

Written in Python using `requests` and `pytest`.

---

# Test Automation Project Setup

This project contains both UI and API tests to demonstrate basic automation principles.

## 🔧 Installation

```bash
  pip install -r requirements.txt
```

## 🚀 Running Tests

### 🔹 Run All Tests

```bash
  pytest
```

### 🔹 Run UI Tests Only

```bash
  pytest -m ui
```

### 🔹 Run API Tests Only

```bash
  pytest -m api
```

### 🔹 Run Negative Tests

```bash
  pytest -m negative
```

### 🔹 Combine Markers

- AND:
```bash
  pytest -m "api and negative"
```
- OR:
```bash
  pytest -m "api or ui"
```

## 🌐 Browser Configuration

### 🔸 Chrome

```bash
  pytest --browser=chrome
```

### 🔸 Firefox

```bash
  pytest --browser=firefox
```

## 🕶 Headless Mode (default).

```bash
  pytest --browser=chrome --headless=true
```

To disable headless mode:

```bash
  pytest --browser=chrome --headless=false
```

## 📄 HTML Report

```bash
  pytest --html=report.html --self-contained-html
```

## 📦 JUnit XML for CI/CD or 3rd Party Integration

```bash
  pytest --junitxml=results.xml
```