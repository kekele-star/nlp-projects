import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preporcessing.text import Tokenizer 

sentences = [ 
	'I love my cars'
	'I love my cat'
]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)