# Example memory block sizes (in KB)
memory_blocks = [100, 500, 200, 300, 600]

# Example process sizes (in KB)
processes = [212, 417, 112, 426]

def first_fit(memory_blocks, processes):
    allocations = [-1] * len(processes)  # Stores block index for each process
    block_status = memory_blocks.copy()  # To track changes

    for i, process in enumerate(processes):
        for j, block in enumerate(block_status):
            if block >= process:
                allocations[i] = j
                block_status[j] -= process  # Reduce available space in that block
                break  # Move to the next process
    return allocations, block_status

allocations, final_blocks = first_fit(memory_blocks, processes)

for i, process in enumerate(processes):
    if allocations[i] != -1:
        print(f"Process {i+1} of size {process} KB allocated to block {allocations[i]+1}")
    else:
        print(f"Process {i+1} of size {process} KB NOT ALLOCATED")

print("\nFinal state of memory blocks (in KB):")
print(final_blocks)