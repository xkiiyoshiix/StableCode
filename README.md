## Text Generation with Hugging Face Transformers

This Python script utilizes the Hugging Face Transformers library to generate text using a pre-trained language model. It reads input text from a file, generates additional text based on the input, and prints the generated text to the console. This README provides information on how to use, configure, and contribute to the project.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## About

This script demonstrates how to use the Hugging Face Transformers library to perform text generation tasks. It leverages a pre-trained model to generate text based on a given input text. The project includes configuration options and the ability to measure execution time.

## Getting Started

Follow these instructions to get started with the project.

### Prerequisites

Before running the code, ensure you have the following prerequisites:

- Conda (used miniconda for this project)
- Python 3.7 or higher (here used 3.10
- PyTorch
- Transformers library

### Installation
1. Create conda environment
  
  ```
  conda create -n stablecode python=3.10
  ```

2. Activate conda environment
  
  ```
  conda activate stablecode
  ```

3. Install dependencies:

  ```
  pip install requirements.txt
  ```

4. Clone the repository:
  
  ```
  git clone https://github.com/xkiiyoshiix/StableCode.git
  ```

5. Change to the project directory:
  
  ```
  cd StableCode
  ```

## Usage
In the instruction file you need to add your instruction under the "Instruction" part

Run the code

  ```
  python main.py
  ```


## Example output from the example in "instructions.txt"

  ```
  ### Instruction
  Convert this code from python to c#:
  print("Hello World!")
  
  ### Response
  using System;
  
  namespace HelloWorld
  {
      class Program
      {
          static void Main(string[] args)
          {
              Console.WriteLine("Hello World!");
          }
      }
  }
  
  Total Execution Time: 64.48 seconds
  ```

## Configuration

The script includes the following configuration options:

debug: Set this variable to True to enable debug mode, which displays the execution time.
You can also configure the maximum number of tokens generated (max_new_tokens) and the temperature for text generation in the generate_text function.


## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them.
5. Push your changes to your fork on GitHub.
6. Create a pull request to the original repository.

Please follow the project's code of conduct and contribution guidelines when contributing.


## Acknowledgments

This project utilizes the Hugging Face Transformers library for text generation. Acknowledgments to the creators of the library and its contributors.

## Final Words

If you like my project, you are welcome to support me with donations or stars.
