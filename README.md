#  Password Audit Suite

A beginner-friendly Python cybersecurity project for auditing password security.

## Features

* 🔑 Generate MD5, SHA1, SHA256 and SHA512 hashes
* 💪 Check password strength
* 🔍 Check hashes against a local wordlist
* 📄 Generate a password audit report

## Technologies

* Python 3
* `hashlib`
* `string`
* `datetime`

## Project Structure

```text
password-audit-suite/
│
├── password_audit.py
├── common.txt
├── password_audit_report.txt
└── README.md
```

## How to Run

```bash
python password_audit.py
```

The program provides an interactive menu:

```text
1. Generate password hash
2. Check password strength
3. Check hash against wordlist
4. Generate audit report
5. Exit
```

## 📄 Report

The **Generate Audit Report** option creates:

```text
password_audit_report.txt
```

The report contains the password audit results, including:

* Password length
* Character types
* Strength score
* Strength level
* Common-password check
* MD5 hash
* SHA1 hash
* SHA256 hash
* SHA512 hash

## 📚 Purpose

This project was created to practice Python and learn basic cybersecurity concepts such as **password hashing, password strength analysis, wordlists, and security reporting**.

## ⚠️ Disclaimer

Use this project only with passwords, hashes, and systems you own or are authorized to test.

## Author

**Mageto Job**
