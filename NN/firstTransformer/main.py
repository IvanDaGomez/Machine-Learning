from mixed.transformer import Transformer
import torch
from torch import nn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import spacy
from collections import defaultdict
from tqdm import tqdm
import json
from functools import reduce
from torch.utils.data import Dataset, DataLoader
# english_file = 'NN/firstTransformer/data/english.txt'
# spanish_file = 'NN/firstTransformer/data/spanish.txt'

# Load English & Spanish NLP Models
# nlp_eng = spacy.load("en_core_web_sm", disable=["ner", "parser"])
# nlp_spa = spacy.load("es_core_news_sm", disable=["ner", "parser"])
import tiktoken

# Use tiktoken from openai
# -------------------------------------------------------------------------Models for word tokens
nlp_spa = spacy.blank('es')
nlp_eng = spacy.blank('en')
nlp = [nlp_eng, nlp_spa]

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


languages = ['english', 'spanish'] # Languages for which the model will be available to switch ()
languages_dict = {}

for language in languages:
   path = f'NN/firstTransformer/data/{language}.txt'
   with open(path, 'r') as file:
      languages_dict[language] = file.read().split('\n')


languages_df = pd.DataFrame(languages_dict)

START_TOKEN = '<START>'
PADDING_TOKEN = '<PAD>'
END_TOKEN = '<END>'
TOKENS_LIST = [START_TOKEN, END_TOKEN, PADDING_TOKEN]
TOTAL_SENTENCES = languages_df.shape[0]

PERCENTILE = 95

# Prints the number of word count of the percentile 95
for language in languages:
    print( f"{PERCENTILE}th percentile length English: {np.percentile([len(x) for x in languages_df[language].values], PERCENTILE)}" )



VOCAB_SIZE = 10000
# Show the most common words in the English language

VOCAB = {}


def tokenize(texts_df, nlp_model):
    list_of_tokens = defaultdict(int)  # Initialize with 0 for each key

    # Iterate through each document
    for doc in tqdm(nlp_model.pipe(texts_df, batch_size=10000, disable=["ner", "parser"])):
        for token in doc:
            # Skip punctuation and spaces
            if token.is_punct or token.is_space:
                continue

            # Count the tokenized word itself
            list_of_tokens[token.text.lower()] = []
            list_of_tokens[token.text.lower()].append(token.text.lower())
            
            # Count the lemma (root form of the word)
            if token.lemma_ != "-PRON-":  # Avoid lemmatized pronouns (which might be "-PRON-")
                list_of_tokens[token.text.lower()].append(token.lemma_.lower())
            
            # Count the prefix (first 3 characters) and suffix (last 3 characters)
            try:
            

                if len(token.text) > 3 and token.text not in TOKENS_LIST:  # Avoid short words
                    # Prefix
                    list_of_tokens[token.text.lower()].append(token.text.lower()[:3] + "-")
                    
                    # Suffix
                    list_of_tokens[token.text.lower()].append("-" + token.text.lower()[-3:])
            except: 
                continue

    return list_of_tokens

# Process English and Spanish separately
with open('NN/firstTransformer/data/vocab.json', 'r') as file:
    VOCAB = json.load(file)

if len(VOCAB.keys()) == 0:
    for i, language in enumerate(languages):

        VOCAB[language] = tokenize(languages_df[language], nlp[i]) 
        VOCAB[language]['tokens'] = [START_TOKEN, END_TOKEN, PADDING_TOKEN]
        
# Save the vocabulary to a JSON file
with open('NN/firstTransformer/data/vocab.json', 'w') as file:
    json.dump(VOCAB, file, ensure_ascii=False, indent=4)


vocab_set = set()
for element in VOCAB['spanish']:
    vocab_set.add(element)

# Maps a word to a specific index
index_to_language = {}
language_to_index = {}
for language in languages:
    index_to_language[language] = {k:v for k, v in enumerate(VOCAB[language])}
    language_to_index[language] = {v:k for k, v in enumerate(VOCAB[language])}

    

# LIMIT NUMBER OF SENTENCES
MAX_SEQUENCE_LENGTH = 350

# Working for single words
def is_valid_tokens(sentence, vocab):
    for token in list(set(sentence)):
        if token not in vocab:
            return False
    return True

