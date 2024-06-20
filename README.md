# Text Pattern Evaluation Using Python and Regular Expressions (Regex)
This Python script demonstrates how to use the re module to evaluate various text patterns from a file (example.txt). Each section uses a specific regular expression pattern (regex) to find and print relevant information:

**URL Evaluation:**
Pattern: (http|https)://[a-z0-9.-_]+

Description: Finds and prints valid URLs starting with http:// or https:// found in the text.

**Email Address Evaluation:**

Pattern: \b[a-zA-Z0-9._%+=]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b

Description: Identifies and prints valid email addresses present in the text, ensuring proper formatting and domain endings.

**Name Evaluation:**

Pattern: (Mrs|Mr|Ms)[. ]*[a-zA-Z ]+

Description: Detects and prints names with common titles (Mr., Mrs., Ms.) found in the text, allowing for variations in title formatting.

**Phone Number Evaluation:**

Pattern: \b\d{5}\*\d{5}\b|\b\d{10}\b|\b\d{5}\-\d{5}\b

Description: Finds and prints various formats of valid phone numbers, including those with asterisks (*), dashes (-), or plain 10-digit sequences.
 

**Note:** Each section opens and reads from example.txt independently. For efficiency and cleaner code, consider consolidating file reading operations if the same data is used across multiple evaluations.
