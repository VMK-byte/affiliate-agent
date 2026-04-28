def run_brain():
    # Learning step tracking
    learning_steps = []
    for step in range(10):
        # Simulate a learning step
        learning_steps.append(f'Step {step + 1} completed')
        print(learning_steps[-1])

run_brain()