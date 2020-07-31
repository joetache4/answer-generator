# answer-generator

Generate pseudorandom answers to account security questions.

Security questions are often provided as way to access an online account if your ever forget your password. However, by supplying correct responses to these questions, you make it possible for other people—those who know you (or know *about* you)—to pass this security check and reset your password. Using pseudorandom answers makes it close to impossible for anyone to successfully respond to security questions and gain unathorized access to your account(s).

## Dependencies

Optionally install `pyperclip` with `pip install pyperclip` to copy answers to the clipboard.

## Configuration

- (If re-configuring) Delete the *words* and *seed* files.
- Run `python answer_generator.py`.
- Enter a password when prompted. 

The password helps ensure everyone gets a different answer to the same security question. This password will be used as the seed for RNG and the salt for hashing. 

You will not be asked for the password again, unless you decide to re-configure this script.

## Useage

`python answer_generator.py [SECURITY_QUESTION]`

If `SECURITY_QUESTION` is omitted, you will be asked for it.

## Input (Security Questions)

You do not need to supply the whole question. You could e.g., just supply the last word of the question. (Of course, the resulting answer will be different than if you did supply the whole question.)

Security question input will be stripped of surrounding whitespace and converted to lowercase. It will retain punctuation.

## Output (Answers)

The script will produce answers in the form `[a-z]{3,12}\d{4}`. The alphabetic portion is selected from the *words* file, which contains about 5000 (somewhat unusual) words, mostly names of people and places. This combination of words and numbers make it secure, yet easy to communicate over the phone if needed.

Answers will be copied to the clipboard if `pyperclip` is installed.

## License

MIT

© Joe Tacheron 2020