#print(is_valid_tokens('Hola soy manuel', VOCAB['spanish']))
#print(list(set('Hola soy manuel')))
def length_is_valid(sentence, max_sequence_length):
    return len(list(sentence)) < (max_sequence_length - 1) # need to re-add the end token so leaving 1 space

# For various languagesç
valid_sentence_indices = []
for index in range(len(languages_df)):
    valid = True
    for language in languages:
        sentence = languages_df[language].values[index].lower().split()
        if not length_is_valid(sentence, MAX_SEQUENCE_LENGTH): #or not is_valid_tokens(sentence, VOCAB[language]):
            valid = False
            break
    if valid:
        valid_sentence_indices.append(index)

valid_sentences = {}
for language in languages:
    valid_sentences[language] = [languages_df[language].values[i].lower() for i in valid_sentence_indices]



# TRANSFORMER MODEL

d_model = 512 
batch_size = 30
ffn_hidden = 2048
num_heads = 8
drop_prob = 0.1
num_layers = 1
max_sequence_length = 200

sp_vocab_size = len(vocab_set)

transformer = Transformer(d_model, 
                          ffn_hidden,
                          num_heads, 
                          drop_prob, 
                          num_layers, 
                          max_sequence_length,
                          sp_vocab_size,
                          language_to_index['english'],
                          language_to_index['spanish'],
                          START_TOKEN, 
                          END_TOKEN, 
                          PADDING_TOKEN).to(device)

class TextDataset(Dataset):

    def __init__(self, english_sentences, kannada_sentences):
        self.english_sentences = english_sentences
        self.kannada_sentences = kannada_sentences

    def __len__(self):
        return len(self.english_sentences)

    def __getitem__(self, idx):
        return self.english_sentences[idx], self.kannada_sentences[idx]
    

dataset = TextDataset(valid_sentences['english'], valid_sentences['spanish'])

train_loader = DataLoader(dataset, batch_size)


loss_fn = nn.CrossEntropyLoss(#ignore_index=language_to_index['spanish'][PADDING_TOKEN],
                                reduction='none')

# When computing the loss, we are ignoring cases when the label is the padding token
for params in transformer.parameters():
    if params.dim() > 1:
        nn.init.xavier_uniform_(params)

optim = torch.optim.Adam(transformer.parameters(), lr=1e-4)

NEG_INFTY = -1e9

def create_masks(eng_batch, kn_batch):
    num_sentences = len(eng_batch)
    look_ahead_mask = torch.full([max_sequence_length, max_sequence_length] , True)
    look_ahead_mask = torch.triu(look_ahead_mask, diagonal=1)
    encoder_padding_mask = torch.full([num_sentences, max_sequence_length, max_sequence_length] , False)
    decoder_padding_mask_self_attention = torch.full([num_sentences, max_sequence_length, max_sequence_length] , False)
    decoder_padding_mask_cross_attention = torch.full([num_sentences, max_sequence_length, max_sequence_length] , False)

    for idx in range(num_sentences):
      eng_sentence_length, kn_sentence_length = len(eng_batch[idx]), len(kn_batch[idx])
      eng_chars_to_padding_mask = np.arange(eng_sentence_length + 1, max_sequence_length)
      kn_chars_to_padding_mask = np.arange(kn_sentence_length + 1, max_sequence_length)
      encoder_padding_mask[idx, :, eng_chars_to_padding_mask] = True
      encoder_padding_mask[idx, eng_chars_to_padding_mask, :] = True
      decoder_padding_mask_self_attention[idx, :, kn_chars_to_padding_mask] = True
      decoder_padding_mask_self_attention[idx, kn_chars_to_padding_mask, :] = True
      decoder_padding_mask_cross_attention[idx, :, eng_chars_to_padding_mask] = True
      decoder_padding_mask_cross_attention[idx, kn_chars_to_padding_mask, :] = True

    encoder_self_attention_mask = torch.where(encoder_padding_mask, NEG_INFTY, 0)
    decoder_self_attention_mask =  torch.where(look_ahead_mask + decoder_padding_mask_self_attention, NEG_INFTY, 0)
    decoder_cross_attention_mask = torch.where(decoder_padding_mask_cross_attention, NEG_INFTY, 0)
    return encoder_self_attention_mask, decoder_self_attention_mask, decoder_cross_attention_mask


