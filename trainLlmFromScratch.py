''' Steps to train your own llm
1. Collect your dataset
2. Clean your data by removing all HTML tags and special characters
3. Tokenize your pure text into tokens. Tokens are the mathematical representations of yourtext data. Your data will now have IDs that can be processed into ndarrays called tensoors. This step is called embedding.
4. Instantiate a GPT-like model and pass your tensor to it.
5. Save your model and upload it to 
'''

import os # this is for loading the file
import tiktoken as tiktoken #this is for generating the token ids
import torch as torch #this is for creating the tensors
import transformers # this is for instantiating the GPT model
import joblib #this is for saving the model
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelForCausalLM,AutoTokenizer
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments


the_tokenizer= GPT2Tokenizer.from_pretrained('gpt2')
# Set padding token to eos token for left-padding (needed for generation/prediction)
the_tokenizer.pad_token = the_tokenizer.eos_token
GPT2_model = GPT2LMHeadModel.from_pretrained('gpt2')


# read the pure dataset from a file and tokenize it
file_name="story1.txt"
if os.path.exists (file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        story1_text = f.read()
        print("\nthe filestory1.txt text\n",story1_text)
else:
    print(f" the file{file_name} does not exist")
#turn the cleantext to token IDs   
tokens=the_tokenizer.encode(story1_text)
print("\ntokenized story1_text \n", tokens)
#this is just a test to return the token IDs to text, it is not part of the steps
tokens_to_text=the_tokenizer.decode(tokens)
print("\n\n converted the tokens back to the story1_text text \n\n", tokens_to_text)
#convert the tokens into a tensor
token_ids_to_tensor=torch.tensor([tokens])
print("\n\n the tokens are converted  into a tensor\n\n", token_ids_to_tensor)
print("this is the shape of the tensor",token_ids_to_tensor)
print("this is the squencelenght of the tensor",token_ids_to_tensor.size(1))
#initialize local GPT model

# You can now pass a tensor directly to the pretrained model. Make sure you use the same
#model for the tikenizer, and the model in this case is gpt2
output_tensor=GPT2_model(token_ids_to_tensor)
print("\n\n Output tensor of the input tensor token_ids_to_tensor\n\n",output_tensor)
# re-evaluate your model
GPT2_model.eval()
joblib.dump(GPT2_model,"my_trained_model.pkl")
# Load the model from the .pkl file
my_trained_loaded_model = joblib.load('my_trained_model.pkl',"utf-8")

input_text = "use pretrained data Hailing from the Treme neighborhood"
inputs = the_tokenizer(input_text, return_tensors="pt")
outputs = my_trained_loaded_model.generate(**inputs, max_length=50)
print(the_tokenizer.decode(outputs[0], skip_special_tokens=True))



print("Model loaded successfully.")
# Make predictions on the test data
#predictions = my_loaded_model.generate(tokenizer.encode("Hailing from"))
#generator = pipeline('text-generation', model='gpt2')
#print(generator("where is Trombone Shorty from?", max_length=30))
# View the predictions
#model_name=my_loaded_model
#print("\n my model here model_name=\n",model_name)
#autotokenizer=AutoTokenizer.from_pretrained(model_name)
#mymodel_instance=AutoModelForCausalLM.from_pretrained(model_name)
