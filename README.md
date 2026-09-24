 🔐 Password Generator — Python Project

A smart and secure **Password Generator** built with Python that creates strong, customizable passwords with guaranteed complexity.

---

## ✨ Features

- 🔢 **Custom Password Length** — You decide how long the password should be
- ✅ **Guaranteed Complexity:**
  - At least **1 Uppercase** letter
  - At least **1 Lowercase** letter
  - At least **1 Number**
  - At least **1 Special Character**
- ⚠️ **Exception Handling** — Handles invalid inputs gracefully, no crashes!
- ⏱️ **Loading Effect** — Smooth experience using the `time` module
- 🔁 **Loop Logic** — Keeps regenerating until all conditions are met

---

## 🛠️ Modules Used

| Module | Purpose |
|--------|---------|
| `random` | Randomly selects characters for the password |
| `string` | Provides character sets (letters, digits, special chars) |
| `time` | Adds a loading/delay effect for better UX |

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Sharkbox-rudra/password-generator.git
cd password-generator
```

**2. Run the script**
```bash
python password_generator.py
```

**3. Follow the prompts**
```
Enter desired password length: 12
Generating your password...
✅ Your Password: aB3$kLm9@Xqz
```

---

## 📁 Project Structure

```
password-generator/
│
├── password_generator.py   # Main script
└── README.md               # Project documentation
```

---

## 💡 How It Works

1. User enters the desired password length
2. The program validates the input (exception handling)
3. Randomly picks characters from uppercase, lowercase, digits & special chars
4. Checks if all conditions are met — if not, regenerates
5. Displays the final secure password with a smooth loading effect

---

## 🔮 Future Improvements

- [ ] Add a GUI using Tkinter
- [ ] Option to copy password to clipboard
- [ ] Save generated passwords to a file
- [ ] Password strength meter

---

## 🙋‍♂️ Author

**RUDRA PRASAD GORAI**
- LinkedIn: [https://www.linkedin.com/in/rudra-prasad-gorai-0927b239b/)
- GitHub: [https://github.com/Sharkbox-rudra)

---

⭐ **If you found this useful, don't forget to star the repo!** ⭐
