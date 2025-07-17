import sys
import subprocess
import os

def main():
    if len(sys.argv) != 3:
        print(
            "Please use in this format: python3 run_mood_taste.py <school> <\"your mood text\">"
            + " Example: python3 run_mood_taste.py 1 \"I am happy today\""
        )
        sys.exit(1)
    school, user_text = sys.argv[1], sys.argv[2]

    hook = os.path.join(os.path.dirname(__file__), 'hooks/mood_selector.py')
    process_1 = subprocess.run(
        ["python3", hook],
        input=user_text,
        text=True,
        capture_output=True,
        encoding='utf-8' 
    )
    if process_1.returncode != 0:
        sys.stderr.write(process_1.stderr)
        sys.exit(1)

    prompt = process_1.stdout

    cmd = ["ollama", "run", "mood-taste:latest"]
    process_2 = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )
    process_2.communicate(input=prompt)

if __name__ == "__main__":
    main()
