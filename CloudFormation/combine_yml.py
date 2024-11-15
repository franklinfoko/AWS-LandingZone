import yaml
import sys

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def combine_yamls(main_file, include_files):
    main_data = load_yaml(main_file)
    
    for include_file in include_files:
        include_data = load_yaml(include_file)
        main_data.update(include_data)
    
    return main_data

def save_yaml(data, output_file):
    with open(output_file, 'w') as file:
        yaml.safe_dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python combine_yml.py <main_file> <output_file> <include_file1> [<include_file2> ...]")
        sys.exit(1)
    
    main_file = sys.argv[1]
    output_file = sys.argv[2]
    include_files = sys.argv[3:]
    
    combined_data = combine_yamls(main_file, include_files)
    save_yaml(combined_data, output_file)
    print(f"Combined YAML saved to {output_file}")