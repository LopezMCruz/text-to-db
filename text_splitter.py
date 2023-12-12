def split_document(input_file, output_prefix):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        current_chunk = []
        word_count = 0
        doc_count = 1

        for line in lines:
            words_in_line = line.split()
            word_count += len(words_in_line)
            current_chunk.append(line)

            if word_count >= 400:
                # Check if there's a sentence end in the last line
                if any(punctuation in line for punctuation in ['.', '?', '!']):
                    # Split at the last sentence end
                    last_period = max(line.rfind('.'), line.rfind('?'), line.rfind('!'))
                    # Include the sentence end
                    current_chunk[-1] = line[:last_period + 1] + '\n'
                    remainder_of_line = line[last_period + 1:]
                else:
                    remainder_of_line = ''

                # Write the current chunk to a file
                output_file = f"{output_prefix}_{doc_count}.txt"
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.writelines(current_chunk)

                # Prepare for the next chunk
                current_chunk = [remainder_of_line] if remainder_of_line else []
                word_count = len(remainder_of_line.split())
                doc_count += 1

        # Write any remaining text
        if current_chunk:
            output_file = f"{output_prefix}_{doc_count}.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                file.writelines(current_chunk)

        print(f"Document split into {doc_count} parts.")
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# Example usage
split_document('dracula_chapter1.txt', 'dracula_chapter1')
