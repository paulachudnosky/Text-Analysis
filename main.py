from text_analysis import *
filename = 'prueba.txt'

def main():
    try:
        word_count = process_file(filename)
        display_most_frequent(word_count)
    
    except FileNotFoundError:
        print("Error: The file '", filename, "' was not found.")

if __name__ == "__main__":
    main()