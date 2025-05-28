def fileRead(file_path):
    try:
        with open(file_path, 'r') as file:
            dataset = []
            for line in file:
                nums = line.split()
                dataset.append([])
                for num in nums:
                    dataset[-1].append(float(num))
            return dataset

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    

