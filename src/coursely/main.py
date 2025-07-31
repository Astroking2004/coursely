from coursely.crew import Coursely
from datetime import datetime


def build_course(topic: str):
    """Run the crew to build a course from a topic and return the output markdown."""
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    try:
        # Run the crew and capture output file
        Coursely().crew().kickoff(inputs=inputs)
        # Read the output file
        with open('course_output.md', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def gradio_ui():
    import gradio as gr
    with gr.Blocks() as demo:
        gr.Markdown("# Online Course Builder\nEnter a topic to generate a full course outline, lessons, and quizzes!")
        topic = gr.Textbox(label="Course Topic", placeholder="e.g. Introduction to Machine Learning")
        output = gr.Markdown(label="Course Output")
        btn = gr.Button("Build Course")
        btn.click(fn=build_course, inputs=topic, outputs=output)
    demo.launch()

import sys
from datetime import datetime
from coursely.crew import Coursely

def run():
    """
    Run the crew from CLI (default topic).
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    try:
        Coursely().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Coursely().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Coursely().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        Coursely().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Coursely CLI and UI")
    parser.add_argument("command", nargs="?", default="run", help="Command to run: run, train, replay, test, ui")
    args = parser.parse_args()

    if args.command == "run":
        run()
    elif args.command == "train":
        train()
    elif args.command == "replay":
        replay()
    elif args.command == "test":
        test()
    elif args.command == "gradio":
        gradio_ui()
    else:
        print(f"Unknown command: {args.command}")