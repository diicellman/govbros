# govbros
how to impress govbros

## Overview

This project extracts information from bank SMS messages and structures the data for easy insertion into a SQL database of your choice. Additionally, it features a text-to-SQL interface, all powered by [LangChain](https://github.com/langchain-ai/langchain).

## Features

- **Extract Information from Bank SMS:** Automatically parse and structure data from bank SMS notifications.
- **Database Integration:** Add the extracted information directly into your preferred SQL database.
- **Text-to-SQL Interface:** Query your data using natural language, which gets converted into SQL queries.
- **Powered by LangChain:** Leverages LangChain for robust natural language processing and text-to-SQL conversion.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/diicellman/govbros.git
   cd govbros
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Specify your environment variables in an .env file in backend directory.
Example .env file:
```yml
ENVIRONMENT=<your_environment_value>
OPENAI_API_KEY=<true or false>
```

## Usage

1. **Start the Service:**
   ```bash
   python main.py
   ```

## API Endpoints

- **`/api/extraction/parse_sms`:** Parses and structures bank SMS data.
  - **Method:** POST
  - **Data:** `sms_text` (string) - The SMS message text.

- **`/api/text_to_sql/query`:** Converts natural language queries into SQL.
  - **Method:** POST
  - **Data:** `query` (string) - The natural language query.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.