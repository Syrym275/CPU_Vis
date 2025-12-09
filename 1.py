def simulate_pipeline(instructions, stages):
    print("CPU Pipeline Simulation\n")
    for instr in instructions:
        print(f"--- {instr} ---")
        for stage in stages:
            print(f"{instr} -> {stage}")
        print()

if __name__ == "__main__":
    simulate_pipeline(instructions, pipeline_stages)
