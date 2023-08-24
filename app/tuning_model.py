import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# result = openai.FineTuningJob.create(training_file="file-lyUgIB3OVWvMEZbjMK72NCs8", model="gpt-3.5-turbo")
# print(result)

model = "ft:gpt-3.5-turbo-0613:personal::7r5hcQls"

"""
{
  "object": "fine_tuning.job",
  "id": "ftjob-tFBBMjnMYEY7SSWvXbw0MyqH",
  "model": "gpt-3.5-turbo-0613",
  "created_at": 1692886857,
  "finished_at": null,
  "fine_tuned_model": null,
  "organization_id": "org-9FaMn9oaWBnDYWd8gZY5OfMa",
  "result_files": [],
  "status": "running",
  "validation_file": null,
  "training_file": "file-lyUgIB3OVWvMEZbjMK72NCs8",
  "hyperparameters": {
    "n_epochs": 3
  },
  "trained_tokens": null
}
"""

result = openai.FineTuningJob.list_events(id="ftjob-tFBBMjnMYEY7SSWvXbw0MyqH", limit=50)["data"]
print("\n".join(m["message"] for m in reversed(result)))

# result = openai.FineTuningJob.retrieve("ftjob-tFBBMjnMYEY7SSWvXbw0MyqH")
# print(result)
