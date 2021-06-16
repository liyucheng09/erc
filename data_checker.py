import pickle
import random

PATH={
    'iemocap':'data/DialogueRNN_features/IEMOCAP_features/IEMOCAP_features_raw.pkl'
}

class IEMOCAP:
    def __init__(self, data):
        self.ids, self.speakers, self.labels, self.text, self.audio, \
            self.visual, self.sentence, self.train_id, self.test_id = data

    def random_one(self):
        selected = random.choice(list(self.ids.keys()))
        return {
            'uid': self.ids[selected],
            'speaker': self.speakers[selected],
            'labels': self.labels[selected],
            'sentence':self.sentence[selected]
        }

CLASS={
    'iemocap':IEMOCAP
}

if __name__ == '__main__':

    data_path='data/DialogueRNN_features/IEMOCAP_features/IEMOCAP_features_raw.pkl'
    with open(data_path, 'rb') as f:
        data = pickle.load(f, encoding='latin1')
    
    data=IEMOCAP(data)

    print(data.random_one())
    
