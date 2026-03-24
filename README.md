📝 Mad Libs Generator (Python)
A simple Python Mad Libs Generator that turns a story into a fun, interactive game.
The program reads a text file, asks the user to fill in missing words (like adjectives, nouns, verbs), and then prints out the completed story.

📌 How It Works
The story is stored in a text file (story.txt).
Words that need to be filled in are written inside square brackets:
	Example: [adjective], [noun], [verb]
The program:
	Finds all bracketed words in the story
	Asks the user to enter replacements
	Inserts the user’s answers back into the story
The final story is printed to the screen.

📂 Project Structure
MadLibsGenerator/
│
├── MadlibsGenertor.py   # Main Python script
├── story.txt            # Story template with placeholders
└── README.md            # Project documentation

▶️ How to Run
Make sure you have Python 3 installed.
Place MadlibsGenertor.py and story.txt in the same folder.
Open a terminal in that folder.
Run the program:
	python MadlibsGenertor.py
Enter words when prompted.
Enjoy your custom-generated story 🎉

✏️ Example Placeholder Format
Inside story.txt:
	Today I woke up feeling [adjective].
	I met a [adjective] [animal] that could [verb].
