🖱️⌨️ Keyboard & Mouse Event Listener (Python)

   A real-time Keyboard and Mouse Event Monitoring Tool built using Python and the pynput library.
   This project demonstrates how to:

    Capture keyboard key presses
    Detect special keys (Shift, Ctrl, Esc, etc.)
    Track mouse movement
    Detect mouse clicks
    Monitor mouse scrolling
    Run keyboard and mouse listeners simultaneously

⚠️ This project is for educational and ethical learning purposes only.


📌 Features
⌨️ Keyboard Monitoring

    Detects normal key presses
    Detects special keys (Shift, Ctrl, Esc, etc.)
    Stops program when ESC key is pressed
    Real-time console output


🖱️ Mouse Monitoring

    Tracks mouse movement (x, y coordinates)
    Detects mouse clicks (button and position)
    Detects mouse scroll events
    Runs simultaneously with keyboard listener
    

⚡ Multi-Listener Execution

    Keyboard and mouse listeners run together
    Uses background threads
    Clean program exit handling
    

🛠️ Technologies Used

    Python 3.x
    pynput library
    pynput.keyboard
    pynput.mouse


📦 Installation
Step 1: Clone the Repository
git clone https://github.com/Haackerspot/key_logger.project/
cd keyboard-mouse-listener

Step 2: Install Required Library
pip install pynput

🚀 How to Run
python keyboard_mouse_listener.py


🖥️ How It Works
1️⃣ Keyboard Events
  🔹 on_press(key)
  🔹 Triggered whenever a key is pressed
  🔹 prints:
       🔹Normal keys (a, b, 1, etc.)
       🔹Special keys (Shift, Ctrl, etc.)

   🔹 on_release(key)
   🔹 Triggered when key is released
   🔹 Stops the program when:
       ESC key is pressed

       
2️⃣ Mouse Events
🔹 on_move(x, y)
🔹Prints mouse cursor position

🔹 on_click(x, y, button, pressed)
🔹Detects mouse button clicks
🔹Shows:
    🔹Position
    🔹Button used

🔹 on_scroll(x, y, dx, dy)
🔹Detects scroll wheel movement


🧠 Program Flow

1.Define keyboard event functions
2.Define mouse event functions
3.Create keyboard listener
4.Create mouse listener
5.Start both listeners
6.Wait for ESC key to terminate


📁 Project Structure
keyboard-mouse-listener/
│
├── keyboard_mouse_listener.py
└── README.md


⚠️ Important Notes

🔹The program runs until ESC is pressed.
🔹It prints all activity to the console.
🔹Some operating systems may require:
🔹Administrator privileges (Windows)
🔹Accessibility permissions (Mac/Linux)

🔐 Ethical Usage Warning

This project captures keyboard and mouse activity.

✔ Use it for:

🔹Learning event handling
🔹Automation testing
🔹Accessibility tools
🔹Input monitoring experiments

❌ Do NOT use it for:

🔹Unauthorized monitoring
🔹Spying on others
🔹Malicious activity
🔹Always obtain proper permission before running monitoring tools on any system.


💡 Possible Enhancements

🔹Save logs to a file instead of console
🔹Add timestamp to each event
🔹Create GUI version
🔹Add start/stop toggle
🔹Convert into background service
🔹Add event filtering


📚 Learning Outcomes

🔹This project helps you understand:
🔹Event-driven programming
🔹Multithreading in Python
🔹System-level input monitoring
🔹Keyboard and mouse hooks
🔹Listener lifecycle management



🤝 Contributing

🔹Contributions are welcome!
🔹Fork the repository
🔹Create a new branch
🔹Commit changes
🔹Open a Pull Request

📜 License

This project is intended for educational purposes.
You may add an MIT License if publishing publicly.

👨‍💻 Developer

Built with Python for learning system-level event handling.