total_loss = 0
num_epochs = 10

for epoch in range(num_epochs):
    print(f"Epoch {epoch}")

    for batch, (X, Y) in enumerate(train_loader):
        print(X[0], Y[0])
        break
        transformer.train()
        encoder_self_attention_mask, decoder_self_attention_mask, decoder_cross_attention_mask = create_masks(X, Y)
        optim.zero_grad()
        kn_predictions = transformer(eng_batch,
                                     kn_batch,
                                     encoder_self_attention_mask.to(device), 
                                     decoder_self_attention_mask.to(device), 
                                     decoder_cross_attention_mask.to(device),
                                     enc_start_token=False,
                                     enc_end_token=False,
                                     dec_start_token=True,
                                     dec_end_token=True)
        labels = transformer.decoder.sentence_embedding.batch_tokenize(kn_batch, start_token=False, end_token=True)
        loss = loss_fn(
            kn_predictions.view(-1, sp_vocab_size).to(device),
            labels.view(-1).to(device)
        ).to(device)
        valid_indicies = torch.where(labels.view(-1) == language_to_index['spanish'][PADDING_TOKEN], False, True)
        loss = loss.sum() / valid_indicies.sum()
        loss.backward()
        optim.step()
        #train_losses.append(loss.item())
        if batch_num % 100 == 0:
            print(f"Iteration {batch_num} : {loss.item()}")
            print(f"English: {eng_batch[0]}")
            print(f"Kannada Translation: {kn_batch[0]}")
            kn_sentence_predicted = torch.argmax(kn_predictions[0], axis=1)
            predicted_sentence = ""
            for idx in kn_sentence_predicted:
              if idx == language_to_index['spanish'][END_TOKEN]:
                break
              predicted_sentence += language_to_index['spanish'][idx.item()]
            print(f"Kannada Prediction: {predicted_sentence}")


            transformer.eval()
            kn_sentence = ("",)
            eng_sentence = ("should we go to the mall?",)
            for word_counter in range(max_sequence_length):
                encoder_self_attention_mask, decoder_self_attention_mask, decoder_cross_attention_mask= create_masks(eng_sentence, kn_sentence)
                predictions = transformer(eng_sentence,
                                          kn_sentence,
                                          encoder_self_attention_mask.to(device), 
                                          decoder_self_attention_mask.to(device), 
                                          decoder_cross_attention_mask.to(device),
                                          enc_start_token=False,
                                          enc_end_token=False,
                                          dec_start_token=True,
                                          dec_end_token=False)
                next_token_prob_distribution = predictions[0][word_counter] # not actual probs
                next_token_index = torch.argmax(next_token_prob_distribution).item()
                next_token = index_to_language['spanish'][next_token_index]
                kn_sentence = (kn_sentence[0] + next_token, )
                if next_token == END_TOKEN:
                  break
            
            print(f"Evaluation translation (should we go to the mall?) : {kn_sentence}")
            print("-------------------------------------------")
    

transformer.eval()
def translate(eng_sentence):
  eng_sentence = (eng_sentence,)
  kn_sentence = ("",)
  for word_counter in range(max_sequence_length):
    encoder_self_attention_mask, decoder_self_attention_mask, decoder_cross_attention_mask= create_masks(eng_sentence, kn_sentence)
    predictions = transformer(eng_sentence,
                              kn_sentence,
                              encoder_self_attention_mask.to(device), 
                              decoder_self_attention_mask.to(device), 
                              decoder_cross_attention_mask.to(device),
                              enc_start_token=False,
                              enc_end_token=False,
                              dec_start_token=True,
                              dec_end_token=False)
    next_token_prob_distribution = predictions[0][word_counter]
    next_token_index = torch.argmax(next_token_prob_distribution).item()
    next_token = index_to_language['spanish'][next_token_index]
    kn_sentence = (kn_sentence[0] + next_token, )
    if next_token == END_TOKEN:
      break
  return kn_sentence[0]

translation = translate("what should we do when the day starts?")
print(translation)