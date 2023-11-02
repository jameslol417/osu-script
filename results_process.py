import argparse
import re
import matplotlib.pyplot as plt

def process_output_data(file_path, x_label, y_label,x_log):
    # Read data from the text file
    with open(file_path, 'r') as file:
        output_data = file.read()

    # Extract benchmark name
    benchmark_match = re.search(r'# (.+)$', output_data, re.MULTILINE)
    benchmark_name = benchmark_match.group(1) if benchmark_match else 'Unknown Benchmark'

    # Extract latency data
    latency_data = re.findall(r'\b(\d+)\s+([\d.]+)\s*', output_data)
    
    # Separate the data into two lists (sizes and latencies)
    sizes, latencies = zip(*map(lambda x: (int(x[0]), float(x[1])), latency_data))

    # Plot the graph
    plt.plot(sizes, latencies, marker='o', linestyle='-')
    plt.xscale('log', base=x_log)  # Set x-axis to log scale (base 2)
    plt.yscale('log')  # Set y-axis to log scale
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'{benchmark_name}')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description='Process and plot benchmark data from a text file.')

    # Add positional argument for the file path
    parser.add_argument('file_path', help='Path to the text file containing benchmark data')

    # Add optional arguments for x-label, y-label, and title
    parser.add_argument('--x_label', default='Message Size (bits)', help='X-axis label (default: Message Size)')
    parser.add_argument('--y_label', default='Latency (us)', help='Y-axis label (default: Latency (us))')
    parser.add_argument('--x_log',type=int, default=2, help='X-axis log-scale')
    # parser.add_argument('--graph_title', default='OSU MPI-ROCM Latency Persistent Test', help='Graph title (default: Latency Persistent Test)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to process and plot the data
    # process_output_data(args.file_path, args.x_label, args.y_label, args.graph_title)
    process_output_data(args.file_path, args.x_label, args.y_label, args.x_log)