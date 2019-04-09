# Zero-shot Text Classification  
question: how to manually design the word embedding for seen and unseen class description?  
how to search the knowledge graph (circuits included) to find new class node that links all the key words in unseen class description?  
for the first frame, how to get unseen data in real situation to train the first level network?  
the challenge for zero-shot text classcification is we do not have labelled data for new class, therefore, there is no way to learn the concept from examples, 
but if our aim is to find a scalable solution for text classification problem, and what we have is some labelled texts with label description and some new labelled with description but without data samples, 
what we can do is to train a network which matches text samples with class descriptions instead of abstract class names. 
in this case, we take feature a text concatenating with feature of class description as input and output the probability that these two matches. 
the seen and labelled data are used for training and validating, then the inference in real applications can be achieved in the 1 vs all others way.  
[Integrating Semantic Knowledge to Tackle Zero-shot Text Classification](https://outlook.office.com/owa/?realm=ic.ac.uk&path=/attachmentlightbox)  
