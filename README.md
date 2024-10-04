# Quick Passphrase Generator

Generate secure passphrases using [EFF's long word list for diceware](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases), which includes 7776 words (approximately 12.9 bits of entropy per word). Passphrases are generated using Python's [SystemRandom](https://docs.python.org/3/library/random.html#random.SystemRandom) to ensure secure randomness.

## Installation

### Clone the Repository
```bash
git clone <url_to_repository> quick_passphrase
cd quick_passphrase
```

### Build an Executable (Optional)
If you prefer to run the program as an executable, follow these steps:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Create the executable:
	- **For Windows**:
	```bash
	pyinstaller --onefile --add-data "wordlist.txt;." passphrase.py
	```
	- **For Linux and Mac**:
	```bash
	pyinstaller --onefile --add-data "wordlist.txt:." passphrase.py
	```

## Usage
To generate a passphrase, run the script or executable with the desired passphrase length as an argument.

### Using Python Script
```bash
python passphrase.py <length>
```

### Using Executable
If you built an executable, you can run it directly:
```bash
passphrase <length>
```

### Example
Generate a passphrase with 8 words:
```bash
> passphrase 8
```
Output:
```
uptight renewable backlight geometry upheld visibly quartered playset - entropy: 103.4 bits
```

## Contributing
Contributions are more than welcome. Consider submitting a pull request.