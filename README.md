# Fine-Tuning GPT-3.5-turbo

This project offers a detailed guide to working with GPT-3.5-turbo using OpenAI, focusing on the fine-tuning process for specialized tasks. The guide is structured to lead you through various stages of preparing, training, and implementing a fine-tuned model. Beginning with an understanding of training example counts and the cost formula, it provides insights into how to manage and predict training expenses. Subsequent sections delve into transforming data into JSON-L files, creating OpenAI training files, fine-tuning the GPT-3.5-turbo model, and using a custom GPT model for specific applications. The project also includes illustrative examples, such as the creation of a sarcastic chatbot named Marv. Designed to cater to both beginners and experts in the field of Natural Language Processing (NLP), this guide simplifies complex concepts and provides practical code snippets to assist in building specialized models.

### Fine Tuning vs Embeddings

Embeddings with retrieval are an advanced technique in the domain of information retrieval and Natural Language Processing (NLP). They are particularly beneficial for scenarios that require access to large collections of documents, each carrying its own context and information. Unlike a mere keyword search, embeddings with retrieval can capture semantic meanings, thereby providing more accurate and relevant results. Retrieval strategies can be used in conjunction with fine-tuning methods to enhance the effectiveness of a model. Rather than being mutually exclusive, these two approaches can be combined to utilize both the efficiency of retrieval strategies and the specificity of fine-tuning. This synergy offers a powerful way to manage large-scale information retrieval tasks. 

For the purpose of brevity and simplicity, this project will showcase fine-tuning without the complexity of embeddings.


### Training Example Count

The training example count specifies the number of examples needed to effectively train an LLM. It can be categorized into four levels:

- Minimum: 10 examples are the bare minimum, suitable for very basic tasks.
- Nominal: 50-100 examples represent a standard requirement for more nuanced tasks.
- Expert: 500-1000 examples are required for complex models with deep learning and specialized outcomes.
- Master: 1000+ examples are needed for highly sophisticated models with intricate tasks. The more examples, the better the model can understand the nuances and intricacies of the data.

### Cost Formula

The cost formula calculates the total cost incurred during the training process. It consists of the following variables:

- c = base cost per 1k tokens, representing the fixed cost for every 1000 tokens.
- n = number of tokens in the input file, indicating the total size of the data.
- e = number of epochs trained, referring to the complete passes through the entire dataset.

The estimated cost is computed as c * n * e. For instance, a training file with 100,000 tokens trained over 3 epochs at a base cost of $0.008 would have an expected cost of approximately $2.40.

### Transform a `List[Dict]` into a JSON-L File

In this project, transforming a `List[Dict]` into a JSON-L (JSON Lines) file is a crucial step, as the JSON-L format is what the OpenAI API specifically expects for training. The line-by-line structure of JSON-L files enables efficient handling and processing of large data sets, making it an optimal choice for this purpose.

The following Python code snippet takes a list of dictionaries, each representing a conversation, and writes them to a JSON-L file. This transformed data is then ready to be used in subsequent steps of the project, such as creating an OpenAI training file for fine-tuning the GPT-3.5-turbo model.

```python
import json

data = [
    {"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
                  {"role": "user", "content": "What's the capital of France?"},
                  {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]},
    # Additional conversation entries
]

with open("marv.jsonl", "w") as jsonl_file:
    for entry in data:
        jsonl_file.write(json.dumps(entry) + "\n")
```

The resulting JSON-L file, "marv.jsonl" contains each conversation entry on a new line, adhering to the format required by the OpenAI API. This step ensures that the data is structured correctly for training, aligning with the API's expectations, and leveraging the benefits of the JSON-L format, such as ease of processing, error resilience, and compatibility.

#### System Prompt vs No System Prompt in the Training Data

When a system prompt is included in the training data, it essentially acts as a guiding signal for the model. The model learns to associate specific responses or behavior with that prompt, and the prompt becomes part of the pattern that the model looks for. In this scenario, if you want to elicit the specific behavior or style that was trained with that system prompt, you would need to use the same or similar system prompt in the actual conversation with the model. The model expects that prompt and responds according to the pattern it learned during training.

On the other hand, if no system prompt is included in the training data, the model does not have that specific guiding signal to rely on. It is trained more generically without associating specific responses with a particular system-initiated context. In this case, the model's responses are likely to be more generalized and may not adhere to a particular style or theme that might have been dictated by a system prompt. The absence of a system prompt in training means that there is no dependency on that prompt during conversation, and the model's behavior is not tied to a particular prompt.

Including a system prompt in the training data creates a dependency where the model associates specific behaviors or responses with that prompt. If you want to access those specific behaviors in conversation, you would typically need to use that prompt. Omitting the system prompt results in a more flexible and generalized model that does not rely on a specific initiating context to guide its responses. The choice between these two approaches depends on whether you desire more or less control.

### Create an OpenAI Training File from JSON-L

This part of the code establishes how to create an OpenAI training file using the JSON-L file created in the previous step. It imports necessary modules and uses OpenAI's API to create a file with a specific purpose of 'fine-tune'. It demonstrates how to handle API keys securely with the dotenv module.

```python
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.File.create(file=open("marv.jsonl", "rb"), purpose='fine-tune')
```

### Fine Tune GPT-3.5-turbo

Here, the Python code snippet is used to initiate a fine-tuning job on the GPT-3.5-turbo model with OpenAI's API. It specifies the training file and model to be used for fine-tuning. This step is crucial for tailoring the model to specific requirements and improving its performance on specialized tasks.

```python
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.FineTuningJob.create(training_file="file-abc123", model="gpt-3.5-turbo")
```

### Use Custom GPT Model

This code section illustrates how to use a custom GPT model that has been fine-tuned previously. It involves creating a chat completion request using the fine-tuned model, exemplified with a query to Marv, the sarcastic chatbot. The code also prints the response from the model. This snippet highlights the ability to customize and employ a model for specific tasks, leveraging the previous steps of transforming data, creating training files, and fine-tuning the model.

```python
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
  messages=[
    {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
    {"role": "user", "content": "What is the capitol of Oregon?"}
  ]
)

print(completion.choices[0].message)
```
