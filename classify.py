from cdam import Cdam
from sklearn.externals import joblib
import numpy as np
import pickle as serializer


result = ''

model = Cdam("wavs/training", {'dry_1.wav':'dry', 'dry_2.wav':'dry', 'dry_3.wav':'dry', 'dry_4.wav':'dry','dry_5.wav':'dry', 'dry_6.wav':'dry', 'dry_7.wav':'dry', 'dry_8.wav':'dry','dry_9.wav':'dry', 'dry_10.wav':'dry', 'wet_1.wav':'wet', 'wet_2.wav':'wet', 'wet_3.wav':'wet', 'wet_4.wav':'wet', 'wet_5.wav':'wet', 'wet_6.wav':'wet', 'wet_7.wav':'wet', 'wet_8.wav':'wet', 'wet_9.wav':'wet', 'wet_10.wav':'wet', 'mid_1.wav':'mid', 'mid_2.wav':'mid', 'mid_3.wav':'mid', 'mid_4.wav':'mid', 'mid_5.wav':'mid', 'mid_6.wav':'mid', 'mid_7.wav':'mid', 'mid_8.wav':'mid', 'mid_9.wav':'mid', 'mid_10.wav':'mid'})

result = model.classify('wavs/testing/2015-10-24-12_24_06.wav')

print "The provided audio file classified as:  %s." % result

#joblib.dump(model, 'model.pkl') 
 
#with open('some_file.txt', 'w') as f:
#    serializer.dump( model01, f)
